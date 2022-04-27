from flask import Flask
def create_app():
    app = Flask(__name__)
    @app.route("/")
    def hello_world():
        return {
            "msg": "Hello from app 2!"
        }
    return app
