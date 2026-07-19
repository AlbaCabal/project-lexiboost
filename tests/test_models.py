# tests/test_models.py
from app.models import User
from werkzeug.security import generate_password_hash

def test_crear_usuario(app, db):
    user = User(username="alba", password_hash=generate_password_hash("miclave123"))
    db.session.add(user)
    db.session.commit()

    assert user.id is not None
    assert user.level == 0  # el default que pusiste en el modelo


def test_verify_password_correcta(app, db):
    user = User(username="test1", password_hash=generate_password_hash("miclave123"))
    db.session.add(user)
    db.session.commit()

    assert user.verify_password("miclave123") is True
    assert user.verify_password("clave_incorrecta") is False