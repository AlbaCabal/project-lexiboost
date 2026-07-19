# tests/test_vocabulary_service.py
from app.services.vocabulary_service import replace_words

class FakeWord:
    def __init__(self, word):
        self.word = word

def test_replace_words_encuentra_sinonimo(mocker):
    mocker.patch(
        "app.services.vocabulary_service.api.words",
        return_value=[{"word": "quick"}, {"word": "rapid"}]
    )

    user_words = [FakeWord("quick")]
    resultado = replace_words("the fast fox", user_words)

    assert "quick" in resultado

def test_delete_word_existente(app, db):
    from app.services.vocabulary_service import save_word, delete_word, get_user_words

    save_word(user=1, word_type="noun", word="ephemeral", level=1)
    palabra = get_user_words(1)[0]

    resultado = delete_word(palabra.id_vocab, user_id=1)

    assert resultado is True
    assert get_user_words(1) == []

def test_delete_word_de_otro_usuario_falla(app, db):
    from app.services.vocabulary_service import save_word, delete_word, get_user_words

    save_word(user=1, word_type="noun", word="ephemeral", level=1)
    palabra = get_user_words(1)[0]

    resultado = delete_word(palabra.id_vocab, user_id=2)  # otro usuario intenta borrarla

    assert resultado is False
    assert len(get_user_words(1)) == 1  # sigue existiendo