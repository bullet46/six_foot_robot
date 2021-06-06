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
        self.log_update("程序启动正常")

    def log_update(self, msg, state='normal'):
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
