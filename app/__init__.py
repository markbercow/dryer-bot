from flask import Flask
from app.routes import init_routes

def create_app():
    app = Flask(__name__, static_folder="../static", template_folder="../templates")
    init_routes(app)
    return app
