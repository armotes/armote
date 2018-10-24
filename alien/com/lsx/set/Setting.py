#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/9/30 22:03
# @Author : Moyan# @Site : armote
# @File : Setting.py
# @Software: PyCharm
# 设置类
class Setting():
    def __init__(self):
        """"初始化游戏的设置"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.caption = "异形入侵-v1.0.20180930.1 作者:阿默特"
        self.ship_speed_factor = 1.5 #飞船的速度
        self.alien_speed_factor = 1 #外星人飞碟的速度
        self.fleet_drop_speed = 10  #外星人飞碟下落的速度
        self.fleet_direction = 1    #舰队方向:1代表右移  -1代表左移
        self.ship_limit = 3         #飞船生命限制条数

        #子弹设置
        self.bullet_speed_factor = 3  #子弹速度
        self.bullet_width = 3   #子弹宽度
        self.bullet_height = 15 #子弹高度
        self.bullet_color = 60,60,60    #子弹颜色
        self.bullet_allowed = 10  #允许最大子弹数量

        #以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5  # 飞船的速度
        self.bullet_speed_factor = 3  # 子弹速度
        self.alien_speed_factor = 1   # 外星人飞碟的速度
        self.fleet_direction = 1  # 舰队方向:1代表右移  -1代表左移

    def increase_speed(self):
        """"提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale  # 飞船提高的速度
        self.bullet_speed_factor *= self.speedup_scale  # 子弹提高速度
        self.alien_speed_factor *= self.speedup_scale  # 外星人飞碟提高速度