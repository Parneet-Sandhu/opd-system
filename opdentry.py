import mysql.connector
import datetime

mydb= mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="opd"
)

mycursor = mydb.cursor()
def opdentry(pid):
    x = datetime.datetime.now()


    date = x.strftime("%d")+"/"+x.strftime("%m")+"/"+x.strftime("%Y")
    
    time=x.strftime("%X")
    sym=input("Enter Symptoms:")
    pres=input("Enter Prescription:")
    ch=input("Enter Charges:")

    query="insert into patient_history (visit_date,visit_time,patient_id,symptoms,prescription,charges) values(%s,%s,%s,%s,%s,%s)"
    values=(date,time,pid,sym,pres,ch)

    mycursor.execute(query,values)
    mydb.commit()
    print("Entry Saved")

    
    
    
