# -*- coding: cp949 -*-
# -*- coding: utf-8 -*-
import cv2  # opencv ���
import numpy as np


def grayscale(img):  # ����̹����� ��ȯ
   return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


def gaussian_blur(img, kernel_size):  # Gaussian ����
   return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)


def region_of_interest(img, vertices, color3=(255, 255, 255), color1=255):  # ROI ����

   mask = np.zeros_like(img)  # mask = img�� ���� ũ���� �� �̹���

   if len(img.shape) > 2:  # Color �̹���(3ä��)��� :
      color = color3
   else:  # ��� �̹���(1ä��)��� :
      color = color1

   # vertices�� ���� ����� �̷��� �ٰ����κ�(ROI �����κ�)�� color�� ä��
   cv2.fillPoly(mask, vertices, color)

   # �̹����� color�� ä���� ROI�� ��ħ
   ROI_image = cv2.bitwise_and(img, mask)
   return ROI_image


def draw_lines(img, lines, color=[0, 0, 255], thickness=2):  # �� �׸���
   print('debug:{}'.format(lines))
   if lines is None:
      print('No Lines')
   else:
      for line in lines:
         for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)



def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):  # ���� ��ȯ
   lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len,
                           maxLineGap=max_line_gap)
   line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
   draw_lines(line_img, lines)

   return line_img


def weighted_img(img, initial_img, ��=1, ��=1., ��=0.):  # �� �̹��� overlap �ϱ�
   return cv2.addWeighted(initial_img, ��, img, ��, ��)


cap= cv2.VideoCapture('C:/Users/CHAEHEE/opencvProj/example2/ch13/yolo_v3/result.avi') # ���� �б�
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size =', frame_size)

while(True):

   retval, src = cap.read()

   if not retval:
      break

   # �̹��� resize
   image = cv2.resize(src, (int(frame_size[0] / 2), int(frame_size[1] / 2)))

   height, width = image.shape[:2]  # �̹��� ����, �ʺ�
   print(image.shape)
   gray_img = grayscale(image)  # ����̹����� ��ȯ

   #blur_img = gaussian_blur(gray_img, 3)  # Blur ȿ��
   equal_img = cv2.equalizeHist(gray_img) #��źȭ ���� ����
   canny_img=cv2.Canny(equal_img, 5000, 1500, apertureSize = 5, L2gradient = True)

   vertices = np.array(
      [[(133, height-70), (width/2-10, height/2+120), (width/2+10, height/2+120), (width-133, height-70)]],
      dtype=np.int32)
   ROI_img = region_of_interest(canny_img, vertices)  # ROI ����

   hough_img = hough_lines(ROI_img, 1, 1 * np.pi / 180, 30, 10, 20)  # ���� ��ȯ

   result = weighted_img(hough_img, image)  # ���� �̹����� ����� �� overlap
   # cv2.imshow('gray_show', gray_img)
   #cv2.imshow('canny', canny_img)
   cv2.imshow('roi_mask', ROI_img)
   cv2.imshow('result', result)  # ��� �̹��� ���
   cv2.waitKey(20)
