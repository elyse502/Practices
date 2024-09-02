#!/home/elysee_niyibizi/Practices/python/UDEMY/flask/flaskenv/bin/python3
# 59. Tutorial 58-Flask Mail Extension

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'elyseniyibizi502@gmail.com'
app.config['MAIL_PASSWORD'] = 'xsfg lhym rhva vube'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def index():
    msg = Message('Hello', sender = 'xyz@gmail.com', recipients = ['abc@gmail.com'])
    msg.body = "Hello Flask! This message is sent from Flask-Mail"
    mail.send(msg)
    return "Message Sent"

if __name__ == '__main__':
    app.run(debug = True)