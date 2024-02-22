#!/usr/bin/python

import sqlite3
import shutil
import os

def populate_database():
    connection = sqlite3.connect("vov/database/vov.db")
    cursor = connection.cursor()
    with open("vov/database/cards.sql") as f:
        cursor.executescript(f.read())

    cursor.execute("SELECT * FROM Cards")
    print(cursor.fetchall())
    connection.commit()
    connection.close()

populate_database()