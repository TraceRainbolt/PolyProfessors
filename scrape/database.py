import os
import datetime

import conversions

import mysql.connector

# Max length of a review is 10000 characters.
# Should be enough to say what you gotta say.
MAX_REVIEW_LEN = 10000

class Database(object):
    config = {
        'host'     : 'localhost',
        'user'     : os.environ['DB_USER'],
        'password' : os.environ['DB_PASSWORD'],
        'db'       : 'poly_professors'
    }

    def __init__(self):
        self.connection = mysql.connector.connect(**self.config)
        self.connection.set_charset_collation(charset='utf8mb4')
        self.cursor = self.connection.cursor()
        self.truncate_tables()


    # Reset all tables for each scrape
    def truncate_tables(self):
        self.cursor.execute("SET FOREIGN_KEY_CHECKS=0")
        self.cursor.execute("TRUNCATE professors")
        self.cursor.execute("TRUNCATE courses")
        self.cursor.execute("TRUNCATE reviews")
        self.cursor.execute("SET FOREIGN_KEY_CHECKS=1")

    # Add a professor to the database. Returns the professors internal ID
    def add_professor(self, name, department, rating):
        add_professor_query = """INSERT INTO professors
                (lastName, firstName, department, rating)
                VALUES (%s, %s, %s, %s)"""

        name_list = [s.strip() for s in name.split(",")]
        if len(name_list) > 2:
            name_list = [name_list[0], name_list[-1]]

        department = conversions.departments[department]

        data_professor = (*name_list, department, rating)

        self.cursor.execute(add_professor_query, data_professor)
        self.connection.commit()

        return self.cursor.lastrowid


    def update_professor(self, name, department, rating):
        name_list = [s.strip().replace(',', '') for s in name.split(' ')][:2]

        update_professor_query = """UPDATE professors SET
                lastName = %s, firstName = %s, department = %s, rating = %s
                WHERE lastName = %s AND firstName = %s"""

        get_id_query = ("SELECT id FROM professors WHERE lastName = %s AND firstName = %s")

        data_professor = (name_list[0], name_list[1], department, rating,
            name_list[0], name_list[1])

        self.cursor.execute(update_professor_query, data_professor)
        self.connection.commit()


    def add_review(self, review_data, review_text, class_, prof_id):
        review_data = review_data[:4]
        review_text = review_text[:MAX_REVIEW_LEN]
        class_dep, class_num = class_.split(' ')

        # convert strings to values that represent them in the database
        month, year = review_data[3].split()
        month = conversions.month_to_num[month]
        year = int(year)

        review_data[0] = conversions.year_to_num[review_data[0]]
        review_data[2] = conversions.req_to_num[review_data[2]]
        review_data[3] = datetime.datetime(year, month, 1)

        add_class_query = """INSERT IGNORE INTO courses (courseDepartment, courseNumber)
            VALUES (%s, %s)"""

        add_review_query = """INSERT INTO reviews (courseDepartment, courseNumber, professorId, studentYear,
            studentGrade, courseRequirement, dateTaken, rating, review) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        self.cursor.execute(add_class_query, (class_dep, class_num))


        self.cursor.execute(add_review_query, (class_dep, class_num, prof_id, *review_data, None, review_text))
        self.connection.commit()


    def update_rating_and_eval(self):
      # Because we do not know the actual rating value of any polyrating reviews,
      # we set them all to the overall average rating. This makes sure new reviews will
      # update the average correctly.
      self.cursor.execute("""UPDATE reviews INNER JOIN professors
        ON reviews.professorId = professors.id SET reviews.rating = professors.rating""")

      self.cursor.execute("""UPDATE professors SET professors.numEvaluations =
        (SELECT COUNT(*) FROM reviews WHERE reviews.professorId = professors.id)""")

      self.connection.commit()


    def __del__(self):
        try:
            self.connection.close()
        except AttributeError:
            print('Cannot close connection: no connection made.')