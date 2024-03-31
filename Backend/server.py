from flask import Flask
from form import LoginForm
from flask import render_template

app = Flask(__name__, template_folder='../Frontend')

app.config['SECRET_KEY'] = '123456790'

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('signup.html', form=form)
