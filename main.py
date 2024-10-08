import pygame
import random

BACKGROUND_COLOUR = (245, 247, 248)
TEXT_COLOURS = [
                (83, 191, 157), (249, 76, 102), (189, 66, 145), (255, 197, 77),
                (55, 226, 213), (89, 6, 150), (199, 10, 128), (251, 203, 10),
                (180, 255, 159), (249, 255, 164), (255, 213, 158), (255, 161, 161),
                (17, 20, 76), (58, 150, 121), (250, 188, 96), (225, 98, 98),
                (8, 95, 99), (73, 190, 183), (250, 207, 90), (255, 89, 89),
                (163, 67, 67), (233, 200, 116), (251, 248, 221), (192, 214, 232)
                ]

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


# Render text on screen while changing letter and colour
def get_letter():
    colour_picker = random.randint(0, 23)
    letter_picker = random.randint(0, len(chars)-1)
    for _ in range(15):
        font = pygame.font.SysFont('hiraginosansgb', 20)
        letter = font.render(chars[letter_picker], True, TEXT_COLOURS[colour_picker])
        return letter


while running:
    x = -10
    y = -20
    screen.fill(BACKGROUND_COLOUR)

    for _ in range(int(HEIGHT / 25)):
        screen.blit(get_letter(), (x, y))

        x = 0
        y += 25
        for _ in range(int(WIDTH / 25)):
            screen.blit(get_letter(), (x, y))
            x += 25

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
