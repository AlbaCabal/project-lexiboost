CREATE TABLE users (
    id_user INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    hash_password TEXT NOT NULL,
    level INTEGER DEFAULT 1
);

CREATE TABLE vocabulary (
    id_vocab INTEGER PRIMARY KEY AUTOINCREMENT,
    id_user INTEGER NOT NULL,
    type TEXT NOT NULL,
    word TEXT NOT NULL,
    level INTEGER NOT NULL,
    FOREIGN KEY (id_user) REFERENCES users(id_user)
);

CREATE TABLE writing_history (
    id_history INTEGER PRIMARY KEY AUTOINCREMENT,
    id_user INTEGER NOT NULL,
    title TEXT NOT NULL,
    original_text TEXT NOT NULL,
    corrected_text TEXT NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    level_used INTEGER NOT NULL,
    FOREIGN KEY (id_user) REFERENCES users(id_user)
);

CREATE TABLE made_list_vocabulary (
    id_list INTEGER PRIMARY KEY AUTOINCREMENT,
    level INTEGER NOT NULL,
    type TEXT NOT NULL,
    word TEXT NOT NULL,
    meaning TEXT NOT NULL,
    example TEXT NOT NULL
);