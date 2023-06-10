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
        response['items'][i]['search_term'])) 

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
    subreddit = reddit.subreddit(subreddit_name)
    submissions = []

    for submission in subreddit.search(query=keyword, sort='comments', time_filter='day'):
        submissions.append(submission.comments)

    for i in range(len(submissions)):
        more_comments = submissions[i].replace_more(limit=None)
        while len(more_comments) > 0:
            try:
                more_comments = submissions[i].replace_more(limit=None)
                break
            except PossibleExceptions:
                print("Handling replace_more exception") # replace with logging
                sleep(1)
        submissions[i] = submissions[i].list()

    response = requests.get(
        'http://127.0.0.1:8090/api/collections/data/records?sort=-post_date&filter=((subreddit=\'{subreddit}\') %26%26 search_term=\'{search_term}\')'
        .format(subreddit=data_source[KEY], search_term=data_source[VALUE]), # do this better
        headers={'Authorization': auth_token}).json() 

    timestamp = 0 
    if response['totalItems'] > 0:
        timestamp = response['items'][0]['post_date']  

    filtered_comments = []
    new_timestamp = timestamp
    for comment_list in submissions: # Not ideal, but can be refactored
        for comment in comment_list:
            if comment.created_utc > timestamp: 
                filtered_comments.append(comment)
            if comment.created_utc > new_timestamp:
                new_timestamp = comment.created_utc

    matches = []
    total_comments = len(filtered_comments)
    for comment in filtered_comments: 
        if comment.body.find(keyword) != -1: # Edit logic to account for case sensitivity 
            matches.append(comment)
            comment.sentiment_analysis = sia.polarity_scores(comment.body)

    #loop over all matches
    for match in matches:                 
        data = {
            'body': match.body, 
            'post_id': match.id, 
            'subreddit': subreddit_name, # subreddit and search term use what is stored in DB
            'search_term': keyword, 
            'post_date': match.created_utc, 
            'sentiment': match.sentiment_analysis
            }
        response = requests.post('http://127.0.0.1:8090/api/collections/data/records', json=data, headers={'Authorization': auth_token}).json()
    

    print(f'Found: {len(matches)} / {total_comments}')