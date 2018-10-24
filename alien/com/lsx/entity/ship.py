#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/9/30 22:33
# @Author : Moyan# @Site : armote
# @File : ship.py
# @Software: PyCharm
# 飞船类
import pygame
from com.lsx.util.utils import Utils

class Ship():
    def __init__(self,setting , screen):
        """初始化飞船并且设置初始的位置"""
        self.screen = screen
        self.setting = setting
        #加载飞船图像并获取其外接矩形:路径默认为工作空间根目录
        utils = Utils()

        #picPath = utils.rootPath+"\\resource\image\\fly_ship.bmp"
        #self.image = pygame.image.load(picPath)
        self.image = utils.readPicture("ff.ico")

        self.rect = self.image.get_rect()  #飞船矩形
        self.screen_rect = screen.get_rect() #屏幕矩形
        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx  #屏幕矩形中央的x坐标赋值给飞船的x坐标
        self.rect.bottom = self.screen_rect.bottom    #屏幕矩形下边缘的坐标赋值给飞船的下坐标

        #在飞船的属性center中储存小数值:配置速度使用 这个就是X坐标 飞船中间的坐标
        self.center = float(self.rect.centerx)

        #自定义一个Y坐标,将飞船的booton下边movingUp
        # 缘坐标作为Y坐标 重新解析
        self.bottomy = float(self.screen_rect.bottom)

        self.movingRight = False    #向右移动flag
        self.movingLeft = False     #向左移动flag
        self.movingUp = False       #向上移动flag
        self.movingDown = False      #向下移动flag

    def update(self):
        """"根据移动flag调整飞船的位置"""
        #更新飞船的center值:这个值是拥有速度属性的小数值
        #飞船向右移动时，飞船矩形右边缘x坐标不能超过屏幕矩形右边缘坐标
        if self.movingRight and self.rect.right < self.screen_rect.right:
            self.center +=self.setting.ship_speed_factor
        #飞船向左移动时，飞船矩形左边缘x坐标不能超过屏幕矩形左边缘起始坐标
        if self.movingLeft and self.rect.left > 0:
            self.center -=self.setting.ship_speed_factor
        if self.movingUp and self.rect.top >0:
            self.bottomy -= self.setting.ship_speed_factor
        if self.movingDown and self.rect.bottom <self.screen_rect.bottom:
            self.bottomy += self.setting.ship_speed_factor

        #根据self.更新rect对象
        self.rect.centerx = self.center
        self.rect.bottom = self.bottomy

    def blitme(self):
        """"在制定位置绘制飞船screen.blit"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom