# noinspection PyUnresolvedReferences
import cv2 as cv
from init import *
from math import  *

class foots(): #足类
    def __init__(self,roots_s,angle_s,length): #初始位置,初始角度:两个二维数组;长度
        self.roots = roots_s
        self.earthing  = [length*cos(angle_s),length*sin(angle_s)]
    def draws(self):


class spider :
