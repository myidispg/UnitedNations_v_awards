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

    @staticmethod
    def insert_user(_id, email, password, name, phone_no, gender, dob, email_verified):
        connection = sqlite3.connect(DATABASE_URI)
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (?,?,?,?,?,?,?,?)"
        cursor.execute(query, (_id, email, password, name, phone_no, gender, dob, email_verified,))

        connection.commit()
        connection.close()

    @staticmethod
    def find_user(email):
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
                'email_verified' : row[7]
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
