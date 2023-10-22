import mysql.connector

mydb= mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="opd"
)


def newentry():
    mycursor = mydb.cursor()
    n = input("Enter name: ")
    age = int(input("Enter age: "))
    g = input("Enter Gender: ")
    c = int(input("Enter Contact no.: "))
    f = input("Enter Father's name: ")
    a = input("Enter Address: ")

    query = "INSERT INTO patients (name,age,gender,contact,father_name,address) values(%s , %s, %s, %s, %s ,%s)"
    val= (n,age,g,c,f,a)

    mycursor.execute(query, val)
    mydb.commit()
    query="select * from patients order by patient_id desc limit 1"
    mycursor.execute(query)
    data=mycursor.fetchall()
    for x in data:
        pid=x[0]
    return pid
