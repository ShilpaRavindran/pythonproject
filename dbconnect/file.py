import mysql.connector
db=mysql.connector.connect(
    host="localhost",user="root",password='Password"123',auth_plugin='mysql_native_password',database='sys'
)
cursor=db.cursor()
f=open("emp","r")
for lines in f:
    data=lines.rstrip("\n").split(",")
    sql="insert into employee1 values(%s,%s,%s,%s)"
    cursor.execute(sql,data)
    db.commit()
