"""
定义一个spider类，用于绘制六足+机器人
"""

import cv2 as cv
import numpy as np
from init import *
from caculater import *
from math import *


class Leg(object):
    """
    定义六足机器人腿的相关方法
    """

    def __init__(self, root, foot):  # 需要传入一个底图
        self.root = root
        self.foot = foot
        self.fixed = True  # 初始为固定状态,即起支撑作用
        self.height = None  # 高度信息
        self.length = None  # 长度信息

    def draw(self, img):
        if self.fixed:  # 固定状态的颜色
            cv.line(img, tuple(self.root), tuple(self.foot), yellow, 4)
            cv.circle(img, tuple(self.foot), 3, red, -1)
        else:
            cv.line(img, tuple(self.root), tuple(self.foot), green, 4)
            cv.circle(img, tuple(self.foot), 3, yellow, -1)
        cv.circle(img, tuple(self.root), 5, orange, -1)  # 腿的根部永远是橘色

    def caculate_angle(self):  # 计算根部与足部产生的角度,第一个舵机
        try:
            if atan((self.foot[0] - self.root[0])) <=0:
                self.angle = int(degrees(atan((self.foot[1] - self.root[1]) / (self.foot[0] - self.root[0]))))+180
            else :
                self.angle = int(degrees(atan((self.foot[1] - self.root[1]) / (self.foot[0] - self.root[0]))))
        except ZeroDivisionError:
            if (self.foot[0] - self.root[0]) >= 0:
                self.angle = 90
            else:
                self.angle = -90


class Spider(object):
    """
    spider类，用于记录机器人目前的活动信息
    """

    def __init__(self, position, dicts: dict):
        self.position = position
        self.forward = 90  # 机器人正方向默认为90
        self.dicts = dicts  # 将长高转角度的读入字典
        self.six_roots = six_roots(position, 90)  # 返回所有根节点
        self.position = position
        self.forward = 90
        self.init_create()

    def init_create(self):  # 用于创建6个leg类与记录摄像头位置
        self.leg_1 = Leg(self.six_roots[1], foot_position(self.six_roots[1], 45, 150, self.forward))
        self.leg_2 = Leg(self.six_roots[2], foot_position(self.six_roots[2], -45, 150, self.forward))
        self.leg_3 = Leg(self.six_roots[3], foot_position(self.six_roots[3], -90, 150, self.forward))
        self.leg_4 = Leg(self.six_roots[4], foot_position(self.six_roots[4], -135, 150, self.forward))
        self.leg_5 = Leg(self.six_roots[5], foot_position(self.six_roots[5], 135, 150, self.forward))
        self.leg_6 = Leg(self.six_roots[6], foot_position(self.six_roots[6], 90, 150, self.forward))
        self.camera_position = self.six_roots[0]

    def move_roots(self, position, forward):  # 传入机器人中心所在位置以及面朝方向
        self.six_roots = six_roots(position, forward)
        for i in range(1, 7):
            self.__dict__[f'leg_{i}'].root = self.six_roots[i]
        self.camera_position = self.six_roots[0]

    def draw(self, img):  # 绘制出整个机器人模型
        for i in range(1, 7):
            self.__dict__[f'leg_{i}'].draw(img)
        cv.circle(img, tuple(self.camera_position), 7, yellow, 2)

    def caculate_angle(self):
        self.angles = []
        for i in range(1, 7):
            self.__dict__[f'leg_{i}'].caculate_angle()
            self.angles.append(self.__dict__[f'leg_{i}'].angle)


def create_img(size: list, color):
    background_img = np.zeros([size[0], size[1], 3], np.uint8)
    background_img[:, :, 0] = np.zeros(size) + color[0]
    background_img[:, :, 1] = np.zeros(size) + color[1]
    background_img[:, :, 2] = np.zeros(size) + color[2]
    return background_img


if __name__ == '__main__':
    img = create_img([800, 800], grey)
    original = img
    with open('l&h_angle.json', 'r') as f:
        dicts = json.load(f)
    spider = Spider([400, 400], dicts)
    spider.draw(img)
    spider.caculate_angle()
    print(spider.angles)
    cv.imshow("new image", img)
    cv.waitKey()
    img = create_img([800, 800], grey)
    spider.move_roots([400, 400], 0)
    spider.caculate_angle()
    print(spider.angles)
    spider.draw(img)
    cv.imshow("new image", img)
    cv.waitKey()
