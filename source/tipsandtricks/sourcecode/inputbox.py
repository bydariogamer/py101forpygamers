import sys
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

font = pygame.font.SysFont(pygame.font.get_default_font(), 32)

input_string = ""
input_surface = font.render(input_string, True, (255, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.unicode:
                input_string += event.unicode
            else:
                if event.key == pygame.K_BACKSPACE:
                    input_string = input_string[:-1]
                if event.key == pygame.K_RETURN:
                    print(f"You typed: '{input_string}'")

            input_surface = font.render(input_string, False, (255, 255, 255))

    window.fill((0, 0, 0))

    pygame.draw.rect(window, (127, 127, 127), ((8, 8), (250, 28)) )
    window.blit(input_surface, (10, 10))
    pygame.display.flip()
    clock.tick(30)
