import pygame
import random

BACKGROUND_COLOUR = (13, 2, 8)
TEXT_COLOURS = [(0, 59, 0), (0, 142, 17), (0, 255, 65)]

CHAR_LIST = []

# pygame setup
pygame.init()
display_size = pygame.display.get_desktop_sizes()
WIDTH = display_size[0][0]
HEIGHT = display_size[0][1]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True

# character set up
chars = []

# Japanese characters
for i in range(96):
    symbol = chr(int('030A0', 16) + i)
    chars.append(symbol)

# Latin characters
for i in range(102):
    symbol = chr(int('0021') + i)
    chars.append(symbol)

print(chars)


while running:

    screen.fill("black")

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()


pygame.quit()


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

