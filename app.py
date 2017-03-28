from flask import Flask, render_template, request, json, session, redirect, url_for, escape, flash
from hashlib import md5
from flaskext.mysql import MySQL
import os

application = Flask(__name__)
mysql = MySQL()

# MySQL configurations
application.config['MYSQL_DATABASE_USER'] = 'trainer'
application.config['MYSQL_DATABASE_PASSWORD'] = 'trainer7'
application.config['MYSQL_DATABASE_DB'] = 'qa_course'
application.config['MYSQL_DATABASE_HOST'] = '52.2.195.57'
application.secret_key = 'FEF9B%399-!8EF6- 4B16-[9BD4-092B1<85D632D'
mysql.init_app(application)


class ServerError(Exception):
    pass


@application.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 404


@application.route("/index")
@application.route("/")
def index():
    if 'username' in session:
        username_session = escape(session['username']).capitalize()
        username_session = username_session.split('@')[0]

        return render_template('index.html', session_user_name=username_session)
    return render_template('index.html')


@application.route('/action_login', methods=['POST'])
def action_login():
    conn = mysql.connect()
    cursor = conn.cursor()
    if 'username' in session:
        return redirect(url_for('index'))

    error = None
    try:
        if request.method == 'POST':
            email_form = request.form['inputEmail']
            cursor.execute("SELECT COUNT(1) FROM users WHERE email = '{0}';".format(email_form))

            if not cursor.fetchone()[0]:
                raise ServerError('Invalid username')

            password_form = request.form['inputPassword']
            cursor.execute("SELECT password FROM users WHERE email = '{0}';".format(email_form))

            for row in cursor.fetchall():
                hash_pwd = md5(md5(application.secret_key).hexdigest() + md5(password_form).hexdigest()).hexdigest()
                print (hash_pwd)
                if hash_pwd == row[0]:
                    session['username'] = request.form['inputEmail']
                    conn.close()
                    return redirect(url_for('index'))
            raise ServerError('Invalid password')
    except ServerError as e:
        error = str(e)
    conn.close()
    return render_template('index.html', error=error)


@application.route('/action_register', methods=['POST'])
def action_register():
    conn = mysql.connect()
    cursor = conn.cursor()
    # read the posted values from the UI
    _fname = request.form['inputFirstName']
    _lname = request.form['inputLastName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    # validate the received values
    if not _email and not _password:
        return json.dumps({'html': '<span>Enter the required fields</span>'})
    else:
        json.dumps({'html': '<span>All fields good !!</span>'})

        cursor.execute("SELECT COUNT(1) FROM users WHERE email = '{0}';".format(_email))

        if cursor.fetchone()[0]:
            flash('Email already used')
            return redirect(url_for('index'))

        _hashed_password = md5(md5(application.secret_key).hexdigest() + md5(_password).hexdigest()).hexdigest()
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES ('{0}', '{1}', '{2}', '{3}')".format(
            _fname, _lname, _email, _hashed_password)
        cursor.execute(query)
        conn.commit()
    return redirect(url_for('index'))


@application.route('/action_logout')
def action_logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    application.run(port=port)
