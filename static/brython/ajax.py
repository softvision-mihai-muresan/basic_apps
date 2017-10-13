
from browser import document, ajax, timer
from browser.local_storage import storage

# URL Query String
qs = ''
# URL to work on
url = ''


def bind_register_link(ev):
    document['register_link'].bind('click', register_link_click)


def bind_register_button(ev):
    document['register_btn'].bind('click', register_button_click)


def bind_login_button(ev):
    document['login_btn'].bind('click', login_button_click)


def bind_logout_button(ev):
    try:
        document['logout'].bind('click', logout_click)
    except: pass


def bind_my_acc_button(ev):
    try:
        document['myacc'].bind('click', account_click)
    except: pass


def reload_page(ev):
    document['main_wrapper'].html = ev.text


def post_data(url, qs, callbacks=None):
    req = ajax.ajax()
    # Bind the complete State to the on_post_complete function
    req.bind('complete', lambda req:on_get_complete(req, callbacks))
    # send a POST request to the url
    req.open('POST', url, True)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    # send data as a dictionary
    req.send(qs)


def get_data(url, qs, callbacks=None):
    req = ajax.ajax()
    req.bind('complete', lambda req:on_get_complete(req, callbacks))
    # Bind the complete State to the on_get_complete function
    req.open('GET', url+'?'+qs, True)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    req.send()


def on_post_complete(req, callbacks=None):
    if req.status == 200 or req.status == 0:
        #  Take our response and inject it into the html div with id='main'
        document["main_area"].html = req.text
        if callbacks is not None:
            for callback in callbacks:
                callback(req)
    else:
        document["main_area"].html = "error " + req.text


def on_get_complete(req, callbacks=None):
    if req.status == 200 or req.status == 0:
        #  Take our response and inject it into the html div with id='main'
        document["main_area"].html = req.text
        if callbacks is not None:
            for callback in callbacks:
                callback(req)
        bind_my_acc_button(req)
        bind_logout_button(req)
    else:
        document["main_area"].html = "error " + req.text


def contact_link_click(ev):
    get_data("/contact", qs)


def logo_link_click(ev):
    get_data("/main_page", qs)


def products_link_click(ev):
    get_data("/products_page", qs)


def register_button_click(ev):
    _firstName = document['inputFirstName'].value
    _lastName = document['inputLastName'].value
    _email = document['inputEmail'].value
    _password = document['inputPassword'].value
    qs = {'inputFirstName': _firstName,
          'inputLastName': _lastName,
          'inputEmail': _email,
          'inputPassword': _password}
    post_data("/register_action", qs)


def login_button_click(ev):
    reload = [reload_page, bind_logout_button, bind_my_acc_button]

    _email = document['login_email'].value
    _password = document['login_password'].value
    qs = {'login_email': _email,
          'login_password': _password}

    post_data("/login_action", qs, reload)


def logout_click(ev):
    callback = [reload_page]
    get_data("/logout", qs, callback)


def account_click(ev):
    callbacks = [bind_register_link, bind_login_button]
    get_data("/account", qs, callbacks)


def register_link_click(ev):
    callbacks = [bind_register_button]
    get_data("/register", qs, callbacks)

try:
    document['myacc'].bind('click', account_click)
except: pass
try:
    document['myacc2'].bind('click', account_click)
except: pass
document['contact_link'].bind('click', contact_link_click)
document['logo_link'].bind('click', logo_link_click)

document['header_running_link'].bind('click', products_link_click)
document['header_fitness_link'].bind('click', products_link_click)
document['header_tennis_link'].bind('click', products_link_click)
document['header_football_link'].bind('click', products_link_click)
document['header_golf_link'].bind('click', products_link_click)

document['footer_running_link'].bind('click', products_link_click)
document['footer_cycling_link'].bind('click', products_link_click)
document['footer_triathlon_link'].bind('click', products_link_click)
document['footer_fitness_link'].bind('click', products_link_click)
document['footer_tennis_link'].bind('click', products_link_click)
document['footer_more_sports_link'].bind('click', products_link_click)
document['footer_style_link'].bind('click', products_link_click)
document['footer_special_link'].bind('click', products_link_click)
document['footer_brand_events_link'].bind('click', products_link_click)
