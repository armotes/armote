#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2018/10/4 1:38
@Author : Moyan# @Site : armote
@File : alien.py
@Software: PyCharm
@Comment: 外星人实体(飞碟)
"""
from com.lsx.util.utils import Utils
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self,setting,screen):
        """初始化外星人并设置初始位置"""
        super().__init__()
        self.screen = screen
        self.setting = setting

        #加载外星人图像,并设置rect矩形属性
        utils = Utils()
        self.image = utils.readPicture("uuu.png")
        self.rect = self.image.get_rect()

        #每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        """如果外星人位于屏幕边缘,就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """向左或者右移动外星人飞碟"""
        #fleet_direction舰队方向:1代表右移  -1代表左移 使用正负数来控制+-x轴数值
        self.x += (self.setting.alien_speed_factor * self.setting.fleet_direction)
        self.rect.x = self.x