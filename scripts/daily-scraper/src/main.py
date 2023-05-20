import requests 
import urllib.parse
import logging 
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


## iterate over every data source ##
# for each kvp                                                                
for data_source in data_sources:
    # check db for most recent timestamp for search term
    response = requests.get(
        'http://127.0.0.1:8090/api/collections/data/records?sort=-post_date&filter=((subreddit=\'{subreddit}\') %26%26 search_term=\'{search_term}\')'
        .format(subreddit=data_source[KEY], search_term=data_source[VALUE]), # do this better
        headers={'Authorization': auth_token}).json() 
    print(response)

    timestamp = 0 
    # if 0/null start at asc from 0                                             
    if response['totalItems'] > 0:
        timestamp = response['items'][0]['post_date']        
    
    # call cf worker with KVP and timestamp
    response = requests.get(
        config['CLOUDFLARE_URL'] + '?q={search_term}&subreddit={subreddit}&after={after}s'
        .format(search_term=data_source[VALUE], subreddit=data_source[KEY], after=timestamp), # do this better
        headers={'Authorization': auth_token})
    print(response)
    # while cf data != null
        # update timestamp in db
        # analyze data
        # push data into db
        # call cf worker with n

# {
#   "subreddit": "investing",
#   "search_terms": [
#     "msft",
#     "aapl",
#     "vti"
#   ]
# }

# {
#   "subreddit": "wallstreetbets",
#   "search_terms": [
#     "gme",
#     "tsla"
#   ]
# }