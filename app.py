from flask import Flask, render_template

from common.database_user import Database
import common.language as language
import create_tables

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = "v12awards34"


@app.before_first_request
def init_db():
    # Database.initialize()
    create_tables


@app.route('/')
def home_english():
    return render_template('forms/register.html', language=0)


@app.route('/hi/')
def home_hindi():
    return render_template('forms/register.html', language=1)


from models.users.views import user_blueprint

app.register_blueprint(user_blueprint, url_prefix='/users')
