"""
该脚本用于生成
angle_l&h.json:将舵机角度转换为长和高
l&h_angle.json:将长和高转换为舵机角度
l_limit.json:指定长度下高度的定义域
h_limit.json:指定高度下长的定义域
"""
import json
from math import *
from Library.caculater import *
from Spider.init import *
from Library.data_find import *


def length_height_exchange():
    """
    穷举出定义域(舵机旋转角度)范围内所有距离与高的结果，返回二维列表，对应值代表某角度下的长与高
    :return:列表，第一个元素代表第一节点的坐标，第二个元素代表第二节点坐标
    """
    angle_1_limit = [0, 180]
    angle_2_limit = [-45, 135]
    lists_all = []
    for i in range(angle_1_limit[0], angle_1_limit[1] + 1):
        lists = []
        for n in range(angle_2_limit[0], angle_2_limit[1] + 1):
            second_point_l = first_arm_length * sin(radians(i)) - second_arm_length * cos(
                radians(i + n)) + joint_between
            second_point_h = first_arm_length * cos(radians(i)) + second_arm_length * sin(radians(i + n))
            lists.append([[first_arm_length * sin(radians(i)) + joint_between, first_arm_length * cos(radians(i))],
                          [second_point_l, second_point_h]])
        print(i)
        lists_all.append(lists)
    return lists_all


def angle_point12_exchange():
    """
    输入一个列表，返回高度与长度相关的舵机角度字典，穷举出限定宽高条件下最适于移动的舵机角度，只需运行一次，将结果保存
    """
    dic_all = {}
    limits = first_arm_length + second_arm_length
    # for l in range(0, h_limits + 45 + 1): # 之前比较(非常)暴力的逆运算求解
    #     l = l + joint_between
    #     for h in range(-h_limits, h_limits + 1):
    #         temp = []
    #         for t in range(len(lists)):
    #             for i in range(len(lists[t])):
    #                 if lists[t][i][0][0] <= lists[t][i][1][0]:  # 防止关节出现内折
    #                     if abs(lists[t][i][1][0] - l) <= 0.7 and abs(lists[t][i][1][1] - h) <= 1:  # 找到逼近精度的位置
    #                         temp = [t, i - 45]
    #         if len(temp) != 0:
    #             dic_all.update({str(str(l) + '_' + str(h)): temp})
    #             print({str(str(l) + '_' + str(h)): temp})
    for length in range(1, limits + 1):
        for height in range(-limits, limits + 1):
            first_angle, second_angle = None, None
            between = line_distance([0, 0], [length, height])
            between_int = int(between)
            if (first_arm_length + second_arm_length >= between) and (  # 如果能构成三角形或直线
                    second_arm_length + between >= first_arm_length) and (
                    between + first_arm_length >= second_arm_length):
                if -225 <= between <= 225:  # 防止超出定义域
                    first_angle = 90 + degrees(atan(height / length)) + degrees(
                        acos((first_arm_length ** 2 + between ** 2 - second_arm_length ** 2) / (
                                2 * first_arm_length * between)))
                if first_arm_length + second_arm_length == between_int:  # 如果在同一条直线上
                    second_angle = 180 - 90
                else:
                    second_angle = degrees(acos((first_arm_length ** 2 + second_arm_length ** 2 - between ** 2) / (
                            2 * first_arm_length * second_arm_length))) - 90
            else:
                pass
            if first_angle is not None:
                if (0 <= first_angle <= 180) and (-45 <= second_angle <= 135):
                    dic_all.update({(str(length+joint_between) + '_' + str(-height)): [int(first_angle), int(second_angle)]})
                    print({(str(length+joint_between) + '_' + str(-height)): [int(first_angle), int(second_angle)]})

    return dic_all


def create_angle_l():
    lists = length_height_exchange()  # 如果length_height_ex有内容改动(如设计参数有变化)，请运行该方法
    with open("angle_l&h.json", "w") as fp:
        fp.write(json.dumps(lists))
        print('angle_l&h.json写入成功')


def create_l_angle():
    with open('l&h_angle.json', 'w') as fp:
        fp.write(json.dumps(angle_point12_exchange()))
        print('l&h_angle.json写入成功')


def l_limit():  # 指定长度可取值的高度范围
    data = data_find()
    empty_dicts = {}
    for i in range(-limits, limits):
        min_h = 2000000
        max_h = -2000000
        for t in range(-limits, limits):
            t1 = data.find_angle(i, t)
            if t1 is not None:
                min_h = min(min_h, t)
                max_h = max(max_h, t)
        if min_h != 2000000:
            empty_dicts.update({str(i): [min_h, max_h]})
    with open('l_limit.json', 'w') as new:
        new.write(json.dumps(empty_dicts))
        print('l_limit.json写入成功')


def h_limit():  # 指定高度的可取值的长度范围
    empty_dicts = {}
    data = data_find()
    for t in range(-limits, limits):
        min_h = 2000000
        max_h = -2000000
        for i in range(-limits, limits):
            t1 = data.find_angle(i, t)
            if t1 is not None:
                min_h = min(min_h, i)
                max_h = max(max_h, i)
        if min_h != 2000000:
            empty_dicts.update({str(t): [min_h, max_h]})
    with open('h_limit.json', 'w') as new:
        new.write(json.dumps(empty_dicts))
        print('h_limit.json写入成功')


if __name__ == "__main__":
    # with open('l&h_angle.json', 'r') as fp:
    #     dicts = json.load(fp)
    # print(find_angle(0,224,dicts))
    create_angle_l()
    create_l_angle()
    l_limit()
    h_limit()
