from statistics import mean 
import requests 
import datetime
from datetime import date, datetime as dt

def is_empty(x):
    if x == '':
        return True
    if x is None:
        return True
    return False

def validate_analytics_form(request):
    chart_type = request.form['chartType']
    data_source = request.form['data-source-selection']
    first_date = request.form['first-date']
    second_date = request.form['second-date']
    if (is_empty(chart_type) or is_empty(data_source) or 
        is_empty(first_date) or is_empty(second_date)):    
        return None

    if not (chart_type == 'Compound' or chart_type == 'Positive' or chart_type == 'Neutral' or chart_type == 'Negative'):
        return None
    
    return chart_type, data_source, first_date, second_date

def get_chart_type_index(chart_type):
    if chart_type == 'Compound':
        return 'compound'
    if chart_type == 'Positive':
        return 'pos'
    if chart_type == 'Neutral':
        return 'neu'
    if chart_type == 'Negative':
        return 'neg'
    return None

def generate_chart(chart_type, first_date, second_date, data_source, auth_token):
    fill_colors = {
        'Compound': 'f3e8ff',
        'Positive': 'dcfce7',
        'Neutral': 'f1f5f9',
        'Negative': 'fee2e2'
    }
    sentiment_list = []
    items = get_all_data_in_date_range(first_date=first_date, second_date=second_date, data_source=data_source, auth_token=auth_token)['items']
    chart_type_index = get_chart_type_index(chart_type=chart_type)
    if chart_type_index is None:
        return None
    for item in items:
        sentiment_list.append(item[chart_type_index])
    x_label = f'{chart_type} list'
    data = {'x': x_label, 'y': sentiment_list, 'type': 'violin', 'fillcolor': fill_colors[chart_type], 'mode': 'markers', 'points': 'all'}
    layout = {'title': chart_type}
    chart_data = {'data': [data], 'layout': layout}
    return chart_data

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
    if avg_compound >= 0.9:
        return 'overwhelmingly positive'
    elif avg_compound < 0.9 and avg_compound >= 0.6:
        return 'very positive'
    elif avg_compound < 0.6 and avg_compound >= 0.3:
        return 'positive'
    elif avg_compound < 0.3 and avg_compound >= 0.15:
        return 'slightly positive'
    elif avg_compound < 0.15 and avg_compound >= -0.15:
        return 'mixed'
    elif avg_compound < -0.15 and avg_compound >= -0.3:
        return 'slightly negative'
    elif avg_compound < -0.3 and avg_compound >= -0.6:
        return 'negative'
    elif avg_compound < -0.6 and avg_compound > -0.9:
        return 'very negative'
    else:
        return 'overwhelmingly negative'

def ordered_form_date_to_unix(first_date, second_date):
    first_date = int (dt.strptime(first_date, '%Y-%m-%d').timestamp())
    second_date = int (dt.strptime(second_date, '%Y-%m-%d').timestamp())

    if second_date < first_date:
        return (second_date, first_date)
    return (first_date, second_date)

def get_most_negative_data_record(first_date, second_date, data_source, auth_token):
    dates = ordered_form_date_to_unix(first_date=first_date, second_date=second_date)
    params = {
        'sort': '+neg',
        'perPage': '1',
        'filter': f'(data_source=\'{data_source}\' && post_date >= {dates[0]} && post_date <= {dates[1]})'
    }
    response = requests.get('http://127.0.0.1:8090/api/collections/data/records',
                            params=params,
                            headers={'Authorization': auth_token}).json() 
    items = response['items']
    return items[0]['body'] if items else 'N/A'

def get_most_positive_data_record(first_date, second_date, data_source, auth_token):
    dates = ordered_form_date_to_unix(first_date=first_date, second_date=second_date)
    params = {
        'sort': '-pos',
        'perPage': '1',
        'filter': f'(data_source=\'{data_source}\' && post_date >= {dates[0]} && post_date <= {dates[1]})'
    }
    response = requests.get('http://127.0.0.1:8090/api/collections/data/records',
                            params=params,
                            headers={'Authorization': auth_token}).json() 
    items = response['items']
    return items[0]['body'] if items else 'N/A'

def get_total_records(url, auth_token):
    params = { 'perPage': 1 }
    response = requests.get(url,
                            params=params,
                            headers={'Authorization': auth_token}).json()
    if response['totalItems'] < 1:
        return None
    return response['totalItems']

def get_all_data(auth_token):
    per_page = get_total_records('http://127.0.0.1:8090/api/collections/data/records', auth_token=auth_token)
    if per_page < 1:
        return None
    params = { 'perPage': per_page }
    response = requests.get('http://127.0.0.1:8090/api/collections/data/records',
                            params=params,
                            headers={'Authorization': auth_token}).json() 
    return response

def get_all_data_sources(auth_token):
    per_page = get_total_records('http://127.0.0.1:8090/api/collections/data_source/records', auth_token=auth_token)
    if per_page < 1:
        return None
    params = { 'perPage': per_page }
    response = requests.get('http://127.0.0.1:8090/api/collections/data_source/records',
                            params=params,
                            headers={'Authorization': auth_token}).json() 
    return response

def get_all_data_in_date_range(first_date, second_date, data_source, auth_token):
    per_page = get_total_records('http://127.0.0.1:8090/api/collections/data/records', auth_token=auth_token)
    if per_page < 1:
        return None
    dates = ordered_form_date_to_unix(first_date=first_date, second_date=second_date)
    params = {
            'per_page': per_page,
            'filter': f'(data_source=\'{data_source}\' && post_date >= {dates[0]} && post_date <= {dates[1]})'
        }
    response = requests.get('http://127.0.0.1:8090/api/collections/data/records',
                            params=params,
                            headers={'Authorization': auth_token}).json() 
    return response
