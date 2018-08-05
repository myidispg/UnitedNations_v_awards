import json
import re

import requests
from passlib.hash import pbkdf2_sha512

from config import ALLOWED_EXTENSIONS, IMAGE_ALLOWED_EXTENSIONS, \
    UPLOAD_FOLDER_PROFILE_PICTURES, UPLOAD_FOLDER_PROFILE_PICTURES_PATH


class Utils:

    @staticmethod
    def email_is_valid(email):
        email_address_matcher = re.compile('^[\w\.\d]+@([\w-]+\.)+[\w]+$')
        return True if email_address_matcher.match(email) else False

    @staticmethod
    def hash_password(password):
        """
        Hashes a password using pbkdf2_sha512
        :param password: The sha512 password from the login/register form
        :return: A sha512-> pbkdf2_sha512 encrypted password
        """
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        """
        Checks that the password user sent matches that of the database
        The database password is encrypted more than the user's password at this stage
        :param password: sha512-hashed password
        :param hashed_password: pbkdf2_sha512 encrypted password
        :return: True if password match, False otherwise
        """

        return pbkdf2_sha512.verify(password, hashed_password)

    @staticmethod
    def is_human(captcha_response):
        """
        Recaptcha validation method
        Validating recaptcha response from google server
        Returns True captcha test passed for submitted form else returns False.

        """
        secret = "6LfKAGUUAAAAAAQ3J0KZuL9NYdfgTDFtHP3HcsOq"
        payload = {'response': captcha_response, 'secret': secret}
        response = requests.post("https://www.google.com/recaptcha/api/siteverify", payload)
        response_text = json.loads(response.text)
        return response_text['success']

    @staticmethod
    def search_list_dictionaries(key, value, list_of_dictionaries):
        return [element for element in list_of_dictionaries if element[key] == value]

    @staticmethod
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in IMAGE_ALLOWED_EXTENSIONS


