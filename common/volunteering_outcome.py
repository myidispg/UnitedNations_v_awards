import sqlite3

from create_tables import DATABASE_URI

__author__ = 'myidispg'


class VolunteeringOrganisation:

    def __init__(self, _id, volunteering_outcome, outcome_community, impact, innovation_initiative,
                 experience_impact):
        self._id = _id
        self.volunteering_outcome = volunteering_outcome
        self.outcome_community = outcome_community
        self.impact = impact
        self.innovation_initiative = innovation_initiative
        self.experience_impact = experience_impact

    def insert_data(self):
        """
        If a row with the user id exists, then update the row otherwise insert a row
        :return: Nothing
        """
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query_find_by_id = "SELECT * from volunteering_organisation where _id = ?"
        result = cursor.execute(query_find_by_id, (self._id,))
        row = result.fetchone()

        if row is None:
            query = "INSERT INTO volunteering_experience values (?,?,?,?,?,?)"

            cursor.execute(query, (self._id, self.volunteering_outcome, self.outcome_community,
                                   self.impact, self.innovation_initiative, self.experience_impact,))
        else:
            query = "UPDATE volunteering_experience " \
                    "SET volunteering_outcome=?, outcome_community=?, impact=?, innovation_initiative=?," \
                    " experience_impact=?" \
                    "WHERE _id=?"
            cursor.execute(query, (self.volunteering_outcome, self.outcome_community, self.impact,
                                   self.innovation_initiative, self.experience_impact, self._id,))

        connection.commit()
        connection.close()

    @classmethod
    def get_by_id(cls, _id):
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query = "SELECT * FROM volunteering_experience WHERE _id = ?"
        result = cursor.execute(query, (_id,))

        row = result.fetchone()

        volunteering_outcome = cls(row[0], row[1], row[2], row[3], row[4], row[5])

        connection.close()
        return volunteering_outcome



