import sys
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

sysfont = pygame.font.SysFont(pygame.font.get_default_font(), 32)
custom_font = pygame.font.Font("myfont.ttf", 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    sysfont_surface = sysfont.render("Welcome", False, (255, 255, 255))
    customfont_surface = custom_font.render("Welcome", False, (255, 255, 255))

    window.fill((0, 0, 0))

    window.blit(sysfont_surface, (10, 10))
    window.blit(customfont_surface, (10, 50))


    pygame.display.flip()
    clock.tick(30)
