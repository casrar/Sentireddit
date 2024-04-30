from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
from reddit_new_comment_iterator import RedditNewCommentIterator
from utils.database.database import auth_with_password, get_all_data_sources
from utils.logger.logger import get_logger
import os
import requests
from nltk.sentiment.vader import SentimentIntensityAnalyzer

logger = get_logger()
scraper = Flask(__name__)
sia = SentimentIntensityAnalyzer()

def __post_comment_to_db(url: str, data: dict, auth_token: str) -> None:
    requests.post('http://127.0.0.1:8090/api/collections/data/records', json=data, headers={'Authorization': auth_token}).raise_for_status()

@scraper.errorhandler(HTTPException)
def handle_exception(e: HTTPException) -> jsonify:
    return jsonify({'error': e.name, 'message': e.description, 'status': e.code})

@scraper.route('/scrape', methods=('POST'))
def scrape() -> jsonify:
    try:
        auth_token = auth_with_password(url=os.getenv('DB_URL'), identity=os.getenv('DB_IDENTITY'), password=os.getenv('DB_PASSWORD'))
        response = get_all_data_sources(url=os.getenv('DB_URL'), identity=os.getenv('DB_IDENTITY'), password=os.getenv('DB_PASSWORD'))
        data_sources = []
        for data_source in response:
            data_sources.append(RedditNewCommentIterator(
                subreddit=data_source.get('subreddit'),
                query=data_source.get('query'),
                proxy_url=os.getenv('proxyurl'),
                api_key=os.getenv('proxyapikey'))
            )
        for data_source in data_sources:
            for comment in data_source:
                data = sia.polarity_scores(comment[0])
                __post_comment_to_db(url=os.getenv('DB_URL'), data=data, auth_token=auth_token)
    except Exception as e:
        logger.warning(f'Error with scrape(): {e}')
        return jsonify({'error': e.name, 'message': e.description, 'status': e.code})
    return jsonify({'status': 200})
