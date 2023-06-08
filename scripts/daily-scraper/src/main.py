import requests 
import urllib.parse
import logging 
import praw
import json
import time
from dotenv import dotenv_values

config = dotenv_values(".env")

# constants
KEY = 0
VALUE = 1

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
#print(data_sources)


reddit = praw.Reddit(
    client_id = config['CLIENT_ID'],
    client_secret = config['CLIENT_SECRET'],
    user_agent = config['USER_AGENT'],
    ratelimit_seconds = config['RATELIMIT_SECONDS']
)

subreddit_name = 'wallstreetbets'
keyword = 'money'
subreddit = reddit.subreddit(subreddit_name)
submissions = []

for submission in subreddit.search(query=keyword, sort='comments', time_filter='day'):
    print(submission.permalink)
    submissions.append(submission.comments)

for comment_forest in submissions:
    more_comments = comment_forest.replace_more(limit=None)
    while len(more_comments) > 0:
        try:
            more_comments = comment_forest.replace_more(limit=None)
            break
        except PossibleExceptions:
            print("Handling replace_more exception") # replace with logging
            sleep(1)
    comment_forest = comment_forest.list()
    print(type(comment_forest))
    print(type(submissions[2]))

# for comment in submissions[2]:
#     print(type(comment))
#     if comment is type(praw.models.MoreComments):
#         print('MORE COMMENT')

# print(submissions[2])


# file_path = str(time.time())
# file = open(file_path, 'w')
# json.dump(all_comments, file)
# file.close()


## iterate over every data source ##
# for each kvp                                                                
for data_source in data_sources:
    # check db for most recent timestamp for search term
    response = requests.get(
        'http://127.0.0.1:8090/api/collections/data/records?sort=-post_date&filter=((subreddit=\'{subreddit}\') %26%26 search_term=\'{search_term}\')'
        .format(subreddit=data_source[KEY], search_term=data_source[VALUE]), # do this better
        headers={'Authorization': auth_token}).json() 
    #print(response)

    timestamp = 0 
    # if 0/null start at asc from 0                                             
    if response['totalItems'] > 0:
        timestamp = response['items'][0]['post_date']        
    