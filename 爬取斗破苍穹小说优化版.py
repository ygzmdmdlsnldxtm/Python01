import re
import requests
list_all = []
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"}

html = requests.get("https://doupocangqiong1.com/1/").text
# print(html)
r = '[\s\S]*?'
pattern1 = re.compile(r'<li><a href="({})" target="_blank"{}>{}</a>{}'.format(r,r,r,r,r,r))
pattern2 = re.compile(r'<li><a href="{}" target="_blank"{}>({})</a>{}'.format(r,r,r,r,r,r))
url = pattern1.findall(html)

name = pattern2.findall(html)
URL = []
NAME = []
dict_list = []
for i in url:
    URL.append("https://doupocangqiong1.com{}".format(i))
# print(URL)
for j in name:
    NAME.append(j)
dict_list = list(map(lambda t:dict([t]),zip(URL,NAME)))
for dict in dict_list[2:-3]:
    print(dict)

