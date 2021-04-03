import sys
import pygame
import time

pygame.init()

screen = pygame.display.set_mode((640, 640))
RECT_SIZE = 10
rect = pygame.Rect(640 // 4, 640 // 4, RECT_SIZE, RECT_SIZE)
isDrawed = False
# С помощью циклов, используя квадрат 10х10 пикселей и его след, нарисовать рамку 100х100 пикселей.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect.move_ip(-RECT_SIZE, 0)
            elif event.key == pygame.K_RIGHT:
                rect.move_ip(RECT_SIZE, 0)
            elif event.key == pygame.K_UP:
                rect.move_ip(0, -RECT_SIZE)
            elif event.key == pygame.K_DOWN:
                rect.move_ip(0, RECT_SIZE)

    pygame.draw.rect(screen, (255, 0, 0), rect, 0)

    i = 0
    while i < 40 and not isDrawed:
        print(f'Printing {i}')
        if 0 <= i < 10:
            rect.move_ip(RECT_SIZE, 0)
        elif 10 <= i < 20:
            rect.move_ip(0, RECT_SIZE)
        elif 20 <= i < 30:
            rect.move_ip(-RECT_SIZE, 0)
        elif 30 <= i < 40:
            rect.move_ip(0, -RECT_SIZE)
        pygame.draw.rect(screen, (255, 0, 0), rect, 0)
        pygame.display.flip()
        i += 1
        if i == 40:
            isDrawed = True
            print(f'Printed {i}')
        time.sleep(0.1)