import streamlit as st
import requests 
from dotenv import dotenv_values

config = dotenv_values(".env")
# error check and log
response = requests.post(
    'http://127.0.0.1:8090/api/collections/users/auth-with-password', 
    data={'identity': config['IDENTITY'], 'password': config['PASSWORD']}).json()
auth_token = response['token']


st.write("Reddit Sentiment Analysis")

data_sources = st.form('data_sources')
subreddit = data_sources.text_input("Subreddit:")
search_term = data_sources.text_input("Search Term:")
data_sources_submit = data_sources.form_submit_button("Add Data Source")
if data_sources_submit:
    data = {
            'subreddit': subreddit, 
            'search_term': search_term,
            }
    response = requests.post('http://127.0.0.1:8090/api/collections/data_source/records', json=data, headers={'Authorization': auth_token}).json()

