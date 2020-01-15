import math
import stastic

trans_toradian = stastic.trans_to_radian()

def point_length(angle_group):  # 传入两个舵机的角度，传出距主轴距离与高度
    x = math.sin(trans_to_radian(angle_group[1] + 90 - angle_group[0])) * second_arm_length + math.sin(
        trans_to_radian(angle_group[0])) * first_arm_length + joint_between
    h = math.cos(trans_to_radian(angle_group[1] + 90 - angle_group[0])) * second_arm_length + math.cos(
        trans_to_radian(angle_group[0])) * first_arm_length
    return x, h

