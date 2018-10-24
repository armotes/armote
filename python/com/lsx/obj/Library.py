from collections import OrderedDict
#从python标准库里面导入模板使用:collections.py里面的OrderedDict类  有序字典:可以记录k-v添加的顺序
class standard():
    def mathNum():
        col = OrderedDict();
        col['c'] = '60分'
        col['java'] = '90分'
        col['c#'] = '70分'
        for k,v in col.items():
            print("科目:"+k+" ,成绩:"+v)

        print(__name__)

    #判断自己是否为主程序:__name__在自己的模板打印为__main__ 如果别人打印就是包名.类名
    if __name__=='__main__':
        mathNum()