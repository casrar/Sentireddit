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

data_source = st.form('data_sources')
subreddit = data_source.text_input("Subreddit:")
search_term = data_source.text_input("Search Term:")
data_source_submit = data_source.form_submit_button("Add Data Source")
if data_source_submit:
    data = {
            'subreddit': subreddit, 
            'search_term': search_term,
            }
    response = requests.post('http://127.0.0.1:8090/api/collections/data_source/records', json=data, headers={'Authorization': auth_token}).json()

response = requests.get(
    'http://127.0.0.1:8090/api/collections/data_source/records', 
    headers={'Authorization': auth_token}).json()

def format_selections(data_source):
    return f'{data_source["subreddit"]}:{data_source["search_term"]}'
st.selectbox(label='Choose Data Source:', options=response['items'], format_func=format_selections)


# st.metric(label='Change', value='.954', delta='.034')
# st.line_chart([1, 2, 3])