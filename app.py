from flask import Flask, redirect, render_template, url_for, session
from forms import LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "abanakakabasanapalaako"

# This tells Flask what to show when you visit the main web address
@app.route('/home2', methods=["GET", "POST"])
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for('login'))
    return render_template('dashboard.html', logged_in = True)

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "admin" and form.password.data == "admin":
            return redirect(url_for("dashboard"))
    return render_template('login.html', title="Login", form=form)

# This starts the local web server when you run this file
if __name__ == '__main__':
    app.run(debug=True)
