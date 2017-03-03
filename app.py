from flask import Flask, render_template, request, json, session, redirect, url_for, escape, flash
from hashlib import md5
import os

application = Flask(__name__)


class ServerError(Exception):
    pass


@application.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 404


@application.route("/index")
@application.route("/")
def index():
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
            email_form = request.form['email']
            cursor.execute("SELECT COUNT(1) FROM users WHERE email = '{0}';".format(email_form))

            if not cursor.fetchone()[0]:
                raise ServerError('Invalid username')

            password_form = request.form['password']
            cursor.execute("SELECT password FROM users WHERE email = '{0}';".format(email_form))

            for row in cursor.fetchall():
                if md5(md5(application.secret_key).hexdigest() + md5(password_form).hexdigest()).hexdigest() == row[0]:
                    session['username'] = request.form['email']
                    conn.close()
                    return redirect(url_for('FEr9B3998EF64B169BD4092B185D632D'))
            raise ServerError('Invalid password')
    except ServerError as e:
        error = str(e)
    conn.close()
    return render_template('FEr9B3998EF64B169BD4092B185D632D.html', error=error)


@application.route('/action_logout')
def action_logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    application.run(port=port)
