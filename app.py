import os

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flaskr.services import series

app = Flask(__name__)
app.config['SECRET_KEY'] = 'someVerySecretKey!'
if(os.environ.get("DATABASE_FILENAME", "database.db") == "database.db"):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+os.environ.get("DATABASE_FILENAME", "database.db")
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))


class Calculation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(15))
    owner = db.Column(db.Integer, unique=True)
    input = db.Column(db.Integer)
    output = db.Column(db.Integer)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])


@app.route('/')
def index():
    return render_template('index.html', authenticated=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return render_template('connected.html',name=form.username.data)

        return '<h1>Invalid username or password</h1>'

    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return render_template('createdAccount.html', name=form.username.data)

    return render_template('signup.html', form=form)


@app.route('/dashboard')
@login_required
def dashboard():
    calculations=Calculation.query.filter_by(owner=current_user.id).all()
    for row in calculations :
        print(row.id, row.owner, row.input, row.output, row.type)

    return render_template('dashboard.html', name=current_user.username,calculations=calculations)


@app.route('/calculator')
@login_required
def calculator():
    return render_template('calculator.html', name=current_user.username, id=current_user.id)


@app.route('/calculator/fibonacci/<input>')
@login_required
def fibonacci(input):
    input=int(input)
    inp = input
    output = series.fibonacci(inp)
    calculation = Calculation(input=input, output=output, owner=current_user.id, type="fibonacci")
    db.session.add(calculation)
    db.session.commit()

    return '<h1>New calculation has been created!' + str(output) + '</h1>'


@app.route('/calculator/square_numbers/<input>')
@login_required
def square_numbers(input):
    input=int(input)
    inp = input
    output = series.square_numbers(inp)
    calculation = Calculation(input=input, output=output, owner=current_user.id, type="square_numbers")
    db.session.add(calculation)
    db.session.commit()

    return '<h1>New calculation has been created!' + str(output) + '</h1>'


@app.route('/calculator/arithmetic_sum/<input>')
@login_required
def arithmetic_sum(input):
    input=int(input)
    inp = input
    output = series.arithmetic_sum(inp)
    calculation = Calculation(input=input, output=output, owner=current_user.id, type="arithmetic_sum")
    db.session.add(calculation)
    db.session.commit()

    return '<h1>New calculation has been created!' + str(output) + '</h1>'


@app.route('/calculator/pentagonal_series/<input>')
@login_required
def pentagonal_series(input):
    input=int(input)
    inp = input
    output = series.pentagonal_series(inp)
    calculation = Calculation(input=input, output=output, owner=current_user.id, type="pentagonal_series")
    db.session.add(calculation)
    db.session.commit()

    return '<h1>New calculation has been created!' + str(output) + '</h1>'


@app.route('/calculator/caterer_sequence/<input>')
@login_required
def caterer_sequence(input):
    input=int(input)
    inp = input
    output = series.caterer_sequence(inp)
    calculation = Calculation(input=input, output=output, owner=current_user.id, type="caterer_sequence")
    db.session.add(calculation)
    db.session.commit()
    return '<h1>New calculation has been created!' + str(output) + '</h1>'


@app.route('/suminputs')
@login_required
def sumInputs():
    calculations=Calculation.query.filter_by(owner=current_user.id).all()
    sum=0
    for row in calculations:
        sum += row.input

    return render_template("sums.html", inputs=True, sum=sum)


@app.route('/sumoutputs')
@login_required
def sumOutput():
    calculations=Calculation.query.filter_by(owner=current_user.id).all()
    sum=0
    for row in calculations:
        sum += row.output
    return render_template("sums.html", input=False, sum=sum)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)