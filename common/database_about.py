import sqlite3

from create_tables import DATABASE_URI

__author__ = 'myidispg'


class About:

    def __init__(self, _id, about_you, why_volunteer, communities_associated, motivation, form_1_status):
        self._id = _id
        self.about_you = about_you
        self.why_volunteer = why_volunteer
        self.communities_associated = communities_associated
        self.motivation = motivation
        self.form_1_status = form_1_status
        self.reminder_status = 'not_reminded'

    def insert_data(self):
        """
        If a row with the user id already exists, then it updates the row, otherwise inserts the data
        :return: Nothing to return
        """
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query_find_by_id = "SELECT * FROM about WHERE _id=?"
        result = cursor.execute(query_find_by_id, (self._id,))
        row = result.fetchone()

        if row is None:
            query = "INSERT INTO about values(?,?,?,?,?,?,?)"
            cursor.execute(query, (self._id, self.about_you, self.why_volunteer, self.communities_associated,
                                   self.motivation, self.form_1_status, self.reminder_status))
        else:
            query = "UPDATE about " \
                    "SET about_you = ?, why_volunteer = ?, communities_associated = ?, motivation = ?," \
                    " form_1_status = ? " \
                    "WHERE _id = ?"
            cursor.execute(query, (self.about_you, self.why_volunteer, self.communities_associated,
                                   self.motivation, self.form_1_status, self._id,))

        connection.commit()
        connection.close()

    @classmethod
    def get_by_id(cls, _id):
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query = 'SELECT * FROM about WHERE _id=?'
        result = cursor.execute(query, (_id,))

        row = result.fetchone()

        about = cls(row[0], row[1], row[2], row[3], row[4], row[5])
        connection.close()

        return about

    @staticmethod
    def get_form_status_by_id(_id):
        """
        this method only returns the form_status of the user as opposed to a whole object.
        :param _id: the id of the user whose status has to be searched
        :return: form_status
        """
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query = 'SELECT * FROM about WHERE _id=?'
        result = cursor.execute(query, (_id,))

        row = result.fetchone()

        connection.close()
        if row is None:
            return 'no_status'
        else:
            return row[5]

    @staticmethod
    def get_all_saved():
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query = "SELECT _id FROM about WHERE form_1_status = ? and reminder_status = ?"
        result = cursor.execute(query, ('saved', 'not_reminded'))

        rows = result.fetchall()
        id_list = []

        for each_row in rows:
            _id = list(each_row)
            id_list.append(_id[0])

        connection.close()
        return id_list

    @staticmethod
    def update_reminder_status(_id, status):
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query = "UPDATE about SET " \
                "reminder_status = ?" \
                "WHERE _id = ?"
        cursor.execute(query, (status, _id))

        connection.commit()
        connection.close()

    @staticmethod
    def get_all():
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query = "SELECT * from about WHERE form_1_status=?"
        result = cursor.execute(query, ('submit', ))

        rows = result.fetchall()

        list = []

        for row in rows:
            dictionary = {
                'id': row[0],
                'about': row[1],
                'why_volunteer': row[2],
                'communities_associated': row[3],
                'motivation': row[4]
            }
            list.append(dictionary)

        connection.close()
        return list



