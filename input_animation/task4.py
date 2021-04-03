import sys
import pygame
import random as rnd
pygame.init()
WIDTH = 400
HEIGHT = 400
BLOCK_SIZE = 100
screen = pygame.display.set_mode((WIDTH, HEIGHT))
rect = pygame.Rect(0, 0, BLOCK_SIZE, BLOCK_SIZE)
random_color = (rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255))
# Написать программу, в которой по нажатию клавиш будет двигаться квадрат размером 20х20 пикселей. Учесть, что квадрат не должен выходить за границы экрана.

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            random_color = (rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255))
            if event.key == pygame.K_LEFT and rect.left >= BLOCK_SIZE:
                rect.move_ip(-100, 0)
            elif event.key == pygame.K_RIGHT and rect.right <= WIDTH - BLOCK_SIZE:
                rect.move_ip(100, 0)
            elif event.key == pygame.K_UP and rect.top >= BLOCK_SIZE:
                rect.move_ip(0, -100)
            elif event.key == pygame.K_DOWN and rect.bottom <= HEIGHT - BLOCK_SIZE:
                rect.move_ip(0, 100)
            print(rect.left, rect.right, rect.top, rect.bottom)

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, random_color, rect, 0)
    pygame.display.flip()