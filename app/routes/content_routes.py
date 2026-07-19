from flask import Blueprint, flash, redirect, render_template, request, session

from app.services.vocabulary_service import replace_words, get_user_words, get_user_words_pag, save_word, delete_word
from app.services.user_service import get_user_level, get_user_id
from app.services.history_service import save_writing, get_history

content_bp = Blueprint("content", __name__)

@content_bp.route("/")
def index():
    """View writing history"""
    if "id" not in session:
        flash("You must be logged in to view this page", "error")
        return redirect("/login")

    # Retrieve and display user's writing history
    writing_history = get_history(session["id"])
    return render_template("/users/index.html", texts=writing_history)

@content_bp.route("/vocabulary", methods=["GET", "POST"])
def vocabulary():
    """Manage vocabulary"""
    if "id" not in session:
        flash("You must be logged in to view this page", "error")
        return redirect("/login")

    if request.method == "POST":
        # Add vocabulary word for user
        word = request.form.get("word")
        word_type = request.form.get("category")
        level = get_user_level(session["id"])
        save_word(session["id"], word_type, word, level)

        flash("Word saved!", "success")
        return redirect("vocabulary")
    else:
        # Display user's vocabulary words
        dictionary = get_user_words_pag(session["id"])
        user = get_user_id(session["id"])

        return render_template("users/vocabulary.html", words=dictionary, user=user)

@content_bp.route("/write", methods=["GET", "POST"])
def write():
    if "id" not in session:
        flash("You must be logged in to view this page", "error")
        return redirect("/login")

    if request.method == "POST":
        # Handle writing submission
        title = request.form.get("title", "")
        given_text = request.form.get("givenText", "")
        dic_words = get_user_words(session["id"])

        replace_test = replace_words(given_text, dic_words)
        level = get_user_level(session["id"])
        save_writing(session["id"], title, given_text, replace_test, level)

        return render_template("users/write.html", text=given_text, newText=replace_test)
    else:
        # Display writing practice interface
        return render_template("users/write.html")

@content_bp.route("/word/<int:word_id>/delete", methods=["POST"])
def delete_word_route(word_id):
    delete_word(word_id, session["id"])
    return redirect("/vocabulary")