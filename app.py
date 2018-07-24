import os

import requests
from flask import Flask, render_template, url_for, json
from flask_mail import Mail
import sched, time
from datetime import date, datetime
from apscheduler.schedulers.background import BlockingScheduler

import create_tables
import temp
from common.utils import Utils

app = Flask(__name__)
# app.config.from_object('config')
app.DEBUG = True
app.secret_key = "v12awards34"
app.config.update(
    DEBUG=True,
    # EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='myidispg@gmail.com',
    MAIL_PASSWORD=temp.PASSWORD
)
mail = Mail(app)


@app.before_first_request
def init_db():
    # Database.initialize()
    create_tables


@app.before_request
def email_alerts():
    if datetime.now() > datetime(2018, 7, 24, 12, 9, 0):
        list = Utils.email_alerts()
        print(list)
    else:
        pass


def is_human(captcha_response):
    """
    Recaptcha validation method
    Validating recaptcha response from google server
    Returns True captcha test passed for submitted form else returns False.

    """
    secret = "6LfKAGUUAAAAAAQ3J0KZuL9NYdfgTDFtHP3HcsOq"
    payload = {'response': captcha_response, 'secret': secret}
    response = requests.post("https://www.google.com/recaptcha/api/siteverify", payload)
    response_text = json.loads(response.text)
    return response_text['success']


@app.route('/')
def home_english():
    return render_template('base.html', language=0, sitekey="6LfKAGUUAAAAABDEXB8lTMBclklOSWtBorh70Say")


@app.route('/hi/')
def home_hindi():
    return render_template('base.html', language=1, sitekey="6LfKAGUUAAAAABDEXB8lTMBclklOSWtBorh70Say")


from models.users.views import user_blueprint
from models.form_1.views import form1_blueprint
from models.form_2.views import form2_blueprint

app.register_blueprint(user_blueprint, url_prefix='/users')
app.register_blueprint(form1_blueprint, url_prefix='/users/form1')
app.register_blueprint(form2_blueprint, url_prefix='/users/form2')

if __name__ == "__main__":
    # app.jinja_env.auto_reload = True
    # app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(Debug=True)


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
