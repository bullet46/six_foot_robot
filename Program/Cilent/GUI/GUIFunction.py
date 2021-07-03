from GUI.MainWindow import Ui_MainWindow
import time


def error_decorator(func):
    """
    error汇报装饰器
    """

    def error_emit(self, *args, **kwargs):
        try:
            func(self, *args, **kwargs)
        except Exception as error:
            print(error)
            self.log_update.emit(repr(error), 'error')

    return error_emit


class GUIFunction(Ui_MainWindow):
    def __init__(self):
        super(GUIFunction, self).__init__()
        self.short_cut_bind()
        self.log_update("程序启动正常")

    def short_cut_bind(self):
        self.forward.setShortcut('w')
        self.back.setShortcut('s')
        self.turn_left.setShortcut('a')
        self.turn_right.setShortcut('d')
        self.stop.setShortcut('p')
        self.TakePhoto.setShortcut(' ')
        self.TakePhoto.clicked.connect(self.take_photo)

    def log_update(self, msg, state='normal'):
        """
        更新日志
        """
        color_map = {
            'normal': 'black',
            'success': 'green',
            'error': 'red'
        }
        try:

            text = """<font face="微软雅黑" size="4" color="{color}">{now_time} {msg}</font>""".format(
                now_time=time.strftime("%Y-%m-%d %H:%M:%S:", time.localtime()),
                color=color_map[state], msg=msg)
            self.textBrowser.append(text)
        except Exception as error:
            print(error)

    @error_decorator
    def update_all_angle(self, angle_list):
        for i in range(1, 19):
            self.__dict__[f'joint_{i}'].display(angle_list[i - 1])

    def up_date_device_state(self, state):
        # 上传设备状态
        # state:1 正常，state:0 掉线
        if state == 0:
            text = """<font face="微软雅黑" size="6" color="red">设备掉线</font>"""
        else:
            text = """<font face="微软雅黑" size="6" color="green">连接正常</font>"""
        self.LinkDetector.setText(text)

    def take_photo(self):
        pix = self.SpiderImage.pixmap()
        print(type(pix))
        now_time = time.strftime("%Y_%m_%d_%H %M %S", time.localtime())
        if self.video_switch is True:
            pix.save(f'Photos/{now_time}.jpg', 'jpg', quality=100000)
