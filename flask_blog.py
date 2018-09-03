from flask import Flask, render_template, url_for, flash, redirect
from form import RegistartionForm, LoginForm

app=Flask(__name__)
app.config['SECRET_KEY'] = '20403a5dcd158371caaf6c893d796ba7'

posts = [
    {
        'author': "Vidya",
        'title': "My first post",
        'content': "Contents of my first post",
        'date_of_posting': "3/9/2018"
    },
    {
        'author': "Shree",
        'title': " Post by shree",
        'content': "Contents of my post",
        'date_of_posting': "2/9/2018"
    }
]
@app.route("/")
@app.route("/home")
def home() :
    return render_template('home.html', title="Home page")

@app.route("/about")
def about() :
    return render_template('about.html', posts=posts)

@app.route("/register", methods=['GET','POST'])
def register() :
    form = RegistartionForm()
    if form.validate_on_submit():
        flash('Account is created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="register", form=form)


@app.route("/login")
def login() :
    form = LoginForm()
    return render_template('login.html', title="login", form=form)


if __name__ == "__main__" :
    app.run(debug=True)

