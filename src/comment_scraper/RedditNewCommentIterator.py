import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import json


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
        try:
            response.raise_for_status()
            response = response.text
            soup = BeautifulSoup(response, 'html.parser')
            comments = self.__format_comments__(soup)
            self.__reddit_partial_url = self.__get_next_reddit_partial_url__(soup)
            return comments
        except requests.exceptions.HTTPError as err:
            # replace with log
            print('error')
       
    def __format_comments__(self, soup):
        comments = soup.find_all(attrs={'data-testid':'search-comment'})
        formatted_comments = []
        for comment in comments:
            post_info = comment.attrs
            comment_info = json.loads(post_info['data-faceplate-tracking-context'])
            comment_info = comment_info['comment']
            comment_id = comment_info['id']
            timestamp = comment_info['created_timestamp']
            comment_body = comment.find_all(id=f'search-comment-{comment_id}-post-rtjson-content')
            comment_body = self.__extract_comment_body__(comment_body)
            formatted_comments.append((self.__subreddit,comment_body, comment_id, timestamp))
        return formatted_comments
    
    def __extract_comment_body__(self, comment_tags):
        root_tag = comment_tags[0]
        p_tags = root_tag.find_all('p')
        comment_body = ""
        for p in p_tags:
            comment_body = comment_body + p.text
        return comment_body

    def __get_next_reddit_partial_url__(self, soup):
        reddit_partial_url=soup.find(name='faceplate-partial', attrs={'loading':'lazy'})
        if reddit_partial_url is None:
            self.__last_iteration = True
            return None
        reddit_partial_url = reddit_partial_url.attrs['src']
        return reddit_partial_url

