import sys
import pygame

pygame.init()
WIDTH = 400
HEIGHT = 400
BLOCK_SIZE = 100
screen = pygame.display.set_mode((WIDTH, HEIGHT))
rect = pygame.Rect(0, 0, BLOCK_SIZE, BLOCK_SIZE)

# Написать программу, в которой по нажатию клавиш будет двигаться квадрат размером 20х20 пикселей. Учесть, что квадрат не должен выходить за границы экрана.

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
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
    pygame.draw.rect(screen, (255, 0, 0), rect, 0)
    pygame.display.flip()