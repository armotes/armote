#!/usr/bin/python3

#######字典:相当于对象,这里的数据结构就和JSON格式类似
people = {'age':25,'address':'武汉','sex':'男','conment':'男'}
print(people['address'])
print(people)

##给字段添加和修改属性(键值对)
people['work']="新鸿海";
people['age']=21;
print(people)

people1 = {
    'age':25,
    'address':'武汉',
    'sex':'男',
    }
if people1:
    print("有值")
else:
    print("空值")

#删除键值对(属性)
del people['work']
print(people)

#遍历输出字段(对象的属性和值).items()
for k,v in sorted(people.items()):
    print("k:"+k+",v:"+str(v))
#遍历键
for key in people.keys():
    print("key:"+key)

#遍历值
for value in people.values():
    print("value:"+str(value));

#set用法:类似于list,但是value储存不会有重复
for value in set(people.values()):
    print("value:"+str(value));