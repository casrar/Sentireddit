from flask import Flask, render_template
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('index.html')

@app.route('/data_management')
def data_management():
    return render_template('data_management.html')

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')