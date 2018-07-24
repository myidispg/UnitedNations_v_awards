import sqlite3

import pymongo

from create_tables import DATABASE_URI


class Database:
    # URI = 'mongodb://127.0.0.1:27017'
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['v-awards']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    # This method is used for the email registration purpose. So, no details like address are required
    # @staticmethod
    # def insert_user(_id, email, password, name, phone_no, gender, dob, email_verified,):
    #     connection = sqlite3.connect(DATABASE_URI)
    #     cursor = connection.cursor()
    #
    #     query = "INSERT INTO users VALUES (?,?,?,?,?,?,?,?)"
    #     cursor.execute(query, (_id, email, password, name, phone_no, gender, dob, email_verified,))
    #
    #     connection.commit()
    #     connection.close()

    @staticmethod
    def insert_user(_id, email, password, name, phone_no, gender, dob, email_verified, current_address,
                    permanent_address, tel_no, nationality, disability, source_awards, photo_path):
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cursor.execute(query, (_id, email, password, name, phone_no, gender, dob, email_verified,
                               current_address, permanent_address, tel_no, nationality, disability,
                               source_awards, photo_path,))

        connection.commit()
        connection.close()

    @staticmethod
    def update_user(_id, email, name, phone_no, gender, dob, current_address,
                    permanent_address, tel_no, nationality, disability, source_awards, photo_path):
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query = "UPDATE users SET " \
                "email=?, name=?, phone_no=?, gender=?, dob=?, current_address=?, permanent_address=?," \
                " tel_no=?, nationality=?, disability=?, source_awards=?, photo_path=?" \
                "WHERE _id = ?"
        cursor.execute(query, (email, name, phone_no, gender, dob, current_address,
                               permanent_address, tel_no, nationality, disability, source_awards, photo_path,
                               _id,))

        connection.commit()
        connection.close()

    @staticmethod
    def find_user_email(email):
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE email = ?"
        result = cursor.execute(query, (email,))
        row = result.fetchone()

        if row is not None:
            user_data_dictionary = {
                'email': row[1],
                'password': row[2],
                'name': row[3],
                'phone_no': row[4],
                'gender': row[5],
                'dob': row[6],
                '_id': row[0],
                'email_verified': row[7],
                'current_address': row[8],
                'permanent_address': row[9],
                'tel_no': row[10],
                'nationality': row[11],
                'disability': row[12],
                'source_awards': row[13],
                'photo_path': row[14]
            }
            return user_data_dictionary
        else:
            return None

    @staticmethod
    def find_user_id(_id):
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE _id = ?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()

        if row is not None:
            user_data_dictionary = {
                'email': row[1],
                'password': row[2],
                'name': row[3],
                'phone_no': row[4],
                'gender': row[5],
                'dob': row[6],
                '_id': row[0],
                'email_verified': row[7],
                'current_address': row[8],
                'permanent_address': row[9],
                'tel_no': row[10],
                'nationality': row[11],
                'disability': row[12],
                'source_awards': row[13],
                'photo_path': row[14]
            }
            return user_data_dictionary
        else:
            return None

    @staticmethod
    def verify_user(email):
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query = "UPDATE users SET email_verified=? where email=?"
        cursor.execute(query, ('yes', email))

        connection.commit()
        connection.close()

    @staticmethod
    def change_password(password, _id):
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query = "UPDATE users SET password = ? where _id = ?"
        cursor.execute(query, (password, _id,))

        connection.commit()
        connection.close()
