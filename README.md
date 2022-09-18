<img width="700" alt="스크린샷 2022-09-15 오후 12 59 35" src="https://user-images.githubusercontent.com/97447841/190310860-9f67ee33-5520-432a-8ede-9629c1e2529d.png">

Date : 2022.6.24~2022.7.6

Tags : `Yolov5`  `OpenCV`  `Flask` 

Link : [https://github.com/heezzing/project5.git](https://github.com/heezzing/project5.git)

발표영상 : [https://youtu.be/b7fFukYAhTo](https://youtu.be/b7fFukYAhTo)

시연영상 : [https://www.youtube.com/watch?v=V6yrb4vcQos](https://www.youtube.com/watch?v=O_KM5aAAW5w)

## 개요
- 주제 : 차종별 object detection
- 데이터 출처  :  YouTube ( 자율주행 객체 탐지 모델을 테스트 하기위한 테스트 영상 )
    
    [[도로주행영상]신구대학교 가는길](https://www.youtube.com/watch?v=Q0Qkqbb_UIU)
    
- 기여 내용 : 자동차,사람**, 신호등인식 등을 구현하여 OPENCV와 YOLOV5를 기반으로 자율주행 영상처리 웹 서비스를 구현한다.**
- 기술 스텍
    - YOLOv5 : 객체인식을 하기 위해 사용한 모델
    - OpenCV : 영상처리를 하기 위해 사용한 모델
    - FLASK : 웹 기반 딥러닝 서비스 구현
    
## 프로젝트 내용
### 목차
<img width="700" alt="스크린샷 2022-09-15 오후 1 01 05" src="https://user-images.githubusercontent.com/97447841/190311058-6721075a-4f86-4942-8cb6-8e00427be622.png">

------

### 주제 및 주제 선정 이유
<img width="700" alt="스크린샷 2022-09-15 오후 1 14 27" src="https://user-images.githubusercontent.com/97447841/190312714-8db34f69-e441-45f0-b986-4cfc96125f78.png">

- 주제 : Yolov5 및 Opencv를 활용하여 객체인식 영상처리 딥러닝 웹 서비스 개발하는 것.
- 주제 선정 이유 : Object Detection 기술에 대한 이해력 상승을 위해 선정하였습니다.
- 프로젝트 개요 : 누구 쉽게 객체탐지를 접하게 하기 위해 구현해 보았습니다.

------

### 팀 구성 및 역할
<img width="700" alt="스크린샷 2022-09-15 오후 1 15 20" src="https://user-images.githubusercontent.com/97447841/190312880-b2816450-69fc-493d-8c57-a2c8fb6fc8d3.png">

- 저희조는 총 4명의 팀원으로 구성되었습니다.
- 역할을 나누지 않고  프로젝트를 단계별로 나누어 필요한 기술을 공부한 후 함께 결과물을 도출하는 방법으로 협업을 진행하였습니다.

-----

### 프로젝트 수행 절차
<img width="700" alt="스크린샷 2022-09-15 오후 1 15 57" src="https://user-images.githubusercontent.com/97447841/190312951-b9b6d33a-3ada-451d-bea7-dc6c8610a631.png">

- 첫날 주제 선정 완료 하였습니다.
- 프로젝트에 필요한 기술인 yolo,opencv에 대해 공부하였습니다.
- 공부한 내용을 바탕으로 참고자료를 찾아 yolov5,opencv를 이용하여 객체탐지 모델을 만들었습니다.
- flask를 이용하여 웹페이지를 제작하였습니다.
- 중간점검에서 받은 피드백을 반영하여 모델을 완성하였습니다.
- 마지막으로 발표자료를 만들고 영상을 촬용하였습니다.

------

### 데이터 파이프라인
<img width="700" alt="스크린샷 2022-09-15 오후 1 16 36" src="https://user-images.githubusercontent.com/97447841/190313033-d94a87aa-4b66-4e47-ac2f-3d772df0637d.png">

1. Yolov5 
    - yolov5를 이용하여 객체를 탐지합니다.
    - one stage detection방법을 고안해서 실시간으로 object detection이 가능하여 선택하였습니다.
    - 후보영역을 추출하기 위해 별도의 네트워크를 적용하지 않아서  빠릅니다.
2. OpenCV
    - Opencv를 이용하여 객체를 추정하고 예측합니다.
    - 영상처리에 사용할 수 있는 오픈소스 라이브러리입니다.
3. Youtube 
    - 객체 탐지 모델 테스트할 영상을 제공합니다.
4. Flask
    - Flask를 이용하여 만든 웹페이지에 유튜브 영상 링크를 입력합니다.
    - 해당 영상의 객체인식을 진행합니다.
    - 동작이 완료되면 웹페이지에서 영상 재생이 가능합니다.

------

### YoloV5를 선택한 이유
<img width="700" alt="스크린샷 2022-09-15 오후 1 17 23" src="https://user-images.githubusercontent.com/97447841/190313156-01b9c08a-8d74-47bf-b45b-7d23cc7d6bdd.png">

→ Yolov5를 선택한 이유는  one stage detector의 연산속도가 빠르고 coco_dataset 으로 사전학습이 되어있어 편리하고 간단하여 선택하였습니다.

- RCNN
    - 이미지 전체를 보는것이 아니라 부분을 봅니다.
    - 딥러닝 회귀를 적용하여 다수의 개체 인식 및 객체의 위치 검출의 한계를 설정하여 해결합니다.
    - 후보영역을 생성하고 영역을 탐지 한 뒤 선형 Svm을 이용해 후보영역 내의 개체를 분류합니다.
    - 물체를 식별하는 Classification 문제와, 물체의 위치를 찾는 Localization문제를 순차적으로 행하는 ‘two_stage_detector’입니다.
    - RCNN 객체 탐지 순서  :  후보영역 생성 → CNN학습 → 후보영역 내의 객체 검출
    - CNN학습 :
        - 이미지 특징을 추출한 뒤 이미지 데이터를 배열 형태로 만든다.
        - Flatten한 배열에서 클래스를 분류하고 찾아진 특징을 가지고 class를 고르는것
- Yolov5
    - 이미지 전체를 한 번 보는걸로 객체 탐지가 가능합니다.( 실시간 객체탐지)
    - 후보 영역을 추출하기 위해 별도의 네트워크를 적용하지 않아도 되어서 RCNN 보다 빠릅니다.
    - 이미지를 그리드셀로 나누고 그리드셀 별로 b개의 바운딩 박스를 예측합니다.
    - 물체를 식별하는 Classification 문제와, 물체의 위치를 찾는 Localization 문제를 동시에 행하는 ‘One_stage_detector’입니다.
    - Yolov5 객체 탐지 순서 :  이미지 분할 → 특징 추출 → 예측 탠서 생성 → bounding box 조정 및 분류

------

### OpenCV
<img width="700" alt="스크린샷 2022-09-15 오후 1 18 08" src="https://user-images.githubusercontent.com/97447841/190313299-80b02dfd-e373-4c7e-ab61-7f1321a1bd4a.png">

- OpenCV
    - 영상처리에 사용할 수 있는 오픈 소스 라이브러리입니다.
    - 컴퓨터가 사물을 인식 할 수 있게 도와줍니다.
    - 카메라로 찍어서 할 수 있는 모든 일은 opencv로 처리할 수 있습니다.
    - opencv에는 sort알고리즘이 있는데 영상처리에서 많이 사용되는 알고리즘입니다.
    - 미래 프레임에 대한 정보 없이 과거와 현재 프레임의 객체 탐지 정보만을 사용하여 연관 관계에 대한 Tracking을 수행하는 방식입니다.
- SORT 알고리즘의 흐름
    - Yolov5를 이용하여 프레임에서 개체를 탐지합니다.
    - Kalman filter를 이용하여 개체를 추적하기 위한 측정치를 예측하고 업데이트하는 과정을 진행합니다.
    - IOU 유사도를 구현한 후 추적되고 있던 개체와 아닌 개체를 분류합니다.
        - 추적되지 않는 데이터는 사라진 개체와 새로 등장한 개체입니다.
    - 추적중인 개체는 kalman filter를 통해 다음 개체 추적하기 위한 측정치를 업데이트 합니다.
    - 이전 box 정보로 현재의 noise가 없는 새로운 box를 생성하기 위하여 위 과정을 반복하며 정보를 업데이트하고 최종 정보인 box를 그려줍니다.

-------

### 시연 동영상
- youtube link : [https://www.youtube.com/watch?v=V6yrb4vcQos](https://www.youtube.com/watch?v=O_KM5aAAW5w)
- 순서
    - 웹 페이지를 실행시킵니다.
    - 객체탐지를 원하는 Youtube 링크를 입력합니다.
    - 영상이 객체탐지가 되는것을 실시간으로 보여줍니다.
    - 객체탐지가 끝나면 웹페이지에서 재생이 가능합니다.
    - mAP가 0.5 이상인 개체만 잡도록 하였고 바운딩 박스 위엔 정확도가 뜨게 하였습니다.
    - 각 객체별로 바운딩 박스 색을 분류하였습니다.
 
------

### 마무리
<img width="700" alt="스크린샷 2022-09-15 오후 1 24 10" src="https://user-images.githubusercontent.com/97447841/190314012-81b63118-bed6-48ee-bd0b-27acf4c2f363.png">

- 아쉬운점 
    - 다른 모델과 (Fast_RCNN,CNN) 성능을 비교하지 못한 것
    - 배포 등 일부 목표를 달성하지 못한 것
- 발전 방향
    - Heroku를 이용한 웹서비스 배포입니다.
- 프로젝트를 하면서 좋았던 점  
    - 일정 지연없이 초기 기획 방향대로 성공한 것
    - 역할 분담없이 단계별로 함께 협업하며 진행했던 부분
    - 능동적인 참여가 가능해서 좋은 팀워크가 나온것 같습니다.
