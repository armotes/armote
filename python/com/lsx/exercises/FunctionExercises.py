#####################
#这里就将方法了!
#######################



#def关键字定义一个方法,而非直接使用
def getIinfo(name,add):
    print("你好呀!"+name+","+add+"的勇士!")

##这个就是普通的参数
getIinfo("赛利亚","武汉")


#这个就是关键字实参:直接将参数名称写进去,然后赋值进行调用
getIinfo(add="武汉",name="赛利亚")


#默认值参数,以及带返回值的方法
def getDo(name,add='武汉'):
    print("你的name="+name+"你的地址="+add)
    result = name.title()+"-"+add.title()
    return result

str=getDo("哎哟")
print(str)
str1=getDo("哎哟","新路")
print(str1)


def greet_users(names):

    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#function_name(list_name[:])

#切片表示法[:]
#创建列表的副本。在print_models.py中，如果不想清空未打印的设计列表，
#可像下面这样调用print_models()：

#print_models(unprinted_designs[:], completed_models)

#多个实参

def doFood(*foods):
    for food in foods:
        print("你喜欢的食物有:"+food)

doFood("大鱼","小鱼啊","好吃的")

###综合使用:解析多个参数和字典：**otherInfo将创建一个空字典，容纳后面多个键值对参数
def doSomething(name, add, **otherInfo):
    info = {}
    info['name']=name
    info['add']=add
    for key,val in otherInfo.items():
        info[key]=val
    #print("解析后info:"+info)
    return info
#可以解析字典中多个键值对参数
infoStr = doSomething('小丫','武汉',local='幸福村',age='25')
print(infoStr)


def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

####调用其他文件的方法
import Method
Method.getInfo("66")

from Method import getInfo
Method.getInfo("调用指定方法")

#调用所有方法,可以不用写模块名:这种就怕方法名冲突了,建议模块名.方法
#from MethodList import *
#getInfo("李大爷")
####推荐这种：这种类似于java
import MethodList as mm
mm.getInfo("大爷")
