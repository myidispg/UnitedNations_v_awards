import io
import csv
from datetime import datetime

from flask import Blueprint, request, make_response

import admin
from common.database_about import About
from common.database_education import Education
from common.database_language import Language
from common.database_reference import Reference
from common.utils import Utils
from email_alerts import EmailAlerts
from models.users.user import User
from temp import *

__author__ = 'myidispg'

admin_blueprint = Blueprint('admin', __name__)


def get_mail(app_mail):
    global mail
    mail = app_mail


@admin_blueprint.route('/save_password', methods=['POST'])
def save_password():
    password = request.form.get('admin_password')
    hashed_password = Utils.hash_password(password)
    admin.ADMIN_PASSWORD = str(hashed_password)

    return str(hashed_password)


@admin_blueprint.route('/auth', methods=['POST', 'GET'])
def login_admin():
    if request.method == 'POST':
        username = request.form.get('admin_username')
        password = request.form.get('admin_password')

        if Utils.check_hashed_password(password, admin.ADMIN_PASSWORD) and username == admin.ADMIN_USERNAME:
            return 'Welcome to admin page'
        else:
            return 'Your credentials were wrong.'
    else:
        return "Page upcoming!!!"


@admin_blueprint.route('/send_email_alerts/email_alerts/form_1')
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


@admin_blueprint.route('/send_email_alerts/email_alerts/form_2')
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


@admin_blueprint.route('/csv_form_1')
def csv_form_1():
    """
    Generates a csv file with form 1 details of all the users in the database.
    :return: returns the name of the excel file.
    """
    user_list = User.get_all_users()
    about_list = About.get_all()
    education_list = Education.get_all()
    reference_list = Reference.get_all()
    language_list = Language.get_all()

    si = io.StringIO()
    wr = csv.writer(si)
    wr.writerow(['email', 'name', 'mobile', 'telephone no', 'gender', 'dob', 'current_address',
                 'permanent_address', 'nationality', 'disability', 'hindi_understand', 'english_understand', ])

    for user in user_list:
        row_list = [user['email'], user['name'], user['mobile'], user['tel_no'], user['gender'],
                    user['dob'], user['current_address'], user['permanent_address'],
                    user['nationality'], user['disability']]

        # wr.writerow([user['email'], user['name'], user['mobile'], user['tel_no'], user['gender'],
        #              user['dob'], user['current_address'], user['permanent_address'],
        #              user['nationality'], user['disability']])
        for language in language_list:
            if language['id'] == user['id']:
                if language['language'] == 'hindi':
                    row_list.append(language['understand'])
                elif language['language'] == 'english':
                    row_list.append(language['understand'])
        wr.writerow(row_list)
    response = make_response(si.getvalue())
    response.headers["Content-Disposition"] = "attachment; filename=form_1.csv"
    response.headers["Content-type"] = "text/csv"

    print(user_list)
    return response
