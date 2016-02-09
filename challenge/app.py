from flask import Flask, render_template, request, redirect, url_for, session
from db import db
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)
app.config['SECRET_KEY'] = 'challenge'
app.debug = True


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        log_dict = request.form.to_dict()
        if 'login' in log_dict:
            return render_template('login.html')
        else:
            return render_template('register.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        reg_dict = request.form.to_dict()
        reg_dict['password'] = pbkdf2_sha256.encrypt(reg_dict['password'], rounds=200, salt_size=16)
        db.insert(
            'db/example.db',
            'profile',
            "'username', 'password', 'email'",
            "'{}', '{}', '{}'".format(reg_dict['username'], reg_dict['password'], reg_dict['email']))
    return render_template('index.html')

#######
# TODO
# ne app.configbol hivja hogy jo-e a login, hanem a db-bol
# igy kell azonostiani: pbkdf2_sha256.verify("password", hash)
#####

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)



if __name__ == '__main__':
    app.run()
