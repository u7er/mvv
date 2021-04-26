import pygame
import sys
import random

WIDTH = 640
HEIGHT = 480
pygame.init()

pygame.display.set_caption("snake")
screen = pygame.display.set_mode((WIDTH,HEIGHT))
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
direction = "RIGHT"
change_to = direction
snake_pos = [50,50]
size = 10
snake_body = [[50,50],[50-size,50],[50-size * 2,50]]
food_pos = [random.randint(1,WIDTH),random.randint(1,HEIGHT)]

def game():
    global change_to
    global direction
    global snake_pos
    global snake_body
    global food_pos
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_w:
                    change_to = "UP"
                elif event.key == pygame.K_s:
                    change_to = "DOWN"
                elif event.key == pygame.K_a:
                    change_to = "LEFT"
                elif event.key == pygame.K_d:
                    change_to = "RIGHT"
        if change_to == "UP" and not direction == "DOWN":
            direction = "UP"
        elif change_to == "DOWN" and not direction == "UP":
            direction = "DOWN"
        elif change_to == "LEFT" and not direction == "RIGHT":
            direction = "LEFT"
        elif change_to == "RIGHT" and not direction == "LEFT":
            direction = "RIGHT"
        if direction == "UP":
            snake_pos[1] -= size
        elif direction == "DOWN":
            snake_pos[1] += size
        elif direction == "RIGHT":
            snake_pos[0] += size
        elif direction == "LEFT":
            snake_pos[0] -= size
                    
game()
            