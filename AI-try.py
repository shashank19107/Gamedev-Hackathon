#MEdiaPipe
import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


# For webcam input:
cap = cv2.VideoCapture(0)
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
    image.flags.writeable = False
    results = hands.process(image)
    image_height, image_width, _ = image.shape

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    #Counting fingers visible in the frame

    count =0
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
    image = cv2.putText(image, str(count), (50, 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    cv2.imshow('Hands', image)
    #print(results.multi_hand_landmarks.landmark(10).y, results.multi_hand_landmarks[11].y, results.multi_hand_landmarks[12].y )

    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()