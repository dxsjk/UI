# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'slider.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(803, 565)

        self.r.setGeometry(QtCore.QRect(150, 230, 541, 22))
        self.r.setOrientation(QtCore.Qt.Horizontal)
        self.r.setObjectName("r")
        self.g = QtWidgets.QSlider(Form)
        self.g.setGeometry(QtCore.QRect(150, 300, 541, 22))
        self.g.setOrientation(QtCore.Qt.Horizontal)
        self.g.setObjectName("g")
        self.b = QtWidgets.QSlider(Form)
        self.b.setGeometry(QtCore.QRect(150, 370, 541, 22))
        self.b.setOrientation(QtCore.Qt.Horizontal)
        self.b.setObjectName("b")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 370, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 300, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 220, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 440, 72, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.font_size = QtWidgets.QSlider(Form)
        self.font_size.setGeometry(QtCore.QRect(150, 440, 521, 22))
        self.font_size.setOrientation(QtCore.Qt.Horizontal)
        self.font_size.setObjectName("font_size")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(130, 50, 481, 141))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "b："))
        self.label_2.setText(_translate("Form", "g："))
        self.label_3.setText(_translate("Form", "r："))
        self.label_4.setText(_translate("Form", "大小："))
        self.label_5.setText(_translate("Form", "测试"))
