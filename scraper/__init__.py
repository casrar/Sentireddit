from flask import Flask, make_response, request
from scraper import scraper, config


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/scrape', methods=['GET'])
    def scrape():
        if request.method != 'GET':
            return make_response('Bad Request', 400)
        scraper.scrape()
        return 200
    
    return app