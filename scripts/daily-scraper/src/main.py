import requests 
import logging 
from dotenv import dotenv_values

config = dotenv_values(".env")

response = requests.post(
    'http://127.0.0.1:8090/api/collections/users/auth-with-password', 
    data={'identity': config['IDENTITY'], 'password': config['PASSWORD']})

response = response.json()
#print(response)

response = requests.get('http://127.0.0.1:8090/api/collections/subreddit/records', headers={'Authorization': response['token']})
print(response.json())

# make call to DB REST
    # gather search terms
    # gather data sourecs
    # gather most recent time stamps from search term items (i.e. time stamp for GME on WSB, GME on investing, TSLA on WSB, etc)
# run through list calling CF Worker with data
# perform SA on data and throw into DB
# log 

