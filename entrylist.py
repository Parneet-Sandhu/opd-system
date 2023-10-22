import mysql.connector
from tabulate import tabulate

mydb= mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="opd"
)


def newlist():
    mycursor = mydb.cursor()
    cmd = "select * from patients"
    mycursor.execute(cmd)
    data = mycursor.fetchall()
    rows=[]
    heading=("Patient ID", "Name","Age","Gender","Contact","Father Name","Address")
      
    rows.append(heading) 
        
        
    for x in data:
        rows.append(x)
    print(tabulate(rows))    

 
