#python支持json开发
#json.dump(data,file) 写入
#json.load(fileObj) 读取
import json
from com.lsx.obj.Library import standard
class Json():
    filePath='D:/file/json.json'

    #用json向文件加入数据
    def wirteJsonFile(filePath,data):
        """用json向文件加入数据"""
        with open(filePath,'a') as file:
            #file.write(str(data)+"\n")
            json.dump(data,file)

    #用json将文件的数据读取
    def readJsonFile(filePath):
        """用json将文件的数据读取"""
        with open(filePath,'r') as file:
            data=json.load(file)
            print(data)

    data=[1,2,3,4,5,6,7,8,9]
    #wirteJsonFile(filePath, data)
    #readJsonFile(filePath)

    standard.mathNum()