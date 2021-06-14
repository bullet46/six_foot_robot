from Cilent.GUI.GUIFunction import *
from Cilent.Spider.SpiderObject import Spider
from Cilent.Library.caculater import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import cv2
from Cilent.Spider import MoveScript


class CoreFunction(GUIFunction):
    def __init__(self):
        super(CoreFunction, self).__init__()
        self.yolo_switch = False
        self.video_switch = False
        # 渲染线程控制
        self.controllerThread = ControllerThread()
        self.controllerThread.log_update.connect(self.log_update)
        self.controllerThread.draw_foot.connect(self.draw_foot)
        self.controllerThread.draw_spider.connect(self.draw_spider)
        self.controllerThread.update_joint.connect(self.update_all_angle)
        self.controllerThread.now_state = 'init'  # 创建一个全局变量，用于与控制线程的沟通
        self.controllerThread.start()
        # 点击事件
        self.forward.clicked.connect(self.forward_script)
        self.stop.clicked.connect(self.stop_script)
        self.back.clicked.connect(self.back_script)
        self.turn_left.clicked.connect(self.turn_left_script)
        self.turn_right.clicked.connect(self.turn_right_script)
        self.ChangeDisplay.clicked.connect(self.change_display)
        self.AddYolo.clicked.connect(self.yolo_switch_script)
        # 图传线程控制
        self.VideoThread = VideoTransThread()
        self.VideoThread.draw_video.connect(self.draw_video)
        self.VideoThread.link_state.connect(self.up_date_device_state)
        self.VideoThread.log_update.connect(self.log_update)
        self.VideoThread.start()

    def change_display(self):
        if self.video_switch is False:
            self.video_switch = True

        else:
            self.video_switch = False
            self.controllerThread.update_spider_image()

    def yolo_switch_script(self):
        if self.yolo_switch == False:
            self.AddYolo.setText("关闭Yolo检测")
            self.yolo_switch = True
            self.VideoThread.yolo_switch = True
        else:
            self.AddYolo.setText("启用Yolo检测")
            self.yolo_switch = False
            self.VideoThread.yolo_switch = False

    def draw_foot(self, order, frame):
        self.__dict__[f'Foot_{order}Image'].setPixmap(QPixmap.fromImage(frame))

    def draw_spider(self, frames):
        if self.video_switch is False:
            self.SpiderImage.setPixmap(QPixmap.fromImage(frames))

    def draw_video(self, frames):
        if self.video_switch is True:
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
    update_joint = pyqtSignal(list)

    def __init__(self):
        super(ControllerThread, self).__init__()
        self.now_state = 'init'

    def run(self):
        self.spider = Spider([500, 250], 90)
        while True:
            if self.now_state == 'finish':
                pass

            if self.now_state == 'init':
                QThread.msleep(100)
                self.update_spider_image()
                self.update_all_foot_image()
                self.log_update.emit('创建六足机器人对象成功', 'success')
                self.now_state = 'finish'

            if self.now_state == 'stop':
                pass

            if self.now_state == 'forward':
                self.log_update.emit('启动向前脚本', 'normal')
                self.forward_script()
                self.log_update.emit('运行完成', 'normal')
                self.now_state = 'finish'

            if self.now_state == 'go_back':
                self.log_update.emit('启动向后脚本', 'normal')
                self.spider = Spider([500, 750], 90)
                self.backward_script()
                self.now_state = 'finish'
                self.log_update.emit('运行完成', 'normal')
                pass

            if self.now_state == 'turn_right':
                self.log_update.emit('启动右转脚本', 'normal')
                self.spider = Spider([500, 500], 90)
                self.turn_right_script()
                self.now_state = 'finish'
                self.log_update.emit('运行完成', 'normal')
                pass

            if self.now_state == 'turn_left':
                self.log_update.emit('启动左转脚本', 'normal')
                self.spider = Spider([500, 500], 90)
                self.turn_left_script()
                self.now_state = 'finish'
                self.log_update.emit('运行完成', 'normal')
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
            QThread.msleep(40)

    @error_decorator
    def update_spider_image(self):
        background_img = create_back_img(1000, 1000, grey)
        img = self.spider.draw(background_img)
        img = cv2.resize(img, (520, 520))
        Qframes = self.opencv_to_Qframe(img)
        self.draw_spider.emit(Qframes)
        QThread.msleep(200)

    @error_decorator
    def forward_script(self):
        self.update_joint_angle()
        MoveScript.forward_script(self, self.spider)

    @error_decorator
    def backward_script(self):
        self.update_joint_angle()
        MoveScript.backward_script(self, self.spider)

    @error_decorator
    def turn_right_script(self):
        self.update_joint_angle()
        MoveScript.turn_right_script(self, self.spider)

    @error_decorator
    def turn_left_script(self):
        self.update_joint_angle()
        MoveScript.turn_left_script(self, self.spider)

    def update_joint_angle_to_message(self):
        joint_list = [0] * 18
        joint_bias_list = [135, 45, 0, 315, 225, 180]  # 原坐标系下的偏置
        for i in range(1, 7):
            joint_list[i - 1] = (self.spider.__dict__[f'Leg{i}'].cod0_angle - joint_bias_list[i - 1] + (
                self.spider.forward) % 360) % 360
            joint_list[i - 1 + 6] = self.spider.__dict__[f'Leg{i}'].cod1_angle
            joint_list[i - 1 + 12] = self.spider.__dict__[f'Leg{i}'].cod2_angle
        self.log_update.emit(str(joint_list), 'normal')

    def update_joint_angle(self):
        joint_list = [0] * 18
        for i in range(1, 7):
            joint_list[i - 1] = self.spider.__dict__[f'Leg{i}'].cod0_angle
            joint_list[i - 1 + 6] = self.spider.__dict__[f'Leg{i}'].cod1_angle
            joint_list[i - 1 + 12] = self.spider.__dict__[f'Leg{i}'].cod2_angle

        self.update_joint.emit(joint_list)


class VideoTransThread(QThread):
    # 视频传输线程
    draw_video = pyqtSignal(QImage)
    link_state = pyqtSignal(int)
    log_update = pyqtSignal(str, str)

    def __init__(self):
        super(VideoTransThread, self).__init__()
        self.yolo_switch = False

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

    def run(self):
        while True:
            try:
                src = f'http://{link_ip}:8080/?action=snapshot'
                cap = cv2.VideoCapture(src)
                ok, frame = cap.read()
                if ok:
                    self.link_state.emit(1)
                    img = cv2.resize(frame, (520, 520))
                    Qframes = self.opencv_to_Qframe(img)
                    self.draw_video.emit(Qframes)
            except Exception as e:
                self.link_state.emit(0)
                self.log_update.emit(str(e), 'error')
            QThread.msleep(int(1 / 24 * 1000))
