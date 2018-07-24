import goslate
from flask import Blueprint, request, session, redirect, url_for, render_template
from flask_mail import Message

from common.database_user import Database
from common.utils import Utils
from models.users.user import User
import models.users.errors as UserErrors
from app import mail
user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email_login']
        password = request.form['password_login']

        try:
            if User.is_login_valid(email, password):
                session['email'] = email
                return redirect(url_for('.user_dashboard'))
        except UserErrors.UserError as e:
            return e.message

    # this return works if the request method is GET or the login credentials are invalid
    return render_template('base.html', language=0)


@user_blueprint.route('/hi/login', methods=['GET', 'POST'])
def login_user_hindi():
    if request.method == 'POST':
        email = request.form['email_login_hindi']
        password = request.form['password_login_hindi']

        try:
            if User.is_login_valid(email, password):
                session['email'] = email
                return redirect(url_for('.user_dashboard'))
        except UserErrors.UserError as e:
            gs = goslate.Goslate()
            message = gs.translate(e.message, 'hi')
            return message

    # this return works if the request method is GET or the login credentials are invalid
    return render_template('base.html', language=1)


@user_blueprint.route('register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form.get('new_password')
        name = request.form.get('name')
        phone_no = request.form.get('phone_no')
        male_gender = request.form.get('gender_male')
        female_gender = request.form.get('gender_female')
        gender = 'M' if female_gender is None else 'F'
        dob = request.form.get('dob')
        captcha_response = request.form.get('g-recaptcha-response')

        try:
            if Utils.is_human(captcha_response):
                if User.register_user(email, password, name, phone_no, gender, dob):
                    session['email'] = email
                    user = User.get_user_object(email)
                    msg = Message('Verify your email',
                                  sender='myidispg@gmail.com',
                                  recipients=[email])
                    msg.body = 'Please verify your email by clicking on the following link-' \
                               ' http://127.0.0.1:5000/users/user-verify/{}\n\n\n' \
                               'कृपया निम्न लिंक पर क्लिक करके अपना ईमेल सत्यापित करें-' \
                               ' http://127.0.0.1:5000/users/hi/user-verify/{}'.format(user._id, user._id)
                    mail.send(msg)
                    return 'Please check your inbox for verification of the email before accessing your dashboard'
                    # return redirect(url_for('.user_dashboard'))
            else:
                return "Please verify the captcha"
        except UserErrors.UserError as e:
            return e.message

    return render_template('base.html', language=0)


@user_blueprint.route('/hi/register', methods=['GET', 'POST'])
def register_user_hindi():
    if request.method == 'POST':
        email = request.form['email_hindi']
        password = request.form.get('new_password_hindi')
        name = request.form.get('name_hindi')
        phone_no = request.form.get('phone_no_hindi')
        male_gender = request.form.get('gender_male_hindi')
        female_gender = request.form.get('gender_female_hindi')
        gender = 'M' if female_gender is None else 'F'
        dob = request.form.get('dob_hindi')
        captcha_response = request.form.get('g-recaptcha-response')

        try:
            if Utils.is_human(captcha_response):
                if User.register_user(email, password, name, phone_no, gender, dob):
                    session['email'] = email
                    user = User.get_user_object(email)
                    msg = Message('Verify your e-mail',
                                  sender='myidispg@gmail.com',
                                  recipients=[email])
                    msg.body = 'Please verify your email by clicking on the following link-' \
                               ' http://127.0.0.1:5000/users/user-verify/{}\n\n\n' \
                               'कृपया निम्न लिंक पर क्लिक करके अपना ईमेल सत्यापित करें-' \
                               ' http://127.0.0.1:5000/users/hi/user-verify/{}'.format(user._id, user._id)
                    mail.send(msg)
                    return 'अपने डैशबोर्ड तक पहुंचने से पहले ईमेल के सत्यापन के लिए कृपया अपना इनबॉक्स जांचें'
                    # return redirect(url_for('.user_dashboard_hindi'))
            else:
                gs = goslate.Goslate()
                message = gs.translate("Please verify the captcha", 'hi')
                return message
        except UserErrors.UserError as e:
            gs = goslate.Goslate()
            message = gs.translate(e.message, 'hi')
            return message

    return render_template('base.html', language=1)


@user_blueprint.route('user-dashboard')
def user_dashboard():
    email = session['email']
    return render_template('user_dash_apply2.html', email=email)
    # return "Welcome to your dashboard {}!".format(email)


@user_blueprint.route('/hi/user-dashboard')
def user_dashboard_hindi():
    email = session['email']
    return render_template('user_dash_apply2.html', email=email)
    # return "आपके डैशबोर्ड में आपका स्वागत है {}!".format(email)


@user_blueprint.route('user-verify/<string:_id>')
def activation_email(_id):
    user = User.get_user_object(_id=_id)
    if user.email_verified == 'no':
        user.save_email_verified_status()
        return redirect(url_for('.user_dashboard'))
    else:
        return 'The email is already verified.'


@user_blueprint.route('/hi/user-verify/<string:_id>')
def activation_email_hindi(_id):
    user = User.get_user_object(_id=_id)
    if user.email_verified == 'no':
        user.save_email_verified_status()
        return redirect(url_for('.user_dashboard_hindi'))
    else:
        # return 'ईमेल पहले से ही सत्यापित है।'
        gs = goslate.Goslate()
        message = gs.translate('The email is already verified', 'hi')
        return message
