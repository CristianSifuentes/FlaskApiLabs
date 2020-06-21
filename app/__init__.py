from flask import Flask

app = Flask(__name__)

def create_app(enviroment):
    app.confi.from_object(enviroment)
    return app