from cv2 import cv2 
import mediapipe as mp
import re

from gesture_classification import GestureClassification


class MediaPipe():

  #def __init__(self)


  def initialize_mediapipe(self):
    mp_hands = mp.solutions.hands

    #remove for jetson
    mp_drawing = mp.solutions.drawing_utils

    # For webcam input:
    hands = mp_hands.Hands(
        min_detection_confidence=0.5, min_tracking_confidence=0.5)
    cap = cv2.VideoCapture(0)
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

      # Draw the hand annotations on the image.
      image.flags.writeable = True
      image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

      if results.multi_hand_landmarks:
        #self.generate_landmarks(results.multi_hand_landmarks)
        classify = GestureClassification()
        for hand_landmarks in results.multi_hand_landmarks:
          landmarks = []
          for x in hand_landmarks.landmark:        
            landmarks.append(re.findall(r'-?0.\d+', str(x)))

        #remove for jetson
        mp_drawing.draw_landmarks(
          image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        classify.classify_gesture(landmarks)
          
      cv2.imshow('MediaPipe Hands', image)
      if cv2.waitKey(5) & 0xFF == 27:
        break
    hands.close()
    cap.release()
