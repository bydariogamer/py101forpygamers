import pygame as pg

pg.init()
screen = pg.display.set_mode([500, 500])

# Button (green)
button = pg.Surface((150, 80))
button.fill((0, 255, 0))
button_rect = button.get_rect(center=(250, 250))

# Pressed button
pressed_button = pg.Surface((150, 80))
pressed_button.fill((255, 0, 0))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    draw_button = button
    if pg.mouse.get_pressed()[0]:
        if button_rect.collidepoint(pg.mouse.get_pos()):
            draw_button = pressed_button

    screen.fill((0, 0, 0))
    screen.blit(draw_button, button_rect)
    pg.display.flip()
