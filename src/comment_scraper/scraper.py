import requests 
import logging 
import json
from nltk.sentiment import SentimentIntensityAnalyzer
from dotenv import dotenv_values
from RedditNewCommentIterator import RedditNewCommentIterator

# CONSTS
SUBREDDIT = 0
QUERY = 1
DATA_SOURCE_ID = 2
COMMENT_BODY = 0
COMMENT_POST_ID = 1
COMMENT_ID = 2
COMMENT_CREATED_TIMESTAMP = 3

def auth_to_db(config):
    # error check and log
    response = requests.post(
        'http://127.0.0.1:8090/api/collections/users/auth-with-password', 
        data={'identity': config['IDENTITY'], 'password': config['PASSWORD']}).json()
    auth_token = response['token']
    return auth_token

def get_data_sources(auth_token):
    # error check and log
    response = requests.get(
        'http://127.0.0.1:8090/api/collections/data_source/records', 
        headers={'Authorization': auth_token}).json()

    data_sources = []
    for i in range(response['totalItems']):
        data_sources.append(
            (response['items'][i]['subreddit'], 
            response['items'][i]['query'],
            response['items'][i]['id'])) 
    return data_sources

def scrape_comments(data_source, auth_token, config):
    pages = RedditNewCommentIterator(subreddit=data_source[SUBREDDIT], query=data_source[QUERY],
                                proxy_url='https://proxy.scrapeops.io/v1/', api_key=config['SCRAPE_OPS_KEY'])
    recent_timestamp = -1 
    recent_comment_id = -1
    params = {'sort':'-created_timestamp', 'filter': f'(data_source=\'{data_source[DATA_SOURCE_ID]}\')'}
    response = requests.get(
        'http://127.0.0.1:8090/api/collections/data/records', 
        headers={'Authorization': auth_token}, params=params).json()
    if response['totalItems'] > 0:  
        recent_timestamp = response['items'][0]['created_timestamp']
        recent_comment_id = response['items'][0]['comment_id']
    data = []
    for page in pages:
        for comment in page:
            if comment[COMMENT_CREATED_TIMESTAMP] <= recent_timestamp or comment[COMMENT_ID] == recent_comment_id: 
                break
            comment = {
                'body': comment[COMMENT_BODY],
                'post_id': comment[COMMENT_POST_ID],
                'comment_id': comment[COMMENT_ID],
                'created_timestamp': comment[COMMENT_CREATED_TIMESTAMP],
                'data_source': data_source[DATA_SOURCE_ID],
            }
            data.append(comment)
    return data

def analyze_comments(comments, sentiment_intensity_analyzer):
    for comment in comments:
        sentiment = sentiment_intensity_analyzer.polarity_scores(comment['body'])
        comment['compound'] = sentiment['compound']
        comment['pos'] = sentiment['pos']
        comment['neu'] = sentiment['neu']
        comment['neg'] = sentiment['neg']
    return comments

def post_comments_to_db(comments, auth_token):
    for comment in comments:
        response = requests.post('http://127.0.0.1:8090/api/collections/data/records', json=comment, headers={'Authorization': auth_token}).json()

def main():
    print('in main')
    # config = dotenv_values("../.env")
    # sia = SentimentIntensityAnalyzer()
    # auth_token = auth_to_db(config)
    # data_sources = get_data_sources(auth_token)
    # for data_source in data_sources:
    #     comments = scrape_comments(data_source=data_source, auth_token=auth_token, config=config)
    #     comments = analyze_comments(comments=comments, sentiment_intensity_analyzer=sia)
    #     post_comments_to_db(comments=comments, auth_token=auth_token)

if __name__ == "__main__":
    main()
