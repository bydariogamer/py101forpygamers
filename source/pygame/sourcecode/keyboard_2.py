import pygame as pg
import random

pg.init()
screen = pg.display.set_mode([500, 500])
square = pg.Surface((20, 20))
square.fill((255, 255, 255))
rect = square.get_rect()
clock = pg.time.Clock()
while True:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            rect.x = random.randrange(0, 479)
            rect.y = random.randrange(0, 479)
    pressed = pg.key.get_pressed()
    if pressed[pg.K_w]:
        rect.y -= 1
    if pressed[pg.K_s]:
        rect.y += 1
    if pressed[pg.K_a]:
        rect.x -= 1
    if pressed[pg.K_d]:
        rect.x += 1
    screen.fill((0, 0, 0))
    screen.blit(square, rect)
    pg.display.flip()
