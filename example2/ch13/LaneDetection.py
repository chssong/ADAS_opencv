import cv2
import numpy as np

def region_of_interest(img, vertices, color3=(255, 255, 255), color1=255):  # ROI 셋팅

   mask = np.zeros_like(img)  # mask = img와 같은 크기의 빈 이미지

   if len(img.shape) > 2:  # Color 이미지(3채널)라면 :
      color = color3
   else:  # 흑백 이미지(1채널)라면 :
      color = color1

   # vertices에 정한 점들로 이뤄진 다각형부분(ROI 설정부분)을 color로 채움
   cv2.fillPoly(mask, vertices, color)

   # 이미지와 color로 채워진 ROI를 합침
   ROI_image = cv2.bitwise_and(img, mask)
   return ROI_image

def mark_img(img, blue_threshold=200, green_threshold=200, red_threshold=200):  # 흰색 차선 찾기

   #  BGR 제한 값
   bgr_threshold = [blue_threshold, green_threshold, red_threshold]

   # BGR 제한 값보다 작으면 검은색으로
   thresholds = (image[:, :, 0] < bgr_threshold[0]) \
                | (image[:, :, 1] < bgr_threshold[1]) \
                | (image[:, :, 2] < bgr_threshold[2])
   mark[thresholds] = [0, 0, 0]
   return mark


cap= cv2.VideoCapture('C:/Users/CHAEHEE/opencvProj/example2/ch13/yolo_v3/result.avi') # 이미지 읽기

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size =', frame_size)

while(True):
   retval, src = cap.read()
   if not retval:
      break

   # 1. 흑백 동영상으로 변환
   gray_frame = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

   # 2. 평탄화
   dst = cv2.equalizeHist(gray_frame)

   # 3. resize
   image = cv2.resize(dst,(int(frame_size[0]/2),int(frame_size[1]/2)))
   #image = cv2.resize(src, (960, 480))

   # 4. canny
   dst1 = cv2.Canny(image, 50, 200)

   # ROI 설정
   # 사다리꼴 모형의 Points
   vertices = np.array([[(447,364),(305,484), (680,484), (524, 364)]], dtype=np.int32)
   roi_img = region_of_interest(dst1, vertices) # vertices에 정한 점들 기준으로 ROI 이미지 생성

   mark = np.copy(roi_img) # roi_img 복사

   # 화면에 출력
   #cv2.imshow('image', image)
   #cv2.imshow('dst', dst)
   #cv2.imshow('dst1', dst1)
   cv2.imshow('roi_mask',mark) # 흰색 차선 추출 결과 출력
   # cv2.imshow('result',image) # 이미지 출력

   cv2.waitKey(25)
