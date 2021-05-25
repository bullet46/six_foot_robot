"""
该模块主要模拟spider的运动并进行仿真
"""
from spider_object import *


class MoveScript(object):
    def __init__(self, state: dict, next_state: dict):
        """
        :param state: 目前所在状态，字典。字典含{position:[,] , forward: ,state ,height} 用于表述当前位置与下一时刻方向与状态
        注:0为暂停态，1为1,3,5固定,2为2,4,6固定不变
        :param next_state: 目标状态，字典。字典含{position:[,] , forward: ,state,height} 用于表示下一时刻位置与方向
        """
        self.position = state['position']
        self.position_next = next_state['position']
        self.move_stat = state['state']  # 用于描述当前状态
        self.move_state_next = next_state['state']  # 用于描述下一刻目标状态
        self.forward = state['forward']
        self.forward_next = next_state['forward']
        self.height = state['height']
        self.height_next = next_state['height']


