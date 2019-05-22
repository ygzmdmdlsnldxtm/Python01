'''过程分析及思路'''
'''
>1先排序，将已知的人员过桥时间用列表保存在升序排列
>2第一次都是最快和次快的出发
>3到达对岸后再由速度最快的返回
>4之后就是列表中最慢的两个过
>5再从已经过桥的列表中找出最快的人返回
>6如果是奇数的话就是最后一波是最快的那个人自己过

'''
import random
def random_list(n):
    index = int(random.random()*10)%len(n)
    return n.pop(index)

a = [1,2,5,8,10]
min_time = 100
min_str=""
for count in range(0,10000):
    a1 = a[:]
    b = []
    #go
    i = random_list(a1)
    j = random_list(a1)
    b.append(i)
    b.append(j)
    # back
    k = random_list(b)
    a1.append(k)
    #go
    l = random_list(a1)
    m = random_list(a1)
    b.append(l)
    b.append(m)
    #back
    q = random_list(b)
    a1.append(q)
    #go
    o = random_list(a1)
    p = random_list(a1)
    b.append(o)
    b.append(p)
    #back
    w = random_list(b)
    a1.append(w)
    #go
    f = random_list(a1)
    h = random_list(a1)
    b.append(f)
    b.append(h)

    time = max(i,j)+k+max(l,m)+q+max(o,p)+w+max(f,h)
    time_str = [' go ',str(i),' ',str(j),' back ',str(k),' go ',str(l),' ',str(m),' back ',str(q),' go ',str(o),' ',str(p),' back ',str(w),' go ',str(f),' ',str(h)]
    if min_time>time:
        min_time = time
        min_str = time_str

print('time :',str(min_time),end='|')
print(''.join(min_str))



