import pymysql
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="project"
)
mycursor = mydb.cursor()

mycursor.execute("USE project")
#mycursor.execute("create table sample(Student_id int,Name varchar(40),Course varchar(40),Ph_no int)")
# i=int(input("Enter a ID"))
# n=input("Enter a Name")
# c=input("Enter a Course")
# p=int(input("Enter a Phone number"))
# mycursor.execute("insert into sample(Student_id,Name,Course,Ph_no) values('%s','%s','%s','%s')"%(i,n,c,p))
# try:
#     mycursor.execute("delete from sample where id=1")
#     mydb.commit()
# except (Exception e):
#     mydb.rollback()
# mydb.close()
