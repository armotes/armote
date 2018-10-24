from Dog import Samoye as sa,Dog as d
#from Dog import Dog as d
###########从Dog.py当中导入多个类 ：from Dog import Samoye as sa,Dog as d

###直接导入整个模块
#import Dog

class People():
    def __init__(self,life,name):
        self.life=life
        self.name=name

b = sa('小白','2','萨摩耶','白色')
#b = Dog.Samoye('小白','2','萨摩耶','白色')  ###直接导入整个模块(.py文件)的写法:类.类
b.showSamoye()
b.sit()

dd = d('小狗','1')
#dd = Dog.Dog('小狗','1')  ###直接导入整个模块(.py文件)的写法:类.类
dd.sit()

