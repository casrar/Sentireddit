from flask import Flask
from flask import request
from markupsafe import escape
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from dotenv import dotenv_values

config = dotenv_values(".env")
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

app = Flask(__name__)

@app.post("/analyze")
def analyze():
    data = request.get_json()
    data = data['body']
    analysis = sia.polarity_scores(data)
    return { "analysis": analysis }
