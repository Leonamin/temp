import cv2 
import sys
from flask import Flask, render_template, Response
import time
import threading

class Camera:
    thread = None
    frame = None
    last_access = 0

    def initialize(self):
        if Camera.thread is None:
            Camera.thread = threading.Thread(target=self._thread)
            Camera.thread.start()

            while self.frame is None:
                time.sleep(0)

    def get_frame(self):
        Camera.last_access = time.time()
        self.initialize()
        return self.frame

    @classmethod
    def _thread(cls):
        cap = cv2.VideoCapture(0)       
        cap.set(3, 480) 
        cap.set(4, 320)
    
        while cap.isOpened():
            _, frame = cap.read() 

            ret, jpeg = cv2.imencode('.jpg', frame)
            cls.frame = jpeg.tobytes()

            if time.time() - cls.last_access > 10:
                break
        
        cls.thread = None
        cap.release() 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
   while True:
       frame = camera.get_frame()
       yield (b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_stream')
def video_stream():
   return Response(gen(Camera()),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True, threaded=True)