import sqlite3

from create_tables import DATABASE_URI

__author__ = 'myidispg'


class About:

    def __init__(self, _id, about_you, why_volunteer, communities_associated, motivation):
        self._id = _id
        self.about_you = about_you
        self.why_volunteer = why_volunteer
        self.communities_associated = communities_associated
        self.motivation = motivation

    def insert_data(self):
        """
        If a row with the user id already exists, then it updates the row, otherwise inserts the data
        :return: Nothing to return
        """
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query_find_by_id = "SELECT * FROM about WHERE _id=?"
        result = cursor.execute(query_find_by_id, (self._id,))
        if result is None:
            query = "INSERT INTO about values(?,?,?,?,?)"
            cursor.execute(query, (self._id, self.about_you, self.why_volunteer, self.communities_associated,
                                   self.motivation,))
        else:
            query = "UPDATE about " \
                    "SET about_you = ?, why_volunteer = ?, communities_associated = ?, motivation = ? " \
                    "WHERE _id = ?"
            cursor.execute(query, (self.about_you, self.why_volunteer, self.communities_associated,
                                   self.motivation, self._id,))

        connection.commit()
        connection.close()

    @classmethod
    def get_by_id(cls, _id):
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query = 'SELECT * FROM about WHERE _id=?'
        result = cursor.execute(query, (_id,))

        row = result.fetchone()

        about = cls(row[0], row[1], row[2], row[3], row[4])
        connection.close()

        return about