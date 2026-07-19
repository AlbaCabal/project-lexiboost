# tests/test_user_service.py
from app.services.user_service import save_user, get_user, get_user_level
from werkzeug.security import generate_password_hash

def test_save_and_get_user(app, db):
    save_user("test", generate_password_hash("clave123"))

    user = get_user("test")

    assert user is not None
    assert user.username == "test"

def test_get_user_level_usuario_existente(app, db):
    save_user("test", generate_password_hash("clave123"))
    user = get_user("test")

    nivel = get_user_level(user.id)

    assert nivel == 0

def test_get_user_level_usuario_inexistente(app, db):
    # id_user 999 no existe en la BD
    nivel = get_user_level(999)
    assert nivel == 0