__author__ = 'myidispg'

import sqlite3

DATABASE_URI = 'database/database.db'

connection = sqlite3.connect(DATABASE_URI)
cursor = connection.cursor()

query = "CREATE TABLE IF NOT EXISTS users (_id text, email text, password text, name text, phone_no text, gender text, dob text)"

cursor.execute(query)

connection.commit()
connection.close()