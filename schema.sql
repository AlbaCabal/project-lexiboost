CREATE database lexiboost;

use lexiboost;

CREATE TABLE users (
    id INTEGER PRIMARY KEY auto_increment,
    username varchar(50) NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    level INTEGER DEFAULT 1
);

CREATE TABLE vocabulary (
    id_vocab INTEGER PRIMARY KEY auto_increment,
    id_user INTEGER NOT NULL,
    category varchar(50) NOT NULL,
    word varchar(50) NOT NULL,
    level INTEGER NOT NULL,
    FOREIGN KEY (id_user) REFERENCES users(id_user)
);

CREATE TABLE writing_history (
    id_history INTEGER PRIMARY KEY auto_increment,
    id_user INTEGER NOT NULL,
    title varchar(50) NOT NULL,
    original_text varchar(500) NOT NULL,
    corrected_text varchar(500) NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    level_used INTEGER NOT NULL,
    FOREIGN KEY (id_user) REFERENCES users(id_user)
);

CREATE TABLE made_list_vocabulary (
    id_list INTEGER PRIMARY KEY auto_increment,
    level INTEGER NOT NULL,
    category varchar(50) NOT NULL,
    word varchar(50) NOT NULL,
    meaning varchar(100) NOT NULL,
    example varchar(100) NOT NULL
);