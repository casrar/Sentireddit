from flask import Flask, render_template, request
import requests 
from dotenv import dotenv_values
import urllib.parse
import plotly.express as px
import pandas as pd
from flask_htmx import HTMX
import jinja_partials
import utils

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

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('index.html')

@app.route('/data_management', methods=['POST', 'GET'])
def data_management():
    context = {}
    context['data_sources'] = utils.get_all_data_sources(auth_token)['items']
    context['data'] = utils.get_all_data(auth_token)['items']

    return render_template('data_management.html', context=context)

@app.route('/add_data_source', methods=['POST'])
def add_data_source():
    context = {}
    data = {
        'subreddit': request.form['subreddit'],
        'search_term': request.form['search-term']
    }
    response = requests.post('http://127.0.0.1:8090/api/collections/data_source/records',
                                json=data).json()     
    context['data_sources'] = utils.get_all_data_sources(auth_token)['items']
    return render_template('/partials/data_sources.html', context=context)

@app.route('/remove_data_source', methods=['DELETE'])
def remove_data_source():
    context = {}
    selected_data = request.form.getlist('selected-data')
    for id in selected_data:
        response = requests.delete(f'http://127.0.0.1:8090/api/collections/data_source/records/{id}')
    context['data_sources'] = utils.get_all_data_sources(auth_token)['items']

    return render_template('/partials/data_sources.html', context=context)

@app.route('/remove_data', methods=['DELETE'])
def remove_data():
    context = {}
    selected_data = request.form.getlist('selected-data')
    for id in selected_data:
        response = requests.delete(f'http://127.0.0.1:8090/api/collections/data/records/{id}')
    context['data'] = utils.get_all_data(auth_token)['items']
        
    return render_template('/partials/data.html', context=context)

@app.route('/analytics', methods=['POST', 'GET'])
def analytics():
    context = {}
    response = requests.get('http://127.0.0.1:8090/api/collections/data_source/records').json() 
    data = {'x': 'compound list', 'y': [], 'type': 'violin', 'mode': 'markers'}
    layout = {'title': 'Compound'}
    # chart_data = {'data': [data], 'layout': layout}
    chart_data = None
    context['data_sources'] = response['items']


    # if request.method == 'POST' and request.form['form-id'] == 'select-data-source':
    #     # need to grab all data from response, I believe I am not grabbing it all
        
    #     first_date = int (dt.strptime(request.form['first-date'], '%Y-%m-%d').timestamp())
    #     second_date = int (dt.strptime(request.form['second-date'], '%Y-%m-%d').timestamp())
    #     params = {
    #         'filter': f'(data_source=\'{request.form["data-source-selection"]}\' && post_date >= {first_date} && post_date <= {second_date})'
    #     }
    #     response = requests.get('http://127.0.0.1:8090/api/collections/data/records',
    #                             params=params,
    #                             headers={'Authorization': auth_token}).json() 
    #     items = response['items']

    #     context['avg_compound'], context['avg_pos'], context['avg_neu'], context['avg_neg'] = utils.calculate_average_sentiments(items)
    #     context['avg_compound'] = round(context['avg_compound'], 2)
    #     context['avg_pos'] = round(context['avg_pos'], 2)
    #     context['avg_neu'] = round(context['avg_neu'], 2) 
    #     context['avg_neg'] = round(context['avg_neg'], 2) 
        
    #     context['summary'] = utils.sentiment_observation(context['avg_compound'])
    #     compound_list = []
    #     for item in items:
    #         compound_list.append(item['compound'])
    #     print(compound_list)
    #     data = {'x': 'compound list', 'y': compound_list, 'type': 'violin', 'mode': 'markers', 'points': 'all'}
    #     layout = {'title': 'Compound'}
    #     chart_data = {'data': [data], 'layout': layout}

    #     params = {
    #         'sort': '-pos',
    #         'perPage': '1',
    #         'filter': f'(data_source=\'{request.form["data-source-selection"]}\' && post_date >= {first_date} && post_date <= {second_date})'
    #     }
    #     response = requests.get('http://127.0.0.1:8090/api/collections/data/records',
    #                             params=params,
    #                             headers={'Authorization': auth_token}).json() 
    #     items = response['items']
    #     context['most_positive_post'] = items[0]['body'] if items else 'N/A'
    #     params = {
    #         'sort': '+neg',
    #         'perPage': '1',
    #         'filter': f'(data_source=\'{request.form["data-source-selection"]}\' && post_date >= {first_date} && post_date <= {second_date})'
    #     }
    #     response = requests.get('http://127.0.0.1:8090/api/collections/data/records',
    #                             params=params,
    #                             headers={'Authorization': auth_token}).json() 
    #     items = response['items']
    #     context['most_negative_post'] = items[0]['body'] if items else 'N/A'
        
    return render_template('analytics.html', context=context, chart_data=chart_data)


@app.route('/update_graph', methods=['POST'])
def update_graph():
    context = {}
    chart_data = None
    chart_type = request.form['chartType']
    data_source = request.form['data-source-selection']
    first_date = request.form['first-date']
    second_date = request.form['second-date']

    # if data sources not selected, then return nothing
    if (utils.is_empty(chart_type) or utils.is_empty(data_source) or 
        utils.is_empty(first_date) or utils.is_empty(second_date)):    
        return render_template('analytics.html', context=context, chart_data=chart_data)
    
    if not (chart_type == 'Compound' or chart_type == 'Positive' or chart_type == 'Neutral' or chart_type == 'Negative'):
        return render_template('analytics.html', context=context, chart_data=chart_data)
    
    items = utils.get_all_data_in_date_range(first_date=first_date, second_date=second_date, data_source=data_source, auth_token=auth_token)['items']
    x_label = f'{chart_type} list'
    data = {'x': x_label, 'y': items, 'type': 'violin', 'mode': 'markers'}
    layout = {'title': chart_type}
    chart_data = {'data': [data], 'layout': layout}
    return render_template('analytics.html', context=context, chart_data=chart_data)

@app.route('/update_data_source', methods=['POST'])
def update_data_source():
    context = {}
    response = requests.get('http://127.0.0.1:8090/api/collections/data_source/records').json() 
    data = {'x': 'compound list', 'y': [], 'type': 'violin', 'mode': 'markers'}
    layout = {'title': 'Compound'}
    # chart_data = {'data': [data], 'layout': layout}
    chart_data = None
    context['data_sources'] = response['items']
    # if data sources arent selected then dont return anything
    # return updated data
    print(request.form)
    return render_template('analytics.html', context=context, chart_data=chart_data)