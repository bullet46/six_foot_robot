import cv2 as cv
import numpy as np
from 初始脚本 import math

# 初始脚的位置
foot_roots = [[100, 60], [100, -60], [0, -90], [0, 90], [-100, 60], [-100, -60]]
# 初始各个脚长度
foot_x = [150, 150, 150, 150, 150, 150]
# 初始各个角角度
foot_angle = [45, -45, -90, 90, 135, -135]


def trans_to_radian(angle):  # 将角度制改为弧度
    return math.radians(int(angle))


def origin(coordinate):  # 将画面中心设为0,0点
    return (coordinate[0] + 512, coordinate[1] + 512)


def l_t(list_0):
    return (int(list_0[0]), int(list_0[1]))


class foot():  # 六足机器人，足类
    def __init__(self, angle_0, root, x):
        self.angle = angle_0 + 90
        self.root = origin(root)
        self.x_h = x
        self.back = origin([int(root[0] + math.cos(trans_to_radian(angle_0)) * x),
                            int(root[1] + math.sin(trans_to_radian(angle_0)) * x)])
        self.root_color = (159, 255, 84)
        self.back_color = (205, 250, 255)

    def draw(self, img):  # 绘画
        cv.line(img, l_t(self.root), l_t(self.back), (255, 255, 0), 3)
        cv.circle(img, l_t(self.root), 5, l_t(self.root_color), thickness=-1)
        cv.circle(img, l_t(self.back), 5, l_t(self.back_color), thickness=-1)

    def angle_caculate(self):  # 知道两点用于计算角度
        vector = [(self.back[0] - self.root[0]), (self.back[1] - self.root[1])]
        if vector[0] == 0:
            if vector[1] > 0:
                self.angle = 90
            else:
                self.angle = -90
        elif vector[0] > 0:
            self.angle = int(math.degrees(math.atan(vector[1] / vector[0])))
        else:
            if vector[1] >= 0:
                self.angle = int(180 - math.degrees(0 - math.atan(vector[1] / vector[0])))
            else:
                self.angle = int(-180 - math.degrees(0 - math.atan(vector[1] / vector[0])))

    def length_caculate(self):
        sqrt = (self.root[0] - self.back[0]) ** 2 + (self.root[1] - self.back[1]) ** 2
        self.x = int(math.pow(sqrt, 1.0 / 2))

    def root_position(self, position):  # 连接点
        self.root = origin(position)
        self.angle_caculate()

    def back_position(self, position):  # 支撑点
        self.back = origin(position)
        self.angle_caculate()


def create_image():  # 生成图像
    img = np.zeros((1024, 1024, 3), np.uint8)
    cv.imshow("image", img)
    state = 0  # 用于记录目前状态
    mode = input("请选择移动模式:")  # 0指平动，1指转动
    step_length = 40
    step_times = 1
    angle = input("请选择移动角度:")
    group_0 = [0, 2, 4]
    group_1 = [1, 3, 5]
    for i in range(0, 6):
        locals()['foot_' + str(i)] = foot(foot_angle[i], foot_roots[i], foot_x[i])
        locals()['foot_' + str(i)].draw(img)
    while 1:
        img = np.zeros((1024, 1024, 3), np.uint8)
        group_root = []
        group_back = []
        angle_date = []  # 输出角度值
        length_date = []  # 输出长度值
        if state == 0:
            group_ = group_0
        elif state == 1 or state == 2:
            group_ = group_1
        elif state == 3 or state == 4:
            group_ = group_0
        for i in range(0, 6):
            group_root.append([
                step_length * step_times * math.cos(trans_to_radian(angle)) + locals()['foot_' + str(i)].root[0],
                step_length * step_times * math.sin(trans_to_radian(angle)) + locals()['foot_' + str(i)].root[1]])
            if i in group_:
                group_back.append([
                    step_length * step_times * 2 * math.cos(trans_to_radian(angle)) +
                    locals()['foot_' + str(i)].back[0],
                    step_length * step_times * 2 * math.sin(trans_to_radian(angle)) +
                    locals()['foot_' + str(i)].back[1]])
            else:
                group_back.append([locals()['foot_' + str(i)].back[0], locals()['foot_' + str(i)].back[1]])
        if state == 4:
            state = 1
        else:
            state += 1
        for i in range(0, 6):
            locals()['foot_' + str(i)].root = group_root[i]
            locals()['foot_' + str(i)].back = group_back[i]
            locals()['foot_' + str(i)].draw(img)
        cv.waitKey(0)
        print(state)
        print(group_)
        for i in range(0, 6):
            locals()['foot_' + str(i)].angle_caculate()
            locals()['foot_' + str(i)].length_caculate()
            angle_date.append(locals()['foot_' + str(i)].angle)
            length_date.append(locals()['foot_' + str(i)].x)
            print(angle_date)
            print(length_date)
        cv.imshow("image", img)

#      img = np.zeros((1024, 1024, 3), np.uint8)
#        for i in range(-720,720):
#             foot1 = foot(i,origin([0,0]),100)
#             foot1.draw(img)
#             print(i)
#             cv.imshow("image",img)
#             cv.waitKey(0)


create_image()
