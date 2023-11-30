import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup


class RedditNewCommentIterator:
    def __init__(self, query, subreddit, proxy_url):
        # will be using scrapeops
        self.__query=query
        self.__subreddit=subreddit
        self.__headers=None
        self.__proxy_url=proxy_url
        self.__reddit_origin_url='https://www.reddit.com'
        self.__reddit_partial_url=f'/svc/shreddit/r/{self.__subreddit}/search/?q={self.__query}&type=comment&sort=new' # use urllib.parse.quote
        self.__last_iteration=False
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__last_iteration:
            raise StopIteration
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
        response = requests.get(url=self.__reddit_origin_url+self.__reddit_partial_url, headers=headers)
        #check response
        # if response.status_code != 200:
        #if error code, raise error
        response = response.text
        soup = BeautifulSoup(response, 'html.parser')
        comments = self.__format_comments__(soup)
        self.__reddit_partial_url = self.__get_next_reddit_partial_url__(soup)
        return comments
    
    def __format_comments__(self, soup):
        comments = soup.find_all(attrs={'data-testid':'search-comment'})
        # this contains both the timestamp for the comment t3, and the post data has id=search-comment-{t1_id}-post-rtjson-content, im not sure about duplicates

        #todo
            # create a model for how i want the comments returned
            # figure out how to destructure the <p> tags for the comment content

        # iterate over top level 'data-testid':'search-comment' tags
            # grab the timestamp created
            # grab the t3 id
            # find id=search-comment-{t1_id}-post-rtjson-content and append all <p> tags to data structure
        
        # return list
        return comments
    
    def __get_next_reddit_partial_url__(self, soup):
        reddit_partial_url=soup.find(name='faceplate-partial', attrs={'loading':'lazy'})
        if reddit_partial_url is None:
            self.__last_iteration = True
            return None
        reddit_partial_url = reddit_partial_url.attrs['src']
        return reddit_partial_url

