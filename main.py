import pygame
import random

BLACK = (13, 2, 8)
TEXT_COLOURS = [(0, 59, 0), (0, 142, 17), (0, 255, 65)]

CHAR_LIST = []

# pygame setup
pygame.init()
display_size = pygame.display.get_desktop_sizes()
WIDTH = display_size[0][0]
HEIGHT = display_size[0][1]
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 1
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

# Render text on screen
# def get_letter():
#     font = pygame.font.SysFont(None, 24)
#     letter = font.render(chars[140], True, TEXT_COLOURS[1])
#     return letter


# Render text on screen while changing letter and colour
def get_letter():
    colour_picker = random.randint(0, 2)
    letter_picker = random.randint(0, len(chars)-1)
    for _ in range(5):
        font = pygame.font.SysFont('hiraginosansgb', 20)
        letter = font.render(chars[letter_picker], True, TEXT_COLOURS[colour_picker])
        return letter

while running:
    clock.tick(FPS)
    x = -10
    y = -20
    screen.fill(BLACK)

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

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
