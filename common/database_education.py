import sqlite3

from create_tables import DATABASE_URI

__author__ = 'myidispg'


class Education:

    def __init__(self, _id, course, institution, board_university):
        self._id = _id
        self.course = course
        self.institution = institution
        self.board_university = board_university

    def insert_data(self):
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query = "INSERT INTO education values(?,?,?,?,)"
        cursor.execute(query, (self._id, self.course, self.institution, self.board_university,))

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