#!/usr/bin/python3
###################
#if的使用方法
ArrauList = [val+1 for val in range(0,5)]
print(ArrauList)

for val in ArrauList:
    if val ==1:
        print("当前数值为1")
    elif val ==2:
        print("当前数值为2")
    else:
        print("啦啦啦")

newList = range(10,100)

for val in newList:
    if val ==98:
        print("当前数值为98")
    elif val ==99:
        print("当前数值为99")
    elif val==10 or val==12:
        print("val为10或者12")


name = "Audi";
print(name.upper())
print(name.lower())

##对列表数据进行判定:不需要像java需要循环 直接用in

if 99 in newList:
    print("有99")

strList = [str(val)+"个" for val in range(0,11)]
strText = "1个";
if strText in strList:
    print("找到"+strText)

if "666个" not in strList:
    print("没有666个")


######判断是否为空 if object
aList = []
if aList:
    print("有值")
else:
    print("空值")