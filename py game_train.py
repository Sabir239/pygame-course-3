import pygame
from sys import exit
pygame.init()

# Draw screen and title
screen = pygame.display.set_mode((800, 600))
title =pygame.display.set_caption('uncunu')  # تم تصحيح هذا السطر

# Import image for the soul
caje = pygame.image.load('Caja.png')

# Text font and size
text_font = pygame.font.Font('pixel-comic-sans-undertale-sans-font.otf', 50)

# Create text
text_surface = text_font.render('start', False, (255, 255, 255))

# Basic animation
soul = pygame.image.load('souls.png')
souls_x_pos = 600
soul = pygame.transform.scale(soul, (60, 30))

# Colors
black = (0, 0, 0)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            exit()

    screen.fill(black)  # تنضيف الشاشة كل فريم
    screen.blit(caje, (100, 350))
    screen.blit(text_surface, (90, 80))

    souls_x_pos += 0.5
    screen.blit(soul, (souls_x_pos, 300))

    pygame.display.update()
    clock.tick(60)
