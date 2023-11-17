import requests 
import urllib.parse
import logging 
import praw
import json
import time
from nltk.sentiment import SentimentIntensityAnalyzer
from dotenv import dotenv_values

config = dotenv_values(".env")

# constants
KEY = 0
VALUE = 1

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

reddit = praw.Reddit(
    client_id = config['CLIENT_ID'],
    client_secret = config['CLIENT_SECRET'],
    user_agent = config['USER_AGENT'],
    ratelimit_seconds = config['RATELIMIT_SECONDS']
)

# REFACTOR 
for data_source in data_sources:
    print(data_source)
    subreddit_name = data_source[KEY]
    keyword = data_source[VALUE]
    data_source_id = data_source[2]
    subreddit = reddit.subreddit(subreddit_name) # if subreddit does not exist, breaking error
    submissions = []

    # Create CF worker to grab comments
        # format for URL https://www.reddit.com/r/{subreddit}/search/?q={search_term}&restrict_sr=1&type=comment&sort=new
        # hitting url, returns web page, need to scrape highlighted comments in below format
            # <div class="Comment t1_{id} P8SGAKMtRxNwlmLz1zdJu _1z5rdmX8TDr6mqwNv7A70U _3nqqnHjXPJkfr8j5t_I85P">
        # Need to get the link for the single comment highlight
        # Then visit the .json page
        # grab the needed meta data (post date, etc)


    # Use Python to call CF worker
    # CF worker runs through tasks
    # Perform SA on CF data
    # Push to DB

    # matches = []
    # #loop over all matches
    # for match in matches:                 
    #     data = {
    #         'body': match.body, 
    #         'post_id': match.id, 
    #         'data_source': data_source_id,
    #         'post_date': match.created_utc, 
    #         'compound': match.sentiment_analysis['compound'],
    #         'pos': match.sentiment_analysis['pos'],
    #         'neu': match.sentiment_analysis['neu'],
    #         'neg': match.sentiment_analysis['neg']
    #         }
    #     response = requests.post('http://127.0.0.1:8090/api/collections/data/records', json=data, headers={'Authorization': auth_token}).json()
    
    # print(f'Found: {len(matches)} / {total_comments}')
