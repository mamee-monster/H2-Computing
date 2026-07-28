import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

# PersonID Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS People(
    PersonID INTEGER PRIMARY KEY AUTOINCREMENT,
    FullName TEXT,
    DateOfBirth TEXT,
    ScreenName TEXT,
    IsAdult INTEGER)
    """)

