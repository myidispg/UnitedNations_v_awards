from flask import Blueprint, request, session

from models.form_1.form_1 import Form1
from models.users.user import User
import models.form_1.errors as Form1Errors

__author__ = 'myidispg'

form1_blueprint = Blueprint('user_form_1', __name__)


@form1_blueprint.route('/save_form', methods=['POST'])
def save_form_1():
    if request.method == 'POST':
        name = request.form.get('name')
        dob = request.form.get('dob')
        current_address = request.form.get('current_address')
        permanent_address = request.form.get('permanent_address')
        tel_no = request.form.get('tel_no')
        mobile_no = request.form.get('mobile_no')
        # email = session['email']
        email = request.form.get('email')
        nationality = request.form.get('nationality')
        gender = request.form.get('gender')
        disability = request.form.get('disability')
        source_awards = request.form.get('source_awards')
        # remember to add an ability for saving a photo later on

        languages = {
            'hindi': {
                'understand': 'no',
                'speak': 'no',
                'read_write': 'no'
            },
            'english': {
                'understand': 'yes',
                'speak': 'yes',
                'read_write': 'yes'
            }
        }

        references = {
            'first': {
                'full_name': request.form.get('first_name'),
                'address': request.form.get('first_address'),
                'tel_no': request.form.get('first_tel_no'),
                'email': request.form.get('first_email'),
                'occupation': request.form.get('first_occupation'),
                'relation': request.form.get('first_relation')
            },
            'second': {
                'full_name': request.form.get('second_name'),
                'address': request.form.get('second_address'),
                'tel_no': request.form.get('second_tel_no'),
                'email': request.form.get('second_email'),
                'occupation': request.form.get('second_occupation'),
                'relation': request.form.get('second_relation')
            }
        }

        about_you = request.form.get('about_you')
        why_volunteer = request.form.get('why_volunteer')
        communities_associated = request.form.get('communities_associated')
        motivation = request.form.get('motivation')

        # None is for education which will be filled in later
        # form 1 status is saved by default.
        # If the form is final, then add the last parameter to Form constructor as 'submit'
        try:
            form_1 = Form1(name, dob, current_address, permanent_address, tel_no, mobile_no, email,
                           nationality, gender, disability, source_awards, languages, None,
                           about_you, why_volunteer, communities_associated, motivation, references)
            form_1.save_form_to_db()
            return 'form 1 has been saved successfully'
        except Form1Errors.Form1Error as e:
            return e.message


@form1_blueprint.route('/submit_form', methods=['POST'])
def submit_form_1():
    if request.method == 'POST':
        name = request.form.get('name')
        dob = request.form.get('dob')
        current_address = request.form.get('current_address')
        permanent_address = request.form.get('permanent_address')
        tel_no = request.form.get('tel_no')
        mobile_no = request.form.get('mobile_no')
        # email = session['email']
        email = request.form.get('email')
        nationality = request.form.get('nationality')
        gender = request.form.get('gender')
        disability = request.form.get('disability')
        source_awards = request.form.get('source_awards')
        # remember to add an ability for saving a photo later on

        languages = {
            'hindi': {
                'understand': 'no',
                'speak': 'no',
                'read_write': 'no'
            },
            'english': {
                'understand': 'yes',
                'speak': 'yes',
                'read_write': 'yes'
            }
        }

        references = {
            'first': {
                'full_name': request.form.get('first_name'),
                'address': request.form.get('first_address'),
                'tel_no': request.form.get('first_tel_no'),
                'email': request.form.get('first_email'),
                'occupation': request.form.get('first_occupation'),
                'relation': request.form.get('first_relation')
            },
            'second': {
                'full_name': request.form.get('second_name'),
                'address': request.form.get('second_address'),
                'tel_no': request.form.get('second_tel_no'),
                'email': request.form.get('second_email'),
                'occupation': request.form.get('second_occupation'),
                'relation': request.form.get('second_relation')
            }
        }

        about_you = request.form.get('about_you')
        why_volunteer = request.form.get('why_volunteer')
        communities_associated = request.form.get('communities_associated')
        motivation = request.form.get('motivation')

        # None is for education which will be filled in later
        # form 1 status is saved by default.
        # If the form is final, then add the last parameter to Form constructor as 'submit'
        try:
            form_1 = Form1(name, dob, current_address, permanent_address, tel_no, mobile_no, email,
                           nationality, gender, disability, source_awards, languages, None,
                           about_you, why_volunteer, communities_associated, motivation, references,
                           form_1_status='submit')
            form_1.save_form_to_db()
            return 'form 1 has been submitted successfully'
        except Form1Errors.Form1Error as e:
            return e.message
