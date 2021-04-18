import pygame
import time
import random
import cv2
import time
import threading
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


count =0
cap = cv2.VideoCapture(0)
cameradone = False

our_score = 3
our_wicket = 3
opp_score = 6
opp_wicket = 0
balls = 0.3
our_curr = 1
opp_curr = 2
#11
global val

pygame.init()



def cameraInput():
    print("aaya")
    with mp_hands.Hands(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:  
        print("aaya")  
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue
            print("Non empty camera frame?")
            # Flip the image horizontally for a later selfie-view display, and convert
            # the BGR image to RGB.
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            global cameradone
            image.flags.writeable = False
            results = hands.process(image)
            image_height, image_width, _ = image.shape

            # Draw the hand annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            #Counting fingers visible in the frame
            global count
            count = 0
            
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Index finger  
                    if(hand_landmarks.landmark[5].y > hand_landmarks.landmark[6].y and hand_landmarks.landmark[7].y > hand_landmarks.landmark[8].y ):
                        count+=1

                    # thumbR
                    if(hand_landmarks.landmark[1].x > hand_landmarks.landmark[2].x and hand_landmarks.landmark[3].x > hand_landmarks.landmark[4].x  and hand_landmarks.landmark[2].y > hand_landmarks.landmark[3].y and hand_landmarks.landmark[3].y > hand_landmarks.landmark[4].y):
                        count+=1
                    #Thumb L
                    if(hand_landmarks.landmark[1].x < hand_landmarks.landmark[2].x and hand_landmarks.landmark[3].x < hand_landmarks.landmark[4].x  and hand_landmarks.landmark[2].y > hand_landmarks.landmark[3].y and hand_landmarks.landmark[3].y > hand_landmarks.landmark[4].y):
                        count+=1        
                    # Middle finger
                    if(hand_landmarks.landmark[9].y > hand_landmarks.landmark[10].y and hand_landmarks.landmark[11].y > hand_landmarks.landmark[12].y ):
                        count+=1        

                    #Ring finger
                    if(hand_landmarks.landmark[13].y > hand_landmarks.landmark[14].y and hand_landmarks.landmark[15].y > hand_landmarks.landmark[16].y ):
                        count+=1

                    #Little finger
                    if(hand_landmarks.landmark[17].y > hand_landmarks.landmark[18].y and hand_landmarks.landmark[19].y > hand_landmarks.landmark[20].y ):
                        count+=1
                    mp_drawing.draw_landmarks(
                        image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            #print(count)   
            #count =0 
            image = cv2.putText(image, str(count), (50, 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            cv2.imshow('Hands', image)
            #print(results.multi_hand_landmarks.landmark(10).y, results.multi_hand_landmarks[11].y, results.multi_hand_landmarks[12].y )
            if cameradone or (cv2.waitKey(5) & 0xFF == 27):
                break
    print("gaya")

t1 = threading.Thread(target=cameraInput, name='t1')
t1.start()

def user_bats_first(lives,overs):
    fot = pygame.font.SysFont(None, 70)
    disp = fot.render("First Innings start!", True, white)
    game_display.blit(disp, (300, 20))
    num_overs=0
    global count
    target=0
    while(num_overs<overs):
        balls=1
        while(balls<=6):
            print("{:.1f}".format(num_overs+balls/10))

            print("Wickets: "+str(lives))
            print("Current Runs: "+str(target))
            #user_num=int(input("Enter num bw 1 to 6: "))
            #pygame.time.delay(2)
            pygame.time.delay(2)
            user_num = count
            computer_num=random.choice([1,2,3,4,5,6])
            print("Computer num: "+str(computer_num))

            if(user_num==computer_num):
                    lives=lives-1
                    print("Out!Wicket lost")
                    pygame.time.delay(2)
                    if(lives<=0):
                        print("Innings Complete!")
                        pygame.time.delay(2)
                        return target
            else:
                target+=user_num

            balls=balls+1
        num_overs+=1
    return target


def user_bowls_first(lives,overs):
    pygame.event.get()
    num_overs=0
    global count
    target=0
    while(num_overs<overs):
        balls=1
        while(balls<=6):
            print("{:.1f}".format(num_overs+balls/10))
            print("Wickets: "+str(lives))
            print("Current Runs: "+str(target))
            #user_num=int(input("Enter num bw 1 to 6: "))
            pygame.time.delay(2)
            user_num=count
            #user_num = count
            computer_num=random.choice([1,2,3,4,5,6])
            print("Computer num: "+str(computer_num))
            pygame.time.delay(2)

            if(user_num==computer_num):
                lives=lives-1
                print("Out!Wicket lost")
                pygame.time.delay(2)
                if(lives<=0):
                    print("Innings Complete!")
                    pygame.time.delay(2)
                    return target
            else:
                target+=computer_num

            balls+=1
        num_overs+=1
    return target

def user_bats_second(lives,overs,limit):
    num_overs=0
    global count
    target=0
    while(num_overs<overs):
        balls=1
        while(balls<=6):
            print("{:.1f}".format(num_overs+balls/10))
            print("Wickets: "+str(lives))
            print("Current Runs: "+str(target))
            #user_num=int(input("Enter num bw 1 to 6: "))
            pygame.time.delay(2)
            user_num = count
            computer_num=random.choice([1,2,3,4,5,6])
            print("Computer num: "+str(computer_num))

            if(user_num==computer_num):
                    lives=lives-1
                    print("Out!Wicket lost")
                    pygame.time.delay(2)
                    if(lives<=0):
                        print("You lost the match!")
                        print("You lost by "+str(limit-target)+" runs!")
                        pygame.time.delay(2)
                        return 0

            else:
                target+=user_num
            if(target>limit):
                print("You won!")
                print("You won by "+str(lives)+" wickets!")
                pygame.time.delay(2)
                return 1
            balls=balls+1
        num_overs+=1
    print("You lost by "+str(limit-target)+" runs!")
    pygame.time.delay(2)
    return 0

def user_balls_second(lives,overs,limit):
    num_overs=0
    target=0
    while(num_overs<overs):
        balls=1
        while(balls<=6):
            print("{:.1f}".format(num_overs+balls/10))
            print("Wickets: "+str(lives))
            print("Current Runs: "+str(target))
            #user_num=int(input("Enter num bw 1 to 6: "))
            pygame.time.delay(2)
            user_num = count
            computer_num=random.choice([1,2,3,4,5,6])
            print("Computer num: "+str(computer_num))

            if(user_num==computer_num):
                    lives=lives-1
                    print("Out!Wicket lost")
                    pygame.time.delay(2)
                    if(lives<=0):
                        print("You won the match!")
                        print("You won by "+str(limit-target)+" runs!")
                        pygame.time.delay(2)
                        return 1 
            else:
                target+=computer_num
            if(target>limit):
                print("You lost!")
                print("You lost by "+str(lives)+" wickets!")
                pygame.time.delay(2)
                return 0

            balls=balls+1
        num_overs+=1
    print("You won the match!")
    print("You won by "+str(limit-target)+" runs!")
    pygame.time.delay(2)
    return 1

#if __name__ == "__main__":
    #global val
    




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
#game_display = pygame.display.set_mode((1600, 1000), pygame.RESIZABLE)
game_display=pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
pygame.display.update()


def button(x_button, y_button, msg, wid, color1, color2):
    global val
    button_width = wid
    button_height = 100
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
        elif click == (1, 0, 0) and msg == "HEADS":
            val=1
            game_loop()
        elif click == (1,0,0) and msg == "TAILS":
            val=1
            game_loop()
        elif click == (1,0,0) and msg == "BATTING":
            val=4
        elif click == (1,0,0) and msg == "BOWLING":
            val=2
        elif msg=="Let's Start!" and click==(1,0,0):
            val=4


def main_menu():
    global val
    val=0
    game_play = False
    while not game_play:
        game_display.blit(main_menu_bg_img, (0, 0))
        button(0, 0, "PLAY", 270, white, off_white)
        button(0, 150, "QUIT", 270, white, off_white)
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
    global val
    x=0
    while not game_over:
        game_display.blit(game_bg_img, (0, 0))
        button(0, 300, "BACK", 270, white, off_white)
        if(val==0):
            button(0, 450, "HEADS", 300, white, off_white)
            button(0, 600, "TAILS", 300, white, off_white)
        elif(val == 1 or val == 3):
            font = pygame.font.SysFont(None, 100)
            if(val==1):
                x+=random.randint(0,1)
                val=3
            if(x==0):                
                button(300, 450, "BATTING", 350, white, off_white)
                button(300, 600, "BOWLING", 350, white, off_white)
                scor = font.render("Toss won!", True, black)
                game_display.blit(scor, (300, 300))
            else:
                sco = font.render("You lost the toss:(", True, black)
                wut = font.render("You will bat first.", True, black)
                game_display.blit(sco, (300, 300))
                game_display.blit(wut, (300, 400))
                button(300, 600, "Let's Start!", 380, white, off_white)
                #val=4
        elif(val == 2 or val == 4):
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
            lives=3
            overs=2 
            result=0
            if(val==2):
                fot = pygame.font.SysFont(None, 70)
                disp = fot.render("First Innings start!", True, white)
                game_display.blit(disp, (300, 20))
                #print()
                #target=user_bowls_first(lives,overs)
                '''print(str(target)+" runs scored by computer!")
                print(str(target+1)+" runs to win!")
                print("Second Innings start!")
                result=user_bats_second(lives,overs,target)'''
                val=7
            elif(val==4):
                fot = pygame.font.SysFont(None, 70)
                disp = fot.render("First Innings start!", True, white)
                game_display.blit(disp, (300, 20))
                #print("aaya 1")
                #pygame.time.delay(2)
                #print("aaya 2")
                target=user_bats_first(lives,overs)
                #target=0
                disp2 = fot.render("Runs to defend: "+str(target), True, white)
                game_display.blit(disp2, (300, 20))
                #print(str(target)+" runs scored by you!")
                #print(str(target+1)+" runs to protect!")
                '''disp = fot.render("Second Innings start!", True, white)
                game_display.blit(disp, (300, 20))
                result=user_balls_second(lives,overs,target)
                if(result==1):
                    print("Congratulations!")
                else:
                    print("Better luck next time!")'''
            #print("Lesee")
                val=7
            elif val == 7:
                t1.join()
                cap.release()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    our_score += 1

        
        
        clock.tick(120)
        pygame.display.update()


main_menu()
pygame.quit()
quit()
