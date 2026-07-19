from app.extensions import api, db
from app.models import Word


def replace_words(text, user_words):
    replace_test = text
    if text is not None:
        words = text.split()

        for originalWord in words:
            synonymous = api.words(ml=originalWord, max=5)

            for item in synonymous:
                syn = item.get("word")

                for z in user_words:
                    if syn == z.word:
                        replace_test = replace_test.replace(originalWord, syn)
                        break
    return  replace_test


def save_word(user, word_type, word, level):
    vocab = Word(id_user=user, category=word_type, word=word, level=level)
    db.session.add(vocab)
    db.session.commit()
    return word

def get_user_words_pag(user_id):
    return db.paginate(db.select(Word).filter_by(id_user=user_id))

def get_user_words(user_id):
    return db.session.execute(db.select(Word).filter_by(id_user=user_id)).scalars().all()

def delete_word(word_id, user_id):
    word = db.session.execute(db.select(Word).filter_by(id_vocab=word_id, id_user=user_id)).scalars().first()
    if word is None:
        return False
    db.session.delete(word)
    db.session.commit()
    return True