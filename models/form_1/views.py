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
        current_address_line_1 = request.form.get('current_address_line_1')
        current_address_line_2 = request.form.get('current_address_line_2')
        current_address = current_address_line_1 + " " + current_address_line_2
        permanent_address_line_1 = request.form.get('permanent_address_line_1')
        permanent_address_line_2 = request.form.get('permanent_address_line_2')
        permanent_address = permanent_address_line_1 + " " + permanent_address_line_2
        tel_no = request.form.get('tel_no')
        email = session['email']
        # email = request.form.get('email')
        nationality = request.form.get('nationality')
        disability = request.form.get('disability')

        education = {}
        course_list = ['tenth', 'twelfth', 'graduate', 'postgraduate']
        for i in course_list:
            if request.form.get(i):
                education[i if request.form.get(i) is not None else None] = {
                    'from': request.form.get('from_' + str(i)),
                    'till': request.form.get('till_' + str(i)),
                    'school': request.form.get('school_' + str(i)),
                    'board': request.form.get('board_' + str(i)),
                }
            else:
                pass

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
        file = request.files.get('file')
        new_file_name = None

        # form 1 status is saved by default.
        # If the form is final, then add the last parameter to Form constructor as 'submit'
        try:
            if file and file.filename == '':
                return 'The uploaded file has no filename.'
            if file and Utils.allowed_file(file.filename):
                filename = secure_filename(file.filename)
                email = session['email']
                user = User.get_user_object(email=email)
                filename_list = filename.split('.')
                new_file_name = os.path.normpath(os.path.join(UPLOAD_FOLDER_PROFILE_PICTURES_PATH, user._id + "." +
                                                              filename_list[len(filename_list) - 1]))
                user.photo_path = new_file_name
                if os.path.exists(new_file_name):
                    os.remove(new_file_name)
                file.save(new_file_name)
            form_1 = Form1(current_address=current_address, permanent_address=permanent_address, tel_no=tel_no,
                           email=email, nationality=nationality, disability=disability, languages=languages,
                           education=education, about_you=about_you, why_volunteer=why_volunteer,
                           communities_associated=communities_associated, motivation=motivation,
                           references=references, photo_path=new_file_name)
            form_1.save_form_to_db()
            return 'form 1 has been saved successfully'
        except Form1Errors.Form1Error as e:
            return e.message


@form1_blueprint.route('/submit_form', methods=['POST'])
def submit_form_1():
    if request.method == 'POST':
        current_address_line_1 = request.form.get('current_address_line_1')
        current_address_line_2 = request.form.get('current_address_line_2')
        current_address = current_address_line_1 + " " + current_address_line_2
        permanent_address_line_1 = request.form.get('permanent_address_line_1')
        permanent_address_line_2 = request.form.get('permanent_address_line_2')
        permanent_address = permanent_address_line_1 + " " + permanent_address_line_2
        tel_no = request.form.get('tel_no')
        email = session['email']
        # email = request.form.get('email')
        nationality = request.form.get('nationality')
        disability = request.form.get('disability')

        education = {}
        course_list = ['tenth', 'twelfth', 'graduate', 'postgraduate']
        for i in course_list:
            if request.form.get(i):
                education[i if request.form.get(i) is not None else None] = {
                    'from': request.form.get('from_' + str(i)),
                    'till': request.form.get('till_' + str(i)),
                    'school': request.form.get('school_' + str(i)),
                    'board': request.form.get('board_' + str(i)),
                }
            else:
                pass

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
        file = request.files.get('file')
        new_file_name = None

        # None is for education which will be filled in later
        # form 1 status is saved by default.
        # If the form is final, then add the last parameter to Form constructor as 'submit'
        try:
            if file and file.filename == '':
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
                # Check if an image of the user already exists and overwrite it.
                if os.path.exists(new_file_name):
                    os.remove(new_file_name)
                file.save(new_file_name)
            form_1 = Form1(current_address=current_address, permanent_address=permanent_address, tel_no=tel_no,
                           email=email, nationality=nationality, disability=disability, languages=languages,
                           education=education, about_you=about_you, why_volunteer=why_volunteer,
                           communities_associated=communities_associated, motivation=motivation,
                           references=references, form_1_status='submit', photo_path=new_file_name)
            form_1.save_form_to_db()
            return 'form 1 has been submitted successfully'
        except Form1Errors.Form1Error as e:
            return e.message
