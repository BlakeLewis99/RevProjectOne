import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password!",
    database="note_schema"
)

mydb.cursor().close()
