import cv2
vidcap = cv2.VideoCapture('C:/Users/CHAEHEE/opencvProj/example2/ch13/yolo_v3/evt0_20220526_180823.MP4')
count = 0
while(vidcap.isOpened()):
   ret, image = vidcap.read()
   if (ret == False):
      break

   if(int(vidcap.get(1))%30 == 0):
      print('save frame number:'+ str(int(vidcap.get(1))))
      cv2.imwrite("C:/Users/CHAEHEE/opencvProj/example2/ch13/yolo_v3/frame/frame%d.png" % count, image)
      count += 1
vidcap.release()
