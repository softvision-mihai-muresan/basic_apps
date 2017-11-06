from flask import render_template, request, json, session, redirect, url_for, escape, flash, g
import os
import typing
from orm import *
from waitress import serve


class ServerError(Exception):
    pass


login_manager.login_view = 'account'


@application.before_request
def before_request():
    g.user = current_user


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@application.errorhandler(404)
def page_not_found(e):
    return render_template('WIP.html'), 404


@application.route("/index")
@application.route("/")
def index():
    if g.user.is_authenticated:
        return render_template('index.html', user_name=g.user.last_name)
    return render_template('index.html')


@application.route("/account", methods=['GET'])
def account():
    return render_template('account.html')


@application.route("/contact", methods=['GET'])
def contact():
    return render_template('contact.html')


@application.route("/products_page", methods=['GET'])
def products_pg():
    products = Product.query.all()
    return render_template('product.html', products=products)


@application.route("/single_product", methods=['GET'])
def single_product_pg():
    return render_template('single.html')


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
    _email = request.form.get('inputEmail')
    _password = request.form.get('inputPassword')

    # validate the received values
    if not _email and not _password:
        return json.dumps({'html': '<span>Enter the required fields</span>'})
    else:
        user = User(_fname, _lname, _email, _password)

        db.session.add(user)
        db.session.commit()
        flash('Record was successfully added')
        return render_template('account.html')


@application.route("/login_action", methods=['POST'])
def login():
    # read the posted values from the UI
    _email = request.form['login_email']
    _password = generate_hash(request.form['login_password'])

    # validate the received values
    if not _email and not _password:
        return json.dumps({'html': '<span>Enter the required fields</span>'})
    else:
        registered_user = User.query.filter_by(email=_email, password=_password).first()
        if registered_user is None:
            flash('Username or Password is invalid', 'error')
            return render_template('account.html')
        login_user(registered_user)
        # return render_template('index.html')
        return render_template('main_page.html')


@application.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return render_template('main_page.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    application.jinja_env.cache = {}
    # application.run(host="0.0.0.0", port=port)
    serve(application, listen='0.0.0.0:{}'.format(port))

