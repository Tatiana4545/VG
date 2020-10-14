import pygame
import random
import sys
import os
import time

os.environ["SDL_VIDEO_POS"] ="0,0"
# os.environ["SDL_VIDEO_CENTERED"] = "1
pygame.init()

info = pygame.display.Info()
WIDTH_WIN, HEIGFT_WIN = Info.current_w * 100//125, Info.current_h 100//150
print(info.curren_w, info.curren)
print(WIDTH_WIN, HEIGFT_WIN)

screen = pygame.display.set_mode((WIDTH_WIN, HEIGFT_WIN))
pygame.mouse.set_visible(False)

FPS = 60
clock = pygame.time.Clock()

run = True
while run
    for  e  in pygame.event.get()
        if e.tyre == pygame.QUIT or e.tyre ==pygame.KEYDOWN and e.key == pygame.K_ESCAP:
        run = False
        