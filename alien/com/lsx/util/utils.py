#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/9/30 22:33
# @Author : Moyan# @Site : armote
# @File : utils.py
# @Software: PyCharm
# 工具类
import os
import pygame

class Utils():

    def __init__(self):
        path = os.getcwd()
        rootPathIndex = path.index('\\alien')
        endIndex = int(rootPathIndex + 6)
        self.rootPath=path[0:endIndex]

    def getRootPath():
        path = os.getcwd()
        rootPathIndex = path.index('\\alien')
        endIndex = int(rootPathIndex+6)
        return path[0:endIndex]


    def readPicture(self,pic):
        path = self.rootPath+'\\resource\image\\'+pic
        #print("解析后的图片地址:"+path)
        picPath = pygame.image.load(path)
        return picPath



