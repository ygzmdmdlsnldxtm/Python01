import pymysql as sql

#创建数据库链接
connc = sql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='*******',
    db='mysql',
    charset='utf8'
)
#获取游标

cursor = connc.cursor()
cursor.execute("use text1;")
cursor.fetchall()
cursor.execute('''
CREATE TABLE userhost
(

name CHAR (20) PRIMARY KEY,
follow CHAR(20)

)
''')
cursor.fetchall()
print(cursor.execute("show tables;"))
print(cursor.fetchall())
