import mysql.connector
from tabulate import tabulate

mydb= mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="opd"
)


def historylist():
    mycursor = mydb.cursor()
    pid=input("Enter Patient ID:")
    cmd = "select * from patient_history where patient_id=%s"
    values=(pid,)
    mycursor.execute(cmd,values)
    data = mycursor.fetchall()
    rows=[]
    heading=("S.No","Visit Date","Visit Time","Patient ID","Symptoms","Prescription","Charges")
      
    rows.append(heading) 
        
        
    for x in data:
        rows.append(x)
    print(tabulate(rows))    
