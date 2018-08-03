import os

from flask import Blueprint, request, session

from common.utils import Utils
from models.form_1.form_1 import Form1
from models.users.user import User
import models.form_1.errors as Form1Errors
from werkzeug.utils import secure_filename
from config import UPLOAD_FOLDER_PROFILE_PICTURES_PATH


__author__ = 'myidispg'

form1_blueprint = Blueprint('form1', __name__)


@form1_blueprint.route('/save_form', methods=['POST'])
def save_form_1():
    if request.method == 'POST':
        name = request.form.get('name')
        dob = request.form.get('dob')
        current_address = request.form.get('current_address')
        permanent_address = request.form.get('permanent_address')
        tel_no = request.form.get('tel_no')
        mobile_no = request.form.get('mobile_no')
        email = session['email']
        # email = request.form.get('email')
        nationality = request.form.get('nationality')
        gender = request.form.get('gender')
        disability = request.form.get('disability')
        source_awards = request.form.get('source_awards')
        # remember to add an ability for saving a photo later on
        file = request.files['file']
        if file.filename == '':
            return 'The uploaded file has no filename.'
        if file and Utils.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            email = session['email']
            user = User.get_user_object(email=email)
            filename_list = filename.split('.')
            new_file_name = os.path.normpath(os.path.join(UPLOAD_FOLDER_PROFILE_PICTURES_PATH, user._id + "." +
                                                          filename_list[len(filename_list) - 1]))
            user.photo_path = new_file_name
            user.save_photo_path()
            file.save(new_file_name)

        education = {}
        for i in range(1, 5):
            education[request.form.get('course_' + str(i))] = {
                'from': request.form.get('from_' + str(i)),
                'till': request.form.get('till_' + str(i)),
                'school': request.form.get('school_' + str(i)),
                'board': request.form.get('board_' + str(i)),
            }

        languages = {
            'hindi': {
                'understand': 'yes' if request.form.get('hindi_understand') is not None else 'no',
                'speak': 'yes' if request.form.get('hindi_speak') is not None else 'no',
                'read_write': 'yes' if request.form.get('hindi_read_write') is not None else 'no'
            },
            'english': {
                'understand': 'yes' if request.form.get('english_understand') is not None else 'no',
                'speak': 'yes' if request.form.get('english_speak') is not None else 'no',
                'read_write': 'yes' if request.form.get('english_read_write') is not None else 'no'
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
                           nationality, gender, disability, source_awards, languages, education,
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
        email = session['email']
        # email = request.form.get('email')
        nationality = request.form.get('nationality')
        gender = request.form.get('gender')
        disability = request.form.get('disability')
        source_awards = request.form.get('source_awards')
        # remember to add an ability for saving a photo later on
        file = request.files['file']
        if file.filename == '':
            return 'The uploaded file has no filename.'
        if file and Utils.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            email = session['email']
            user = User.get_user_object(email=email)
            filename_list = filename.split('.')
            new_file_name = os.path.normpath(os.path.join(UPLOAD_FOLDER_PROFILE_PICTURES_PATH, user._id + "." +
                                                          filename_list[len(filename_list) - 1]))
            user.photo_path = new_file_name
            user.save_photo_path()
            file.save(new_file_name)

        education = {}
        for i in range(1, 5):
            education[request.form.get('course_' + str(i))] = {
                'from': request.form.get('from_' + str(i)),
                'till': request.form.get('till_' + str(i)),
                'school': request.form.get('school_' + str(i)),
                'board': request.form.get('board_' + str(i)),
            }

        languages = {
            'hindi': {
                'understand': 'yes' if request.form.get('hindi_understand') is not None else 'no',
                'speak': 'yes' if request.form.get('hindi_speak') is not None else 'no',
                'read_write': 'yes' if request.form.get('hindi_read_write') is not None else 'no'
            },
            'english': {
                'understand': 'yes' if request.form.get('english_understand') is not None else 'no',
                'speak': 'yes' if request.form.get('english_speak') is not None else 'no',
                'read_write': 'yes' if request.form.get('english_read_write') is not None else 'no'
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
                           nationality, gender, disability, source_awards, languages, education,
                           about_you, why_volunteer, communities_associated, motivation, references,
                           form_1_status='submit')
            form_1.save_form_to_db()
            return 'form 1 has been submitted successfully'
        except Form1Errors.Form1Error as e:
            return e.message


# @form1_blueprint.route('/profile-pic', methods=['GET', 'POST'])
# def upload_profile_picture():
#     if request.method == 'POST':
#         file = request['file']
#         if file.filename == '':
#             return 'The uploaded file has no filename.'
#         if file and Utils.allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             email = session['email']
#             user = User.get_user_object(email=email)
#             filename_list = filename.split('.')
#             new_file_name = os.path.normpath(os.path.join(UPLOAD_FOLDER_PROFILE_PICTURES_PATH, user._id +
#                                                           filename_list[len(filename_list) - 1]))
#             user.
#             file.save(new_file_name)
#             return "Picture saved successfully."

