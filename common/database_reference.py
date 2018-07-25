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
        """
        If a row with the user id already exists, then it updates the row, otherwise inserts the data
        :return: Nothing to return
        """
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()
        query_find_by_id = "SELECT first_second FROM reference WHERE _id=? and first_second=?"
        result = cursor.execute(query_find_by_id, (self._id, self.first_second,))
        rows = result.fetchone()

        if rows is not None:
            query = "UPDATE reference SET " \
                    "first_second = ?, full_name = ?, address = ?, tel_no = ?, email = ?, occupation = ?," \
                    " relation = ?" \
                    "WHERE _id = ? AND  first_second = ? "
            cursor.execute(query, (self.first_second, self.full_name, self.address, self.tel_no,
                                   self.email, self.occupation, self.relation, self._id, self.first_second,))
        else:
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

    @staticmethod
    def get_all():
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query = "SELECT * from reference"
        result = cursor.execute(query)

        rows = result.fetchall()

        list = []

        for row in rows:
            dictionary = {
                'id': row[0],
                'name': row[2],
                'address': row[3],
                'tel_no': row[4],
                'email': row[5],
                'occupation': row[6],
                'relation': row[7]
            }
            list.append(dictionary)

        connection.close()
        return list
