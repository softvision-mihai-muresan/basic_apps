from flask import render_template, request, json, session, redirect, url_for, escape, flash
import os
from orm import *


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


@application.route("/products_page", methods=['GET'])
def products_pg():
    return render_template('product.html')


@application.route("/main_page", methods=['GET'])
def main_pg():
    return render_template('main_page.html')


@application.route("/register", methods=['GET'])
def register_pg():
    return render_template('register.html')


@application.route("/register_action", methods=['POST'])
def register():
    # read the posted values from the UI
    _fname = request.form.get('inputFirstName')
    _lname = request.form.get('inputLastName')
    _email = escape(request.form.get('inputEmail'))
    _password = request.form.get('inputPassword')

    print("-" * 40)
    print(_fname)
    print(_lname)
    print(_email)
    print(_password)
    print("-" * 40)
    # validate the received values
    if not _email and not _password:
        return json.dumps({'html': '<span>Enter the required fields</span>'})
    else:
        user = User(_email, _fname, _lname, _password)
        # user.password.set(_password)

        db.session.add(user)
        db.session.commit()
        flash('Record was successfully added')
        return redirect(url_for('show_all'))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    application.jinja_env.cache = {}
    application.run(host="0.0.0.0", port=port)
