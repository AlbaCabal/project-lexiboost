import sqlite3
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = sqlite3.connect("lexiboost.db", check_same_thread=False)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Validate submission
        if not username:
            flash("Must provide username", "error")
            return render_template("register.html")
        if not password:
            flash("Must provide password", "error")
            return render_template("register.html")
        if password != confirmation:
            flash("Passwords do not match", "error")
            return render_template("register.html")

        # Check if username already exists
        cur = db.cursor()
        cur.execute("SELECT * FROM users WHERE username = ?", (username,))
        if cur.fetchone():
            flash("Username already taken", "error")
            return render_template("register.html")

        # Insert new user into database
        hashed_password = generate_password_hash(password)
        cur.execute("INSERT INTO users (username, hash_password) VALUES (?, ?)", (username, hashed_password))
        db.commit()

        flash("Registered successfully!", "success")
        return redirect("/")

    else:
        return render_template("register.html")
    
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Validate submission
        if not username:
            flash("Must provide username", "error")
            return render_template("login.html")
        if not password:
            flash("Must provide password", "error")
            return render_template("login.html")

        # Query database for username
        cur = db.cursor()
        cur.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cur.fetchone()

        # Ensure username exists and password is correct
        if not user or not check_password_hash(user[2], password):
            flash("Invalid username and/or password", "error")
            return render_template("login.html")

        # Remember which user has logged in
        session["user_id"] = user[0]

        flash("Logged in successfully!", "success")
        return redirect("/")

    else:
        return render_template("login.html")
    

@app.route("/logout")
def logout():
    """Log user out"""
    session.clear()
    flash("Logged out successfully!", "success")
    return redirect("/")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

@app.route("/")
def index():
    """View writing history"""
    if "user_id" not in session:
        flash("You must be logged in to view this page", "error")
        return redirect("/login")

    # TO DO: Retrieve and display user's writing history
    writing_history = db.execute("SELECT * FROM writing_history WHERE id_user = ?", (session["user_id"],)).fetchall()
    return render_template("index.html", docs=writing_history)

@app.route("/vocabulary", methods=["GET", "POST"])
def vocabulary():
    """Manage vocabulary"""
    if "user_id" not in session:
        flash("You must be logged in to view this page", "error")
        return redirect("/login")

    if request.method == "POST":
        # TO DO: Add vocabulary word for user
        pass
    else:
        # TO DO: Display user's vocabulary words
        pass

    return render_template("vocabulary.html")

@app.route("/write", methods=["GET", "POST"])
def write():
    """Writing practice"""
    if "user_id" not in session:
        flash("You must be logged in to view this page", "error")
        return redirect("/login")

    if request.method == "POST":
        # TO DO: Handle writing submission
        pass
    else:
        # TO DO: Display writing practice interface
        pass

    return render_template("write.html")


if __name__ == "__main__":
    app.run(debug=True)

app.secret_key = "Clase.España.2007"
