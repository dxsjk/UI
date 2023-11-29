# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listwidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1220, 848)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(130, 130, 941, 551))
        self.listWidget.setObjectName("listWidget")
        self.dele = QtWidgets.QPushButton(Form)
        self.dele.setGeometry(QtCore.QRect(270, 60, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dele.setFont(font)
        self.dele.setStyleSheet("border-radius:25px;border:1px groove blue ")
        self.dele.setObjectName("dele")
        self.download = QtWidgets.QPushButton(Form)
        self.download.setGeometry(QtCore.QRect(130, 60, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.download.setFont(font)
        self.download.setStyleSheet("border-radius:25px;border:1px groove blue ")
        self.download.setObjectName("download")
        self.seek = QtWidgets.QPushButton(Form)
        self.seek.setGeometry(QtCore.QRect(380, 60, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.seek.setFont(font)
        self.seek.setStyleSheet("border-radius:25px;border:1px groove blue ")
        self.seek.setObjectName("seek")
        self.seek_content = QtWidgets.QLineEdit(Form)
        self.seek_content.setGeometry(QtCore.QRect(510, 70, 231, 31))
        self.seek_content.setObjectName("seek_content")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(530, 0, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.play_slider = Slider(Form)
        self.play_slider.setGeometry(QtCore.QRect(140, 720, 871, 22))
        self.play_slider.setOrientation(QtCore.Qt.Horizontal)
        self.play_slider.setObjectName("play_slider")
        self.music_name = QtWidgets.QLabel(Form)
        self.music_name.setGeometry(QtCore.QRect(140, 690, 72, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.music_name.setFont(font)
        self.music_name.setObjectName("music_name")
        self.next_music = QtWidgets.QPushButton(Form)
        self.next_music.setGeometry(QtCore.QRect(250, 760, 61, 41))
        self.next_music.setStyleSheet("border:none;")
        self.next_music.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/下一首.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_music.setIcon(icon)
        self.next_music.setIconSize(QtCore.QSize(32, 32))
        self.next_music.setObjectName("next_music")
        self.previous_music = QtWidgets.QPushButton(Form)
        self.previous_music.setGeometry(QtCore.QRect(130, 760, 61, 41))
        self.previous_music.setStyleSheet("border:none;")
        self.previous_music.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/上一首.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous_music.setIcon(icon1)
        self.previous_music.setIconSize(QtCore.QSize(32, 32))
        self.previous_music.setObjectName("previous_music")
        self.play_pause = QtWidgets.QPushButton(Form)
        self.play_pause.setGeometry(QtCore.QRect(190, 760, 61, 41))
        self.play_pause.setStyleSheet("border:none;")
        self.play_pause.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/播放.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_pause.setIcon(icon2)
        self.play_pause.setIconSize(QtCore.QSize(32, 32))
        self.play_pause.setObjectName("play_pause")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(380, 760, 72, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(460, 780, 261, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.dele.setText(_translate("Form", "删"))
        self.download.setText(_translate("Form", "下载"))
        self.seek.setText(_translate("Form", "查"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#0000ff;\">简易音乐播放器</span></p></body></html>"))
        self.music_name.setText(_translate("Form", "音乐:"))
        self.label_2.setText(_translate("Form", "音量："))
from control.RadiusSlider import Slider
import img_rc