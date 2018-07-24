import threading
import time

from flask_mail import Message

from common.database_about import About
from common.database_user import Database
from common.database_volunteering_experience import VolunteeringExperience

__author__ = 'myidispg'


class EmailAlerts:

    @staticmethod
    def email_alerts_form_1(mail, reminder_number):
        """
        This sends an email alert to those whose form 1 is incomplete.
        :param mail: not to be touched. mail instance from app.py
        :param reminder_number: reminder_1 or reminder_2
        :return: nothing
        """
        about = About(None, None, None, None, None, None)

        id_list = about.get_all_saved()

        for each_id in id_list:
            email = Database.find_user_id(each_id)['email']
            msg = Message('Your phase 1 form is incomplete',
                          sender='myidispg@gmail.com',
                          recipients=[email])
            msg.body = "Your phase 1 form is incomplete, please go to your dashboard to do the same.\n" \
                       "आपका चरण 1 फॉर्म अधूरा है, कृपया ऐसा करने के लिए अपने डैशबोर्ड पर जाएं।"
            mail.send(msg)
            About.update_reminder_status(each_id, reminder_number)
            time.sleep(8)

    @staticmethod
    def email_alerts_form_2(mail, reminder_number):
        """
        This sends an email alert to those whose form 2 is incomplete.
        :param mail: not to be touched. mail instance from app.py
        :param reminder_number: reminder_1 or reminder_2
        :return: nothing
        """
        volunteering_experience = VolunteeringExperience(None, None, None, None, None, None, None, None)

        id_list = volunteering_experience.get_all_saved()

        for each_id in id_list:
            email = Database.find_user_id(each_id)['email']
            msg = Message('Your phase 1 form is incomplete',
                          sender='myidispg@gmail.com',
                          recipients=[email])
            msg.body = "Your phase 2 form is incomplete, please go to your dashboard to do the same.\n" \
                       "आपका चरण 2 फॉर्म अधूरा है, कृपया ऐसा करने के लिए अपने डैशबोर्ड पर जाएं।"
            mail.send(msg)
            VolunteeringExperience.update_reminder_status(each_id, reminder_number)
            time.sleep(8)


