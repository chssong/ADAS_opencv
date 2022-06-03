# ADAS_opencv

### 1. Description & Result ###
ADAS구현을 위해 객체 인식 연습하기

1. 'videoCapture.py'  
블랙박스 영상 가져오기  
: while문 안에 cv2.VideoCapture() 사용해서 30프레임당 하나씩 이미지 추출  
-> frame 폴더에 frame1, frame2,... 이름으로 저장

![1](https://user-images.githubusercontent.com/105180751/171773260-2b4b3fc0-b639-4654-9b85-b04a32858e6f.JPG)

2. 'LaneDetection.py'  
차선 검출 방법 연습1  
: 블랙박스 영상 가져와서  
흑백으로 변환, 평탄화, 이미지 resize, Edge Detection  
-> ROI설정해서 관심 영역만 화면에 출력하기

3. 'HoughLine.py'  
차선 검출 방법 연습2  
: 블래박스 영상 가져와서  
이미지 resize, 흑백으로 변환, 평탄화 후에
cv2.HoughLinesP()를 이용해서 원본 이미지에 검출된 선 overlap 
-> ROI 영역만 화면에 출력하기

### 2. Information ##
개발 환경: Pycharm  
언어: Python

