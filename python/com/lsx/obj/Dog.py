class Dog():
        #"""一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
        #"""初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
    #"""模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")


    def roll_over(self):
    #"""模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")

###########类lift可以作为其他类的一个属性
class Life():
    def __init__(self,):
        self.val='10'



###########下面的是继承:继承了父类Dog的属性和方法,也有属于自己的属性和方法,也可以重写父类方法
class Samoye(Dog):
    def __init__(self,name,age,type,color):
        super().__init__(name,age)
        self.type=type
        self.color=color
        self.life=Life()

    ##展示自己的属性,继承父类的属性,以及将其他类作为自己的属性
    def showSamoye(self):
        print("info ： type:"+self.type+" , color:"+self.color+" , name:"+self.name+" , age:"+self.age+" , life is :"+self.life.val)

    ####这里就是重写父类方法
    def sit(self):
        print("萨摩耶=>>>"+self.name.title() + " is now sitting.")

#bb = Samoye('小白','1','萨摩耶','白色')
#bb.showSamoye()
#bb.roll_over()
#bb.sit()