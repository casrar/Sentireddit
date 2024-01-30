from flask import Flask, render_template, request
import requests 
from dotenv import dotenv_values
import urllib.parse
import plotly.express as px
import pandas as pd
from flask_htmx import HTMX
import jinja_partials
import utils.utils as utils


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
    try:
        context['data_sources'] = utils.get_all_data_sources(auth_token)['items']
        context['data'] = utils.get_all_data(auth_token)['items']
    except:
        if 'data_sources' not in context:
            context['data_sources'] = {}
        if 'data' not in context:
            context['data'] = {}

    return render_template('data_management.html', context=context)

@app.route('/add_data_source', methods=['POST'])
def add_data_source():
    context = {}
    data = {
        'subreddit': request.form['subreddit'],
        'query': request.form['query']
    }
    response = requests.post('http://127.0.0.1:8090/api/collections/data_source/records',
                                json=data).json()     
    context['data_sources'] = utils.get_all_data_sources(auth_token)['items']
    return render_template('/partials/data_sources.html', context=context)

@app.route('/remove_data_source', methods=['DELETE'])
def remove_data_source():
    context = {}
    selected_data = request.form.getlist('selected-data')
    data = []
    for id in selected_data:
        data += utils.get_all_data_from_data_source(data_source=id, auth_token=auth_token)['items']
    for item in data: 
        id = item['id']
        response = requests.delete(f'http://127.0.0.1:8090/api/collections/data/records/{id}')

    for id in selected_data:
        response = requests.delete(f'http://127.0.0.1:8090/api/collections/data_source/records/{id}')
    try:
        context['data_sources'] = utils.get_all_data_sources(auth_token)['items']
        context['data'] = utils.get_all_data(auth_token)['items']
    except:
        if 'data_sources' not in context:
            context['data_sources'] = {}
        if 'data' not in context:
            context['data'] = {}
    return render_template('/partials/data_sources_and_data.html', context=context)

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
    chart_data = None
    context['data_sources'] = response['items']
        
    return render_template('analytics.html', context=context, chart_data=chart_data)


@app.route('/update_graph', methods=['POST'])
def update_graph():
    context = {}
    chart_data = None

    validated_form = utils.validate_analytics_form(request) 
    if validated_form is None:
        return render_template('partials/chart.html', context=context, chart_data=chart_data)
    chart_type, data_source, first_date, second_date = validated_form
    
    chart_data = utils.generate_chart(chart_type=chart_type, first_date=first_date, second_date=second_date, data_source=data_source, auth_token=auth_token)
    if chart_data is None:
        return render_template('partials/chart.html', context=context, chart_data=chart_data)

    return render_template('partials/chart.html', context=context, chart_data=chart_data)

@app.route('/update_data_source', methods=['POST'])
def update_data_source():
    context = {}
    chart_data = None
    
    validated_form = utils.validate_analytics_form(request) 
    if validated_form is None:
        return render_template('partials/analytics_metrics.html', context=context, chart_data=chart_data)
    chart_type, data_source, first_date, second_date = validated_form

    chart_data = utils.generate_chart(chart_type=chart_type, first_date=first_date, second_date=second_date, data_source=data_source, auth_token=auth_token)
    if chart_data is None:
        return render_template('partials/chart.html', context=context, chart_data=chart_data)
    
    items = utils.get_all_data_in_date_range(first_date=first_date, second_date=second_date, data_source=data_source, auth_token=auth_token)['items']
    if not items: # Return nothing if no data exists
        return render_template('partials/analytics_metrics.html', context=context, chart_data=chart_data)
    context['avg_compound'], context['avg_pos'], context['avg_neu'], context['avg_neg'] = utils.calculate_average_sentiments(items)
    context['avg_compound'] = round(context['avg_compound'], 2)
    context['avg_pos'] = round(context['avg_pos'], 2)
    context['avg_neu'] = round(context['avg_neu'], 2) 
    context['avg_neg'] = round(context['avg_neg'], 2) 
    context['summary'] = utils.sentiment_observation(context['avg_compound'])
    context['most_positive_post'] = utils.get_most_positive_data_record(first_date=first_date, second_date=second_date, data_source=data_source, auth_token=auth_token)
    context['most_negative_post'] = utils.get_most_negative_data_record(first_date=first_date, second_date=second_date, data_source=data_source, auth_token=auth_token)
    return render_template('partials/analytics_metrics.html', context=context, chart_data=chart_data)