import mysql.connector
db=mysql.connector.connect(
    host="localhost",user="root",password='Password"123',auth_plugin='mysql_native_password',database='sys'
)
cursor=db.cursor()
sql="insert into employee1 values(1000,'anu',20000,'developer')"
cursor.execute(sql)
db.commit()
db.close()