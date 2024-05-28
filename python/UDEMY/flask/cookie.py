#!/home/elysee_niyibizi/Practices/python/UDEMY/flask/flaskenv/bin/python3
# Tutorial 55-Flask Framework Cookies

from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('setcookie.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)
        return resp
    
@app.route('/getcookie')
def getcookie():
    """
    Get the value of the 'userID' cookie from the request and return a welcome message if the cookie exists,
    otherwise return a message indicating that no cookie was found.

    :return: A string containing a welcome message if the 'userID' cookie exists, otherwise a message indicating
             that no cookie was found.
    """
    name = request.cookies.get('userID')
    if name:
        return '<h1>welcome {}</h1>'.format(name)
    else:
        return '<h1>No cookie found</h1>'

if __name__ == '__main__':
    app.run(debug = True)