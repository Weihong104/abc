# -*- coding: utf-8 -*-
"""
1.建立2個串列,我方,敵方,可放入3個角色
2.三人互打或三人打一人，用POP移除死亡角色
3.戰鬥三回合後，統計血量比較多的贏
4.做出閃避
"""

from GM import Advister,Dancer,Saber

import random

def changeRole(me,you):

    me.fight()
    blood=random.randint(0, 10)#閃避
    youblood=you.getHp()-blood
    you.setHp(youblood)
    print('{}損失{}血量,目前血量:{}'.format(you.getName(),blood,youblood))

if __name__=='__main__':
    
    advister=Advister('孔明',100,400)
    
    dancer=Dancer('大喬',150,300)
    
    saber=Saber('亞瑟',150,100)

    while (dancer.getHp()>0 and saber.getHp()>0):
        num=random.randint(1, 50)
        if num%2==0:
            changeRole(dancer,saber)
        else:
            changeRole(saber, dancer)

    if dancer.getHp()<=0:
        print(saber.getName(),'win')
    else:
        print(dancer.getName(),'win')
        