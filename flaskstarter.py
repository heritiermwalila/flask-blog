from flask import Flask, render_template, flash, redirect, url_for
from forms import RegisterForm, LoginForm
from time import sleep

app = Flask(__name__)


app.config['SECRET_KEY'] = '653224d654b7d9f90d5c7764acb3ca44'

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about-us')
def about_us():
    return render_template('about-us.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        return redirect(url_for('home'))

    return render_template('login.html', form=form, title="Account login")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        flash(f'Your account was successfully created for {form.username.data}', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


if __name__ == '__main__':
    app.run(debug=True)