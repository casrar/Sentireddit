import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import json


class RedditNewCommentIterator:
    def __init__(self, subreddit, query, proxy_url, api_key):
        self.__subreddit=subreddit
        self.__query=query
        self.__proxy_url=proxy_url
        self.__api_key=api_key
        self.__reddit_origin_url='https://www.reddit.com'
        self.__reddit_partial_url=f'/svc/shreddit/r/{self.__subreddit}/search/?q={self.__query}&type=comment&sort=new'
        self.__last_iteration=False
        self.__proxy_params = {
            'api_key': self.__api_key,
            'url': self.__reddit_origin_url + self.__reddit_partial_url
        }
    
    def __scrape(self): 
        ## test version
        try:
            response = requests.get(url=self.__reddit_origin_url + self.__reddit_partial_url)
            response.raise_for_status()
            response = response.text
            return response
        except requests.exceptions.HTTPError as err:
            # handle out of credits 
            # replace with log
            return err
        

        ## live version 
        # response = requests.get(
        #     url=self.__proxy_url,
        #     params=urlencode(self.__proxy_params),
        # )
        # try:
        #     response.raise_for_status()
        #     response = response.text
        #     return response
        # except requests.exceptions.HTTPError as err:
        #     # handle out of credits 
        #     # replace with log
        #     print('error')

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__last_iteration:
            raise StopIteration
        self.__proxy_params['url'] = self.__reddit_origin_url + self.__reddit_partial_url
        page = self.__scrape()
        # check for errors
        soup = BeautifulSoup(page, 'html.parser')
        comments = self.__format_comments__(soup)
        self.__reddit_partial_url = self.__get_next_reddit_partial_url__(soup)
        return comments
       
    def __format_comments__(self, soup):
        comments = soup.find_all(attrs={'data-testid':'search-comment'})
        formatted_comments = []
        for comment in comments:
            post_info = comment.attrs
            comment_info = json.loads(post_info['data-faceplate-tracking-context'])
            comment_info = comment_info['comment']
            post_id = comment_info['post_id']
            comment_id = comment_info['id']
            created_timestamp = comment_info['created_timestamp']
            comment_body = comment.find_all(id=f'search-comment-{comment_id}-post-rtjson-content')
            comment_body = self.__extract_comment_body__(comment_body)
            formatted_comments.append((comment_body, post_id, comment_id, created_timestamp))
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
    
    

