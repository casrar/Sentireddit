import streamlit as st
import requests 
from dotenv import dotenv_values
import datetime
from datetime import date, datetime as dt
import urllib.parse
import plotly.express as px
import pandas as pd

config = dotenv_values(".env")
# error check and log
response = requests.post(
    'http://127.0.0.1:8090/api/collections/users/auth-with-password', 
    data={'identity': config['IDENTITY'], 'password': config['PASSWORD']}).json()
auth_token = response['token']

if 'data_source_length' not in st.session_state:
    response = requests.get(
        f"http://127.0.0.1:8090/api/collections/data_source/records", 
        headers={'Authorization': auth_token}).json()
    st.session_state['data_source_length'] = response['totalItems']
    st.session_state['data_source_list'] = []

if 'sentiment' not in st.session_state:
    st.session_state['sentiment'] = {'compound': 0, 'neg': 0, 'neu': 0, 'pos': 0}


st.write("Reddit Sentiment Analysis")

data_source = st.form('add_data_sources')
subreddit = data_source.text_input("Subreddit:")
search_term = data_source.text_input("Search Term:")
data_source_submit = data_source.form_submit_button("Add Data Source")
if data_source_submit:
    data = {
            'subreddit': subreddit, 
            'search_term': search_term,
            }
    response = requests.post('http://127.0.0.1:8090/api/collections/data_source/records', json=data, headers={'Authorization': auth_token}).json()
    st.session_state['data_source_length'] += 1


response = requests.get(
    'http://127.0.0.1:8090/api/collections/data_source/records', 
    headers={'Authorization': auth_token}).json()

def format_selections(data_source):
    return f'{data_source["subreddit"]}:{data_source["search_term"]}'
def get_data(data_source):
    com_value = neg_value = neu_value = pos_value = 0
    response = requests.get(
        f"http://127.0.0.1:8090/api/collections/data/records?filter=(data_source=\'{data_source['id']}\')", 
        headers={'Authorization': auth_token}).json()
    item_count = response['totalItems'] 
    if item_count < 1:
        st.warning('No data exists for selected Data Source.')
        return com_value, neg_value, neu_value, pos_value
    for item in response['items']:
        com_value += item['sentiment']['compound']
        neg_value += item['sentiment']['neg']
        neu_value += item['sentiment']['neu']
        pos_value += item['sentiment']['pos']
    com_value = com_value / item_count
    neg_value = neg_value / item_count
    neu_value = neu_value / item_count
    pos_value = pos_value / item_count
    return {'compound': com_value, 'neg': neg_value, 'neu': neu_value, 'pos': pos_value}

with st.form('select_data_sources', clear_on_submit=True):
    st.session_state['data_source_list'] = response['items']
    selectbox_data = st.selectbox(label='Choose Data Source:', options=st.session_state['data_source_list'], format_func=format_selections)
    selectbox_submit = st.form_submit_button('Change Data Source') 
    selectbox_remove = st.form_submit_button('Remove Data Source')
    if selectbox_submit and st.session_state['data_source_length'] > 0:
        st.session_state['sentiment'] = {'compound': 0, 'neg': 0, 'neu': 0, 'pos': 0}
        st.session_state['sentiment'] = get_data(selectbox_data)
    elif selectbox_remove and st.session_state['data_source_length'] > 0:
        base_url = f"http://127.0.0.1:8090/api/collections/data_source/records/{selectbox_data['id']}"
        response = requests.delete(
            url=base_url, 
            headers={'Authorization': auth_token})
        st.session_state['data_source_length'] -= 1
        st.session_state['data_source_list'].remove(selectbox_data)
    elif selectbox_remove and st.session_state['data_source_length'] < 1:
        st.warning('No Data Sources exist.')

response = requests.get(
    'http://127.0.0.1:8090/api/collections/data/records', 
    headers={'Authorization': auth_token}).json()

com, neg, neu, pos = st.columns(4)
if selectbox_data is not None:
    com.metric('Compound', st.session_state['sentiment']['compound'])
    neg.metric('Negative', st.session_state['sentiment']['neg'])
    neu.metric('Neutral', st.session_state['sentiment']['neu'])
    pos.metric('Positive', st.session_state['sentiment']['pos'])

date_input, graph = st.columns(2)
date_input.form('Date Range')

start_date_input = date_input.date_input("start date")
start_date = datetime.datetime(start_date_input.year, start_date_input.month, start_date_input.day)
start_date = int(start_date.timestamp())

end_date_input = date_input.date_input("end date")
end_date = datetime.datetime(end_date_input.year, end_date_input.month, end_date_input.day)
end_date = int(end_date.timestamp())
sentiment_list = []
if end_date < start_date and selectbox_data is not None:
    st.warning('End Date is before Start Date.')
elif selectbox_data is not None: 
    base_url = 'http://127.0.0.1:8090/api/collections/data/records'
    filter = f"(data_source=\'{selectbox_data['id']}\'&&post_date>\'{start_date}\'&&post_date<\'{end_date}\')"
    response = requests.get(
        url=base_url,
        params= {'filter':filter}, 
        headers={'Authorization': auth_token}).json()
    for item in response['items']:
        sentiment_list.append(item['sentiment']['compound'])
    fig = px.violin(pd.DataFrame(sentiment_list, columns=['Sentiment']), y='Sentiment', points='all')
    graph.plotly_chart(fig, theme='streamlit', use_container_width=True)


