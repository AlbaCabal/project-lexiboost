from app.extensions import db
from app.models import User

def get_user_level(user_id):
    user = db.session.execute(db.select(User).filter_by(id=user_id)).scalars().first()
    return user.level if user else 0

def save_user(username, hashed_password):
    user = User(username=username, password_hash=hashed_password, level=0)
    db.session.add(user)
    db.session.commit()
    return user

def get_user(username):
    return db.session.execute(db.select(User).filter_by(username=username)).scalars().first()


def get_user_id(id):
    return db.session.execute(db.select(User).filter_by(id=id)).scalars().first()
