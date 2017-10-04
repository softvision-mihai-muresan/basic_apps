from flask import Flask, render_template, request, json, session, redirect, url_for, escape, flash
from hashlib import md5
from flaskext.mysql import MySQL
import os

application = Flask(__name__)
# mysql = MySQL()
#
# # MySQL configurations
# application.config['MYSQL_DATABASE_USER'] = 'trainer'
# application.config['MYSQL_DATABASE_PASSWORD'] = 'trainer7'
# application.config['MYSQL_DATABASE_DB'] = 'qa_course'
# application.config['MYSQL_DATABASE_HOST'] = '52.2.195.57'
# application.secret_key = 'FEF9B%399-!8EF6- 4B16-[9BD4-092B1<85D632D'
# mysql.init_app(application)


class ServerError(Exception):
    pass


@application.errorhandler(404)
def page_not_found(e):
    # return render_template('index.html'), 404
    return render_template('WIP.html'), 404


@application.route("/index")
@application.route("/")
def index():
    if 'username' in session:
        username_session = escape(session['username']).capitalize()
        username_session = username_session.split('@')[0]

        return render_template('index.html', session_user_name=username_session, row=session['rows'])
    return render_template('index.html')


@application.route("/account", methods=['GET'])
def account():
    return render_template('account.html')


@application.route("/contact", methods=['GET'])
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    application.jinja_env.cache = {}
    application.run(host="0.0.0.0", port=port)
