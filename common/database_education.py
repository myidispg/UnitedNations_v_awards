import sqlite3

from create_tables import DATABASE_URI

__author__ = 'myidispg'


class Education:

    def __init__(self, _id, course, from_date, to_date, institution, board_university):
        self._id = _id
        self.course = course
        self.from_date = from_date
        self.to_date = to_date
        self.institution = institution
        self.board_university = board_university

    def insert_data(self):
        """
        If a row with the user id already exists, then it updates the row, otherwise inserts the data
        :return: Nothing to return
        """
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query_find_by_id = "SELECT * FROM about WHERE _id=?"
        result = cursor.execute(query_find_by_id, (self._id,))

        if result is  None:
            query = "INSERT INTO education values(?,?,?,?,?,?,)"
            cursor.execute(query, (self._id, self.course, self.from_date, self.to_date, self.institution,
                                   self.board_university,))
        else:
            query = "UPDATE about " \
                    "SET course = ?,from_date=?, to_date=?, institution = ?, board_university = ? " \
                    "WHERE _id = ?"
            cursor.execute(query, (self.course, self.from_date, self.to_date,
                                   self.institution, self.board_university, self._id,))

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