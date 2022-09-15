import torch
import sys
import cv2
import pafy
from time import time
import numpy as np

# 영상 처리 클래스


class ObjectDetection:
    # YouTube 동영상에 YOLOv5 구현

    def __init__(self, url, out_file):
        # 객체 생성 시 호출
        # url: 예측 대상 YouTube URL
        # out_file: 유효한 출력 파일 이름 *.avi
        self._URL = url
        self.model = self.load_model()
        self.classes = self.model.names
        self.out_file = out_file
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'

    def get_video_from_url(self):
        # url에서 새 비디오 스트리밍 객체 생성
        print(pafy.new(self._URL))
        play = pafy.new(self._URL).streams[-1]

        assert play is not None
        return cv2.VideoCapture(play.url)

    def load_model(self):
        # YOLOv5 모델 로드
        model = torch.hub.load('ultralytics/yolov5',
                               'yolov5s', pretrained=True)
        model.classes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12]
        return model

    def score_frame(self, frame):
        # frame: 단일 프레임; numpy/list/tuple 형식
        # return: 프레임에서 모델이 감지한 객체의 레이블과 좌표
        self.model.to(self.device)
        frame = [frame]
        results = self.model(frame)
        labels, cord = results.xyxyn[0][:, -
                                        1].cpu().numpy(), results.xyxyn[0][:, :-1].cpu().numpy()
        return labels, cord

    def class_to_label(self, x):
        # x 숫자 레이블 -> 문자열 레이블로 반환
        return self.classes[int(x)]

    def plot_boxes(self, results, frame):
        # 경계상자와 레이블을 프레임에 플로팅
        # results: 프레임에서 모델이 감지한 객체의 레이블과 좌표
        # frame: 점수화된 프레임
        # return: 경계 상자와 레이블이 플로팅된 프레임
        labels, cord = results
        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0] # 프레임 크기
        for i in range(n): # 객체 수만큼 반복
            row = cord[i] # 좌표
            if row[4] >= 0.5: # 점수 확률이 0.2 이상인 경우
                x1, y1, x2, y2 = int(
                    row[0]*x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape)
                bgr = (0, 255, 0) # 색상
                if self.class_to_label(labels[i]) == 'person':
                    bgr = (0, 0, 255)
                if self.class_to_label(labels[i]) == 'car':
                    bgr = (255, 0, 0)
                if self.class_to_label(labels[i]) == 'bus':
                    bgr = (0, 255, 255)
                if self.class_to_label(labels[i]) == 'truck':
                    bgr = (255, 255, 0)
                if self.class_to_label(labels[i]) == 'traffic light':
                    bgr = (255, 0, 255)
                cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                cv2.putText(frame, self.class_to_label(labels[i])
                            + ':' + str(round(row[4], 2)),
                            (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)
        return frame

    def show_frame(self):
        # 인스턴스 생성 시 호출; 프레임 단위로 비디오 로드
        player = self.get_video_from_url()
        print(player)
        assert player.isOpened()
        x_shape = int(player.get(cv2.CAP_PROP_FRAME_WIDTH))
        y_shape = int(player.get(cv2.CAP_PROP_FRAME_HEIGHT))
        four_cc = cv2.VideoWriter_fourcc(*"H264")
        out = cv2.VideoWriter(self.out_file, four_cc, 20, (x_shape, y_shape))
        #코덱 H264, 20fps, 크기는 x_shape, y_shape
        assert out.isOpened()
        while player.isOpened(): # 비디오 스트리밍 시작
            ret, frame = player.read() # 프레임 로드
            if ret:
                frame = self.plot_boxes(self.score_frame(frame), frame) # 경계상자와 레이블 플로팅
                out.write(frame) # 프레임 저장
                cv2.imshow('Real-time image processing', frame) # 프레임 출력
                if cv2.waitKey(1) & 0xFF == ord('q'): # q를 누르면 종료
                    break
            else:
                break

        while True:
            start_time = time() # 시작 시간
            ret, frame = player.read() # 프레임 로드
            if not ret: # 비디오 끝나면 종료
                break
            results = self.score_frame(frame) # 경계상자와 레이블 플로팅
            frame = self.plot_boxes(results, frame) # 경계상자와 레이블 플로팅
            end_time = time() # 종료 시간
            fps = 1/np.round(end_time - start_time, 3) # 프레임 속도
            print(f"Frames Per Second : {fps}") # 프레임 속도 출력
            out.write(frame) # 프레임 저장