from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'challenge'
app.debug = True


@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    session['username'] = request.form["username"]
    session['password'] = request.form["password"]
    print (session)
    #return session


if __name__ == '__main__':
    app.run()
