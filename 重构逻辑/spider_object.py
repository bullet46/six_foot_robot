"""
定义一个spider类，用于绘制六足+机器人
"""
import cv2 as cv
import numpy as np
from init import *
from math import *


class Leg(object):
    """
    定义六足机器人腿的相关方法
    """

    def __init__(self, img, root, foot):  # 需要传入一个底图
        self.img = img
        self.root = root
        self.foot = foot
        self.fixed = True  # 初始为固定状态

    def draw(self):
        if self.fixed:  # 固定状态的颜色
            cv.line(self.img, self.root, self.foot, yellow, 4)
            cv.circle(self.img, self.foot, 3, red, -1)
        else:
            cv.line(self.img, self.root, self.foot, green, 4)
            cv.circle(self.img, self.foot, 3, yellow, -1)
        cv.circle(self.img, self.root, 5, orange, -1)  # 腿的根部永远是橘色


class Spider(object):
    def __init__(self, img, position):
        self.position = position
        self.img = img
        self.forward = 90  # 机器人正方向默认为90


def creat_img(color):
    img = np.zeros([400, 400, 3], np.uint8)
    img[:, :, 0] = np.zeros([400, 400]) + color[0]
    img[:, :, 1] = np.zeros([400, 400]) + color[1]
    img[:, :, 2] = np.zeros([400, 400]) + color[2]
    return img


if __name__ == '__main__':
    img = creat_img(grey)
    foot = Leg(img, (200, 200), (300, 300))
    foot.fixed = False
    foot.draw()
    cv.imshow("new image", img)
    cv.waitKey()
