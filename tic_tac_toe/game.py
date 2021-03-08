import pygame
import sys

pygame.init()
block_size = 100
margin = 15
width = height = block_size * 3 + margin * 4

def check_win(mas, sign):
    zeroes = 0
    for row in mas:
        zeroes += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[1][1] == sign and mas[0][2] == sign and mas[2][0] == sign:
        return sign
    if zeroes == 0:
        return 'Ничья'
    return False

windows_size = (width, height)
screen = pygame.display.set_mode(windows_size)
pygame.display.set_caption('Крестики-нолики')

black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)

mas = [[0]*3 for _ in range(3)]
query = 0 # очередность хода
game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(0)
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (block_size + margin)
            row = y_mouse // (block_size + margin)
            if mas[row][col] != 0:
                continue

            if query % 2 == 0:
                mas[row][col] = 'x'
            else:
                mas[row][col] = 'o'
            query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0]*3 for _ in range(3)]
            query = 0
            screen.fill(black)
    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'x':
                    color = red
                elif mas[row][col] == 'o':
                    color = green
                else:
                    color = white
                # формула поиска координат
                x = col*block_size + (col + 1) * margin
                y = row*block_size + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, block_size, block_size))
                if color == red:
                    pygame.draw.line(screen, white, (x, y), (x + block_size, y + block_size), 3)
                    pygame.draw.line(screen, white, (x + block_size, y), (x, y + block_size), 3)
                elif color == green:
                    pygame.draw.circle(screen, white, (x+block_size//2, y + block_size // 2), block_size//2 - 3, 3)
    if (query - 1) % 2 == 0:
        game_over = check_win(mas, 'x')
    else:
        game_over = check_win(mas, 'o')

    if game_over:
        screen.fill(black)
        font = pygame.font.SysFont('stxinqkai', 36)
        text1 = font.render('Победил: ' + game_over, True, white)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, [text_x, text_y])
    pygame.display.update()