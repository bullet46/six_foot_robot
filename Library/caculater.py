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
    return pow((length ** 2 + height ** 2), 2)


def foot_position(root: list, angle, length, forward):  # 给定原点坐标，角度，长度，起始方向角度；返还延伸点坐标
    radian = radians(angle + forward)
    return [int(root[0] + cos(radian) * length), int(root[1] + sin(radian) * length)]


def six_roots(position: list, forwards):  # 给定机器人中心位置，机器人面朝方向，计算机器人摄像头位置以及6个根节点坐标
    orignal = np.array([[0, -50], [-58, 98], [58, 98], [88, 0], [58, -98], [-58, -98], [-88, 0]])
    trans = np.array([[cos(radians(forwards - 90)), sin(radians(forwards - 90))],
                      [cos(radians(forwards)), sin(radians(forwards))]], np.float64)  # 2*2的变换基底矩阵
    lists = []
    for i in range(7):
        roots = list(np.inner(trans, orignal[i, :].T).astype(int))
        lists.append([roots[0] + position[0], roots[1] + position[1]])
    return lists


def length_height_ex():  # 穷举出定义域(舵机旋转角度)范围内所有距离与高的结果，返回二维列表，对应值代表某角度下的长与高
    angle_1_limit = [0, 180]
    angle_2_limit = [-45, 135]
    lists_all = []
    for i in range(angle_1_limit[0], angle_1_limit[1] + 1):
        lists = []
        for n in range(angle_2_limit[0], angle_2_limit[1] + 1):
            length = first_arm_length * sin(radians(i)) - second_arm_length * cos(radians(i + n)) + joint_between
            height = first_arm_length * cos(radians(i)) + second_arm_length * sin(radians(i + n))
            lists.append([length, height])
        print(i)
        lists_all.append(lists)
    return lists_all


def angle_12_ex(lists):
    """
    输入一个列表，返回高度与长度相关的舵机角度字典，穷举出限定宽高条件下最适于移动的舵机角度，只需运行一次，将结果保存
    """
    dic_all = {}
    for l in range(0, 375):
        print(l)
        for h in range(-225, 225):
            temp = []
            for t in range(len(lists)):
                for i in range(len(lists[t])):
                    if abs(lists[t][i][0] - l) <= 1 and abs(lists[t][i][1] - h) <= 1:
                        temp = [t, i - 45]
            if len(temp) != 0:
                dic_all.update({str(str(l) + '_' + str(h)): temp})
                print({str(str(l) + '_' + str(h)): temp})
    return dic_all


def find_angle(length, height, dic: dict):
    """
    :param length: 需求的长度
    :param height: 需求的高度
    :param dic: l&h_angle高度
    :return: 返回角度信息
    """
    try:
        return dic[str(length) + '_' + str(height)]
    except:
        return None

