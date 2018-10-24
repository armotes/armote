#!/usr/bin/env python
# -*- coding: utf-8 -*-
class GameStats():
    """跟踪游戏的统计信息:模型"""
    def __init__(self,setting):
        """初始化统计信息"""
        self.setting = setting
        #游戏刚启动时处于非活动状态
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        #飞船生命
        self.ships_life = self.setting.ship_limit
