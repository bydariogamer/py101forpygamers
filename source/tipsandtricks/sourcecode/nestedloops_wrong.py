import sys
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

def keyboard_handler():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            do_something()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keyboard_handler()

    window.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(30)
