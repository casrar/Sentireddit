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

response = requests.get(
    'http://127.0.0.1:8090/api/collections/data_source/records', 
    headers={'Authorization': auth_token}).json()

def format_selections(data_source):
    return f'{data_source["subreddit"]}:{data_source["search_term"]}'
def get_data(data_source):
    com_value = neg_value = neu_value =pos_value = 0
    response = requests.get(
        f"http://127.0.0.1:8090/api/collections/data/records?filter=(data_source=\'{data_source['id']}\')", 
        headers={'Authorization': auth_token}).json()
    item_count = response['totalItems']
    for item in response['items']:
        com_value += item['sentiment']['compound']
        neg_value += item['sentiment']['neg']
        neu_value += item['sentiment']['neu']
        pos_value += item['sentiment']['pos']
    com_value = com_value / item_count
    neg_value = neg_value / item_count
    neu_value = neu_value / item_count
    pos_value = pos_value / item_count
    return com_value, neg_value, neu_value, pos_value
select_data_source = st.form('select_data_sources')
selectbox_data = select_data_source.selectbox(label='Choose Data Source:', options=response['items'], format_func=format_selections)
selectbox_submit = select_data_source.form_submit_button('Change Data Source')
com_value = neg_value = neu_value = pos_value = 0
if selectbox_submit:
    com_value, neg_value, neu_value, pos_value = get_data(selectbox_data)


# TESTING

response = requests.get(
    'http://127.0.0.1:8090/api/collections/data/records', 
    headers={'Authorization': auth_token}).json()

com, neg, neu, pos = st.columns(4)
com.metric('Compound',com_value)
neg.metric('Negative', neg_value)
neu.metric('Neutral',neu_value)
pos.metric('Positive',pos_value)

date_input, graph = st.columns(2)
date_input.form('Date Range')
start_date = date_input.date_input("start date")
end_date = date_input.date_input("end date")
graph.line_chart(response['items'][0]['sentiment'])