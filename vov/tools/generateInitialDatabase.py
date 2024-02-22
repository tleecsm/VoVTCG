#!/usr/bin/python

import sqlite3
import shutil
import os

def initialize_database():
    # Backup the database then delete it 
    if os.path.exists("vov/database/vov.db"):
        shutil.copyfile("vov/database/vov.db", "vov/database/vov.backup.db")
        os.remove("vov/database/vov.db")

    # Apply the schema
    connection = sqlite3.connect("vov/database/vov.db")
    cursor = connection.cursor()
    with open("vov/database/schema.sql") as f:
        cursor.executescript(f.read())

    connection.commit()
    connection.close()

initialize_database()