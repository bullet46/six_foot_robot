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
        self.forward.clicked.connect(self.forward_script)
        self.stop.clicked.connect(self.stop_script)
        self.back.clicked.connect(self.back_script)
        self.turn_left.clicked.connect(self.turn_left_script)
        self.turn_right.clicked.connect(self.turn_right_script)

    def draw_foot(self, order, frame):
        self.__dict__[f'Foot_{order}Image'].setPixmap(QPixmap.fromImage(frame))

    def draw_spider(self, frames):
        self.SpiderImage.setPixmap(QPixmap.fromImage(frames))

    def forward_script(self):
        self.controllerThread.now_state = 'forward'

    def stop_script(self):
        self.controllerThread.now_state = 'stop'

    def back_script(self):
        self.controllerThread.now_state = 'go_back'

    def turn_right_script(self):
        self.controllerThread.now_state = 'turn_right'

    def turn_left_script(self):
        self.controllerThread.now_state = 'turn_left'


class ControllerThread(QThread):
    draw_foot = pyqtSignal(int, QImage)
    draw_spider = pyqtSignal(QImage)
    log_update = pyqtSignal(str, str)

    def __init__(self):
        super(ControllerThread, self).__init__()
        self.now_state = 'init'

    def run(self):
        self.spider = Spider([500, 250], 90)
        while True:
            if self.now_state == 'finish':
                pass

            if self.now_state == 'init':
                self.update_spider_image()
                self.update_all_foot_image()
                self.log_update.emit('创建六足机器人对象成功', 'success')
                self.now_state = 'finish'

            if self.now_state == 'stop':
                pass

            if self.now_state == 'forward':
                self.log_update.emit('启动向前脚本', 'normal')
                self.forward_script()
                self.now_state = 'finish'

            if self.now_state == 'go_back':
                pass

            if self.now_state == 'turn_right':
                pass

            if self.now_state == 'turn_left':
                pass

            QThread.msleep(50)

    def opencv_to_Qframe(self, img):
        """
        将OpenCV格式的图片转换为Qframe
        """
        image_height, image_width, image_depth = img.shape
        video_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        Qframe = QImage(video_frame.data, image_width, image_height,  # 创建QImage格式的图像，并读入图像信息
                        image_width * image_depth,
                        QImage.Format_RGB888)
        return Qframe

    @error_decorator
    def update_all_foot_image(self):
        for order in range(1, 7):
            background_img = create_back_img(300, 300, grey)
            img = self.spider.__dict__[f'Leg{order}'].draw(background_img)
            img = cv2.resize(img, (160, 160))
            Qframes = self.opencv_to_Qframe(img)
            self.draw_foot.emit(order, Qframes)
            QThread.msleep(50)

    @error_decorator
    def update_spider_image(self):
        QThread.msleep(50)
        background_img = create_back_img(1000, 1000, grey)
        img = self.spider.draw(background_img)
        img = cv2.resize(img, (520, 520))
        Qframes = self.opencv_to_Qframe(img)
        self.draw_spider.emit(Qframes)
        QThread.msleep(200)

    def forward_script(self):
        self.spider.move_spider([500, 300], 90)
        self.spider.Leg1.fixed_state = False
        self.spider.Leg1.mov_support_point(0, 20)
        self.spider.Leg1.calculate_cod(self.spider.Leg1.root_point, self.spider.Leg1.support_point, 30)
        self.spider.Leg3.fixed_state = False
        self.spider.Leg3.mov_support_point(0, 80)
        self.spider.Leg3.calculate_cod(self.spider.Leg2.root_point, self.spider.Leg2.support_point, 30)
        self.spider.Leg5.fixed_state = False
        self.spider.Leg5.mov_support_point(0, 80)
        self.spider.Leg5.calculate_cod(self.spider.Leg3.root_point, self.spider.Leg3.support_point, 30)

        self.spider.Leg2.calculate_cod(self.spider.Leg2.root_point, self.spider.Leg2.support_point, 50)
        self.spider.Leg4.calculate_cod(self.spider.Leg4.root_point, self.spider.Leg4.support_point, 50)
        self.spider.Leg6.calculate_cod(self.spider.Leg6.root_point, self.spider.Leg6.support_point, 50)
        self.update_all_foot_image()
        self.update_spider_image()

        QThread.msleep(300)
        self.spider.move_spider([500, 300], 90)
        self.spider.Leg1.fixed_state = True
        self.spider.Leg1.calculate_cod(self.spider.Leg1.root_point, self.spider.Leg1.support_point, 50)
        self.spider.Leg3.fixed_state = True
        self.spider.Leg3.calculate_cod(self.spider.Leg2.root_point, self.spider.Leg2.support_point, 50)
        self.spider.Leg5.fixed_state = True
        self.spider.Leg5.calculate_cod(self.spider.Leg2.root_point, self.spider.Leg2.support_point, 50)

        self.spider.Leg2.fixed_state = False
        self.spider.Leg4.fixed_state = False
        self.spider.Leg6.fixed_state = False
        self.update_all_foot_image()
        self.update_spider_image()

        QThread.msleep(300)
        self.spider.move_spider([500, 350], 90)
        self.spider.Leg2.fixed_state = False
        self.spider.Leg2.mov_support_point(0, 20)
        self.spider.Leg2.calculate_cod(self.spider.Leg2.root_point, self.spider.Leg2.support_point, 30)
        self.spider.Leg4.fixed_state = False
        self.spider.Leg4.mov_support_point(0, 80)
        self.spider.Leg4.calculate_cod(self.spider.Leg4.root_point, self.spider.Leg4.support_point, 30)
        self.spider.Leg6.fixed_state = False
        self.spider.Leg6.mov_support_point(0, 80)
        self.spider.Leg6.calculate_cod(self.spider.Leg6.root_point, self.spider.Leg6.support_point, 30)

        self.spider.Leg2.fixed_state = False
        self.spider.Leg4.fixed_state = False
        self.spider.Leg6.fixed_state = False
        self.update_all_foot_image()
        self.update_spider_image()

        pass
