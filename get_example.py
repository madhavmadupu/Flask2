from flask import *

app = Flask(__name__)


@app.route('/login', methods=['GET'])
def login():
    uname = request.args.get('uname')
    passwrd = request.args.get('pass')
    if uname == "Liji" and passwrd == "1234":
        return f"Welcome {uname}"
    else:
        return "Wrong username and password"


if __name__ == '__main__':
    app.run(debug=True)