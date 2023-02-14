import cv2
import mediapipe as mp
# import pyautogui

cap = cv2.VideoCapture(0)
mp_faces = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
faces = mp_faces.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

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

  results = results.multi_face_landmarks
  
  if results:
    for face_landmarks in results:
      mp_drawing.draw_landmarks(
        image=image, 
        landmark_list = face_landmarks, 
        connections = mp_faces.FACEMESH_TESSELATION, 
        landmark_drawing_spec = None, 
        connection_drawing_spec = mp_drawing_styles.get_default_face_mesh_tesselation_style()
      )

      # mp_drawing.draw_landmarks(
      #   image=image, 
      #   landmark_list = face_landmarks, 
      #   connections = mp_faces.FACEMESH_CONTOURS, 
      #   landmark_drawing_spec = None, 
      #   connection_drawing_spec = mp_drawing_styles.get_default_face_mesh_contours_style()
      # )

      # mp_drawing.draw_landmarks(
      #   image=image, 
      #   landmark_list = face_landmarks, 
      #   connections = mp_faces.FACEMESH_IRISES, 
      #   landmark_drawing_spec = None, 
      #   connection_drawing_spec = mp_drawing_styles.get_default_face_mesh_iris_connections_style()
      # )      

  cv2.imshow('detect face', image)
  if cv2.waitKey(1) & 0xFF == 27:
    break

cap.release()
