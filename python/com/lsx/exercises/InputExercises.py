#!/usr/bin/python3
####下面是控制台输入
inputAccount = input("请输入您的账号: ")
inputPassword = input("请输入您的密码: ")
print("请核实您输入的信息:账号"+inputAccount+",密码:"+inputPassword)

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

#求模运算符%自动计算余数 可以除以2的都是偶数
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")