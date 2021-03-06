from common.database_about import About
from common.database_education import Education
from common.database_language import Language
from common.database_reference import Reference
from models.users.user import User
import models.form_1.errors as Form1Errors

__author__ = 'myidispg'


class Form1:

    def __init__(self, current_address=None, permanent_address=None, tel_no=None, email=None, nationality=None,
                 gender=None, disability=None,
                 languages=None, education=None, about_you=None,
                 why_volunteer=None, communities_associated=None, motivation=None, references=None,
                 form_1_status=None, photo_path=None):
        user = User.get_user_object(email=email)
        self._id = user._id
        self.current_address = current_address
        self.permanent_address = permanent_address
        self.tel_no = tel_no
        self.email = email
        self.nationality = nationality
        self.gender = gender
        self.disability = disability
        self.languages = languages
        self.education = education
        self.about_you = about_you
        self.why_volunteer = why_volunteer
        self.communities_associated = communities_associated
        self.motivation = motivation
        self.references = references
        self.form_1_status = form_1_status if form_1_status is not None else 'saved'
        self.photo_path = photo_path

    def save_form_to_db(self):
        """
        A Form1 object is initialized in the views file. All the necessary data is supplied to the
        necessary objects and the data is inserted into required tables.
        About class has a variable to check whether the form is saved or submitted.
        If the form is submitted, no further changes are allowed.
        :return: nothing
        """

        about = About(self._id, self.about_you, self.why_volunteer, self.communities_associated, self.motivation,
                      self.form_1_status)
        if about.get_form_status_by_id(self._id) == 'submit':
            raise Form1Errors.Form1AlreadySubmitted('Form 1 is submitted and cannot be updated.')
        else:
            about.insert_data()
            for each_education in self.education:
                education = Education(self._id, each_education,
                                      self.education[each_education]['from'],
                                      self.education[each_education]['till'],
                                      self.education[each_education]['school'],
                                      self.education[each_education]['board']
                                      )
                education.insert_data()
            User.save_form_1_details(self._id, self.current_address, self.permanent_address, self.tel_no,
                                     self.nationality, self.disability)

            # user = User(self.email, email_verified='yes', _id=self._id, current_address=self.current_address,
            #             permanent_address=self.permanent_address, tel_no=self.tel_no,
            #             nationality=self.nationality, disability=self.disability, photo_path=self.photo_path)
            # user.update_database()

            for each_language in self.languages:
                language = Language(self._id, each_language,
                                    self.languages[each_language]['understand'],
                                    self.languages[each_language]['speak'],
                                    self.languages[each_language]['read_write'])
                language.insert_data()

            for each_reference in self.references:
                reference = Reference(self._id, str(each_reference),
                                      self.references[each_reference]['full_name'],
                                      self.references[each_reference]['address'],
                                      self.references[each_reference]['tel_no'],
                                      self.references[each_reference]['email'],
                                      self.references[each_reference]['occupation'],
                                      self.references[each_reference]['relation'])
                reference.insert_data()
