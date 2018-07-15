from flask import Flask, render_template

from common.database_user import Database
import create_tables

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = "v12awards34"


@app.before_first_request
def init_db():
    # Database.initialize()
    create_tables


@app.route('/')
def home():
    return render_template('forms/register.html')

from models.users.views import user_blueprint

app.register_blueprint(user_blueprint, url_prefix='/users')
