##########异常模块
# try:写入可能出现bug异常的代码 except告诉发生异常时如何处理
# else 依赖于try代码块成功执行的代码都放在else代码块中:相当于try部分的代码没有异常,成功的回调
#pass代表可以什么都不处理  except 后面异常捕捉里面默认必须要声明式写代码,如果不想处理就写pass
import com.lsx.exercises.Method as m
class TryExcept():
    def exceptMethod():
        print(5 /1)

    def fileIO(filePath):
        with open(filePath,'rb') as file:
            text = file.readlines()
            for str in text:
                print(str.strip())


    filePath='D:/file/pythonFDF.pdf'
    try:
        exceptMethod()
        m.getInfo('你大爷')
        fileIO('')
    except ZeroDivisionError:
        print("0不能被除!")
    except FileNotFoundError:
        pass  # pass代表可以什么都不处理  except 后面异常捕捉里面默认必须要声明式写代码,如果不想处理就写pass
        #print('文件不存在!')
    else:
        print("终于没有bug")

