import sqlite3

from create_tables import DATABASE_URI

__author__ = 'myidispg'


class VolunteeringOrganisation:

    def __init__(self, _id, name, address, contact_person, phone, mobile, email):
        self._id = _id
        self.name = name
        self.address = address
        self.contact_person = contact_person
        self.phone = phone
        self.mobile = mobile
        self.email = email

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
            query = "INSERT INTO volunteering_experience values (?,?,?,?,?,?,?)"

            cursor.execute(query, (self._id, self.name, self.address, self.contact_person, self.phone,
                                   self.mobile, self.email,))
        else:
            query = "UPDATE volunteering_experience " \
                    "SET name=?, address=?, contact_person=?, phone=?," \
                    " mobile=?, email=?" \
                    "WHERE _id=?"
            cursor.execute(query, (self.name, self.address, self.contact_person, self.phone, self.mobile,
                                   self.email, self._id,))

        connection.commit()
        connection.close()

    @classmethod
    def get_by_id(cls, _id):
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query = "SELECT * FROM volunteering_experience WHERE _id = ?"
        result = cursor.execute(query, (_id,))

        row = result.fetchone()

        volunteering_organisation = cls(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

        connection.close()
        return volunteering_organisation



