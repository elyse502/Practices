#!/home/elysee_niyibizi/Practices/python/UDEMY/flask/flaskenv/bin/python3
# Tutorial 54-Flask Framework Template

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    str="""
<html>
<body>
<h1>Hello, World!</h1>
</body>
</html>
"""
    return str

if __name__ == '__main__':
    app.run(debug=True)