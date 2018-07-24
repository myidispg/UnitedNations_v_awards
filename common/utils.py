import json
import re

import requests
from passlib.hash import pbkdf2_sha512

from common.database_about import About
from common.database_user import Database
from app import mail
from flask_mail import Message


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




