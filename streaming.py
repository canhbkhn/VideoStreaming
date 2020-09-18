from flask import Flask, render_template, Response, request, redirect, url_for
import cv2
import time

from testlog import Logger

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
def logger():
    print("test logger")
def gen():
    cap = cv2.VideoCapture(0)
    count = 0
    while True:
        ret, frame = cap.read()
        fps = cap.get(cv2.CAP_PROP_FPS)
        # fps = count/(time.time() - _time_)
        # print("FPS: {0}".format(fps))
        log = Logger('config.json')
        log.WriteLog(1, fps)

        font = font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,  
                'FPS: '+ str(fps),  
                (50, 50),  
                font, 1,  
                (0, 255, 255),  
                2,  
                cv2.LINE_4)

        if not ret:
            print("Error: failed to capture image")
            break

        cv2.imwrite('demo.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('demo.jpg', 'rb').read() + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/log')
def log():
    return Response(logger())
if __name__ == '__main__':
    app.run(debug=True)
