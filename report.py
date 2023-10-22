import mysql.connector
import tabulate

mydb= mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="opd"
)
mycursor = mydb.cursor()

def collection():
    startdate=input("Enter Start date: ")
    enddate=input("Enter End date: ")
    cmd='select * from patient_history where STR_TO_DATE(visit_date,"%d/%m/%Y")>=STR_TO_DATE(%s,"%d/%m/%Y")and STR_TO_DATE(visit_date,"%d/%m/%Y")<=STR_TO_DATE(%s,"%d/%m/%Y") '
    value=(startdate,enddate)
    mycursor.execute(cmd,value)
    data=mycursor.fetchall()
    
    print(tabulate.tabulate(data))
    total=0
    for x in data:
        total=total+float(x[6])
    print("Total=",total)    
