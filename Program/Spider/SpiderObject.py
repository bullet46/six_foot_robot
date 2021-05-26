import math
from Library.caculater import *
from Spider.Config import *
import cv2 as cv
from math import *


class Leg(object):
    """
    足对象,用于描述单个足部属性
    """

    def __init__(self, order, root_point, support_point, root_height, forward_angle):
        self.leg_order = order  # 传入1~6的足部信号
        self.root_point = root_point  # 针对于上视图,根部位置,[x,y]
        print(root_point[0] - 250, root_point[1] - 250)
        self.root_height = root_height  # 针对于正视图,设置默认高度
        self.support_point = support_point  # 针对于上视图,支撑点位置,[x,y]
        self.forward_angle = forward_angle  # 关节朝向的正方向
        self.support_length = None  # 针对于正视图,计算长度
        # 真实舵机角度
        self.servo0_angle = None
        self.servo1_angle = None
        self.servo2_angle = None
        # 空间坐标角度
        self.cod0_angle = None
        self.cod1_angle = None
        self.cod2_angle = None
        self.fixed_state = True  # 目前状态是否作为支撑
        self.calculate_cod(root_point, support_point, root_height)

    def calculate_cod(self, root_point, support_point, height):
        """
        给定腿部在上视图坐标位置与该腿目前高度,计算三个空间坐标系角度
        """
        self.support_length = line_distance(root_point, support_point)
        self.cod0_angle = int(calculate_angle(sub_position(support_point, root_point)))
        self.cod1_angle, self.cod2_angle = inverse_kinematics(self.support_length, height)

    def control_by_angle(self, angle, length):
        """
        通过给定全局角度和延伸长度来更新位置信息
        """
        self.support_point[0] = self.root_point[0] + cos(radians(angle)) * length
        self.support_point[1] = self.root_point[1] + sin(radians(angle)) * length

    def mov_support_point(self,x,y):
        """
        向前移动支撑足
        """
        self.support_point = [self.support_point[0]+x,self.support_point[1]+y]

    def draw(self, back_img):
        """
        绘制侧视图,需要传参背景图片,应为300*300
        """
        if self.fixed_state is True:
            leg_color = red  # 通过不同的状态来表示目前腿部起的作用
        else:
            leg_color = green

        self.point0 = [240, 60 + self.root_height]
        self.point1 = [240 - joint_between, 60 + self.root_height]
        self.point2 = [self.point1[0] - int(cos(radians(self.cod1_angle)) * first_arm_length),
                       self.point1[1] + int(sin(radians(self.cod1_angle)) * first_arm_length)]
        self.point3 = [self.point2[0] - int(sin(radians(self.cod2_angle)) * second_arm_length),
                       self.point2[1] - int(cos(radians(self.cod2_angle)) * second_arm_length)]
        back_img = cv.rectangle(back_img, trans_cor_leg(0, 0), trans_cor_leg(300, 60), grey_ground, -1)
        img = cv.line(back_img, trans_cor_leg(self.point0[0], self.point0[1]),
                      trans_cor_leg(self.point1[0], self.point1[1]), leg_color, 2)
        img = cv.line(img, trans_cor_leg(self.point1[0], self.point1[1]),
                      trans_cor_leg(self.point2[0], self.point2[1]), leg_color, 2)
        img = cv.line(img, trans_cor_leg(self.point2[0], self.point2[1]),
                      trans_cor_leg(self.point3[0], self.point3[1]), leg_color, 2)
        img = cv.circle(img, trans_cor_leg(self.point0[0], self.point0[1]), 3, blue, -1)
        img = cv.circle(img, trans_cor_leg(self.point1[0], self.point1[1]), 3, blue, -1)
        img = cv.circle(img, trans_cor_leg(self.point2[0], self.point2[1]), 3, blue, -1)
        img = cv.circle(img, trans_cor_leg(self.point3[0], self.point3[1]), 3, blue, -1)

        if self.leg_order in [1, 2, 3]:  # 若为左侧编号，则不对图像进行翻转处理
            cv.putText(img, 'cod0_angle:' + str(self.cod0_angle), (10, 30), cv.FONT_HERSHEY_COMPLEX, 0.8,
                       (255, 255, 255), 1)
            cv.putText(img, 'cod1_angle:' + str(self.cod1_angle), (10, 60), cv.FONT_HERSHEY_COMPLEX, 0.8,
                       (255, 255, 255), 1)
            cv.putText(img, 'cod2_angle:' + str(self.cod2_angle), (10, 90), cv.FONT_HERSHEY_COMPLEX, 0.8,
                       (255, 255, 255), 1)
            cv.putText(img, 'height:' + str(round(self.root_height, 2)), (10, 260), cv.FONT_HERSHEY_COMPLEX, 0.8,
                       (0, 0, 0), 1)
            cv.putText(img, 'length:' + str(round(self.support_length, 2)), (10, 290), cv.FONT_HERSHEY_COMPLEX, 0.8,
                       (0, 0, 0), 1)
            return img
        else:
            img = cv.flip(img, 1)
            cv.putText(img, 'cod0_angle:' + str(self.cod0_angle), (10, 30), cv.FONT_HERSHEY_COMPLEX, 0.8,
                       (255, 255, 255), 1)
            cv.putText(img, 'cod1_angle:' + str(self.cod1_angle), (10, 60), cv.FONT_HERSHEY_COMPLEX, 0.8,
                       (255, 255, 255), 1)
            cv.putText(img, 'cod2_angle:' + str(self.cod2_angle), (10, 90), cv.FONT_HERSHEY_COMPLEX, 0.8,
                       (255, 255, 255), 1)
            cv.putText(img, 'height:' + str(round(self.root_height, 2)), (10, 260), cv.FONT_HERSHEY_COMPLEX, 0.8,
                       (0, 0, 0), 1)
            cv.putText(img, 'length:' + str(round(self.support_length, 2)), (10, 290), cv.FONT_HERSHEY_COMPLEX, 0.8,
                       (0, 0, 0), 1)
            return img


