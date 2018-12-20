import mysql.connector
import datetime

year_to_num = {'Freshman' : 0,
               'Sophomore' : 1,
               'Junior' : 2,
               'Senior' : 3,
               '5th Year Senior': 4,
               'Graduate Student' : 5}

req_to_num = {'General Ed' : 0,
              'Required (Major)' : 1,
              'Required (Support)' : 2,
              'Elective' : 3,
              'N/A' : 4}

month_to_num = { 'Jan' : 1,
                 'Feb' : 2,
                 'Mar' : 3,
                 'Apr' : 4,
                 'May' : 5,
                 'Jun' : 6,
                 'Jul' : 7,
                 'Aug' : 8,
                 'Sep' : 9,
                 'Oct' : 10,
                 'Nov' : 11,
                 'Dec' : 12 }

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


    def add_professor(self, name, department, rating):
        add_professor_query = """INSERT INTO professors
                (lastName, firstName, department, rating)
                VALUES (%s, %s, %s, %s)"""

        name_list = [s.strip() for s in name.split(",")]
        if len(name_list) > 2:
            name_list = [name_list[0], name_list[-1]]

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
        review_text = review_text[:10000]
        class_dep, class_num = class_.split(' ')
        month, year = review_data[3].split()
        month = month_to_num[month]
        year = int(year)

        review_data[0] = year_to_num[review_data[0]]
        review_data[2] = req_to_num[review_data[2]]
        review_data[3] = datetime.datetime(year, month, 1)

        add_class_query = """INSERT IGNORE INTO courses (courseDepartment, courseNumber)
            VALUES (%s, %s)"""

        add_review_query = """INSERT INTO reviews (courseDepartment, courseNumber, professorId, studentYear,
            studentGrade, courseRequirement, dateTaken, rating, review) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        self.cursor.execute(add_class_query, (class_dep, class_num))


        self.cursor.execute(add_review_query, (class_dep, class_num, prof_id, *review_data, None, review_text))
        self.connection.commit()


    def __del__(self):
        try:
            self.connection.close()
        except AttributeError:
            print('Cannot close connection: no connection made.')