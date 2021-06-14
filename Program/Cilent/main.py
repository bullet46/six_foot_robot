import sys
from PyQt5.QtWidgets import QApplication
from Cilent.GUI.launcher import Launcher

# 用于启动QT应用
if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = Launcher()
    windows.show()
    sys.exit(app.exec_())
