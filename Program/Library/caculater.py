"""
该函数用于封装一些与数学计算有关的方法
"""
from math import *
import numpy as np
import json
from Spider.Config import *


def line_distance(point_1: list, point_2: list):
    """
    给定两点坐标，计算距离
    """
    length = abs(point_1[0] - point_2[0])
    height = abs(point_1[1] - point_2[1])
    return pow((length ** 2 + height ** 2), 1 / 2)


def forward_kinematics_servo(angle1, angle2):
    """
    针对舵机定义角度的正运动学
    """
    length = -(first_arm_length * sin(radians(angle1)) - second_arm_length * cos(
        radians(angle2 + angle1)) + joint_between)
    height = -(first_arm_length * cos(radians(angle2)) - second_arm_length * cos(radians(angle2 - angle1)))
    return length, height


def forward_kinematics(angle1, angle2):
    """
    针对全局坐标系的正运动学
    """
    L1 = first_arm_length
    L2 = second_arm_length
    x = L2 * sin(angle1) + L1 * cos(angle2)
    y = L2 * cos(angle2) - L1 * sin(angle1)
    return x, y


def inverse_kinematics(x, y):
    """
    逆运动学
    """
    try:
        x = x - joint_between
        L1 = first_arm_length
        L2 = second_arm_length
        F1 = - L1 ** 2 + 2 * L1 * L2 - L2 ** 2 + x ** 2 + y ** 2
        F2 = (L1 ** 2 + 2 * L1 * L2 + L2 ** 2 - x ** 2 - y ** 2)
        F3 = (- L1 ** 2 + L2 ** 2 + 2 * L2 * y + x ** 2 + y ** 2)
        F4 = (2 * L2 * x - sqrt(F1 * F2))
        F5 = (L1 ** 2 + 2 * L1 * x - L2 ** 2 + x ** 2 + y ** 2)
        a1 = -2 * atan(
            (2 * L1 * y - 2 * L2 * x - (L1 ** 2 * (F4)) / F3 + (L2 ** 2 * (F4)) / F3 + (x ** 2 * (F4)) / F3 + (
                    y ** 2 * (F4)) / F3 + (2 * L2 * y * (F4)) / F3) / F5)

        F1 = (- L1 ** 2 + 2 * L1 * L2 - L2 ** 2 + x ** 2 + y ** 2)
        F2 = (L1 ** 2 + 2 * L1 * L2 + L2 ** 2 - x ** 2 - y ** 2)
        F3 = (- L1 ** 2 + L2 ** 2 + 2 * L2 * y + x ** 2 + y ** 2)
        a2 = 2 * atan((2 * L2 * x - sqrt(F1 * F2)) / F3)
        return int(degrees(a1)), int(degrees(a2))
    except:
        return None,None


def calculate_angle(v1):
    """
    计算向量针对全局角度
    """
    x = v1[0]
    y = v1[1]
    if x == 0:
        if y > 0:
            return 90
        else:
            return 270
    if y == 0:
        if x < 0:
            return 0
        else:
            return 180
    ratio = y / x
    if x > 0 and y > 0:
        return abs(degrees(atan(ratio)))
    elif x < 0 and y > 0:
        return 180 - abs(degrees(atan(ratio)))
    elif x < 0 and y < 0:
        return 180 + abs(degrees(atan(ratio)))
    elif x > 0 and y < 0:
        return 360 - abs(degrees(atan(ratio)))


def add_position(pos1, pos2):  # 两个二维数组内的元素逐个相加
    return [pos1[0] + pos2[0], pos1[1] + pos2[1]]


def sub_position(pos1, pos2):  # 将两个二位数组内的元素对应相减
    return [pos1[0] - pos2[0], pos1[1] - pos2[1]]


def trans_cor_leg(x, y):  # 用于腿部绘图相关的坐标转换，将左上角零点转换为右下角
    return x, int(300 - y)


def trans_cor_spi(lists:list):  # 用于六足体绘图相关的坐标转换，将左上角零点转换为右下角
    return lists[0], int(500 - lists[1])


def calculate_foot_position(root: list, angle, length, forward=0):  # 给定原点坐标，角度，长度，起始方向角度；返还延伸点坐标
    return [
        int(root[0] + cos(radians(angle + forward)) * length), int(root[1] + sin(radians(angle + forward)) * length)]


def create_back_img(x, y, bgr):
    img = np.zeros([x, y, 3], np.uint8)
    img[:, :, 0] = np.zeros([x, y]) + bgr[0]
    img[:, :, 1] = np.ones([x, y]) + bgr[1]
    img[:, :, 2] = np.ones([x, y]) * bgr[2]
    return img


def calculate_six_roots(position: list, forwards):  # 给定机器人中心位置，机器人面朝方向，计算机器人摄像头位置以及6个根节点坐标
    forwards = forwards
    orignal = np.array([[-58, 98],  [-88, 0],[-58, -98],[58, -98],[88, 0], [58, 98]])
    trans = np.array([[cos(radians(forwards - 90)), sin(radians(forwards - 90))],
                      [cos(radians(forwards)), sin(radians(forwards))]], np.float64)  # 2*2的变换基底矩阵
    lists = []
    for i in range(6):
        roots = list(np.inner(trans, orignal[i, :].T).astype(int))
        lists.append([roots[0] + position[0], roots[1] + position[1]])
    return lists


def space_angle_to_machine_angle(angle, forward):  # 将机器人在空间坐标系的角度转为机器人为90度方向的角度
    machine_angle = angle + (90 - forward)
    if machine_angle <= -180:
        machine_angle = machine_angle + 360
    elif machine_angle >= 180:
        machine_angle = machine_angle - 360
    return machine_angle


if __name__ == '__main__':
    # print(forward_kinematics_new(0, 0))
    # print(calculate_angle([0, 0, -45, -45]))
    # print(inverse_kinematics(181, 106))
    # print(calculate_angle([12, -12]))
    print(calculate_foot_position([0,0],225,20))
