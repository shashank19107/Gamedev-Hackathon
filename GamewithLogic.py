 
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


def cameraInput():
    with mp_hands.Hands(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:    
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue

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

                    #print(hand_landmarks.x)
                    # print('hand_landmarks:', hand_landmarks)
                    # print(type(hand_landmarks))
                    # print(hand_landmarks.landmark[0].x)
                    # print(
                    #     f'Index finger tip coordinates: (',
                    #     f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
                    #     f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'
                    # )
                    mp_drawing.draw_landmarks(
                        image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            #print(count)   
            #count =0 
            image = cv2.putText(image, str(count), (50, 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            cv2.imshow('Hands', image)
            #print(results.multi_hand_landmarks.landmark(10).y, results.multi_hand_landmarks[11].y, results.multi_hand_landmarks[12].y )
            if cameradone or (cv2.waitKey(5) & 0xFF == 27):
                break

t1 = threading.Thread(target=cameraInput, name='t1')
t1.start()

def user_bats_first(lives,overs):
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
            time.sleep(2)
            user_num = count
            computer_num=random.choice([1,2,3,4,5,6])
            print("Computer num: "+str(computer_num))

            if(user_num==computer_num):
                    lives=lives-1
                    print("Out!Wicket lost")
                    time.sleep(1)
                    if(lives<=0):
                        print("Innings Complete!")
                        time.sleep(2)
                        return target
            else:
                target+=user_num

            balls=balls+1
        num_overs+=1
    return target


def user_bowls_first(lives,overs):

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
            time.sleep(2)
            user_num=count
            #user_num = count
            computer_num=random.choice([1,2,3,4,5,6])
            print("Computer num: "+str(computer_num))
            time.sleep(1)

            if(user_num==computer_num):
                lives=lives-1
                print("Out!Wicket lost")
                time.sleep(1)
                if(lives<=0):
                    print("Innings Complete!")
                    time.sleep(2)
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
            time.sleep(2)
            user_num = count
            computer_num=random.choice([1,2,3,4,5,6])
            print("Computer num: "+str(computer_num))

            if(user_num==computer_num):
                    lives=lives-1
                    print("Out!Wicket lost")
                    time.sleep(1)
                    if(lives<=0):
                        print("You lost the match!")
                        print("You lost by "+str(limit-target)+" runs!")
                        time.sleep(2)
                        return 0

            else:
                target+=user_num
            if(target>limit):
                print("You won!")
                print("You won by "+str(lives)+" wickets!")
                time.sleep(2)
                return 1

            balls=balls+1
        num_overs+=1
    print("You lost by "+str(limit-target)+" runs!")
    time.sleep(2)
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
            time.sleep(2)
            user_num = count
            computer_num=random.choice([1,2,3,4,5,6])
            print("Computer num: "+str(computer_num))

            if(user_num==computer_num):
                    lives=lives-1
                    print("Out!Wicket lost")
                    time.sleep(1)
                    if(lives<=0):
                        print("You won the match!")
                        print("You won by "+str(limit-target)+" runs!")
                        time.sleep(2)
                        return 1 
            else:
                target+=computer_num
            if(target>limit):
                print("You lost!")
                print("You lost by "+str(lives)+" wickets!")
                time.sleep(2)
                return 0

            balls=balls+1
        num_overs+=1
    print("You won the match!")
    print("You won by "+str(limit-target)+" runs!")
    time.sleep(2)
    return 1



if __name__ == "__main__":


	lives=3
	overs=2 #int(input(('Enter overs: ')))
	#print("Hello")

	#toss
	print("Toss")
	toss_choice=int(input("Enter 0 or 1: "))
	result=random.choice([0,1])
	choice=0
	if(toss_choice!=result):
		print("You lost the toss!")
		choice=random.choice([0,1]) #0-bat first,1-ball first
		if(choice==0):
			print("Computer chose to bat first")
		else:
			print("Computer chose to ball first")

	else:
		print("You won the toss!")
		print("Choices : 0)Ball first 1)Bat first")
		choice=int(input("Enter 0 or 1: ")) #0-ball first,1-bat first
	#declaration
	if(choice==0):
		print("You are balling first!")
	else:
		print("You are batting first!")

	#simulation
	result=0

	if(choice==0):
		print("First Innings start!")
		target=user_bowls_first(lives,overs)
		print(str(target)+" runs scored by computer!")
		print(str(target+1)+" runs to win!")
		print("Second Innings start!")
		result=user_bats_second(lives,overs,target)
	else:
		print("First Innings start!")
		target=user_bats_first(lives,overs)
		print(str(target)+" runs scored by you!")
		print(str(target+1)+" runs to protect!")
		print("Second Innings start!")
		result=user_balls_second(lives,overs,target)
	if(result==1):
			print("Congratulations!")
	else:
			print("Better luck next time!")
cameradone = True
t1.join()
cap.release()


























