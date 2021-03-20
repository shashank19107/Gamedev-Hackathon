import pygame

pygame.init()

clock = pygame.time.Clock()

white = (255, 255, 255)
off_white = (240, 240, 240)
black = (0, 0, 0)
red = (255, 0, 0)
light_red = (200, 0, 0)
blue = (0, 0, 255)
red_highlight = (240, 50, 50, 100)


main_menu_bg_img = pygame.image.load("background_main_menu.jpeg")
game_bg_img = pygame.image.load("game_bg.png")
number1_img = pygame.image.load("number1.png")
number2_img = pygame.image.load("number2.png")
number3_img = pygame.image.load("number3.png")
number4_img = pygame.image.load("number4.png")
number5_img = pygame.image.load("number5.png")
number6_img = pygame.image.load("number6.png")

game_display = pygame.display.set_mode((1280, 720))
pygame.display.update()


def button(x_button, y_button, msg):
    pygame.draw.rect(game_display, white, [x_button, y_button, 100, 30])
    message(50, msg, x_button, y_button, black)
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x_button + 100 > mouse_pos[0] > x_button and y_button + 30 > mouse_pos[1] > y_button:
        pygame.draw.rect(game_display, off_white, [x_button, y_button, 100, 30])
        message(50, msg, x_button, y_button, black)
        if click == (1, 0, 0) and msg == "PLAY":
            game_loop()
        elif click == (1, 0, 0) and msg == "QUIT":
            pygame.quit()
            quit()
        elif click == (1, 0, 0) and msg == "BACK":
            main_menu()


def main_menu():
    game_play = False
    while not game_play:
        game_display.blit(main_menu_bg_img, (0, 0))
        button(1120, 550, "PLAY")
        button(1120, 630, "QUIT")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()


def message(size, msg, x_pos, y_pos, col):
    font = pygame.font.SysFont(None, size)
    render = font.render(msg, True, col)
    game_display.blit(render, (x_pos, y_pos))


def game_loop():
    game_over = False
    while not game_over:
        game_display.blit(game_bg_img, (0, 0))
        button(300, 300, "BACK")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        message(100, "HAND CRICKET", 500, 50, white)
        clock.tick(60)
        pygame.display.update()
        

main_menu()
pygame.quit()
quit()