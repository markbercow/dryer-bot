from flask import Flask
from flask_socketio import SocketIO, emit
from app.routes import init_routes
from app.status import dryer_status

socketio = SocketIO(cors_allowed_origins="*")

@socketio.on("connect")
def handle_connect():
    emit("status", dryer_status)

def create_app():
    app = Flask(__name__, static_folder="../static", template_folder="../templates")
    init_routes(app)
    socketio.init_app(app)
    return app
