#!/usr/bin/python3

###下面是while循环
init_num=1
while init_num<5:
    print("当前循环次数:"+str(init_num))
    init_num+=1


objList =['啊1','啊2','啊3','啊4']

#while也可以循环遍历list,但是记得要移出已经使用的或者删除遍历条件的元素,否则无限循环
while objList:
   mmstr = objList.pop();
   print("Verifying user: " + mmstr.title())



##使用continue
num=1
while num<10:
    num+=1
    if num%2 ==0:
        print("发现整数:"+str(num))
    else:
        continue
msg=''
while msg !='quit':
    msg = input("请输入指令,quit退出循环,输入0退出后面的程序:\n")
    if msg=='0':
        exit(0)




############
#while参数为boolean值,可以用flag控制条件,或者特定条件触发直接break跳出当前循环
flag=True
while flag:
    str=input("请输入指令,0为退出:\n")
    if str!='0':
        flag=True
    else:
        ###flag=False
        break