import sqlite3

from create_tables import DATABASE_URI

__author__ = 'myidispg'


class Education:

    def __init__(self, _id, course, from_date, till_date, institution, board_university):
        self._id = _id
        self.course = course
        self.from_date = from_date
        self.till_date = till_date
        self.institution = institution
        self.board_university = board_university

    def insert_data(self):
        """
        If a row with the user id already exists, then it updates the row, otherwise inserts the data
        :return: Nothing to return
        """
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query_find_by_id = "SELECT * FROM education WHERE _id=? and course=?"
        result = cursor.execute(query_find_by_id, (self._id,self.course,))
        rows = result.fetchone()

        if rows is not None:
            query = "UPDATE education " \
                    "SET course = ?, from_date=?, till_date=?, institution = ?, board_university = ? " \
                    "WHERE _id = ?"
            cursor.execute(query, (self.course, self.from_date, self.till_date,
                                   self.institution, self.board_university, self._id,))

        else:
            query = "INSERT INTO education values(?,?,?,?,?,?)"
            cursor.execute(query, (self._id, self.course, self.from_date, self.till_date, self.institution,
                                   self.board_university,))

        connection.commit()
        connection.close()

    @classmethod
    def get_by_id(cls, _id):
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query = 'SELECT * FROM education WHERE _id=?'
        result = cursor.execute(query, (_id,))

        row = result.fetchone()

        education = cls(row[0], row[1], row[2], row[3], row[4])
        connection.close()

        return education

    @staticmethod
    def get_all():
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query = "SELECT * from education"
        result = cursor.execute(query)

        rows = result.fetchall()

        list = []

        for row in rows:
            dictionary = {
                'id': row[0],
                'course': row[1],
                'from_date': row[2],
                'till_date': row[3],
                'institution': row[4],
                'board': row[5]
            }
            list.append(dictionary)

        connection.close()
        return list
