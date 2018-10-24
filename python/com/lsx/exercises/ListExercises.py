#!/usr/bin/python3
#创建一个list : list(agr)
numList = list(range(0,10,2));

#或者newList=[];


#for value in numList:
#    print("数字:"+str(value));

#print(numList);
#print(min(numList))
#print(max(numList))
#print(sum(numList))


nl = [value*2 for value in range(1,11)]
print(nl);

#value**2 代表当前数值的乘方运算
#使用另外一种方式创建列表:需要[] 同时第一个参数需要指定一个表达式 后面跟值
#相当于在循环1-10，然后每个数值乘方计算
nl1 = [value**2 for value in range(1,11)]
print(nl1);
#列表切片:获取下标从0开始,到3结束的元素(不包含3)
print(nl1[0:3]);
print(nl1[-2:]);

#列表复制:切片复制
newList = nl1[:];
print(newList)

####不要使用 这种只是把nl1的元素副本移植过来了,两个变量指向用一个元素列表,需要使用切片复制
aList = nl1;


###############
#下面的是元组:可以理解为不可修改的list,使用()区分
finalList = list((0,11));
print(finalList)
##下面的操作是不被允许的,因为元组的元素不可修改,否则报错
#finalList(0)=1;
for value in finalList:
    value+=value;
    print(value)

