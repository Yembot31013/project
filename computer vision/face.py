import cv2
import mediapipe as mp
# import pyautogui

cap = cv2.VideoCapture(0)
mp_faces = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

faces = mp_faces.FaceDetection()
# screen_width, screen_height = pyautogui.size()

# index_y = 0
# index_x = 0

while cap.isOpened():
  success, image = cap.read()
  # image = cv2.flip(image, 1)
  # height, width, _ = image.shape

  if not success:
    print("ignoring empty camera frame ")
    continue

  image.flags.writeable = False
  img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  results = faces.process(img)

  results = results.detections
  
  if results:
    for face in results:
      mp_drawing.draw_detection(image, face)

        

  cv2.imshow('detect face', image)
  if cv2.waitKey(1) & 0xFF == 27:
    break

cap.release()
