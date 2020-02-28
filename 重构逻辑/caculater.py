'''
该函数用于封装一些与数学计算有关的方法
'''
from math import *
import numpy as np
from init import *


def line_distance(point_1: list, point_2: list):  # 给定两点坐标，计算距离
    length = abs(point_1[0] - point_2[0])
    height = abs(point_1[1] - point_2[1])
    return pow((length ** 2 + height ** 2), 2)


def foot_position(root: list, angle, length, forward):  # 给定原点坐标，角度，长度，起始方向角度；返还延伸点坐标
    radian = radians(angle + forward)
    return [int(root[0] + cos(radian) * length), int(root[1] + sin(radian) * length)]


def six_roots(position: list, forwards):  # 给定机器人中心位置，机器人面朝方向，计算机器人6个根节点坐标
    orignal = np.array([[-58, 98], [58, 98], [88, 0], [58, -98], [-58, -98], [-88, 0]])
    trans = np.array([[cos(radians(forwards - 90)), sin(radians(forwards - 90))],
                      [cos(radians(forwards)), sin(radians(forwards))]], np.float64)  # 2*2的变换基底矩阵
    lists = []
    for i in range(6):
        roots = list(np.inner(trans, orignal[i, :].T).astype(int))
        lists.append([roots[0] + position[0], roots[1] + position[1]])
    return lists
