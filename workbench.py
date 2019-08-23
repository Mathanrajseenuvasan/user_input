import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "testdb"
)

cursor = db.cursor()

def user():
    name = raw_input("Enter name : ")
    age = raw_input("Enter age : ")
    cursor.execute("INSERT INTO students(name, age) VALUES (%s, %s)" , (name,age))

def delete():
    
    cursor.execute("DELETE FROM students WHERE name = 'muthu'")



delete()
db.commit()
