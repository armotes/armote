#!/usr/bin/python3

list = ['哈哈','嘿嘿','呵呵'];

mgs = "使用变量在加列表的数据,下标为2:"+list[2].title();
print(mgs);

#修改指定元素
list[2] = "我被修改啦";
mgs = "使用变量在加列表的数据,下标为2:"+list[2].title();
print(mgs);

#往最后append元素
list.append("往最后添加的哟");
#print(list)

list1 = list;
print(list1)

#在指下标插入元素
list1.insert(0,'插入的');
print(list1);

#删除指定元素
del list1[4];
print(list1);

#使用pop方法删除并提取指定元素,类似于mv命令
msg1 = list1.pop(0);
print(list1);
print(msg1);

#根据元素值来删除指定元素
#list.remove("哈哈")

list.append("c");
list.append("b");
list.append("x");

#使用sort函数进行永久性排序
list.sort();
print(list);

length = len(list);
print(length);

for str in list :
    print(str);
    print("结束啦");


print("结束啦");

