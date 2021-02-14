from flask import render_template, redirect, flash, url_for
from blog import app
from blog.forms import LoginForm, RegisterForm


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


@app.route('/news')
def news():
    return render_template("news.html", title="News")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash("You have successfully logged in", 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password', 'danger')

    return render_template('login.html', form=form, title="Account login")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        flash(f'Your account was successfully created for {form.username.data}', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)