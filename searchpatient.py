import mysql.connector
import tabulate

mydb= mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="opd"
)

mycursor = mydb.cursor()
def search():
    q = input("Enter Patient ID/Name/Contact: ")
    cmd = "select * from patients where patient_id= %s or name=%s or contact=%s"
    values= (q,q,q)


    mycursor.execute(cmd, values)


    data = mycursor.fetchall() 
    print(tabulate.tabulate(data))
