CREATE TABLE Users(
  username TEXT NOT NULL PRIMARY KEY
);

CREATE TABLE Cards(
    id TEXT NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    rank INT NULL,
    type TEXT NOT NULL,
    class TEXT NULL,
    attribute TEXT NULL,
    cost INT NULL,
    power INT NULL,
    life INT NULL,
    hand INT NULL,
    text TEXT NULL
);

CREATE TABLE Decks(
    id INT NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NULL,
    user TEXT NOT NULL,
    favorite TEXT NULL,
    FOREIGN KEY (favorite) REFERENCES Cards(id),
    FOREIGN KEY (user) REFERENCES Cards(username)
);

CREATE TABLE DeckCards(
    id INT NOT NULL PRIMARY KEY,
    card TEXT NOT NULL,
    deck INT NOT NULL,
    FOREIGN KEY (card) REFERENCES Cards(id),
    FOREIGN KEY (deck) REFERENCES Decks(id)
);

CREATE TABLE Keywords(
    name TEXT NOT NULL PRIMARY KEY,
    template TEXT NOT NULL,
    replacement TEXT NOT NULL
);