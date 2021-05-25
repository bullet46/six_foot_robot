# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 718)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 718))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 718))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#Foot_1,#Foot_2,#Foot_3,#Foot_4,#Foot_5,#Foot_6{\n"
                                         "background-color: rgb(85, 85, 127);\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.Foot_1Image = QtWidgets.QLabel(self.centralwidget)
        self.Foot_1Image.setGeometry(QtCore.QRect(20, 20, 160, 160))
        self.Foot_1Image.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.Foot_1Image.setObjectName("Foot_1Image")
        self.Foot_2Image = QtWidgets.QLabel(self.centralwidget)
        self.Foot_2Image.setGeometry(QtCore.QRect(20, 200, 160, 160))
        self.Foot_2Image.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.Foot_2Image.setObjectName("Foot_2Image")
        self.Foot_5Image = QtWidgets.QLabel(self.centralwidget)
        self.Foot_5Image.setGeometry(QtCore.QRect(720, 200, 160, 160))
        self.Foot_5Image.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.Foot_5Image.setObjectName("Foot_5Image")
        self.Foot_6Image = QtWidgets.QLabel(self.centralwidget)
        self.Foot_6Image.setGeometry(QtCore.QRect(720, 380, 160, 160))
        self.Foot_6Image.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.Foot_6Image.setObjectName("Foot_6Image")
        self.Foot_4Image = QtWidgets.QLabel(self.centralwidget)
        self.Foot_4Image.setGeometry(QtCore.QRect(720, 20, 160, 160))
        self.Foot_4Image.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.Foot_4Image.setObjectName("Foot_4Image_2")
        self.Foot_3Image = QtWidgets.QLabel(self.centralwidget)
        self.Foot_3Image.setGeometry(QtCore.QRect(20, 380, 160, 160))
        self.Foot_3Image.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.Foot_3Image.setObjectName("Foot_3Image")
        self.SpiderImage = QtWidgets.QLabel(self.centralwidget)
        self.SpiderImage.setGeometry(QtCore.QRect(190, 20, 520, 520))
        self.SpiderImage.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.SpiderImage.setObjectName("SpiderImage")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 550, 1251, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.forward = QtWidgets.QPushButton(self.centralwidget)
        self.forward.setGeometry(QtCore.QRect(1070, 190, 60, 60))
        self.forward.setObjectName("forward")
        self.turn_left = QtWidgets.QPushButton(self.centralwidget)
        self.turn_left.setGeometry(QtCore.QRect(990, 270, 60, 60))
        self.turn_left.setObjectName("turn_left")
        self.turn_right = QtWidgets.QPushButton(self.centralwidget)
        self.turn_right.setGeometry(QtCore.QRect(1150, 270, 60, 60))
        self.turn_right.setObjectName("turn_right")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(1070, 350, 60, 60))
        self.back.setObjectName("back")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(1070, 270, 60, 60))
        self.stop.setObjectName("stop")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 570, 1241, 121))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "六足机器人步态逆解demo"))
        self.Foot_1Image.setText(_translate("MainWindow", ""))
        self.Foot_2Image.setText(_translate("MainWindow", ""))
        self.Foot_5Image.setText(_translate("MainWindow", ""))
        self.Foot_6Image.setText(_translate("MainWindow", ""))
        self.Foot_4Image.setText(_translate("MainWindow", ""))
        self.Foot_3Image.setText(_translate("MainWindow", ""))
        self.SpiderImage.setText(_translate("MainWindow", ""))
        self.forward.setText(_translate("MainWindow", "前进"))
        self.turn_left.setText(_translate("MainWindow", "左转"))
        self.turn_right.setText(_translate("MainWindow", "右转"))
        self.back.setText(_translate("MainWindow", "后退"))
        self.stop.setText(_translate("MainWindow", "停止"))
