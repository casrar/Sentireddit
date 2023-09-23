from flask import Flask, render_template, request
import requests 
from dotenv import dotenv_values
import datetime
from datetime import date, datetime as dt
import urllib.parse
import plotly.express as px
import pandas as pd
from statistics import mean 
from flask_htmx import HTMX
import jinja_partials

config = dotenv_values(".env")
# error check and log
try:
    response = requests.post(
        'http://127.0.0.1:8090/api/collections/users/auth-with-password', 
        data={'identity': config['IDENTITY'], 'password': config['PASSWORD']}).json()
except:
    #log
    print('Error with database, quiting')
    quit()
auth_token = response['token']

app = Flask(__name__)
htmx = HTMX(app)
jinja_partials.register_extensions(app)

def calculate_average_sentiments(items):
    avg_compound = avg_pos = avg_neu = avg_neg = 0 
    if len(items) < 1:
        return avg_compound, avg_pos, avg_neu, avg_neg
    compound_list, pos_list, neu_list, neg_list = [], [], [], []
    for item in items:
        compound_list.append(item['compound'])
        pos_list.append(item['pos'])
        neu_list.append(item['neu'])
        neg_list.append(item['neg'])
    return mean(compound_list), mean(pos_list), mean(neu_list), mean(neg_list), 

def sentiment_observation(avg_compound): # error with overwhelmingly negative, compound = .3
    if avg_compound > 0.9:
        return 'overwhelmingly positive'
    elif avg_compound < 0.9 and avg_compound > 0.6:
        return 'very positive'
    elif avg_compound < 0.6 and avg_compound > 0.3:
        return 'positive'
    elif avg_compound < 0.3 and avg_compound > 0.15:
        return 'slightly positive'
    elif avg_compound < 0.15 and avg_compound > -0.15:
        return 'mixed'
    elif avg_compound < -0.15 and avg_compound > -0.3:
        return 'slightly negative'
    elif avg_compound < -0.3 and avg_compound > -0.6:
        return 'negative'
    elif avg_compound < -0.6 and avg_compound > -0.9:
        return 'very negative'
    else:
        return 'overwhelmingly negative'

def get_max_items(request):
    print(response)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('index.html')

@app.route('/data_management', methods=['POST', 'GET'])
def data_management():
    context = {}
    response = requests.get('http://127.0.0.1:8090/api/collections/data_source/records').json() 
    context['data_sources'] = response['items']
    response = requests.get('http://127.0.0.1:8090/api/collections/data/records').json() 
    context['data'] = response['items']

    if request.method == 'POST' and request.form['form-id'] == 'add-data-source':
        data = {
            'subreddit': request.form['subreddit'],
            'search_term': request.form['search-term']
        }
        response = requests.post('http://127.0.0.1:8090/api/collections/data_source/records',
                                 json=data).json() 
    if request.method == 'POST' and request.form['form-id'] == 'remove-data-source':
        selected_data = request.form.getlist('selected-data')
        for data in selected_data:
            response = requests.delete(f'http://127.0.0.1:8090/api/collections/data_source/records/{data}')
    if request.method == 'POST' and request.form['form-id'] == 'remove-data':
        selected_data = request.form.getlist('selected-data')
        for data in selected_data:
            response = requests.delete(f'http://127.0.0.1:8090/api/collections/data/records/{data}')
   

    return render_template('data_management.html', context=context)

@app.route('/analytics', methods=['POST', 'GET'])
def analytics():
    context = {}
    response = requests.get('http://127.0.0.1:8090/api/collections/data_source/records').json() 
    data = {'x': 'compound list', 'y': [], 'type': 'violin', 'mode': 'markers'}
    layout = {'title': 'Compound'}
    chart_data = {'data': [data], 'layout': layout}
    context['data_sources'] = response['items']
    if request.method == 'POST' and request.form['form-id'] == 'select-data-source':
        # need to grab all data from response, I believe I am not grabbing it all
        
        first_date = int (dt.strptime(request.form['first-date'], '%Y-%m-%d').timestamp())
        second_date = int (dt.strptime(request.form['second-date'], '%Y-%m-%d').timestamp())
        params = {
            'filter': f'(data_source=\'{request.form["data-source-selection"]}\' && post_date >= {first_date} && post_date <= {second_date})'
        }
        response = requests.get('http://127.0.0.1:8090/api/collections/data/records',
                                params=params,
                                headers={'Authorization': auth_token}).json() 
        items = response['items']

        context['avg_compound'], context['avg_pos'], context['avg_neu'], context['avg_neg'] = calculate_average_sentiments(items)
        context['avg_compound'] = round(context['avg_compound'], 2)
        context['avg_pos'] = round(context['avg_pos'], 2)
        context['avg_neu'] = round(context['avg_neu'], 2) 
        context['avg_neg'] = round(context['avg_neg'], 2) 
        
        context['summary'] = sentiment_observation(context['avg_compound'])
        compound_list = []
        for item in items:
            compound_list.append(item['compound'])
        print(compound_list)
        data = {'x': 'compound list', 'y': compound_list, 'type': 'violin', 'mode': 'markers', 'points': 'all'}
        layout = {'title': 'Compound'}
        chart_data = {'data': [data], 'layout': layout}

        params = {
            'sort': '-pos',
            'perPage': '1',
            'filter': f'(data_source=\'{request.form["data-source-selection"]}\' && post_date >= {first_date} && post_date <= {second_date})'
        }
        response = requests.get('http://127.0.0.1:8090/api/collections/data/records',
                                params=params,
                                headers={'Authorization': auth_token}).json() 
        items = response['items']
        context['most_positive_post'] = items[0]['body'] if items else 'N/A'
        params = {
            'sort': '+neg',
            'perPage': '1',
            'filter': f'(data_source=\'{request.form["data-source-selection"]}\' && post_date >= {first_date} && post_date <= {second_date})'
        }
        response = requests.get('http://127.0.0.1:8090/api/collections/data/records',
                                params=params,
                                headers={'Authorization': auth_token}).json() 
        items = response['items']
        context['most_negative_post'] = items[0]['body'] if items else 'N/A'
        
    return render_template('analytics.html', context=context, chart_data=chart_data)

