from flask import *

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    uname = request.form['uname']
    passwrd = request.form['pass']
    if uname == "Liji" and passwrd == "1234":
        return render_template('response2.html',name=uname)
    else:
        return render_template('response2.html',name=uname)


@app.route('/')
def message():
      return render_template('mypage.html') # opens the html page specified


if __name__ == '__main__':
    app.run(debug=True)