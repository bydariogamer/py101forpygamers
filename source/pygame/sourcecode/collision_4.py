import pygame as pg

pg.init()
screen = pg.display.set_mode([500, 500])

# Dangerzone
dangerzone = pg.Surface((150, 80))
dangerzone.fill((255, 0, 0))
dangerzone_rect = dangerzone.get_rect(center=(250, 250))

# Player
player = pg.Surface((50, 50))
player.fill((0, 0, 255))
player_rect = player.get_rect(topleft=(10, 10))

clock = pg.time.Clock()

while True:
    clock.tick(30)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    keys = pg.key.get_pressed()

    if keys[pg.K_w]:
        player_rect.top -= 3
    if keys[pg.K_a]:
        player_rect.left -= 3
    if keys[pg.K_s]:
        player_rect.top += 3
    if keys[pg.K_d]:
        player_rect.left += 3

    if player_rect.colliderect(dangerzone_rect):
        player_rect.topleft = (10, 10)

    screen.fill((0, 0, 0))
    screen.blit(dangerzone, dangerzone_rect)
    screen.blit(player, player_rect)
    pg.display.flip()
