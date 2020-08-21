import os

from flask import Flask
from flask_cors import CORS

from src.controller.RoomController import chat_controller


class FlaskConfig:
    app = Flask(__name__)
    cors = CORS(app)

    def __call__(self):
        self.register_blue_prints()
        self.run_app()

    def register_blue_prints(self):
        self.app.register_blueprint(chat_controller)

    def run_app(self):
        self.app.run(
            debug=True,
            use_reloader=False,
            host=os.getenv("FLASK_HOST"),
            port=os.getenv("FLASK_PORT")
        )
