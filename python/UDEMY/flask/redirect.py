# #!/home/elysee_niyibizi/Practices/python/UDEMY/flask/flaskenv/bin/python3

from flask import Flask, redirect, url_for, render_template, request

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')