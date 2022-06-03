# ADAS_opencv

### 1. Description & Result ###
ADAS구현을 위해 객체 인식 연습하기

1. 'videoCapture.py'  
블랙박스 영상 가져오기  
: while문 안에 cv2.VideoCapture() 사용해서 30프레임당 하나씩 이미지 추출  
-> frame 폴더에 frame1, frame2,... 이름으로 저장  
<br/>
<img src="https://user-images.githubusercontent.com/105180751/171773260-2b4b3fc0-b639-4654-9b85-b04a32858e6f.JPG" width="625" height="250"/></center>
<br/><br/><br/>

2. 'LaneDetection.py'  
차선 검출 방법 연습1  
: 블랙박스 영상 가져와서  
흑백으로 변환, 평탄화, 이미지 resize, Edge Detection  
-> ROI설정해서 관심 영역만 화면에 출력하기
<br/><br/>
<img src="https://user-images.githubusercontent.com/105180751/171774105-fb195b5e-1b9b-4263-bfca-56faac750745.JPG" width="450" height="300"/></center>
<br/><br/><br/>

3. 'HoughLine.py'  
차선 검출 방법 연습2  
: 블래박스 영상 가져와서  
이미지 resize, 흑백으로 변환, 평탄화 후에
cv2.HoughLinesP()를 이용해서 원본 이미지에 검출된 선 overlap 
-> ROI 영역만 화면에 출력하기
    ##### 그림자 인식, 노이즈 제거, 더 정확한 차선 인식을 하기 위한 업데이트 필요!
    <img src="https://user-images.githubusercontent.com/105180751/171773954-b024117b-d95d-4e4b-80b2-6a5fb9e7223c.JPG" width="450" height="300"/></center>
<br/><br/><br/>

4. 'HoughLineDe.py'  
차선 인식이 가장 어려운 frame을 골라 'frame1'폴더에 저장 (Debug) -> 효율적인 개발 환경 
<br/><br/>
![44](https://user-images.githubusercontent.com/105180751/171839198-578dac78-b5c3-4a74-822a-5173a1ad9064.JPG)
<br/><br/><br/>

5. 'HSV.py'
'HoughLine.py' 에서 그림자 인식, 어두울 때 차선 인식X, 노란 중앙선 인식X 문제를 해결하기 위해 HSV로 변환하여 영상처리 시도.  
cv2.split()으로 H,S,V각각 나눠 다시 확인-> H만 평준화를 통해 다시 한 번 영상 처리.
<br/><br/>

### 2. Information ##
개발 환경: Pycharm  
언어: Python

