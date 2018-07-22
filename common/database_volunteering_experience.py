import sqlite3

from create_tables import DATABASE_URI

__author__ = 'myidispg'


class VolunteeringExperience:

    def __init__(self, _id, volunteered_as, intended_impact, assignment_details, period_engagement,
                 frequency_engagement, hours_volunteering, form_2_status):
        self._id = _id
        self.volunteered_as = volunteered_as
        self.intended_impact = intended_impact
        self.assignment_details = assignment_details
        self.period_engagement = period_engagement
        self.frequency_engagement = frequency_engagement
        self.hours_volunteering = hours_volunteering
        self.form_2_status = form_2_status

    def insert_data(self):
        """
        If a row with the user id exists, then update the row otherwise insert a row
        :return: Nothing
        """
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query_find_by_id = "SELECT * from volunteering_experience where _id = ?"
        result = cursor.execute(query_find_by_id, (self._id,))
        row = result.fetchone()

        if row is None:
            query = "INSERT INTO volunteering_experience values (?,?,?,?,?,?,?,?)"

            cursor.execute(query, (self._id, self.volunteered_as, self.intended_impact,
                                   self.assignment_details, self.period_engagement,
                                   self.frequency_engagement, self.hours_volunteering,
                                   self.form_2_status))
        else:
            query = "UPDATE volunteering_experience " \
                    "SET volunteered_as=?, intended_impact=?, assignment_details=?, period_engagement=?," \
                    " frequency_engagement=?, hours_volunteering=?, form_2_status=?" \
                    "WHERE _id=?"
            cursor.execute(query, (self.volunteered_as, self.intended_impact, self.assignment_details,
                                   self.period_engagement, self.frequency_engagement,
                                   self.hours_volunteering, self.form_2_status, self._id,))

        connection.commit()
        connection.close()

    @classmethod
    def get_by_id(cls, _id):
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query = "SELECT * FROM volunteering_experience WHERE _id = ?"
        result = cursor.execute(query, (_id,))

        row = result.fetchone()

        volunteering_experience = cls(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])

        connection.close()
        return volunteering_experience

    @staticmethod
    def get_form_status_by_id(_id):
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query = 'SELECT * FROM volunteering_experience WHERE _id=?'
        result = cursor.execute(query, (_id,))

        row = result.fetchone()

        status = row[7] if row is not None else 'nothing'
        connection.close()

        return status



