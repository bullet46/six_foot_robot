import math
import cv2 as cv
import numpy as np
from framework import data_


def trans(coordinates):
    return (512 + coordinates[0], 512 + coordinates[1])


def trans_to_radian(angle):  # 将角度制改为弧度
    return math.radians(int(angle))


def circle(center, r):
    img = np.zeros((1024, 1024, 3), np.uint8)
    cv.circle(img, center, r, (255, 255, 255), 1)
    n = 200
    position = input("输入原点位置:")
    angle = int(input("输入角度"))
    print(angle)
    cv.line(img, trans([0, -512]), trans([0, 512]), (255, 255, 255), 1)
    cv.line(img, trans([-512, 0]), trans([512, 0]), (255, 255, 255), 1)
    r = int(-n * math.sin(trans_to_radian(angle)) / (math.sin(trans_to_radian(angle)) - 1))
    for i in range(-90, 90):
        try:
            if i < 0:
                r = int(-n * math.sin(trans_to_radian(-i)) / (math.sin(trans_to_radian(-i)) - 1))
                cv.circle(img, trans([-r, 0]), r, (255, 255, 0), 1)
            else:
                r = int(-n * math.sin(trans_to_radian(i)) / (math.sin(trans_to_radian(i)) - 1))
                cv.circle(img, trans([r, 0]), r, (255, 255, 0), 1)
        except(ZeroDivisionError):
            cv.line(img, trans([0, -512]), trans([0, 512]), (255, 255, 0), 1)
        print(i,r)
        cv.imshow("1", img)
        cv.waitKey()


circle((512, 512), 50)
