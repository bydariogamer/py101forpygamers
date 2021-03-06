import pygame as pg
import random

pg.init()
screen = pg.display.set_mode([500, 500])

class MySprite:
    def __init__(self, image, initial_pos):
        self.image = image
        self.rect = image.get_rect(topleft=initial_pos)

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def draw(self, surface):
        surface.blit(self.image, self.rect)

square = pg.Surface((20, 20))
square.fill((255, 255, 255))

my_sprite = MySprite(square, (10, 10))

clock = pg.time.Clock()
while True:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    pressed = pg.key.get_pressed()
    if pressed[pg.K_w]:
        my_sprite.move(0, -1)
    if pressed[pg.K_s]:
        my_sprite.move(0, 1)
    if pressed[pg.K_a]:
        my_sprite.move(-1, 0)
    if pressed[pg.K_d]:
        my_sprite.move(1, 0)
    screen.fill((0, 0, 0))
    my_sprite.draw(screen)
    pg.display.flip()
