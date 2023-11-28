import requests

class GQLNewCommentIterator:
    def __init__(self, search_term, subreddit, proxy_url):
        # gql endpoint and headers are temporary, will replace with scrapeops
        self.__search_term=search_term
        self.__subreddit=subreddit # Not implemented yet
        self.__proxy_url=proxy_url
        self.__gql_endpoint='https://gql.reddit.com/' 
        self.__headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
           'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzAxMjM2NjY4Ljg0Mzk5NiwiaWF0IjoxNzAxMTUwMjY4Ljg0Mzk5NiwianRpIjoiWDlRUHRDMGE0enBlRThOVXpnVWFkRWVYOUdESF9nIiwiY2lkIjoiOXRMb0Ywc29wNVJKZ0EiLCJsaWQiOiJ0Ml9xbmViaWt0IiwiYWlkIjoidDJfcW5lYmlrdCIsImxjYSI6MTUxNTAwMTgzNTg1Mywic2NwIjoiZUp4a2tkR090REFJaGQtbDF6N0JfeXBfTmh0c2NZYXNMUWFvazNuN0RWb2NrNzN5d1BuYXd2Rl9ncHk1TjB0VHlvS2xrR21hRWhieXpySUNTWnJTazlSWTNtbEtWTEFabWN1VmRxelE0SUZwU3BWTDVyYlE0OUltTkhkajBiTVRWMVV1S3ctcUFxMm5hbXpqRnJZbnhwbU4xWVpVWEpkVG1jQ3lVRDZMRl8yUXE3ZjItVFA5SnJTRFlVVlZlS0IzQktFY240M0ZGMVBZX1QwMTZkbTZZRkY3cndlcGZhN0g3dHBuelVLemNfczVucjgya25FNUxzMVBzSDkzX1JJNjhNanpNcU1PWU1RYWZwUmhSOWJoWDNVQWxRc0tHRXNRbjBZZ1Z5N2Zfa3V3WFpQLU5XNUhmUEhOaUp2ZThGc3pVTThsaUVPZnh0ZHZBQUFBX18tQ3lkUW4iLCJyY2lkIjoielRBYUluREZPLWdIZVdtYUhXSjZGVmxDaXFST2lNZVJuS1E0OS0tdERIOCIsImZsbyI6Mn0.e6iGXSoqSCp0QtYXqaYbdT8izQnN4gK2PtzJEgs9tXGblIP_0rxJ0AeoYS020qX_6gaqNqWlAK9tPGPHD-YYNRbq1zd9bUh4rRhb9LbVlPzQQAY1T4JrRmw7SSF-S4t_bNNBeiFoTFYRkApuZjhgUKbGIPCRgiq8TnC20qkA8Ukvgw1cIufnmvo-LVK-X-boIJoa-FPIY97TkgJMDalmglrH2qXzBCeWa01hZISQR0U8PT-zBqhum8IUygpEyVQVIyxt03M0HccD6jyhizEczZ42QxdMTnEmzgfOIaSuEyn45lQ5uYpw6j78cWDXAPxddnOb-nnfhTO2ScMyQ_4AEQ',
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
                        "value": "redditdev"
                    }
                ],
                "includeAuthors": False,
                "includeComments": True,
                "includeCommunities": False,
                "includePosts": False,
                "postsAfter": None,
                "productSurface": "web2x",
                "query": "search",
                "searchInput": {
                    "queryId": "1b91cfc5-16a4-4477-a698-4be6bec3ba08",
                    "structureType": "search"
                },
                "sort": None,
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
        print(page_info)
        if (page_info['hasNextPage'] is False and page_info['hasPreviousPage'] is False 
            and page_info['startCursor'] is None and page_info['endCursor'] is None):
                raise StopIteration
        self.__gql_new_comment_search = page_info['endCursor']
        return res['data']['search']['general']['comments']['edges']
  


