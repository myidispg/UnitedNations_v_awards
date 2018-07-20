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
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

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
