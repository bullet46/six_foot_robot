import cv2
from Cilent.Spider.Config import *

if __name__ == '__main__':
    while True:
        src = f'http://{link_ip}:8080/?action=snapshot'
        cap = cv2.VideoCapture(src)
        ok, frame = cap.read()
        print(ok)
        if ok:
            cv2.imshow('frame', frame)
        cv2.waitKey(int(1 / 50 * 1000))
