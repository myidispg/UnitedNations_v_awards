from flask import Blueprint, request, session, redirect, url_for, render_template

from models.users.user import User
import models.users.errors as UserErrors

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['hashed']

        try:
            if User.is_login_valid(email, password):
                session['email'] = email
                return redirect(url_for('.user_dashboard'))
        except UserErrors.UserError as e:
            return e.message

    # this return works if the request method is GET or the login credentials are invalid
    return render_template('users/login.html')


@user_blueprint.route('register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        # password = request.form['hashed'] if request.form['hashed'] else None
        # name = request.form['name'] if request.form['name'] else None
        # phone_no = request.form['phone_no'] if request.form['phone_no'] else None
        # gender = request.form['gender'] if request.form['gender'] else None
        # dob = request.form['dob'] if request.form['dob'] else None
        # # if request.form['hashed']:
        #     password = request.form['hashed']
        # if request.form['name']:
        #     name = request.form['name']
        # if request.form['phone_no']:
        #     phone_no = request.form['phone_no']
        # if request.form['gender']:
        #     gender = request.form['gender']
        # if request.form['dob']:
        #     dob = request.form['dob']
        # try:
        #     password = request.form['hashed']
        #     name = request.form['name']
        #     phone_no = request.form['phone_no']
        #     gender = request.form['gender']
        #     dob = request.form['dob']
        # except NameError:
        #     password = None
        #     name = None
        #     phone_no = None
        #     gender = None
        #     dob = None
        password = request.form.get('hashed')
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
        return render_template('users/register.html')


@user_blueprint.route('user-dashboard')
def user_dashboard():
    email = session['email']
    return "Welcome to your dashboard {}!".format(email)
