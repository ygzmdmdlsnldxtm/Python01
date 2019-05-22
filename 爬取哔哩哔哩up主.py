import requests
user_mid = '28496477'
url = requests.get("https://api.bilibili.com/x/relation/stat?vmid={}".format(user_mid)).json()

r = url
following = r['data']['following']
follower = r['data']['follower']

import pymysql as sql

#创建数据库链接
connc = sql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='wbsyx1024',
    db='mysql',
    charset='utf8'
)
#获取游标

cursor = connc.cursor()
cursor.execute("use text;")
cursor.fetchall()
# cursor.execute('''
# CREATE TABLE Anchor
# (
#
# uname int (20) primary key not null ,
# follow int (20) NOT null
# )
# ''')
# cursor.fetchall()

print(cursor.execute("select Sname,Ssex from student;"))
print(cursor.fetchall())