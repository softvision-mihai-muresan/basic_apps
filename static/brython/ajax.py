from browser import document, ajax

# URL Query String
qs = ''
# URL to work on
url = ''


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


def account_click(ev):
    get_data("/account", qs)


def contact_link_click(ev):
    get_data("/contact", qs)


def logo_link_click(ev):
    get_data("/main_page", qs)


def products_link_click(ev):
    get_data("/products_page", qs)

document['myacc'].bind('click', account_click)
document['contact_link'].bind('click', contact_link_click)
document['logo_link'].bind('click', logo_link_click)

document['running_link'].bind('click', products_link_click)
document['fitness_link'].bind('click', products_link_click)
document['tennis_link'].bind('click', products_link_click)
document['football_link'].bind('click', products_link_click)
document['golf_link'].bind('click', products_link_click)
document['running_link'].bind('click', products_link_click)
document['cycling_link'].bind('click', products_link_click)
document['triathlon_link'].bind('click', products_link_click)
document['fitness_link'].bind('click', products_link_click)
document['tennis_link'].bind('click', products_link_click)
document['more_sports_link'].bind('click', products_link_click)
document['style_link'].bind('click', products_link_click)
document['special_link'].bind('click', products_link_click)
document['brand_events_link'].bind('click', products_link_click)
