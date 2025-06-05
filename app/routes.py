from flask import jsonify, render_template
from app.status import dryer_status

def init_routes(app):
    @app.route("/status")
    def status():
        return jsonify(dryer_status)

    @app.route("/")
    def index():
        return render_template("index.html")
