from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    uname = request.form['uname']
    passwrd = request.form['pass']
    if uname == "admin" and passwrd == "1234":
        return render_template("newpage.html")
    else:
        return "Wrong username and password"


@app.route('/')
def load():
      return render_template('login.html') # opens the html page specified


if __name__ == '__main__':
    app.run(debug=True)