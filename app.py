from flask import Flask

from common.database import Database

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = "v12awards34"


@app.before_first_request
def init_db():
    Database.initialize()


@app.route('/')
def hello_world():
    return 'Hello World!'

from models.users.views import user_blueprint

app.register_blueprint(user_blueprint, url_prefix='/users')
