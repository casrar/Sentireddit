import requests 
import urllib.parse
import logging 
import praw
import json
import time
from nltk.sentiment import SentimentIntensityAnalyzer
from dotenv import dotenv_values
from RedditNewCommentIterator import RedditNewCommentIterator

# CONSTS
SUBREDDIT = 0
QUERY = 1
DATA_SOURCE_ID = 2
COMMENT_BODY = 0
POST_ID = 1
COMMENT_ID = 2
COMMENT_CREATED_TIMESTAMP = 3

config = dotenv_values(".env")
sia = SentimentIntensityAnalyzer()

# error check and log
response = requests.post(
    'http://127.0.0.1:8090/api/collections/users/auth-with-password', 
    data={'identity': config['IDENTITY'], 'password': config['PASSWORD']}).json()
auth_token = response['token']

# error check and log
response = requests.get(
    'http://127.0.0.1:8090/api/collections/data_source/records', 
    headers={'Authorization': auth_token}).json()

data_sources = []
for i in range(response['totalItems']):
    data_sources.append(
        (response['items'][i]['subreddit'], 
        response['items'][i]['search_term'],
        response['items'][i]['id'])) 

for data_source in data_sources:
    comments = RedditNewCommentIterator(subreddit=data_source[SUBREDDIT], query=data_source[QUERY],
                                proxy_url='https://proxy.scrapeops.io/v1/', api_key=config['SCRAPE_OPS_KEY'])
    recent_timestamp = 0
    params = {'sort':'-post_date', 'filter': f'(data_source={data_source[DATA_SOURCE_ID]})'}
    response = requests.get(
        'http://127.0.0.1:8090/api/collections/data_source/records', 
        headers={'Authorization': auth_token}, params=params).json()
    if response['totalItems'] > 0:  
        recent_timestamp = response['items'][0]['post_date']
    for comment in comments:
        # get most recent timestamp, if hit, break
        curr_timestamp = comment[COMMENT_CREATED_TIMESTAMP]
        if curr_timestamp <= recent_timestamp: # also check for same comment id 
            break
        recent_timestamp = curr_timestamp
        sentiment = sia.sia.polarity_scores(comment[COMMENT_BODY])
        data = {
            'id': 'RECORD_ID',
            'body': comment[COMMENT_BODY],
            'post_id': comment[POST_ID],
            'comment_id': comment[COMMENT_ID],
            'created_timestamp': recent_timestamp,
            'data_source': data_source[id],
            'compound': sentiment['compound'],
            'pos': sentiment['post'],
            'neu': sentiment['neu'],
            'neg': sentiment['neg']
        }
        response = requests.post('http://127.0.0.1:8090/api/collections/data/records', json=data, headers={'Authorization': auth_token}).json()
    
