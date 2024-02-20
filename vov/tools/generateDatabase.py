import sqlite3
import shutil
import os

def initialize_database():
    # Backup the database then delete it 
    if os.path.exists("../database/database.db"):
        shutil.copyfile("../database/database.db", "../database/database.backup.db")
        os.remove("../database/database.db")

    connection = sqlite3.connect("../database/database.db")
    cursor = connection.cursor()
    with open("schema.sql") as f:
        cursor.executescript(f.read())
        
    cursor.execute("SELECT * FROM Cards")
    print(cursor.fetchall())
    connection.commit()
    connection.close()

initialize_database()