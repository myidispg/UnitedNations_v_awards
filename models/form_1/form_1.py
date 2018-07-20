from common.database_about import About
from models.users.user import User

__author__ = 'myidispg'


class Form1:

    def __init__(self, name=None, dob=None, current_address=None, permanent_address=None, tel_no=None,
                 mobile_no=None, email=None, nationality=None, gender=None, disability=None,
                 source_awards=None, languages=None, education=None, about_you=None,
                 why_volunteer=None, communities_associated=None, motivation=None, references=None):
        user = User().get_user_object(email=email)
        self._id = user._id
        self.name = name
        self.dob = dob
        self.current_address = current_address
        self.permanent_address = permanent_address
        self.tel_no = tel_no
        self.mobile_no = mobile_no
        self.email = email
        self.nationality = nationality
        self.gender = gender
        self.disability = disability
        self.source_awards = source_awards
        self.languages = languages
        self.education = education
        self.about_you = about_you
        self.why_volunteer = why_volunteer
        self.communities_associated = communities_associated
        self.motivation = motivation
        self.references = references

    def save_form_to_db(self):
        user = User(self.email, name=self.name, phone_no=self.mobile_no, gender=self.gender, dob=self.dob,
                    email_verified='yes', _id=self._id, current_address=self.current_address,
                    permanent_address=self.permanent_address, tel_no=self.tel_no,
                    nationality=self.nationality, disability=self.disability, source_awards=self.source_awards)
        user.update_database()

        about = About(self._id, self.about_you, self.why_volunteer, self.communities_associated, self.motivation)
        about.insert_data()

