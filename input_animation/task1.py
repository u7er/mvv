import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
rect = pygame.Rect(40, 40, 120, 120)
sprite = pygame.image.load("input_animation\snake.png")


# Написать программу, которая будет писать в консоль названия нажатых клавиш. Реализовать поддержку enter, space, w, a, s, d, esc.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                print("Нажата клавиша enter")
            elif keys[pygame.K_SPACE]:
                print("Нажата клавиша space")
            elif keys[pygame.K_w]:
                print("Нажата клавиша W")
            elif keys[pygame.K_s]:
                print("Нажата клавиша S")
            elif keys[pygame.K_d]:
                print("Нажата клавиша D")
            elif keys[pygame.K_a]:
                print("Нажата клавиша A")
            elif keys[pygame.K_ESCAPE]:
                print("Нажата клавиша escape")
    pygame.display.flip()