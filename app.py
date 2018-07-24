import os

from flask import Flask, render_template, url_for
from flask_mail import Mail
from datetime import date, datetime
import threading

import create_tables
import temp
from email_alerts import EmailAlerts

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


@app.route('/send_email_alerts/email_alerts')
def email_alerts():
    # if the datetime is greater than datetime set for email alerts,
    #  this function will proceed otherwise pass
    if datetime(2018, 7, 25, 0, 0, ) > datetime.now() > datetime(2018, 7, 24, 12, 9, 0):
        EmailAlerts.email_alerts(mail, 'reminder_1')
    elif datetime(2018, 7, 28, 0, 0, ) > datetime.now() > datetime(2018, 7, 28, 12, 9, 0):
        EmailAlerts.email_alerts(mail, 'reminder_2')
    else:
        pass

    return 'emails sent'


@app.route('/')
def home_english():
    # thread = threading.Thread(target=email_alerts, args=())
    # thread.daemon = True
    # thread.start()
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
