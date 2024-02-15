import cv2
import matplotlib.pyplot as plt
import mediapipe as mp

#access mediapipe functions
mp_pose=mp.solutions.pose
pose=mp_pose.Pose()
mp_drawings=mp.solutions.drawing_utils

cap=cv2.VideoCapture('Mr. Bean and the art of seduction..mp4')

while True:
    success,frame=cap.read()
    frame=cv2.resize(frame,(500,500))

    results=pose.process(frame)
    if results.pose_landmarks:
     mp_drawings.draw_landmarks(frame,results.pose_landmarks,mp_pose.POSE_CONNECTIONS)

    cv2.imshow('video capture',frame)
    if cv2.waitKey(1) & 0XFF==27:
        break
cap.release()
cv2.destroyAllWindows()