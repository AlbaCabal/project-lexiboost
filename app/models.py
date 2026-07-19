from app.extensions import db
from werkzeug.security import check_password_hash

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    level = db.Column(db.Integer, default=0)

    @property
    def password(self):
        """Prevent accessing the password attribute directly."""
        raise AttributeError("Password is not a readable attribute.")

    def verify_password(self, password):
        """Check if the provided password matches the stored hash."""
        return check_password_hash(self.password_hash, password)


class Word(db.Model):
    __tablename__ = "vocabulary"

    id_vocab = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    word = db.Column(db.String(50), nullable=False)
    level = db.Column(db.Integer, default=0)



class History(db.Model):
    __tablename__ = "writing_history"

    id_history = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    original_text = db.Column(db.String(500), nullable=False)
    corrected_text = db.Column(db.String(500), nullable=False)
    date = db.Column(db.Date)
    level_used = db.Column(db.Integer, nullable=False)



class SearchedWord(db.Model):
    __tablename__ = "made_list_vocabulary"

    id_list = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer, default=0)
    category = db.Column(db.String(50), nullable=False)
    word = db.Column(db.String(50), nullable=False)
    meaning = db.Column(db.String(100), nullable=False)
    example = db.Column(db.String(100), nullable=False)


