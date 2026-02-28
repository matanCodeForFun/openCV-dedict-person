import cv2
import numpy as np
import imutils

def camera():
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("can't open camera")
        return

    print("camera open")

    while True:
        ret, frame = cap.read()

        frame = imutils.resize(frame, width=min(500, frame.shape[1]))

        if not ret:
            print("Can't receive frame")
            break

        cv2.imshow('Camera feed', frame)

        (regions, _) = hog.detectMultiScale(frame, winStride=(8, 8), padding=(4, 4), scale=1.05)

        for (x, y, w, h) in regions:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    camra()
