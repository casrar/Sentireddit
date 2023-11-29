import requests
from dotenv import dotenv_values

config = dotenv_values(".env")

class GQLNewCommentIterator:
    def __init__(self, search_term, subreddit, proxy_url):
        # gql endpoint and headers are temporary, will replace with scrapeops
        # bearer token changes, need a way to keep it updated
        self.__search_term=search_term
        self.__subreddit=subreddit # Not implemented yet
        self.__proxy_url=proxy_url
        self.__gql_endpoint='https://gql.reddit.com/' 
        self.__headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
           'Authorization': config['BEARER_TOKEN'],
           'Content-Type': 'application/json'}
        self.__gql_new_comment_search = {
            "id": "6c87f86c5706",
            "variables": {
                "authorsAfter": None,
                "commentsAfter": None,
                "communitiesAfter": None,
                "communitySearch": True,
                "customFeedSearch": False,
                "filters": [
                    {
                        "key": "nsfw",
                        "value": "1"
                    },
                    {
                        "key": "subreddit_names",
                        "value": self.__subreddit
                    }
                ],
                "includeAuthors": False,
                "includeComments": True,
                "includeCommunities": False,
                "includePosts": False,
                "postsAfter": None,
                "productSurface": "web2x",
                "query": self.__search_term,
                # "searchInput": {  # This line is not needed for search, it may in the future, so for now it stays
                #     "queryId": "1b91cfc5-16a4-4477-a698-4be6bec3ba08",
                #     "structureType": "search"
                # },
                "sort": "NEW",
                "subredditNames": [
                    "redditdev"
                ]
            }
        }
        self.__comments_after = None 
    
    def __iter__(self):
        return self
    
    def __next__(self):
        # A lot of the request stuff will get changed when i use scrapeops
        # need to implement subreddit search
        self.__gql_new_comment_search['commentsAfter'] = self.__comments_after
        res = requests.post(url=self.__gql_endpoint, json=self.__gql_new_comment_search, headers=self.__headers) 
        res = res.json()
        page_info = res['data']['search']['general']['comments']['feedMetadata']['appliedFilters']['pageInfo']
        if (page_info['hasNextPage'] is False and page_info['hasPreviousPage'] is False 
            and page_info['startCursor'] is None and page_info['endCursor'] is None):
                raise StopIteration
        self.__gql_new_comment_search = page_info['endCursor']
        return res['data']['search']['general']['comments']['edges']
  


