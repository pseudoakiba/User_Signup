from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

username = ''
password = ''

@app.route("/register", methods=['POST'])
def signup():
    username_error = ''
    password_error = ''
    confirm_error = ''
    email_error = ''

    username = request.form['username']
    password = request.form['password']
    password_confirm = request.form['password_confirm']
    email = request.form['email']
    if email != '':
        if email.find('@') != 1 or email.find('.') != 1 or len(email) <3:
            email_error = ' Emails must be formatted properly'
    if len(username) <3 or len(password) <3 or password != password_confirm or email_error != '':
        error = "Error(s) detected"
        if len(username) <3:
            username_error = ' Username should be 3 or more characters'
        if len(password) <3:
            password_error = ' Password should be 3 or more characters'
        if password_confirm != password:
            confirm_error = ' Passwords must match'
        return render_template('index.html',username=username,email=email,username_error=username_error,password_error=password_error,confirm_error=confirm_error,email_error=email_error,error=error) #redirect("/?error")
    return render_template('welcome.html',username=username)

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('index.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()
