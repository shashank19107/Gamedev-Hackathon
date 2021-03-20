import pygame
import time

our_score = 3
our_wicket = 3
opp_score = 6
opp_wicket = 0
balls = 0.3
our_curr = 1
opp_curr = 2


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

# create screen
game_display = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
pygame.display.update()


def button(x_button, y_button, msg, color1, color2):
    button_width = 150
    button_height = 50
    pygame.draw.rect(game_display, color1, [x_button, y_button, button_width, button_height])
    message(100, msg, x_button, y_button, black)
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x_button + button_width > mouse_pos[0] > x_button and y_button + button_height > mouse_pos[1] > y_button:
        pygame.draw.rect(game_display, color2, [x_button, y_button, button_width, button_height])
        message(100, msg, x_button, y_button, black)
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
        button(1700, 800, "PLAY", white, off_white)
        button(1700, 950, "QUIT", white, off_white)
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
    global our_score
    while not game_over:
        game_display.blit(game_bg_img, (0, 0))
        button(50, 50, "BACK", white, off_white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    our_score += 1

        font = pygame.font.SysFont(None, 200)
        score1 = font.render(str(our_score) + "/" + str(our_wicket), True, white)
        game_display.blit(score1, (500, 50))
        score2 = font.render(str(opp_score) + "/" + str(opp_wicket), True, white)
        game_display.blit(score2, (800, 50))
        balls_thrown = font.render(str(balls), True, white)
        game_display.blit(balls_thrown, (1500, 50))
        font2 = pygame.font.SysFont(None, 500)
        our_curr_score = font2.render(str(our_curr), True, white)
        game_display.blit(our_curr_score, (600, 300))
        opp_curr_score = font2.render(str(opp_curr), True, white)
        game_display.blit(opp_curr_score, (1100, 300))
        # seconds = 4
        # render = font.render(str(seconds), True, white)
        # game_display.blit(render, (500, 50))
        # for i in range(seconds):
        #     render = font.render(str(seconds - i), True, white)
        #     game_display.blit(render, (500, 50))
        #     time.sleep(i)
        # message(100, "HAND CRICKET", 500, 50, white)

        clock.tick(60)
        pygame.display.update()


main_menu()
pygame.quit()
quit()
