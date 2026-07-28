# TASK 4.3 ------
import sqlite3
from flask import Flask, render_template

connection = sqlite3.connect("school.db")
connection.execute("""CREATE TABLE IF NOT EXISTS People(
                   PersonIDINTEGER PRIMARY KEY AUTOINCREMENT,
                   FullName TEXT NOT NULL,
                   DateOfBirth TEXT NOT NULL,
                   ScreenName TEXT,
                   isAdult INTEGER")
                   """)
connection.commit()

with open("people.txt","r") as file:
    for line in file:
        line = line.strip().split(",")
        fullname, dob, identity = line[0], line[1], line[2]
        connection.execute("INSERT INTO People (PersonID, FullName, DateOfBirth, ScreenName, IsAdult) VALUES(?,?,?,?,?)", (fullname, dob, 'abc', identity))
    connection.commit()
    # file auto close
recs = connection.execute("SELECT * FROM People")

connection.close()

def read_people():
    file = open("people.txt", "r")
    connection = sqlite3.connect("school.db")
    cursor = connection.cursor()
    recs = cursor.execute("SELECT FullName, ScreenName FROM PEOPLE")

    people = []

    for rec in recs:
        name, screenName = rec[0], rec[1]
        people.append([name, screenName])

    person = 0  # 

    for line in file:
        identity = rec.strip().split(",")[2]
        people[person].append(identity)
        person += 1

    file.close()
    return people

app = Flask(__name__)
@app.route("/") # decorator (landing page)

def index():
    return render_template("people.html", people=read_people())

# main program
app.run() 

