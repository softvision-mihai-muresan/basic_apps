from browser import document, ajax

qs = ''
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
        document["main_area"].html = "error "+req.text


def on_get_complete(req):
    if req.status == 200 or req.status == 0:
        #  Take our response and inject it into the html div with id='main'
        document["main_area"].html = req.text
    else:
        document["main_area"].html = "error "+req.text


# get_data(url, qs)
# post_data(url, qs)

def account_click():
    get_data("/account", qs)
document['myacc'].bind('click', lambda:  account_click)