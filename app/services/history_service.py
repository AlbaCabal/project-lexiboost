from app.extensions import db
from app.models import History
import datetime

def save_writing(user_id, title, original_text, corrected_text, level):
    writing = History(
        id_user=user_id, title=title,
        original_text=original_text, corrected_text=corrected_text,
        date=datetime.date.today(), level_used=level
    )
    db.session.add(writing)
    db.session.commit()
    return writing

def get_history(id_user):
    return db.session.execute(db.select(History).filter_by(id_user=id_user)).scalars().all()