import sqlite3

__author__ = 'myidispg'

from create_tables import DATABASE_URI


class Language:

    def __init__(self, _id, language, understand, speak, read_write):
        self._id = _id
        self.language = language
        self.understand = understand
        self.speak = speak
        self.read_write = read_write

    def insert_data(self):
        """
        If a row with the user id already exists, then it updates the row, otherwise inserts the data
        :return: Nothing to return
        """
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()
        query_find_by_id = "SELECT * FROM language WHERE _id=? and language = ?"
        result = cursor.execute(query_find_by_id, (self._id, self.language))
        rows = result.fetchone()

        if rows is not None:
            query = "UPDATE language " \
                    "SET language = ?, understand = ?, speak = ?, read_write = ?" \
                    "WHERE _id = ? and language=?"
            cursor.execute(query,
                           (self.language, self.understand, self.speak, self.read_write, self._id,
                            self.language,))
        else:
            query = "INSERT INTO language values(?,?,?,?,?)"
            cursor.execute(query, (self._id, self.language, self.understand, self.speak, self.read_write,))

        connection.commit()
        connection.close()

    @classmethod
    def get_by_id(cls, _id):
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query = 'SELECT * FROM language WHERE _id=?'
        result = cursor.execute(query, (_id,))

        row = result.fetchone()

        language = cls(row[0], row[1], row[2], row[3], row[4])
        connection.close()

        return language

    @staticmethod
    def get_all():
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query = "SELECT * from language"
        result = cursor.execute(query)

        rows = result.fetchall()

        list = []

        for row in rows:
            dictionary = {
                "id": row[0],
                'language': row[1],
                'understand': row[2],
                'speak': row[3],
                'read_write': row[4]
            }
            list.append(dictionary)

        connection.close()
        return list