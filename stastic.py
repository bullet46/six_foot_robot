import openpyxl
import math
import numpy as np
import cv2

back_img = np.zeros((1024, 1024, 3), np.uint8)
while (1):
    cv2.imshow("dw", back_img)
    cv2.waitKey(0)
joint_between = 50  # 第一关节间距
first_arm_length = 75  # 第一手臂长度
second_arm_length = 150  # 第二手臂长度
first_joint = [2, 3, 8, 9, 14, 15]  # 第一关节编号
second_joint = [1, 4, 7, 10, 13, 16]  # 第二关节编号
third_joint = [0, 5, 6, 11, 12, 17]  # 第三关节编号
slope_unit = [1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1]  # 舵机正负调试
b_number = [1250, 1500, 3000, 0, 1500, 1750, 1250, 1500, 2500, 500, 1500, 1250, 1250, 1500, 2000, 1000, 1500,
            1750]  # 舵机归为0度初始值
speed = 500  # 舵机转速


def trans_angle(angle):
    if len(angle) == 18:
        angle_trans = []
        for i in range(0, 18):
            angle_trans.append((100 / 9) * slope_unit[i] + b_number[i])  # 用于线性变换，将角度化为pwm值
        return angle_trans
    else:
        return 0


def trans_to_radian(angle):  # 将角度制改为弧度
    return math.radians(angle)


def point_length(angle_group):  # 传入两个舵机的角度，传出距主轴距离与高度
    x = math.sin(trans_to_radian(angle_group[1] + 90 - angle_group[0])) * second_arm_length + math.sin(
        trans_to_radian(angle_group[0])) * first_arm_length + joint_between
    h = math.cos(trans_to_radian(angle_group[1] + 90 - angle_group[0])) * second_arm_length + math.cos(
        trans_to_radian(angle_group[0])) * first_arm_length
    return x, h


def standard_number(number):  # 将数字转换为0001格式
    return str(number).rjust(4, '0')


def standard_number3(number):  # 将数字转换为001格式
    return str(number).rjust(3, '0')


def stastic_trans():  # 用于将每组数据保存为ini文件的支持格式
    data = openpyxl.load_workbook("舵机编写.xlsx", data_only=True)
    sheet2 = data['Sheet2']
    for t in range(ord('B'), ord('S')):
        print('G' + standard_number(t - ord('A')) + '={G' + standard_number(t - ord('A')), end='')
        for i in range(2, 20):
            print("#" + standard_number3(i - 2) + 'P' + str(sheet2[str(chr(t)) + str(i)].value) + 'T' +
                  standard_number(speed) + '!', end="")
        print('}')



if __name__ == '__main__':
    stastic_trans()
