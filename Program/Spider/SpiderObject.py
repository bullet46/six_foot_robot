import math
from Library.caculater import *
from Spider.Config import *


class Leg(object):
    """
    足对象,用于描述单个足部属性
    """

    def __init__(self, root_point, support_point, root_height, forward_angle):
        self.root_point = root_point  # 针对于上视图,根部位置,[x,y]
        self.root_height = root_height  # 针对于正视图,设置默认高度
        self.support_point = support_point  # 针对于上视图,支撑点位置,[x,y]
        self.forward_angle = forward_angle  # 关节朝向的正方向
        self.support_length = None  # 针对于正视图,计算长度
        self.servo1 = None
        self.servo2 = None
        self.servo3 = None
        self.fixed_state = True  # 目前状态是否作为支撑

    def calculate_servo(self, root_point, support_point, root_height):
        """
        给定腿部在上视图坐标位置与该腿目前高度,计算三个舵机角度
        """
        self.support_length = line_distance(root_point, support_point)


if __name__ == '__main__':
    print(forward_kinematics(90, 0))
