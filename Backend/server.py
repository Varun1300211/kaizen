from flask import Flask
from form import LoginForm
from flask import render_template

app = Flask(__name__, template_folder='../Frontend')

app.config['SECRET_KEY'] = '123456790'

@app.route('/')
def kaizen():
    return render_template('index.html')


@app.route('/form')
def login():
    impact_data = ['P', 'Q', 'C', 'D', 'S', 'M', 'E']  
    form = LoginForm()
    form.impact.choices = [(impact, impact) for impact in impact_data]
    return render_template('form.html', form=form)
