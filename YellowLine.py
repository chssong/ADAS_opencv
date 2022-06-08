import sys
import numpy as np
import cv2
import os

def onChange(x):
    pass

def setting_bar():
    cv2.namedWindow('HSV_settings')

    cv2.createTrackbar('H_MAX', 'HSV_settings', 0, 255, onChange)
    cv2.setTrackbarPos('H_MAX', 'HSV_settings', 255)
    cv2.createTrackbar('H_MIN', 'HSV_settings', 0, 255, onChange)
    cv2.setTrackbarPos('H_MIN', 'HSV_settings', 0)
    cv2.createTrackbar('S_MAX', 'HSV_settings', 0, 255, onChange)
    cv2.setTrackbarPos('S_MAX', 'HSV_settings', 255)
    cv2.createTrackbar('S_MIN', 'HSV_settings', 0, 255, onChange)
    cv2.setTrackbarPos('S_MIN', 'HSV_settings', 0)
    cv2.createTrackbar('V_MAX', 'HSV_settings', 0, 255, onChange)
    cv2.setTrackbarPos('V_MAX', 'HSV_settings', 255)
    cv2.createTrackbar('V_MIN', 'HSV_settings', 0, 255, onChange)
    cv2.setTrackbarPos('V_MIN', 'HSV_settings', 0)

setting_bar()

edgeImageDir = 'C:/Users/CHAEHEE/opencvProj/example2/ch13/yolo_v3/frame1/'
edgeList = os.listdir(edgeImageDir)

# 노란 차선 검출하기
# trackbar 숫자: 48 18 255 94 255 140

while(1):
    for image in edgeList:
        src = cv2.imread(os.path.join(edgeImageDir, image))

        if src is None:
            print('Image load failed!')
            sys.exit()

        src2 = cv2.resize(src,(640,480))
        src_hsv = cv2.cvtColor(src2, cv2.COLOR_BGR2HSV)

        while (1):
            cv2.imshow('original', src2)

            if cv2.waitKey(1) == 27:
                break

            H_MAX = cv2.getTrackbarPos('H_MAX', 'HSV_settings')
            H_MIN = cv2.getTrackbarPos('H_MIN', 'HSV_settings')
            S_MAX = cv2.getTrackbarPos('S_MAX', 'HSV_settings')
            S_MIN = cv2.getTrackbarPos('S_MIN', 'HSV_settings')
            V_MAX = cv2.getTrackbarPos('V_MAX', 'HSV_settings')
            V_MIN = cv2.getTrackbarPos('V_MIN', 'HSV_settings')
            lower = np.array([H_MIN, S_MIN, V_MIN])
            higher = np.array([H_MAX, S_MAX, V_MAX])
            hsv = cv2.cvtColor(src2, cv2.COLOR_BGR2HSV)
            Gmask = cv2.inRange(hsv, lower, higher)
            G = cv2.bitwise_and(src2, src2, mask=Gmask)

            cv2.imshow('G', G)

            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break

