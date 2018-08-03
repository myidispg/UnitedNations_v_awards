import os

from flask import Flask, render_template, url_for
from flask_mail import Mail
from datetime import datetime

import create_tables
import temp
from models.admin.views import admin_blueprint, get_mail
from temp import *
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
    get_mail(mail)
    current_directory = os.getcwd()
    profile_pictures_directory = os.path.join(current_directory, 'profile-pictures')
    if not os.path.exists(profile_pictures_directory):
        os.makedirs(profile_pictures_directory)


@app.route('/send_email_alerts/email_alerts/form_1')
def email_alerts_form_1():
    # if date is greater than reminder date but less than one day added to the reminder date,
    #  the function will proceed.
    if datetime(form_1_reminder_1_year, form_1_reminder_1_month, form_1_reminder_1_day + 1,
                form_1_reminder_1_hour, form_1_reminder_1_minute, form_1_reminder_1_seconds) > \
            datetime.now() > \
            datetime(form_1_reminder_1_year, form_1_reminder_1_month, form_1_reminder_1_day,
                     form_1_reminder_1_hour, form_1_reminder_1_minute, form_1_reminder_1_seconds):
        EmailAlerts.email_alerts_form_1(mail, 'reminder_1')
    elif datetime(form_1_reminder_2_year, form_1_reminder_2_month, form_1_reminder_2_day + 1,
                  form_1_reminder_2_hour, form_1_reminder_2_minute, form_1_reminder_2_seconds) > \
            datetime.now() > \
            datetime(form_1_reminder_2_year, form_1_reminder_2_month, form_1_reminder_2_day,
                     form_1_reminder_2_hour, form_1_reminder_2_minute, form_1_reminder_2_seconds):
        EmailAlerts.email_alerts_form_1(mail, 'reminder_2')
    else:
        pass

    return 'emails sent'


@app.route('/send_email_alerts/email_alerts/form_2')
def email_alerts_form_2():
    # if date is greater than reminder date but less than one day added to the reminder date,
    # the function will proceed.
    if datetime(form_2_reminder_1_year, form_2_reminder_1_month, form_2_reminder_1_day + 1,
                form_2_reminder_1_hour, form_2_reminder_1_minute, form_2_reminder_1_seconds) > \
            datetime.now() > \
            datetime(form_2_reminder_1_year, form_2_reminder_1_month, form_2_reminder_1_day,
                     form_2_reminder_1_hour, form_2_reminder_1_minute, form_2_reminder_2_seconds):
        EmailAlerts.email_alerts_form_2(mail, 'reminder_1')
    elif datetime(form_2_reminder_2_year, form_2_reminder_2_month, form_2_reminder_2_day + 1,
                  form_2_reminder_2_hour, form_2_reminder_2_minute, form_2_reminder_2_seconds) > \
            datetime.now() > \
            datetime(form_2_reminder_2_year, form_2_reminder_2_month, form_2_reminder_2_day,
                     form_2_reminder_2_hour, form_2_reminder_2_minute, form_2_reminder_2_seconds):
        EmailAlerts.email_alerts_form_2(mail, 'reminder_2')
    else:
        pass

    return 'emails sent'


@app.route('/')
def home_english():
    # thread = threading.Thread(target=email_alerts, args=())
    # thread.daemon = True
    # thread.start()
    return render_template('base.html', language=0)


@app.route('/hi/')
def home_hindi():
    return render_template('base.html', language=1, sitekey="6LfKAGUUAAAAABDEXB8lTMBclklOSWtBorh70Say")


from models.users.views import user_blueprint
from models.form_1.views import form1_blueprint
from models.form_2.views import form2_blueprint

app.register_blueprint(user_blueprint, url_prefix='/users')
app.register_blueprint(form1_blueprint, url_prefix='/users/form1')
app.register_blueprint(form2_blueprint, url_prefix='/users/form2')
app.register_blueprint(admin_blueprint, url_prefix='/admin')


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
