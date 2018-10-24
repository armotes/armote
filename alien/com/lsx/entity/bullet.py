#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time : 2018/10/3 22:19
@Author : Moyan# @Site : armote
@File : bullet.py
@Software: PyCharm
@Comment: 子弹实体 继承Sprite 可对元素进行编组
"""
import pygame
from pygame.sprite import Sprite
class Bullte(Sprite):
    """飞船子弹管理类"""
    def __init__(self,setting,screen,ship):
        """在飞船所处的位置创建一个子弹对象"""
        #super(Bullte,self).__init__() 这个是python2.7的语法 虽然python3也可以用
        super().__init__()
        self.screen = screen

        #在(0,0)处创建一个表示子弹的初始矩形,在设置正确的位置
        self.rect = pygame.Rect(0,0,setting.bullet_width,setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #储存用小数表示的子弹位置:实际使用的是rect 这里是另外转为小数点使用
        self.y = float(self.rect.y)

        self.color = setting.bullet_color
        self.speed_factor = setting.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        #更新表示子弹位置的小数值
        self.y -= self.speed_factor
        #更新表示子弹rect矩形的位位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上面绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)