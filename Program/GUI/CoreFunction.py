from GUI.GUIFunction import *
from Spider.SpiderObject import Spider
from Library.caculater import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import cv2
import numpy as np
import time


class CoreFunction(GUIFunction):
    def __init__(self):
        super(GUIFunction, self).__init__()
        self.controllerThread = ControllerThread()
        self.controllerThread.log_update.connect(self.log_update)
        self.controllerThread.draw_foot.connect(self.draw_foot)
        self.controllerThread.draw_spider.connect(self.draw_spider)
        self.controllerThread.now_state = 'init'  # 创建一个全局变量，用于与控制线程的沟通
        self.controllerThread.start()
        self.log_update("动画线程已启动", 'success')

    @error_decorator
    def draw_foot(self, order, frame):
        self.__dict__[f'Foot_{order}Image'].setPixmap(QPixmap.fromImage(frame))


    def draw_spider(self, frame):
        self.SpiderImage.setPixmap(QPixmap.fromImage(frame))


class ControllerThread(QThread):
    draw_foot = pyqtSignal(int, QImage)
    draw_spider = pyqtSignal(QImage)
    log_update = pyqtSignal(str, str)

    def __init__(self):
        super(ControllerThread, self).__init__()
        self.spider = Spider([250, 250], 90)



    def run(self):
        while True:
            time.sleep(1)
            if self.now_state == 'finish':
                pass
            if self.now_state == 'init':
                self.update_all_foot_image()
                self.update_spider_image()
                self.log_update.emit('创建六足机器人对象成功', 'success')
                self.now_state = 'finish'
            if self.now_state == 'stop':
                pass
            if self.now_state == 'forward':
                pass
            if self.now_state == 'go_back':
                pass
            if self.now_state == 'turn_right':
                pass
            if self.now_state == 'turn_left':
                pass

    def opencv_to_Qframe(self, img):
        """
        将OpenCV格式的图片转换为Qframe
        """
        try:
            image_height, image_width, image_depth = img.shape
            video_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            Qframe = QImage(video_frame.data, image_width, image_height,  # 创建QImage格式的图像，并读入图像信息
                            image_width * image_depth,
                            QImage.Format_RGB888)
            return Qframe
        except Exception as error:
            print(error)

    @error_decorator
    def update_all_foot_image(self):
        for order in range(1, 7):
            background_img = create_back_img(300, 300, grey)
            img = self.spider.__dict__[f'Leg{order}'].draw(background_img)
            img = cv2.resize(img, (160, 160))
            Qframes = self.opencv_to_Qframe(img)
            time.sleep(0.01)
            self.draw_foot.emit(order, Qframes)

    @error_decorator
    def update_spider_image(self):
        background_img = create_back_img(500, 500, grey)
        img = self.spider.draw(background_img)
        img = cv2.resize(img, (520, 520))
        Qframes = self.opencv_to_Qframe(img)
        self.draw_spider.emit(Qframes)
