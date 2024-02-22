CREATE TABLE Users(
  username TEXT NOT NULL PRIMARY KEY
);

CREATE TABLE Cards(
    id TEXT NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    rank INTEGER NULL,
    type TEXT NOT NULL,
    class TEXT NULL,
    attribute TEXT NULL,
    cost TEXT NULL,
    power INTEGER NULL,
    life INTEGER NULL,
    hand INTEGER NULL,
    text TEXT NULL
);

CREATE TABLE Decks(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NULL,
    user TEXT NOT NULL,
    favorite TEXT NULL,
    FOREIGN KEY (favorite) REFERENCES Cards(id),
    FOREIGN KEY (user) REFERENCES Users(username)
);

CREATE TABLE DeckCards(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    card TEXT NOT NULL,
    deck INTEGER NOT NULL,
    FOREIGN KEY (card) REFERENCES Cards(id),
    FOREIGN KEY (deck) REFERENCES Decks(id)
);

CREATE TABLE Keywords(
    name TEXT NOT NULL PRIMARY KEY,
    template TEXT NOT NULL,
    replacement TEXT NOT NULL
);