#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Created on 2011-11-25
author: shiweifu
  mail: shiweifu@126.com
'''
import struct
import sys
import os
import pygame
from random import randint
 
 
import pygame.sprite as Sprite
from pygame.locals import *
 
debug = True
 
FONT_NAME = "Arial"
FONT_SIZE = 25
 
SCREENRECT = Rect(0, 0, 640, 480)
RECT_LEN = 15
 
class Box:
    def __init__(self, x, y, f):
        self.x = x
        self.y = y
        self.flag = f
        if self.flag:
            self.surface = get_font_surface("b")
        else:
            self.surface = pygame.Surface((15,15))
 
    def __str__(self):
        return "x:%s y:%s" % (str(self.x),str(self.y))
 
 
class Link(object):
     
    def __init__(self, x, y, surface):
        self.x = x
        self.y = y
        self.surface = surface
     
    def __str__(self):
        return "x:%s y:%s" % (str(self.x),str(self.y))
         
class Player:
    def __init__(self,x,y):
        self.snake_body = []
        self.append(x,y)
 
    def append(self,x,y):
        l = Link(x,y,get_font_surface("s",(255,0,0)))        
        self.snake_body.append(l)
 
    def abc(self):
        print("test")
     
    def move_left(self):
        i = len(self.snake_body) - 1
 
        while i >= 1:
#            debug_output("i:"+str(i))
            self.snake_body[i].x = self.snake_body[i-1].x
            self.snake_body[i].y = self.snake_body[i-1].y
            i -= 1
        self.snake_body[0].x -= 1       
 
 
    def move_right(self):
        i = len(self.snake_body) - 1
 
        while i >= 1:
#            debug_output("i:"+str(i))
            self.snake_body[i].x = self.snake_body[i-1].x
            self.snake_body[i].y = self.snake_body[i-1].y
            i -= 1
        self.snake_body[0].x += 1
 
    def move_up(self):
        i = len(self.snake_body) - 1
 
        while i >= 1:
            self.snake_body[i].x = self.snake_body[i-1].x
            self.snake_body[i].y = self.snake_body[i-1].y
            i -= 1
        self.snake_body[0].y -= 1
     
    def move_down(self):
        i = len(self.snake_body) - 1
 
        while i >= 1:
            self.snake_body[i].x = self.snake_body[i-1].x
            self.snake_body[i].y = self.snake_body[i-1].y
            i -= 1
        self.snake_body[0].y += 1
 
    def move(self,target):
        if target == "up":
            self.move_up()
        if target == "down":
            self.move_down()
        if target == "left":
            self.move_left()
        if target == "right":
            self.move_right() 
                 
def get_font_surface(s,color = (0,255,0),font_size=25):
    font = pygame.font.SysFont(FONT_NAME,font_size)
    #color = (0,255,0)
    backcolor = (0,0,0)
    r = font.render(s,True,color,backcolor)
    return r
 
def create_map(width,height,rect_len):
    y = 0
    map_pos = []
    snake_map = []
    flag =True
    while y < height:
        x = 0       
        flag = False
        while x < width:        
            if x < rect_len or x+rect_len >= width:
                flag = True
            elif y < rect_len or y+rect_len >= height:
                flag = True
            else:
                flag = False
 
            snake_map.append(Box(x/rect_len,y/rect_len,flag))
            x += 15
        y += 15
 
    return snake_map
 
def debug_output(s, f=sys.stdout):
    if debug == True:
        f.write("debug info: " + s + "\n")
        f.flush()
 
class Game:
     
    WIDTH = 640
    HEIGHT = 480
    BOX_SIZE = 15
     
    def __init__(self, caption="CooooolSnake"):
     
        pygame.init()
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode(SCREENRECT.size, 0, 32)    
        pygame.mouse.set_visible(0)
        self.background = pygame.Surface(SCREENRECT.size)
         
        self.map_size = (Game.WIDTH/15-1,Game.HEIGHT/15-1)
         
        self.snake_map = create_map(Game.WIDTH,Game.HEIGHT,self.BOX_SIZE)
         
        self.stages = []
         
        self.__crate_player__()
 
    def get_new_pos(self):
        done = False
        pos = None
        while not done:
            x = randint(2,self.map_size[0]-1)
            y = randint(2,self.map_size[1]-2)
 
            for link in self.player.snake_body:
                if x == link.x and y == link.y:
                    continue
            pos = (x,y)
            done = True
 
        return pos
                
 
    def __crate_player__(self):
        x = randint(2,self.map_size[0]-1)
        y = randint(2,self.map_size[1]-2)
        self.player = Player(x,y)
 
    def is_over(self):
        head = self.player.snake_body[0]
        i = 0
         
        for link in self.player.snake_body[1:]:
            if head.x == link.x and head.y == link.y:
                return True
         
        for box in self.snake_map:
            if box.flag:
                if head.x == box.x and head.y == box.y:
                    return True
        return False
         
    def update_snake(self):
         
        for link in self.player.snake_body:
            self.background.blit(link.surface,(link.x*Game.BOX_SIZE,link.y*Game.BOX_SIZE))
             
    def update_map(self):
        for box in self.snake_map:
            self.background.blit(box.surface,(box.x*Game.BOX_SIZE,box.y*Game.BOX_SIZE))
 
    def add_stage(self):
        x,y = self.get_new_pos()
        s = get_font_surface("s",(255,0,0))
        l = Link(x,y,s)
        self.stages.append(l)
     
    def update_stage(self):
        head = self.player.snake_body[0]
        for stage in self.stages:
            if stage.x == head.x and stage.y == head.y:
                self.player.append(stage.x,stage.y)
                self.stages.remove(stage)
                 
        for stage in self.stages:
            self.background.blit(stage.surface,(stage.x*Game.BOX_SIZE,stage.y*Game.BOX_SIZE))
 
    def refresh_background(self):
        self.background.fill((0,0,0))
        self.update_map()
        self.update_snake()
         
        self.update_stage()
         
        self.screen.blit(self.background, (0, 0))
         
    def over(self):        
        logo = get_font_surface("YOU ARE LOST!",(0,0,255),60)
        self.background.blit(logo,(100,200))
 
        clock = pygame.time.Clock()
        done = False
 
        count = 0
 
        while not done:
            clock.tick(10)
            count += 1
            if count == 5:
                done = True        
            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()
     
    def loop(self):
        pygame.display.update()
        clock = pygame.time.Clock()
        target = ["up","down","left","right"][randint(0,3)]
         
        count = 0
        stage_time = randint(0,50)
 
         
        done = False
        while not done:
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    keystate = pygame.key.get_pressed()
                    if keystate[K_UP]:
                        if target != "down":                        
                            target = "up"
 
                    elif keystate[K_DOWN]:
                        if target != "up":                        
                            target = "down"
 
                    elif keystate[K_LEFT]:
                        if target != "right":                        
                            target = "left"
 
                    elif keystate[K_RIGHT]:
                        if target != "left":                        
                            target = "right"
                             
                if e.type == QUIT:
                    done = True
            self.player.move(target)
            if count == stage_time:
                self.add_stage()
                stage_time = randint(0,50)
                count = 0
  
            if self.is_over():
                done = True
                 
            clock.tick(10)
             
            count += 1
             
            self.refresh_background()
             
            if done:
                self.over()
             
            pygame.display.flip()
 
if __name__ == '__main__':
    game = Game()
    game.loop()
    pass
