from flask import Blueprint, request

from models.users.user import User

__author__ = 'myidispg'

view_blueprint = Blueprint('user_form_1', __name__)


@view_blueprint.route('/save_form', methods=['POST'])
def save_form_1():
    if request.method == 'POST':
        name = request.form.get('name')
        dob = request.form.get('dob')
        current_address = request.form.get('current_address')
        permanent_address = request.form.get('permanent_address')
        tel_no = request.form.get('tel_no')
        mobile_no = request.form.get('mobile_no')
        email = request.form.get('email')
        nationality = request.form.get('nationality')
        gender = request.form.get('gender')
        disability = request.form.get('disability')
        source_awards = request.form.get('source_awards')
        # remember to add an ability for saving a photo later on

        languages = {
            'hindi': {
                'understand': 'yes',
                'speak': 'yes',
                'read_write': 'yes'
            },
            'english': {
                'understand': 'yes',
                'speak': 'yes',
                'read_write': 'yes'
            }
        }

        references = {
            'first': {
                'full_name': '',
                'address': '',
                'tel_no': '',
                'email': '',
                'occupation': '',
                'relation': ''
            },
            'second': {
                'full_name': '',
                'address': '',
                'tel_no': '',
                'email': '',
                'occupation': '',
                'relation': ''
            }
        }

        user = User(email, name=name, phone_no=mobile_no, gender=gender, dob=dob,
                    current_address=current_address, permanent_address=permanent_address,
                    tel_no=tel_no, nationality=nationality, disability=disability, source_awards=source_awards)
        user.save_to_database()
