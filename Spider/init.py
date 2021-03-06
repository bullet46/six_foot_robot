# 关节长度信息说明
joint_between = 50  # 第一关节间距
first_arm_length = 75  # 第一手臂长度
second_arm_length = 150  # 第二手臂长度

limits = joint_between + first_arm_length + second_arm_length  # 最大伸展距离

# 关节编号说明
first_joint = [1, 2, 3, 4, 5, 6]  # 第一关节编号
second_joint = [7, 8, 9, 10, 11, 12]  # 第二关节编号
third_joint = [13, 14, 15, 16, 17, 18]  # 第三关节编号

slope_unit = [1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1]  # 舵机正负调试
b_number = [1250, 1500, 3000, 0, 1500, 1750, 1250, 1500, 2500, 500, 1500, 1250, 1250, 1500, 2000, 1000, 1500,
            1750]  # 舵机归为0度初始值
speed = 500  # 舵机转速

# 定义部分颜色以及BGR值
red = (0, 69, 255)
green = (0, 244, 0)
yellow = (80, 196, 255)
dark = (19, 16, 11)
grey = (70, 60, 60)
blue = (211, 168, 81)
orange = (28, 94, 240)
