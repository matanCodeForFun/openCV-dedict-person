import cv2
import numpy as np
import imutils

class CameraApp:

    widt = 500
    higt = 600

    def __init__(self, cam_index=0, width_limit=500):
        # helper cascade detectors
        self.hog = cv2.HOGDescriptor()
        self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        self.face_cascade = cv2.CascadeClassifier(cascade_path)
        self.upperbody_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_upperbody.xml')
        self.fullbody_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

        self.cap = cv2.VideoCapture(cam_index)
        self.width_limit = width_limit

    # funcsan to get x y w and h
    @staticmethod
    def get_x(region):
        return region[0]

    @staticmethod
    def get_y(region):
        return region[1]

    @staticmethod
    def get_w(region):
        return region[2]

    @staticmethod
    def get_h(region):
        return region[3]

    def get_higt():
        return 800
    
    def get_widt():
        return 500

    def run(self):
        if not self.cap.isOpened():
            print("can't open camera")
            return

        print("camera open")
        self._capture_loop()

    def _capture_loop(self):
        """Internal loop that reads frames and processes detections."""
        while True:
            ret, frame = self.cap.read()

            if not ret:
                print("Can't receive frame")
                break

            frame = imutils.resize(frame, width=min(self.width_limit, frame.shape[1]))

            # convert to grayscale for Haar cascades
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # face detection
            faces = self.face_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=5,minSize=(30, 30))
            for region in faces:
                x = self.get_x(region)
                y = self.get_y(region)
                w = self.get_w(region)
                h = self.get_h(region)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # upper and full body
            uppers = self.upperbody_cascade.detectMultiScale(gray,
                                                            scaleFactor=1.1,
                                                            minNeighbors=5)
            for region in uppers:
                x = self.get_x(region)
                y = self.get_y(region)
                w = self.get_w(region)
                h = self.get_h(region)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            fulls = self.fullbody_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=3)
            for region in fulls:
                x = self.get_x(region)
                y = self.get_y(region)
                w = self.get_w(region)
                h = self.get_h(region)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)


            self.width_limit = 500
            self.higth_liate = 800

            frame = cv2.resize(frame, (self.width_limit, self.higth_liate))

            cv2.imshow('Camera feed', frame)

            print("x" + x + "y" + y + "h" + h + "w" + w)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()
