import pygame
import random

BACKGROUND_COLOUR = (247, 249, 242)
TEXT_COLOURS = [(83, 191, 157), (249, 76, 102), (189, 66, 145), (255, 197, 77),
                (55, 226, 213), (89, 6, 150), (199, 10, 128), (251, 203, 10),
                (180, 255, 159), (249, 255, 164), (255, 213, 158), (255, 161, 161)]

print(len(TEXT_COLOURS))

CHAR_LIST = []

# pygame setup
pygame.init()
display_size = pygame.display.get_desktop_sizes()
WIDTH = display_size[0][0]
HEIGHT = display_size[0][1]
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 15
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
    colour_picker = random.randint(0, 11)
    letter_picker = random.randint(0, len(chars)-1)
    for _ in range(5):
        font = pygame.font.SysFont('hiraginosansgb', 20)
        letter = font.render(chars[letter_picker], True, TEXT_COLOURS[colour_picker])
        return letter


while running:
    clock.tick(FPS)
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
