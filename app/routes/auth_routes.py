from flask import Blueprint, flash, redirect, render_template, request, session
from werkzeug.security import generate_password_hash
from app.models import User
from app.services.user_service import save_user, get_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
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
        if get_user(username):
            flash("Username already taken", "error")
            return render_template("register.html")

        hashed_password = generate_password_hash(password)
        # Insert new user into database
        save_user(username, hashed_password)

        flash("Registered successfully!", "success")
        return redirect("/")

    else:
        return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
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
        user = get_user(username)

        # Ensure username exists and password is correct
        if not user or not User.verify_password(user, password):
            flash("Invalid username and/or password", "error")
            return render_template("login.html")

        # Remember which user has logged in
        session["id"] = user.id

        flash("Logged in successfully!", "success")
        return redirect("/")
    else:
        return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    """Log user out"""
    session.clear()
    flash("Logged out successfully!", "success")
    return redirect("/")