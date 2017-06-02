from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect 
from flask import session
app = Flask(__name__)
app.secret_key = '\x02gM\x8f\xa1^\xd7c\xdaPj!\xfa\xce]\x1d\x1dDS\xdf\xac\x0b\xa3S'

email_addresses = [] 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/hahn'
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    author = "Me"
    name = "You"
    return render_template('index.html', author=author, name=name)

@app.route('/signup', methods = ['POST'])
def signup(): 
    email = request.form['email']
    email_addresses.append(email)
    session['email'] = email
    print(email_addresses)
    return redirect('/')

@app.route('/emails.html')
def emails():
    return render_template('emails.html', email_addresses=email_addresses)

@app.route('/unregister')
def unregister():
    # Make sure they've already registered an email address
    if 'email' not in session:
        return "You haven't submitted an email!"
    email = session['email']
    # Make sure it was already in our address list
    if email not in email_addresses:
        return "That address isn't on our list"
    email_addresses.remove(email)
    del session['email'] # Make sure to remove it from the session
    return 'We have removed ' + email + ' from the list!'


if __name__ == '__main__':
    app.run()
