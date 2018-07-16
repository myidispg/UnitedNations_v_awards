import uuid
import models.users.errors as UserErrors
from common.database_user import Database
from common.utils import Utils
from models.users.constants import COLLECTION


class User:

    def __init__(self, email, password=None, name=None, phone_no=None, gender=None, dob=None, _id=None,
                 email_verified='no'):
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
        # By default, email will not be verified.
        # It will be verified only when the user clicks on the activation link sent to the email
        self.email_verified = email_verified

    def __repr__(self):
        return "<user {} with e-mail- {}>".format(self.name, self.email)

    @classmethod
    def get_user_object(cls, email=None, _id=None):
        """
        This method returns a user object by searching either through the email or the unique id
        :param email: The email of the user, None by default
        :param _id: The unique id of the user, None by default
        :return: returns a User object either by searching with email or _id
        """
        if email is not None:
            user_data = Database.find_user_email(email)
            user = cls(user_data['email'], user_data['password'], user_data['name'], user_data['phone_no'],
                       user_data['gender'], user_data['dob'], user_data['_id'], user_data['email_verified'])
        else:
            user_data = Database.find_user_id(_id)
            user = cls(user_data['email'], user_data['password'], user_data['name'], user_data['phone_no'],
                       user_data['gender'], user_data['dob'], user_data['_id'], user_data['email_verified'])
        return user

    @staticmethod
    def is_login_valid(email, password):
        """
        This method verifies that an email and password combo(as sent by the site forms) is valid or not.
        Checks that the email exists and the password associated with it is correct.
        :param email: The user's email
        :param password: A sha512 hashed password
        :return: True if valid, False otherwise
        """
        user_data = Database.find_user_email(email)  # password in sha512-> pbkdf2_sha512
        if user_data is None:
            # tell the user the email does not exists
            raise UserErrors.UserNotExistsError("This email does not exists.")
        if not Utils.check_hashed_password(password, user_data['password']):
            # tell the user that the password is incorrect
            raise UserErrors.IncorrectPasswordError("Your password was wrong.")
        if user_data['email_verified'] == 'yes':
            raise UserErrors.EmailNotVerfiedError("Please verify your e-mail before accessing your dashboard.")

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
        user_data = Database.find_user_email(email)
        if user_data is not None:
            raise UserErrors.UserAlreadyRegisteredError('This email is already registered with us.')
        if not Utils.email_is_valid(email):
            raise UserErrors.InvalidEmailError('The email is not of a valid format')

        User(email, Utils.hash_password(password), name, phone_no, gender, dob).save_to_database()
        return True

    # def save_to_mongo(self):
    #     Database.insert(COLLECTION, self.json())

    def save_to_database(self):
        Database.insert_user(self._id, self.email, self.password, self.name, self.phone_no, self.gender,
                             self.dob, self.email_verified)

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

    def save_email_verified_status(self):
        Database.verify_user(self.email)
