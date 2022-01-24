# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 10:41:29 2021

@author: Admin
"""
# Chuyển code về hướng đối tượng
# Class trò chơi: Hàm khởi tạo; có phương thức chạy vòng lặp game


from os import pipe, spawnl
from types import new_class
import pygame, sys,random
from pygame.time import Clock
#tao ham
def draw_floor():
    screen.blit(floor,(floor_x_pos,650))
    screen.blit(floor,(floor_x_pos+432,650))
def creat_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bot_pipe = pipe_s.get_rect(midtop = (500,random_pipe_pos))
    top_pipe = pipe_s.get_rect(midtop = (500,random_pipe_pos-650))
    return bot_pipe,top_pipe
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -=5
    return pipes
def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600: 
            screen.blit(pipe_s,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_s,False,True)
            screen.blit(flip_pipe,pipe)
def va_cham(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            hit_sound.play()
            return False
        if bird_rect.top <= -75 or bird_rect.bottom >= 650:
            return False
    return True
def score_display(game_state):
    if game_state =='main game':
        score_s = game_font.render(str(int(score)),True,(255,255,255))
        score_rect = score_s.get_rect(center=(216,100))
        screen.blit(score_s,score_rect)
    if game_state =='game_over':
        score_s = game_font.render(f'Score:{(int(score))}',True,(255,255,255))
        score_rect = score_s.get_rect(center=(216,100))
        screen.blit(score_s,score_rect)

        high_score_s = game_font.render(f'High Score:{(int(high_score))}',True,(255,255,255))
        high_score_rect = high_score_s.get_rect(center=(216,630))
        screen.blit(high_score_s,high_score_rect)
def upd_score(score,high_score):
    if score > high_score:
        high_score = score
    return high_score
pygame.init()
screen = pygame.display.set_mode((432,768))
clock = pygame.time.Clock()
game_font = pygame.font.SysFont('Consolas',40)
#tao trong luc cho chim
gravity = 0.25
bird_move =0
game_active = True
score = 0
high_score = 0
#chen background
bg = pygame.image.load('/Users/builehuyentrang/Documents/19001725-BuiLeHuyenTrang-K9CNTT/image_sound/background.png')
bg = pygame.transform.scale2x(bg)
#chen floor
floor = pygame.image.load('/Users/builehuyentrang/Documents/19001725-BuiLeHuyenTrang-K9CNTT/image_sound/floor.png')
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
#tao chim
bird = pygame.image.load('/Users/builehuyentrang/Documents/19001725-BuiLeHuyenTrang-K9CNTT/image_sound/birdmid.png')
bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center = (100,348))
#tao ong
pipe_s = pygame.image.load('/Users/builehuyentrang/Documents/19001725-BuiLeHuyenTrang-K9CNTT/image_sound/pipe.png')
pipe_s = pygame.transform.scale2x(pipe_s)
pipe_list =[]
#tao timer
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe,1200)
pipe_height = [200,300,400]
#tao man hinh ket thuc
game_over_s = pygame.transform.scale2x(pygame.image.load('/Users/builehuyentrang/Documents/19001725-BuiLeHuyenTrang-K9CNTT/image_sound/message.png'))
game_over_rect = game_over_s.get_rect(center=(216,384))
#chen am thanh
flap_sound = pygame.mixer.Sound('/Users/builehuyentrang/Documents/19001725-BuiLeHuyenTrang-K9CNTT/image_sound/sfx_wing.wav')
hit_sound = pygame.mixer.Sound('/Users/builehuyentrang/Documents/19001725-BuiLeHuyenTrang-K9CNTT/image_sound/sfx_hit.wav')
score_sound = pygame.mixer.Sound('/Users/builehuyentrang/Documents/19001725-BuiLeHuyenTrang-K9CNTT/image_sound/sfx_point.wav')
score_countdown = 100
#while loop cua tro choi
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_move = 0
                bird_move = -7
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active==False:
                 game_active = True
                 pipe_list.clear()
                 bird_rect.center = (100,384)
                 bird_move = 0
                 score = 0
        if event.type == spawnpipe:
            pipe_list.extend(creat_pipe())
            
    screen.blit(bg,(0,0))
    if game_active:
        bird_move +=gravity
        bird_rect.centery += bird_move
        screen.blit(bird,bird_rect)
        game_active = va_cham(pipe_list)
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
        score += 0.01
        score_display('main game')
        score_countdown -=1
        if score_countdown <=0:
            score_sound.play()
            score_countdown = 100
    else:
        screen.blit(game_over_s,game_over_rect)
        high_score =upd_score(score,high_score)
        score_display('game_over')
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(120)

