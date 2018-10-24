class UserInfo():

###########上面的语法就是定义一个类
################构造方法:自动加载,默认名字就是__init__ 而不是UserInfo:第一个参数是默认的返回值
    def __init__(user,name,add):
        user.name=name
        user.add=add


    def getUserInfo(user):
        print("userName is : "+user.name+" ,userAdd is "+user.add)

    def setAdd(user,add):
        user.add=add


myFriend = UserInfo('armote','wuhan')
print("my name is "+myFriend.name+" , add is "+myFriend.add)

myFriend.getUserInfo()
myFriend.setAdd('湖北')
print(myFriend.add)