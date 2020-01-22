from 初始脚本 import math

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


def trans_to_radian(angle):  # 将角度制改为弧度
    return math.radians(angle)


def point_length(angle_group):  # 传入两个舵机的角度，传出距主轴距离与高度
    x = math.sin(trans_to_radian(angle_group[1] + 90 - angle_group[0])) * second_arm_length + math.sin(
        trans_to_radian(angle_group[0])) * first_arm_length + joint_between
    h = math.cos(trans_to_radian(angle_group[1] + 90 - angle_group[0])) * second_arm_length + math.cos(
        trans_to_radian(angle_group[0])) * first_arm_length
    return float(x), float(h)


def angle_back(x_h, list):  # 传入臂长与高度，求出角度
    D_value1 = 9999  # 定义一个差值，以此逐步查表找出最逼近的运算值
    a_b = 0
    m = 0
    n = 0
    for x in list:
        for y in x:
            sum_ = abs(x_h[0] - y[0]) + abs(x_h[1] - y[1])
            if D_value1 > sum_:
                D_value1 = sum_
                a_b = [-90 + m, -45 + n]
            n += 1
        m += 1
        n = 0
    if D_value1 > 10:
        return None  # 如果找不到那个值，则返回None
    else:
        return a_b


def standard_number(number):  # 将数字转换为0001格式
    return str(number).rjust(4, '0')


def standard_number3(number):  # 将数字转换为001格式
    return str(number).rjust(3, '0')


def x_h_array():  # 生成一个90x90的矩阵，记录每个角度所对应的x与h距离
    create_list = []
    for x in range(-90, 90):
        temp_list = []
        for y in range(-45, 135):
            temp_list.append(point_length([x, y]))
        create_list.append(temp_list)
    return create_list


if __name__ == '__main__':
    list = x_h_array()
    back = []
    temp = 0

    for h in range(40, 200,5):  # 高度50~200mm
        back.append([0, 0])
        for x in range(0, 300):  # 长度0-20
            if angle_back([x, h],list) is not None:
                back[temp][1] = x
        print(h,back[temp][1])
        back[temp][0] = h
        temp += 1

    fileObject = open('sampleList.txt', 'w+')
    for ip in back:
        fileObject.write(str(ip))
        fileObject.write('\n')
        fileObject.close()
