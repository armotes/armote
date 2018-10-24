##############
#游戏函数模块组件
#类似于静态方法,但又不一样,需要就直接导入模块.方法名,不需要实例化
#无法存储属性的,仅作为方法函数调用,比较方便
#约定:模块方法使用_分割英文,区别于类里的驼峰命名法,同时导入的模块命名为m开头
##############
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from com.lsx.entity.bullet import Bullte
from com.lsx.entity.alien import Alien
from time import sleep


###event

def check_key_events(event,setting,screen,ship,bullets,flag):
    """"监控键盘事件,根据按下或者松开设置指定值flag:True按下 False松开"""
    if event.key == pygame.K_RIGHT:
        ship.movingRight = flag
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = flag
    elif event.key == pygame.K_UP:
        ship.movingUp = flag
    elif event.key == pygame.K_DOWN:
        ship.movingDown = flag
    elif event.key == pygame.K_SPACE and flag:
        # 空格:创建一颗子弹,并加入到编组bullets中 并且flag为True 仅限按下事件
        fire_bullet(setting, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE and flag:
        sys.exit()

def fire_bullet(setting,screen,ship,bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    if len(bullets) < setting.bullet_allowed:
        bullet = Bullte(setting, screen, ship)
        bullets.add(bullet)


def check_events(setting,screen,stats,play_button,ship,aliens,bullets):
    """"响应按键和鼠标事件"""
    for event in pygame.event.get():
        #监控退出
        if event.type == pygame.QUIT:
            sys.exit()
        #监控键控按下事件:按下键盘:True开始移动
        elif event.type == pygame.KEYDOWN:
            check_key_events(event,setting,screen,ship,bullets,True)
        #监控监控按上事件:松开键盘:False结束移动
        elif event.type == pygame.KEYUP:
            check_key_events(event,setting,screen, ship,bullets,False)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # get_pos：返回一个元组:包含当前鼠标点击x,y轴坐标
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(setting,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y)

def check_play_button(setting,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    """在玩家单击Play按钮时开始新游戏"""
    #collidepoint检查鼠标单击位置是否在Play按钮的rect内（参数:传入单击的x,y坐标）
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        #重置游戏设置
        setting.initialize_dynamic_setting()

        #隐藏光标
        pygame.mouse.set_visible(False)
        #重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        #创建一群新的外星人,并让飞船居中
        create_fleet(setting,screen,ship,aliens)
        ship.center_ship()



def update_screen(setting,screen,stats,ship,aliens,bullets,play_button):
    """ 每次循环时都会重绘屏幕:fill参数只接受一个实参，一个RGB (red,green,blue),让最近的绘制屏幕可见"""
    # 每次循环时都会重绘屏幕:fill参数只接受一个实参，一个RGB (red,green,blue)
    screen.fill(setting.bg_color)

    #如果游戏处于非活动状态:就会绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    #在屏幕上绘制编组中的每个外星人
    aliens.draw(screen)
    # 让最近的绘制屏幕可见
    pygame.display.flip()

def check_bullet_alien_collisions(setting, screen, ship,aliens,bullets):
    """响应子弹和外星人的碰撞"""
    # 删除发生碰撞的子弹和外星人:
    # 1检查是否有子弹击中了外星人
    # 2如果是这样,就删除相应的子弹和外星人
    # 3遍历编组bullets中的每颗子弹，再遍历编组aliens中的每个外星人。
    # 4每当有子弹和外星人的rect重叠时， groupcollide()就在它返回的字典中添加一个键值对
    # 5两个实参True告诉Pygame删除发生碰撞的子弹和外星人 如果子弹的布尔值为True,就有穿透单的效果了
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # 在更新子弹的时候:检查外星人数量
    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人
        bullets.empty()
        setting.increase_speed()
        create_fleet(setting, screen, ship, aliens)

def update_bullets(setting, screen, ship,aliens,bullets):
    """更新子弹的位置,并删除已消失的子弹"""
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #print("当前屏幕子弹数量:" + str(len(bullets)))

    check_bullet_alien_collisions(setting, screen, ship, aliens, bullets)

def  get_number_aliens_x(setting,alien_width):
    """计算可以创建外星人的数量"""
    # 先去掉2个外星人宽度,左右不靠边
    available_sapce_x = setting.screen_width - (2 * alien_width)
    # 外星人飞碟之间空余宽度为飞碟自身宽度:即隔1个
    number_alien_x = int(available_sapce_x / (2 * alien_width))
    return number_alien_x

def get_number_rows(setting,ship_height,alien_height):
    """计算屏幕可以兼容多少行外星人"""
    #demo计算有问题,需要减少
    available_space_y = (setting.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(setting,screen,aliens,alien_number,row_number):

    """创建一个外星人并加入当前行"""
    alien = Alien(setting,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)



def create_fleet(setting,screen,ship,aliens):
    """创建外星人群"""
    #创建一个外星人,并计算一行可容纳多少外星人
    #外星人间距为外星人宽度
    alien = Alien(setting,screen)
    alien_width = alien.rect.width
    number_alien_x = get_number_aliens_x(setting, alien_width)
    number_rows = get_number_rows(setting,ship.rect.height,alien.rect.height)


    for row_number in range(number_rows):
    # 创建第一行外星人
        for alien_number in range(number_alien_x):
            create_alien(setting, screen, aliens, alien_number,row_number)

def check_fleet_edges(setting,aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        #遍历外星人组,如果有外星人到达了边缘,True
        if alien.check_edges():
            change_fleet_direction(setting,aliens)
            break

def change_fleet_direction(setting,aliens):
    """将整群外星人下移,并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += setting.fleet_drop_speed
    #这里改变方向就是*-1,因为1*-1=-1  -1*-1=1 这样就可以来回改变方向
    setting.fleet_direction *= -1



def ship_hit(setting,stats,screen,ship,aliens,bullets):
    """响应被外星人撞到的飞船"""
    #print("当前剩余生命:"+str(stats.ships_life))
    if stats.ships_life > 0:
        #将ships_life 减1
        stats.ships_life -= 1
        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        #创建一群新的外星人,并将飞船放到屏幕底端中央
        create_fleet(setting,screen,ship,aliens)
        ship.center_ship()
        #暂停
        sleep(0.5)
    else:
        #print("游戏即将结束")
        stats.game_active = False
        pygame.mouse.set_visible(True)

def update_alien(setting,stats,screen,ship,aliens,bullets):
    """检查是否有外星人位于屏幕边缘,并更新整群外星人的位置"""
    check_fleet_edges(setting,aliens)
    #aliens已经将所有外星人进行编组,那么aliens.update()将对所有外星人进行update方法操作
    aliens.update()

    #检查外星人和飞船之间的碰撞
    #spritecollideany参数:一个精灵sprite 一个编组Group:
    #检查编组是否有成员与精灵发生碰撞,如果有,则停止遍历,返回第一个与飞船发生了碰撞的外星人
    #如果没有,返回None
    if pygame.sprite.spritecollideany(ship,aliens):
        #print("撞船啦!")
        ship_hit(setting,stats,screen,ship,aliens,bullets)

    #检查是否有外星人到达了屏幕底端
    check_aliens_bottom(setting, stats, screen, ship, aliens, bullets)

def check_aliens_bottom(setting,stats,screen,ship,aliens,bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #撞船那样进行处理
            ship_hit(setting,stats,screen,ship,aliens,bullets)
            break
