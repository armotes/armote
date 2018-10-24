#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from com.lsx.set.Setting import Setting
from com.lsx.entity.ship import Ship
from com.lsx.entity.bullet import Bullte
from pygame.sprite import Group
from com.lsx.model.game_stats import GameStats
from com.lsx.model.button import Button
import com.lsx.module.game_funtions as mgf



class alienInvasionGame():
    def run_game():
        """"初始化游戏并创建一个屏幕对象,并且写入标题"""
        pygame.init()
        #获取配置信息
        setting = Setting()
        screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))
        pygame.display.set_caption(setting.caption)

        #创建Play按钮
        play_button = Button(setting,screen,"Play")
        #创建一个用于存储游戏统计信息的实例
        stats = GameStats(setting)

        #创建一艘飞船,子弹编组,外星人飞船编组
        ship = Ship(setting,screen)
        bullets = Group()
        aliens = Group()
        mgf.create_fleet(setting,screen,ship,aliens)
        #开始游戏的主循环
        while True:
            #监视键盘和鼠标事件
            mgf.check_events(setting,screen,stats,play_button,ship,aliens,bullets)

            #如果游戏活动状态为True:飞船生命>0
            if stats.game_active:
                #更新飞船位置以及属性
                ship.update()
                #更新子弹位置以及属性
                mgf.update_bullets(setting, screen, ship,aliens,bullets)
                mgf.update_alien(setting,stats,screen,ship,aliens,bullets)
            #更新屏幕
            mgf.update_screen(setting,screen,stats,ship,aliens,bullets,play_button)

    run_game()