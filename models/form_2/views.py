from flask import Blueprint, request

from models.form_2.form_2 import Form2
import models.form_2.errors as Form2Errors

__author__ = 'myidispg'

form2_blueprint = Blueprint('form2', __name__)


@form2_blueprint.route('/save_form', methods=['POST'])
def save_form_2():
    if request.method == 'POST':
        email = request.form.get('email')
        volunteered_as = request.form.get('volunteered_as')
        intended_impact = request.form.get('intended_impact')
        assignment_details = request.form.get('assignment_details')
        period_engagement = request.form.get('period_engagement')
        frequency_engagement = request.form.get('frequency_engagement')
        hours_volunteering = request.form.get('hours_volunteering')
        organisation_name = request.form.get('organisation_name')
        organisation_address = request.form.get('organisation_address')
        organisation_contact_person = request.form.get('organisation_contact_person')
        organisation_phone = request.form.get('organisation_phone')
        organisation_mobile = request.form.get('organisation_mobile')
        organisation_email = request.form.get('organisation_email')
        volunteering_outcome = request.form.get('volunteering_outcome')
        outcome_community = request.form.get('outcome_community')
        impact = request.form.get('impact')
        innovation_initiative = request.form.get('innovation_initiative')
        experience_impact = request.form.get('experience_impact')

        try:
            form_2 = Form2(email, volunteered_as, intended_impact, assignment_details, period_engagement,
                           frequency_engagement, hours_volunteering, organisation_name,
                           organisation_address, organisation_contact_person, organisation_phone,
                           organisation_mobile, organisation_email, volunteering_outcome,
                           outcome_community, impact, innovation_initiative, experience_impact)
            form_2.save_form_to_db()
            return 'Form 2 saved successfully.'
        except Form2Errors.Form2Error as e:
            return e.message


@form2_blueprint.route('/submit_form', methods=['POST'])
def submit_form_2():
    if request.method == 'POST':
        email = request.form.get('email')
        volunteered_as = request.form.get('volunteered_as')
        intended_impact = request.form.get('intended_impact')
        assignment_details = request.form.get('assignment_details')
        period_engagement = request.form.get('period_engagement')
        frequency_engagement = request.form.get('frequency_engagement')
        hours_volunteering = request.form.get('hours_volunteering')
        organisation_name = request.form.get('organisation_name')
        organisation_address = request.form.get('organisation_address')
        organisation_contact_person = request.form.get('organisation_contact_person')
        organisation_phone = request.form.get('organisation_phone')
        organisation_mobile = request.form.get('organisation_mobile')
        organisation_email = request.form.get('organisation_email')
        volunteering_outcome = request.form.get('volunteering_outcome')
        outcome_community = request.form.get('outcome_community')
        impact = request.form.get('impact')
        innovation_initiative = request.form.get('innovation_initiative')
        experience_impact = request.form.get('experience_impact')

        try:
            form_2 = Form2(email, volunteered_as, intended_impact, assignment_details, period_engagement,
                           frequency_engagement, hours_volunteering, organisation_name,
                           organisation_address, organisation_contact_person, organisation_phone,
                           organisation_mobile, organisation_email, volunteering_outcome,
                           outcome_community, impact, innovation_initiative, experience_impact,
                           form_2_status='submit')
            form_2.save_form_to_db()
            return 'Form 2 submitted successfully.'
        except Form2Errors.Form2Error as e:
            return e.message




