""""
该库用于创建一个查询列表
"""
import json
import os
from Spider.init import *

class data_find():
    def __init__(self):
        try:
            with open('../Data/angle_l&h.json', 'r') as f:
                self.angle_lh = json.load(f)
            with open('../Data/l&h_angle.json', 'r') as f:
                self.lh_angle = json.load(f)
            with open('../Data/h_limit.json', 'r') as f:
                self.h_limit = json.load(f)
            with open('../Data/l_limit.json', 'r') as f:
                self.l_limit = json.load(f)
        except:
            pass

    def find_angle(self, length, height):
        """
        用于找到对应长高下的两只关节角度
        :param length: 需求的长度
        :param height: 需求的高度
        :return: 返回角度信息
        """
        dic = self.lh_angle
        latitude = 2  # 宽容度为2个mm，且只对目标长度宽容
        ranges = [0]
        for i in range(1, latitude + 1):  # 生成[0,-1,+1,-2,+2...]的宽容度列表
            ranges.append(-i)
            ranges.append(+i)
        backs = None
        for e in ranges:
            length = length + e
            try:
                backs = dic[str(length) + '_' + str(height)]
                if backs is not None:
                    return backs
            except:
                pass
        return None

    def find_lh(self, angle1, angle2):
        """
        用于找到对应关节角度下的长高
        :param angle1: 第一个关节的角度
        :param angle2: 第二个关节的角度
        :return 对应两只关节的坐标(二维数组)
        """
        lists = self.angle_lh
        bck_list = []
        for i in lists[angle1][angle2 + 45]:
            temp_list= []
            for t in i:
                temp_list.append(int(t)) # 需要将浮点数转化为整数才能按像素显示
            bck_list.append(temp_list)
        return bck_list

    def find_l_limit(self, length):
        """
        指定长度下高的取值
        :param length:需要的长度
        :return: list:表明指定长度下高的值范围(为固定两个值)
        """
        dic = self.l_limit
        return dic[str(length)]

    def find_h_limit(self, height):
        """
        指定长度下高的取值
        :param height:需要的高度
        :return: list:表明指定长度下高的值(为两值区间)
        """
        dic = self.l_limit
        return dic[str(height)]
