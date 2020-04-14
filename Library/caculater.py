'''
该函数用于封装一些与数学计算有关的方法
'''
from math import *
import numpy as np
import json
from Spider.init import *


def line_distance(point_1: list, point_2: list):  # 给定两点坐标，计算距离
    length = abs(point_1[0] - point_2[0])
    height = abs(point_1[1] - point_2[1])
    return pow((length ** 2 + height ** 2), 1 / 2)


def foot_position(root: list, angle, length, forward):  # 给定原点坐标，角度，长度，起始方向角度；返还延伸点坐标
    radian = radians(angle + forward)
    return [int(root[0] + cos(radian) * length), int(root[1] + sin(radian) * length)]


def six_roots(position: list, forwards):  # 给定机器人中心位置，机器人面朝方向，计算机器人摄像头位置以及6个根节点坐标
    forwards = forwards + 90
    orignal = np.array([[0, -50], [-58, 98], [58, 98], [88, 0], [58, -98], [-58, -98], [-88, 0]])
    trans = np.array([[cos(radians(forwards - 90)), sin(radians(forwards - 90))],
                      [cos(radians(forwards)), sin(radians(forwards))]], np.float64)  # 2*2的变换基底矩阵
    lists = []
    for i in range(7):
        roots = list(np.inner(trans, orignal[i, :].T).astype(int))
        lists.append([roots[0] + position[0], roots[1] + position[1]])
    return lists


def add_position(pos1, pos2):  # 两个二维数组内的元素逐个相加
    return tuple([pos1[0] + pos2[0], pos1[1] + pos2[1]])


def space_angle_to_machine_angle(angle, forward):  # 将机器人在空间坐标系的角度转为机器人为90度方向的角度
    machine_angle = angle + (90 - forward)
    if machine_angle <= -180:
        machine_angle = machine_angle + 360
    elif machine_angle >= 180:
        machine_angle = machine_angle - 360
    return machine_angle


def if_intersect(line1, line2):  # 判断两线段是否相交
    def cross(p1, p2, p3):  # 跨立实验
        x1 = p2[0] - p1[0]
        y1 = p2[1] - p1[1]
        x2 = p3[0] - p1[0]
        y2 = p3[1] - p1[1]
        return x1 * y2 - x2 * y1

    p1 = line1[0]
    p2 = line1[1]
    p3 = line2[0]
    p4 = line2[1]

    # 快速排斥，以l1、l2为对角线的矩形必相交，否则两线段不相交
    if (max(p1[0], p2[0]) >= min(p3[0], p4[0])  # 矩形1最右端大于矩形2最左端
            and max(p3[0], p4[0]) >= min(p1[0], p2[0])  # 矩形2最右端大于矩形最左端
            and max(p1[1], p2[1]) >= min(p3[1], p4[1])  # 矩形1最高端大于矩形最低端
            and max(p3[1], p4[1]) >= min(p1[1], p2[1])):  # 矩形2最高端大于矩形最低端

        # 若通过快速排斥则进行跨立实验
        if (cross(p1, p2, p3) * cross(p1, p2, p4) <= 0
                and cross(p3, p4, p1) * cross(p3, p4, p2) <= 0):
            D = True
        else:
            D = False
    else:
        D = False
    return D
