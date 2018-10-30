class File():
    ##################文件流
    filePath='D:/file/设备sql.txt'

    #打印全部
    def showFileText(filePath):
        with open(filePath) as sqlFile:
            sqlContents = sqlFile.read() #读取全部
            print(sqlContents.rstrip())
            print("打印完毕")

    #逐行读取
    def showFileByLine(filePath):
        with open(filePath) as sqlFiles:
            count=0
            for line in sqlFiles: #使用循环输出每一行
                print(line.rstrip())
                #print("第"+str(count)+"行:"+line)
                count+=1

    #将文件读取的内容转为list
    def coverListByFile(filePath):
        with open(filePath) as sqlFiles:
            lines = sqlFiles.readlines() #readlines()方法将逐行读取,返回list
        for line in lines:
            print(line.rstrip())

    ##纯写入模式:如果文件不存在,自动创建,如果存在,将会覆盖原来的内容
    def writeFile(filePath):
        with open(filePath,'w') as file:
            file.write('这是我writeFile方法写入的汉字')

    #读写模式:如果文件不存在,自动创建,如果存在,将会覆盖原来的内容
    def rwFile(filePath):
        with open(filePath,'r+') as file:
            file.write('1这是我rwFile方法写入的汉字\n')
            file.write('2这是我rwFile方法写入的汉字\n')

    #附加模式:如果文件不存在,自动创建,如果存在,则在文本最后附加添加数据
    def additionalFile(filePath):
        with open(filePath,'a') as file:
            file.write('这个是我追加的内容\n')

    #showFileText(filePath)
    #showFileByLine(filePath)
    #coverListByFile(filePath)
    #writeFile('D:/file/write.txt')
    #rwFile('D:/file/write.txt')
    additionalFile('D:/file/write.txt')
