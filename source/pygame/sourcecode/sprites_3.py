import pygame as pg
import random

pg.init()
screen = pg.display.set_mode([500, 500])

class MySprite(pg.sprite.Sprite):
    def __init__(self, image, initial_pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=initial_pos)

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

square = pg.Surface((20, 20))
square.fill((255, 255, 255))

my_sprite = MySprite(square, (10, 10))
player_group = pg.sprite.Group([my_sprite])

square2 = pg.Surface((20, 20))
square2.fill((0, 255, 0))

my_sprite2 = MySprite(square2, (240, 240))
enemy_group = pg.sprite.Group([my_sprite2])

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

    if pg.sprite.groupcollide(player_group, enemy_group, False, False):
        my_sprite.rect.topleft = (10, 10)

    screen.fill((0, 0, 0))
    player_group.draw(screen)
    enemy_group.draw(screen)
    pg.display.flip()
