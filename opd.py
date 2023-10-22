import mysql.connector
import pwinput
from tabulate import tabulate
import entry
import entrylist
import searchpatient
import opdentry
import historylist
import report


mydb= mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="opd"
)

mycursor = mydb.cursor()

user = input("Enter Userame: ")

pas=pwinput.pwinput()

cmd ="SELECT admin_id FROM admin_login WHERE username=%s AND password=%s"
values = (user, pas)
mycursor.execute(cmd, values)

data = mycursor.fetchall()

if len(data) > 0:

        y='y'

        while y=='y' or y=='Y':
            print("ENter 1 to New Patient: ")
            print("Enter 2 to Patient List: ")
            print("Enter 3 to old Patient: ")
            print("Enter 4 to Patient History:")
            print("Enter 5 to Search Patient: ")
            print("Enter 6 to Financial Report: ")
            op = int( input())

            if op==1:
                pid=entry.newentry()
                opdentry.opdentry(pid)
            elif op==2:
                    entrylist.newlist()
            elif op==3:
                    pid=input("Enter Patient ID:")
                    opdentry.opdentry(pid)
            elif op==4:
                    historylist.historylist()
                    
            elif op==5:
                    searchpatient.search()
            elif op==6:
                    report.collection()

            y = input("Y to continue/ N to Exit")
        

else:
    print("Incorrect username or password")



        



