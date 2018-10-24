#!/usr/bin/python3
###############
#字典列表综合:就相当于对象List
##############

##先创建一个外星人list容器
alienList = [];

#然后开始疯狂爆兵
for num in range(1,31):
    newAlien = {"color":"green","code_num":"编号"+str(num),"level":"0"}
    alienList.append(newAlien)
    #print("创建外星人完毕,当前编号："+newAlien["code_num"])

print("开始检查所有外星人aline")

#修改部分属性
for alien in alienList:
    codeNum = alien["code_num"]
    codeNum = codeNum.replace("编号","")
    if int(codeNum)  <2:
        #alien["level"]="1";
       # alien["code_num"]="aa111";
        alien1 = {"color":"red","code_num":"编号"+str(num)+"","level":"1"}
        alienList[int(codeNum)] = alien1


for new_alien in alienList:
    print(new_alien);


