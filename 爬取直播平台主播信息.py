# coding=utf-8
import re
import requests
from prettytable import from_db_cursor
#requests获取HTML网页的代码
#模仿浏览器发出请求

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"}

url = requests.get("https://www.douyu.com/g_LOL",headers=headers).text
#print(url)
#<li class="layout-Cover-item"><div class="DyListCover HeaderCell is-href" subdata="[object Object]" delay="100" error="0"><a href="/606118" target="_blank" class="DyListCover-wrap"><div class="DyListCover-imgWrap"><div class="LazyLoad is-visible DyImg DyListCover-pic"><img src="https://rpic.douyucdn.cn/asrpic/190427/606118_1712.png/webpdy1" class="DyImg-content is-normal "></div><div class="DyListCover-superscript"><span class="HeaderCell-corner is-corner0"></span><span class="HeaderCell-corner is-corner1"></span><span class="HeaderCell-corner is-corner2"></span><span class="HeaderCell-corner is-corner3"><img src="https://sta-op.douyucdn.cn/dy-listicon/47b24dcfe308b9630f17e3c70faea1ba.png?x-oss-process=image/format,webp" data-id="306" data-score="502"></span></div></div><div class="DyListCover-content"><div class="DyListCover-info"><span class="DyListCover-zone">英雄联盟</span><h3 class="DyListCover-intro" title="大司马：正在处理点事情，十点半开播">大司马：正在处理点事情，十点半开播</h3></div><div class="DyListCover-info"><span class="DyListCover-hot"><svg class="DyListCover-hotIcon"><use xlink:href="#icon-hot_889d4a1"></use></svg>105万</span><h2 class="DyListCover-user"><svg class="DyListCover-userIcon"><use xlink:href="#icon-user_5c5ddf7"></use></svg>芜湖大司马丶</h2></div><span class="HeaderCell-label-wrap is-od"><i></i>LOL金牌讲师 </span></div></a><a href="/606118" target="_blank"></a></div></li>
#<h2 class="DyListCover-user"><svg class="DyListCover-userIcon"><use xlink:href="#icon-user_5c5ddf7"></use></svg>英雄联盟赛事</h2>
#<h2 class="DyListCover-user"><svg class="DyListCover-userIcon"><use xlink:href="#icon-user_5c5ddf7"></use></svg>芜湖大司马丶</h2>
r = '[\s\S]*?'
pattern1 = re.compile(r'<li class="layout-Cover-item">{}</svg>{}</span><h2 class="DyListCover-user is-template"><svg><use xlink:href="#icon-user_05fb112"></use></svg>({})</h2>'.format(r,r,r))
pattern2 = re.compile(r'<li class="layout-Cover-item">{}</svg>({})</span><h2 class="DyListCover-user is-template"><svg><use xlink:href="#icon-user_05fb112"></use></svg>{}</h2>'.format(r,r,r))
name = pattern1.findall(url)
# for i in name:
#     print(i)
follower = pattern2.findall(url)
#主播名字
name1 = tuple(name)
#主播热度
follower1 = tuple(follower)


# for j i follower:
#     print(j)
import pymysql as sql

#创建数据库链接
connc = sql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='******',
    db='mysql',
    charset='utf8'
)
#获取游标

cursor = connc.cursor()
cursor.execute("use text1;")
cursor.fetchall()
# cursor.execute('''
# CREATE TABLE Anchor
# (
#
# uname varchar (20) primary key not null ,
# follow varchar (20) NOT null
# )
# ''')
# cursor.fetchall()
# print(name1)
# print(follower1)

for (i1, i2) in zip(name1,follower1):
    #print(i1,i2)
    cursor.execute('''insert into anchor(uname,follow) VALUES ("{}","{}");'''.format(i1,i2))

# print(cursor.execute('''insert into Anchor(uname,follow) VALUES ("{}","{}");'''.format(name1,follower1)))
connc.commit()#插入数据必要的一步！
cursor.fetchall()
print(cursor.execute("select uname,follow from anchor;"))
print(from_db_cursor(cursor))#按照数据库形式输出 界面更美观