import mysql.connector
db=mysql.connector.connect(
    host="localhost",user="root",password='Password"123',auth_plugin='mysql_native_password',database='sys'
)
cursor=db.cursor()
sql="select * from employee1"
cursor.execute(sql)
data=cursor.fetchone()
db.close()
print(data)
