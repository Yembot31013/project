import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands()
screen_width, screen_height = pyautogui.size()

index_y = 0
index_x = 0

while cap.isOpened():
  success, image = cap.read()
  image = cv2.flip(image, 1)
  height, width, _ = image.shape

  if not success:
    print("ignoring empty camera frame ")
    continue

  image.flags.writeable = False
  img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  results = hands.process(img)

  results = results.multi_hand_landmarks

  if results:
    for hand in results:
      mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, mp_drawing_styles.get_default_hand_landmarks_style(), mp_drawing_styles.get_default_hand_connections_style())
      landmarks = hand.landmark
      for id, landmark in enumerate(landmarks):
        x = int(landmark.x*width)
        y = int(landmark.y*height)
        
        if id == 8:
          image = cv2.circle(img = image, center = (x, y), radius = 20, color = (0, 255, 255))
          index_x = screen_width/width*x
          index_y = screen_height/height*y
          pyautogui.moveTo(index_x, index_y)
        if id == 4:
          image = cv2.circle(img = image, center = (x, y), radius = 20, color = (0, 255, 255))
          thumb_x = screen_width/width*x
          thumb_y = screen_height/height*y
          if abs(index_y - thumb_y) < 20:
            print("click")
            pyautogui.click()
            pyautogui.sleep(1)
        if id == 20:
          image = cv2.circle(img = image, center = (x, y), radius = 20, color = (0, 255, 255))
          little_x = screen_width/width*x
          little_y = screen_height/height*y
          print(abs(index_x - little_x))
          if abs(index_x - little_x) < 20:
            print("stop")
            break
        # little finger = 20
        # ring finger = 16
        # long finger = 12
        

  cv2.imshow('virtual mouse', image)
  if cv2.waitKey(1) & 0xFF == 27:
    break

cap.release()




# value = dir(cv2)
# for i in value:
#   if 'read' in i.lower():
#     print(i)