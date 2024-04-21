CREATE TABLE USERS (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    country VARCHAR(100),
    id_console INTEGER
);

CREATE TABLE IF NOT EXISTS VIDEOGAMES (
    id_console SERIAL PRIMARY KEY,
    name VARCHAR(100),
    id_company INTEGER,
    release_date DATE
);

CREATE TABLE IF NOT EXISTS GAMES (
    id_game SERIAL PRIMARY KEY,
    title VARCHAR(100),
    genre VARCHAR(100),
    release_date DATE,
    id_console INTEGER
);

CREATE TABLE IF NOT EXISTS COMPANY (
    id_company SERIAL PRIMARY KEY,
    name VARCHAR(100),
    country VARCHAR(100)
);