import os
import datetime

import conversions

from flask import Flask
from flask import request
from flask import jsonify
from flask import abort
from flask_cors import CORS

from flaskext.mysql import MySQL

DEBUG = True

app = Flask(__name__)

CORS(app)

app.config.from_object(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = os.environ['DB_USER']
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ['DB_PASSWORD']
app.config['MYSQL_DATABASE_DB'] = 'poly_professors'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_CHARSET'] = 'utf8mb4'
mysql.init_app(app)


# Return a list of professors
@app.route('/search', methods=['GET'])
def search_results():
    search = request.args.get('terms')
    sort = request.args.get('sort')
    department = request.args.get('department')
    search_by_dep = False

    search_mode = ''

    conn = mysql.connect()
    cursor = conn.cursor()

    if department is not None and department in conversions.departments.keys():
            search_mode = f" department='{department}'"
            search_by_dep = True

    if sort == 'rating':
        search_mode += " ORDER BY rating DESC, numEvaluations DESC"
    elif sort == 'department':
        search_mode += " ORDER BY department ASC"
    elif sort == 'review':
        search_mode += " ORDER BY department ASC"

    if search is None:
        if search_by_dep:
            search_mode = " WHERE" + search_mode

        cursor.execute("SELECT * FROM professors" + search_mode)
        data = cursor.fetchall()

        conn.close()
        return jsonify(data)

    if search_by_dep:
        search_mode = " AND" + search_mode

    search_str = f'%{search.lower()}%'
    cursor.execute("""SELECT * FROM professors
                      WHERE (CONCAT(firstName, ' ', lastName) LIKE %s
                      OR CONCAT(lastName, ' ', firstName) LIKE %s)""" + search_mode,
        (search_str, search_str))
    data = cursor.fetchall()

    # we found nothing, lets keep trying
    if len(data) == 0:
        data = smart_search(search, cursor, search_mode)

    conn.close()
    return jsonify(data)


# Get a single professor
@app.route('/professor', methods=['GET'])
def get_professor():
    try:
        id = int(request.args.get('id'))
    except:
        abort(405)

    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM professors WHERE id=%s", id)
    conn.close()
    return jsonify(cursor.fetchone())


# Return all reviews
@app.route('/reviews', methods=['GET'])
def get_reviews():
    prof_id = request.args.get('id')

    if not prof_id:
        abort(400)
    try:
        prof_id = int(prof_id)
    except:
        abort(400)

    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reviews WHERE professorId = %s ORDER BY dateTaken DESC", prof_id)

    conn.close()
    return jsonify(cursor.fetchall())


# Add a review
@app.route('/reviews', methods=['POST'])
def add_review():
    review_data = []
    data_keys = ['department', 'num', 'profId', 'year', 'requirement', 'grade', 'date', 'rating', 'review']

    for key in data_keys:
        data = request.form.get(key)
        if key == 'date':
            now = datetime.datetime.today()
            str_now = now.date().isoformat()
            review_data.append(str_now)
            continue

        format_data = check_valid(key, data)
        review_data.append(format_data)

    conn = mysql.connect()
    cursor = conn.cursor()

    prof_id = review_data[2]

    # add course if it wasn't already in DB
    cursor.execute("INSERT IGNORE courses (courseDepartment, courseNumber) VALUES (%s, %s)",
        review_data[:2])

    # add review
    cursor.execute("""INSERT INTO reviews (courseDepartment, courseNumber, professorId,
        studentYear, courseRequirement, studentGrade, dateTaken, rating, review)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
        review_data)

    # recalculate professor rating
    cursor.execute("""UPDATE professors SET professors.rating =
        (SELECT AVG(reviews.rating) FROM reviews
        WHERE reviews.professorId = professors.id) WHERE professors.id = %s""",
        prof_id)

    # recalculate number of evaluations for professor
    cursor.execute("""UPDATE professors SET professors.numEvaluations =
        (SELECT COUNT(*) FROM reviews
        WHERE reviews.professorId = professors.id) WHERE professors.id = %s""",
        prof_id)

    conn.commit()
    conn.close()
    return jsonify(success=True)


# Return all courses
@app.route('/courses', methods=['GET'])
def get_courses():
    prof_id = request.args.get('id')

    if not prof_id:
        courses = list(conversions.departments.keys())
    else:
        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT DISTINCT courseDepartment FROM reviews WHERE professorId = %s",
            prof_id)
        courses = [row[0] for row in cursor.fetchall()]

        conn.close()

    return jsonify(courses)


# make sure the review doesn't have any funny business going on
def check_valid(key, data):
    if data is None:
        abort(400)

    if key == 'review' and len(data) == 0:
        abort(400)

    elif key == 'profId':
        try:
            data = int(data)
            if not data > 0:
                abort(400)
        except:
            abort(400)

    elif key == 'grade' and data not in conversions.valid_grades:
        abort(400)

    elif key == 'rating':
        data = conversions.rating_to_num.get(data)
        if data is None:
            abort(400)

    elif key == 'requirement':
        data = conversions.req_to_num.get(data)
        if data is None:
            abort(400)

    elif key == 'year':
        data = conversions.year_to_num.get(data)
        if data is None:
            abort(400)

    elif key == 'num':
        try:
            data = int(data)
            if not 0 <= data <= 1000:
                abort(400)
        except:
            abort(400)

    return data

# Try and find mispellings for a professor search

# NOTE: the LEVENSHTEIN function does not come with mysql,
# the implementation was found at:
# https://gist.github.com/Kovah/df90d336478a47d869b9683766cff718
def smart_search(search, cursor, search_mode):
    search = search.split(' ')
    l_threshold = 1

    # Search had 1 name
    if len(search) == 1:
        cursor.execute(f"""SELECT * FROM professors
                            WHERE (LEVENSHTEIN(lastName, %s) <= {l_threshold}
                            OR LEVENSHTEIN(firstName, %s) <= {l_threshold})""" + search_mode,
                (search, search))

        return cursor.fetchall()

    # Search had 2+ names
    else:
        l_threshold + 1

        # first assume that the first word is the first name
        cursor.execute(f"""SELECT * FROM professors
                    WHERE (LEVENSHTEIN(lastName, %s) <= {l_threshold}
                    AND LEVENSHTEIN(firstName, %s) <= {l_threshold})""" + search_mode,
        (search[0], search[1]))

        # if that yields nothing, then assume first word is the last name
        data = cursor.fetchall()
        if(len(data) > 0):
            return data

        cursor.execute(f"""SELECT * FROM professors
                    WHERE (LEVENSHTEIN(lastName, %s) <= {l_threshold}
                    AND LEVENSHTEIN(firstName, %s) <= {l_threshold})""" + search_mode,
        (search[1], search[0]))

        return cursor.fetchall()