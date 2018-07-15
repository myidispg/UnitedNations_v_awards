import goslate
from flask import Blueprint, request, session, redirect, url_for, render_template

from models.users.user import User
import models.users.errors as UserErrors

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            if User.is_login_valid(email, password):
                session['email'] = email
                return redirect(url_for('.user_dashboard'))
        except UserErrors.UserError as e:
            return e.message

    # this return works if the request method is GET or the login credentials are invalid
    return render_template('forms/login.html')


@user_blueprint.route('register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form.get('password')
        name = request.form.get('name')
        phone_no = request.form.get('phone_no')
        gender = request.form.get('gender')
        dob = request.form.get('dob')

        try:
            if User.register_user(email, password, name, phone_no, gender, dob):
                session['email'] = email
                return redirect(url_for('.user_dashboard'))
        except UserErrors.UserError as e:
            return e.message

    return render_template('forms/register.html')


@user_blueprint.route('/hi/register', methods=['GET', 'POST'])
def register_user_hindi():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form.get('password')
        name = request.form.get('name')
        phone_no = request.form.get('phone_no')
        gender = request.form.get('gender')
        dob = request.form.get('dob')

        try:
            if User.register_user(email, password, name, phone_no, gender, dob):
                session['email'] = email
                return redirect(url_for('.user_dashboard_hindi'))
        except UserErrors.UserError as e:
            gs = goslate.Goslate()
            message = gs.translate(e.message, 'hi')
            return message

    return render_template('forms/register.html')


@user_blueprint.route('user-dashboard')
def user_dashboard():
    email = session['email']
    return "Welcome to your dashboard {}!".format(email)


@user_blueprint.route('/hi/user-dashboard')
def user_dashboard_hindi():
    email = session['email']
    return "आपके डैशबोर्ड में आपका स्वागत है {}!".format(email)