class Spider(object):
    """
    六足蜘蛛对象
    """

    def __init__(self, center_position, forward):
        # 根据正方向计算根部位置
        root_position_list = calculate_six_roots(center_position, forward)
        # 创建六足对象
        self.Leg1 = Leg(1, root_position_list[0], calculate_foot_position(root_position_list[0], 135, 150), 50, 135)
        self.Leg2 = Leg(2, root_position_list[1], calculate_foot_position(root_position_list[1], 180, 150), 50, 180)
        self.Leg3 = Leg(3, root_position_list[2], calculate_foot_position(root_position_list[2], 225, 150), 50, 225)
        self.Leg4 = Leg(4, root_position_list[3], calculate_foot_position(root_position_list[3], 315, 150), 50, 315)
        self.Leg5 = Leg(5, root_position_list[4], calculate_foot_position(root_position_list[4], 0, 150), 50, 0)
        self.Leg6 = Leg(6, root_position_list[5], calculate_foot_position(root_position_list[5], 45, 150), 50, 45)
        # 有三种状态
        # 0状态为全部直立,
        # 1状态1,3,5关节支撑
        # 2状态2,4,6关节支撑
        self.state = 0

    def draw(self, background_img):
        """
        用于显示六足全局图像
        """
        root_point_list = []
        support_point_list = []
        for i in range(1, 7):
            root_point_list.append(self.__dict__[f'Leg{i}'].root_point)
            support_point_list.append(self.__dict__[f'Leg{i}'].support_point)
        img = background_img
        for i in range(0, 6):
            if self.__dict__[f'Leg{i + 1}'].fixed_state is True:
                line_color = red
            else:
                line_color = green
            img = cv.line(img, trans_cor_spi(root_point_list[i]), trans_cor_spi(support_point_list[i]), line_color, 2)
            img = cv.circle(img, trans_cor_spi(root_point_list[i]), 3, blue, -1)
            img = cv.circle(img, trans_cor_spi(support_point_list[i]), 3, blue, -1)
        return img

    def move_spider(self, center_position, forward):
        root_position_list = calculate_six_roots(center_position, forward)
        for i in range(0, 6):
            self.__dict__[f'Leg{i + 1}'].root_point = root_position_list[i]


if __name__ == '__main__':
    # spider = Spider(trans_cor_spi([250, 250]), 90)
    back_img = create_back_img(300, 300, grey)
    # img = spider.draw(back_img)
    leg = Leg(1, [0, 0], [150, 0], 50, 90)
    img = leg.draw(back_img)
