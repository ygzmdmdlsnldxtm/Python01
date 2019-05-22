'''测试封装特性'''
'''
使用对象引用做为另一个对象的实例属性
'''
class Gun(object):
    def __init__(self,model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self,count):
        self.bullet_count = count

    def gun_shoot(self):
        self.bullet_count -= 1
        print("{0}突突突......[子弹剩余]{1}".format(self.model,self.bullet_count))

class Soldier(object):
    def __init__(self,name):
        self.name = name
        self.gun = None#并不是所有的新兵都有枪
    def fire(self):
        #先判断是否有枪，没有枪没法冲锋
        if self.gun is None:
            print("士兵{}没有枪，没办法冲锋陷阵......".format(self.name))
            return
        print("冲鸭！！！！！士兵{}".format(self.name))
        #给自己的枪装上子弹
        self.gun.add_bullet(50)
        #射击
        self.gun.gun_shoot()

gun = Gun("AK47")
soldier = Soldier("大兵")
soldier.gun = gun#因为士兵并不是都有枪默认是None，所以为士兵添加一把枪的属性
soldier.fire()

