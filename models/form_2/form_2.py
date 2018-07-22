from common.database_volunteering_experience import VolunteeringExperience
from common.database_volunteering_organisation import VolunteeringOrganisation
from common.database_volunteering_outcome import VolunteeringOutcome
from models.users.user import User
import models.form_2.errors as Form2Errors

__author__ = 'myidispg'

class Form2:

    def __init__(self, email, volunteered_as, intended_impact, assignment_details, period_engagement,
                 frequency_engagement, hours_volunteering, organisation_name, organisation_address,
                 organisation_contact_person, organisation_phone, organisation_mobile, organisation_email,
                 volunteering_outcome, outcome_community, impact, innovation_initiative,
                 experience_impact, form_2_status=None):
        # The user's email has to be supplied to get the unique id of the user
        user = User.get_user_object(email=email)
        self._id = user._id
        self.volunteered_as = volunteered_as
        self.intended_impact = intended_impact
        self.assignment_details = assignment_details
        self.period_engagement = period_engagement
        self.frequency_engagement = frequency_engagement
        self.hours_volunteering = hours_volunteering
        self.organisation_name = organisation_name
        self.organisation_address = organisation_address
        self.organisation_contact_person = organisation_contact_person
        self.organisation_phone = organisation_phone
        self.organisation_mobile = organisation_mobile
        self.organisation_email = organisation_email
        self.volunteering_outcome = volunteering_outcome
        self.outcome_community = outcome_community
        self.impact = impact
        self.innovation_initiative = innovation_initiative
        self.experience_impact = experience_impact
        self.form_2_status = form_2_status if form_2_status else 'saved'

    def save_form_to_db(self):
        """
        A Form2 object is initialized in the views file. All the necessary data is supplied to the
        necessary objects and the data is inserted into required tables.
        :return: nothing
        """
        volunteering_experience = VolunteeringExperience(self._id, self.volunteered_as,
                                                         self.intended_impact, self.assignment_details,
                                                         self.period_engagement, self.frequency_engagement,
                                                         self.hours_volunteering, self.form_2_status)
        if volunteering_experience.get_form_status_by_id(self._id) == 'submit':
            raise Form2Errors.Form2AlreadySubmitted('Form 2 is submitted and cannot be updated.')
        else:
            volunteering_experience.insert_data()

            volunteering_organisation = VolunteeringOrganisation(self._id, self.organisation_name,
                                                                 self.organisation_contact_person,
                                                                 self.organisation_contact_person,
                                                                 self.organisation_phone,
                                                                 self.organisation_mobile,
                                                                 self.organisation_email)
            volunteering_organisation.insert_data()

            volunteering_outcome = VolunteeringOutcome(self._id, self.volunteering_outcome,
                                                       self.outcome_community, self.impact,
                                                       self.innovation_initiative, self.experience_impact)
            volunteering_outcome.insert_data()
