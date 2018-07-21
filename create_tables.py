__author__ = 'myidispg'

import sqlite3

DATABASE_URI = 'database/database.db'

connection = sqlite3.connect(DATABASE_URI)
cursor = connection.cursor()

query_personal_info = "CREATE TABLE IF NOT EXISTS users (_id text, email text, password text, " \
                      "name text, phone_no text, gender text, dob text, email_verified text, " \
                      "current_address text, permanent _address text, tel_no text, nationality text," \
                      " disability text, source_awards text, photo_path text, PRIMARY KEY('_id'))"

# tables for 1st form

query_language_table = "CREATE TABLE IF NOT EXISTS language (_id text, language text, understand text, " \
                       "speak text, read_write text, PRIMARY KEY('_id'))"

query_education = "CREATE TABLE IF NOT EXISTS education (_id text, course text, from_date text," \
                  " till_date text, institution text, " \
                  "board_university text, PRIMARY KEY('_id'))"

query_about = "CREATE TABLE IF NOT EXISTS about (_id text, about_you text, why_volunteer text, " \
              "communities_associated text, motivation text, form_1_status text,PRIMARY KEY('_id'))"

# query_references = "CREATE TABLE IF NOT EXISTS references (_id text, first_second text, full_name text," \
#                    " address text, tel_no text, email text, occupation text, relation text)"

query_reference = "CREATE TABLE IF NOT EXISTS reference (_id text, first_second text, " \
                   "full_name text, address text, tel_no text, email text, occupation text," \
                  " relation text, PRIMARY KEY('_id'))"

# Tables for 2nd form

query_volunteering_experience = "CREATE TABLE IF NOT EXISTS volunteering_experience (_id text, " \
                                "voluteered_as text, organisation_name text, intended_impact text," \
                                " assignment_details text, period_engagement text, " \
                                "frequency_engagement text, hours_volunteering text, PRIMARY KEY('_id'))"


query_volunteering_outcome = "CREATE TABLE IF NOT EXISTS volunteering_outcome (_id text, " \
                             "volunteering_outcome text, outcome_community text, impact text, " \
                             "innovation_initiative text, experience_impact text, PRIMARY KEY('_id'))"

query_volunteering_organisation = "CREATE TABLE IF NOT EXISTS volunteering_organisation (_id text," \
                                  " name text, address text, contact_person text, phone text, " \
                                  "mobile text, email text, PRIMARY KEY('_id'))"

# another table for the videos and photos of the volunteer

cursor.execute(query_personal_info)
cursor.execute(query_language_table)
cursor.execute(query_education)
cursor.execute(query_about)
cursor.execute(query_reference)
cursor.execute(query_volunteering_experience)
cursor.execute(query_volunteering_outcome)
cursor.execute(query_volunteering_organisation)


connection.commit()
connection.close()
