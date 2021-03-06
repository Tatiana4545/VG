import pygame
import random
import sys
import os
import time
from colors import COLOR

os.environ["SDL_VIDEO_WINDOW_POS"] = "0,0"
# os.environ["SDL_VIDEO_CENTERED"] = "1
pygame.init()

info = pygame.display.Info()
WIDTH_WIN, HEIGFT_WIN = info.current_w, info.current_h
# print(info.curren_w, info.curren)
# print(WIDTH_WIN, HEIGFT_WIN)

path = os.path.dirname(os.path.abspath(__file__))

saturn = os.path.join(path, "6s.png")
pygame.display.set_icon(pygame.image.load(saturn))
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((WIDTH_WIN, HEIGFT_WIN))
pygame.mouse.set_visible(False)

FPS = 30
clock = pygame.time.Clock()
NUMBER_OF_STARS = 200
NIGHT_BG_COLOR = (5, 0, 50)
p = " " * (WIDTH_WIN// 2 // 4)

class Stars(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = random.randint(1,2)
        self.size = random.randrange(1,3)
        self.pos = random.randrange(WIDTH_WIN), random.randrange(HEIGFT_WIN)
        self.image = pygame.Surface((self.size * 2, self.size * 2))
        pygame.draw.circle(self.image, pygame.Color(
            random.choice(COLOR[238:262])), [self.size, self.size], self.size)
        self.rect = self.image.get_rect(center=self.pos)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.left = WIDTH_WIN



class Planet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.image.load(os.path.join(path, '6s.png'))
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect(center=(x, y))
        self.rot = 0 
        self.angel = .5

    def update(self):
        self.rot = (self.rot + self.angel) % 360
        self.image = pygame.transform.rotate(self.image_orig, self.rot)
        self.rect = self.image/get_rect(center=self.rect.center)


sprites = pygame.sprite.LayeredUpdates()
for _ in range(NUMBER_OF_STARS):
    stars = Stars()
    sprites.add(stars, layer=0)

    pl = Planet(WIDTH_WIN // 3, HEIGFT_WIN // 2)
    sprites.add(pl, layer=0)

run = True
while run:
    clock.tick(FPS)
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            run = False

    sprites.update()
    screen.fill(NIGHT_BG_COLOR)
    sprites.draw(screen)
    pygame.display.update()
    pygame.display.set_cartion(f"Stars {p}FPS: {int(clock.get_fps())}"
