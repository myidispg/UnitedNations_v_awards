import sqlite3

from create_tables import DATABASE_URI

__author__ = 'myidispg'


class Reference:

    def __init__(self, _id, first_second, full_name, address, tel_no, email, occupation, relation):
        self._id = _id
        self.first_second = first_second
        self.full_name = full_name
        self.address = address
        self.tel_no = tel_no
        self.email = email
        self.occupation = occupation
        self.relation = relation

    def insert_data(self):
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query = "INSERT INTO reference values(?,?,?,?,?,?,?,?)"
        cursor.execute(query, (self._id, self.first_second, self.full_name, self.address, self.tel_no,
                               self.email, self.occupation, self.relation,))

        connection.commit()
        connection.close()

    @classmethod
    def get_by_id(cls, _id):
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query = 'SELECT * FROM reference WHERE _id=?'
        result = cursor.execute(query, (_id,))

        row = result.fetchone()

        reference = cls(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        connection.close()

        return reference