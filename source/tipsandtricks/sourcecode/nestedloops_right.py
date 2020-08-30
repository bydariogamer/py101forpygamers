import sys
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

def keyboard_handler(events):
    for event in events:
        if event.type == pygame.KEYDOWN:
            do_something()

while True:
    events = pygame.events.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()

    keyboard_handler(events)

    window.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(30)
