import time
from random import randint 
while True:
    c1 = 0
    c2 = 0
    for i in range(1,4):
        time.sleep(2)
        print(' \n——————现在是第'+str(i)+'局——————')

        a1 = randint(100,150)  #!血量
        b1 = randint(30,50)    #!攻击
        a2 = randint(100,150)  #!血量
        b2 = randint(30,50)    #!攻击

        #! 生成随机属性
        #? print('【玩家】\n血量：{}\n攻击：{}'.format(a1,b1))
        #? print('血量：%s 攻击：%s' % (a1,b1))另一种更方便的写法
        #? %s字符串   %f浮点数   %d整数
        print('【玩家】\n'+'血量：'+str(a1)+'\n攻击:'+str(b1))
        print('------------------------')  
        time.sleep(2)
        #暂停2秒，再继续运行后面的代码
        print('【敌人】\n'+'血量：'+str(a2)+'\n攻击:'+str(b2))  
        print('------------------------')
        time.sleep(2)

        while (a1 >0) and (a2 >0):
            a2 = a2 - b1
            print('你发起了攻击，【敌人】剩余血量'+str(a2)) 
            a1 = a1 - b2
            print('你发起了攻击，【玩家】剩余血量'+str(a1))  
            print('------------------------')
            time.sleep(1.5)


        if a1 > 0 and a2<= 0:
            c1 +=1
            print('玩家赢得一局')
        elif a2 > 0 and a1<= 0:
            c2 +=1
            print('敌方赢得一局')
        else:
            print('打平了')

    if c1 > c2:
        print('玩家获胜')
    elif c1 < c2:
        print('敌方获胜')

    again = input("输入n退出游戏，输入其他再来一局:")
    if again == 'n':
        break

    