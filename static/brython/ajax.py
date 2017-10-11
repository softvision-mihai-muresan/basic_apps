
from browser import document, ajax, timer

# URL Query String
qs = ''
# URL to work on
url = ''


def bind_register_link():
    document['register_link'].bind('click', register_link_click)


def bind_register_button():
    document['register_btn'].bind('click', register_button_click)


def bind_login_button():
    document['login_button'].bind('click', login_button_click)


def post_data(url, qs):
    req = ajax.ajax()
    # Bind the complete State to the on_post_complete function
    req.bind('complete', on_post_complete)
    # send a POST request to the url
    req.open('POST', url, True)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    # send data as a dictionary
    req.send(qs)


def get_data(url, qs):
    req = ajax.ajax()
    req.bind('complete', on_get_complete)
    # Bind the complete State to the on_get_complete function
    req.open('GET', url+'?'+qs, True)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    req.send()


def on_post_complete(req):
    if req.status == 200 or req.status == 0:
        #  Take our response and inject it into the html div with id='main'
        document["main_area"].html = req.text
    else:
        document["main_area"].html = "error " + req.text


def on_get_complete(req):
    if req.status == 200 or req.status == 0:
        #  Take our response and inject it into the html div with id='main'
        document["main_area"].html = req.text
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
    _email = document['inputEmail'].value
    _password = document['inputPassword'].value
    qs = {'inputEmail': _email,
          'inputPassword': _password}
    post_data("/login_action", qs)


def account_click(ev):
    get_data("/account", qs)
    timer.set_timeout(bind_register_link, 1000)


def register_link_click(ev):
    get_data("/register", qs)
    timer.set_timeout(bind_register_button, 1000)


document['myacc'].bind('click', account_click)
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
