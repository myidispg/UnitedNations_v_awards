import uuid
import models.users.errors as UserErrors
from common.database_user import Database
from common.utils import Utils
from models.users.constants import COLLECTION


class User:

    def __init__(self, email, password=None, name=None, phone_no=None, gender=None, dob=None, _id=None):
        self.email = email
        # As soon as the email is completed, the email gets registered to the database.
        #  If all other details are supplied, the status will be marked as registered otherwise unregistered
        self.password = password
        self.name = name
        self.phone_no = phone_no
        self.gender = gender
        self.dob = dob
        #  _id will be given a unique hexcode id if the user is a new registartion.
        # If the user already exists, the already generated ID will be used
        self._id = uuid.uuid4().hex if _id is None else _id
        if password and name and phone_no and gender and dob:
            self.status = 'registered'
        else:
            self.status = 'unregistered'

    def __repr__(self):
        return "<user {} with e-mail- {}>".format(self.name, self.email)

    @staticmethod
    def is_login_valid(email, password):
        """
        This method verifies that an email and password combo(as sent by the site forms) is valid or not.
        Checks that the email exists and the password associated with it is correct.
        :param email: The user's email
        :param password: A sha512 hashed password
        :return: True if valid, False otherwise
        """
        user_data = Database.find_user(email)  # password in sha512-> pbkdf2_sha512
        if user_data is None:
            # tell the user the email does not exists
            raise UserErrors.UserNotExistsError("This email does not exists.")
        if not Utils.check_hashed_password(password, user_data['password']):
            # tell the user that the password is incorrect
            raise UserErrors.IncorrectPasswordError("Your password was wrong.")

        return True

    @staticmethod
    def register_user(email, password, name, phone_no, gender, dob):
        """
        This method registers a user to the database using the entered details.
        The password already comes in a sha512 hashed format
        :param email: Email entered by the user
        :param password: sha512 hashed password
        :return: True if registration is successful, an exception is raised otherwise

        """
        # user_data = Database.find_one(COLLECTION, {'email': email})
        user_data = Database.find_user(email)
        if user_data is not None:
            raise UserErrors.UserAlreadyRegisteredError('This email is already registered with us.')
        if not Utils.email_is_valid(email):
            raise UserErrors.InvalidEmailError('The email is not of a valid format')

        User(email, Utils.hash_password(password), name, phone_no, gender, dob).save_to_database()
        return True

    # def save_to_mongo(self):
    #     Database.insert(COLLECTION, self.json())

    def save_to_database(self):
        Database.insert_user(self._id, self.email, self.password, self.name, self.phone_no, self.gender, self.dob)

    def json(self):
        return {
            '_id': self._id,
            'email': self.email,
            "password": self.password,
            'name': self.name,
            'phone_no': self.phone_no,
            'gender': self.gender,
            'dob': self.dob,
            'status': self.status
        }
