# Tutorial 48-Flask Hello World (demonstration)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello TutorialsPoint!'

if __name__ == '__main__':
    app.run(debug=True)