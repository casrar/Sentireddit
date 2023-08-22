from flask import Flask, render_template, request
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

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('index.html')

@app.route('/data_management', methods=['POST', 'GET'])
def data_management():
    response = requests.get('http://127.0.0.1:8090/api/collections/data_source/records').json() 
    context = {}
    context['data_sources'] = response['items']
    response = requests.get('http://127.0.0.1:8090/api/collections/data/records').json() 
    context['data'] = response['items']

    if request.method == 'POST':
        print('post')

    return render_template('data_management.html', context=context)

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')