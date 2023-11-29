import requests
from dotenv import dotenv_values


class GQLNewCommentIterator:
    def __init__(self, query, subreddit, proxy_url):
        # gql endpoint and headers are temporary, will replace with scrapeops
        # bearer token changes, need a way to keep it updated
        self.__query=query
        self.__subreddit=subreddit # Not implemented yet
        self.__proxy_url=proxy_url
        self.__url='https://www.reddit.com/r/{__subreddit}/search/?q={__query}&type=comment&sort=new&commentsCursor={__comments_cursor}' # use urllib.parse.quote
        self.__headers = None
        self.__comments_cursor = None 
    
    def __iter__(self):
        return self
    
    def __next__(self):
        return None


