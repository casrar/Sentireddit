from flask import Flask
from website.routes import about, analytics, management


def create_app():
    app = Flask(__name__, instance_relative_config=True, template_folder='templates', static_folder='static')
    
    app.register_blueprint(about)
    app.register_blueprint(analytics)
    app.register_blueprint(management)

    return app