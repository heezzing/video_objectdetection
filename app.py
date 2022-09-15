# 필요한 라이브러리
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import pandas as pd
import sys
import os
import OD_YOLO
import pathlib 
import shutil

# 테스트 링크 https://www.youtube.com/watch?v=Q0Qkqbb_UIU
# 쇼츠 테스트 영상
# https://youtube.com/shorts/1SNWu_hXbbc?feature=share

# 플라스크 실행

app = Flask(__name__)

save_video_path = os.path.dirname(os.path.abspath(__file__))
#비디오 저장위치
video_forder = '/static'
#비디오 이동위치
move_video_path = save_video_path + video_forder


# 페이지 구성

@ app.route('/')  # 기본 페이지
def main_html():
    # print("this is main page")
    return render_template('main.html')
# 파일 업로드 처리


@ app.route('/fileUpload', methods=['POST', 'GET'])
def file_upload_html():
    # 파일을 받았을 경우
    if request.method == 'POST':
        # 데이터 불러오기
        input_link = request.form.get("url")
        #filename 저장
        file_name = 'sample.mp4'
        # filename 으로 동영상 모델 확인
        result_vedio = OD_YOLO.ObjectDetection(input_link, file_name)
        result_vedio.show_frame()
        #result_vedio.save(save_video_path +
        #                  secure_filename(result_vedio.filename))
        # 결과물 이동시키기
        shutil.move(save_video_path + '/' + file_name, move_video_path)
        if os.path.exists(move_video_path + '/' + file_name):
            return render_template('file_upload.html')

        return render_template('file_upload.html', test_message=input_link)

    return render_template('file_upload.html')

# 처리된 영상을 보여준다


@ app.route('/view', methods=['GET', 'POST'])
def view_html():

    return render_template('view.html')  # html을 렌더하며 DB에서 받아온 값들을 넘김


if __name__ == "__main__":
    app.run(debug=True)