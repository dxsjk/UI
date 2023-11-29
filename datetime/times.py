# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'times.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(890, 536)
        self.data_ming = QtWidgets.QDateTimeEdit(Form)
        self.data_ming.setGeometry(QtCore.QRect(70, 60, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.data_ming.setFont(font)
        self.data_ming.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.data_ming.setCalendarPopup(True)
        self.data_ming.setObjectName("data_ming")
        self.ciphertext = QtWidgets.QLabel(Form)
        self.ciphertext.setGeometry(QtCore.QRect(100, 330, 431, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ciphertext.setFont(font)
        self.ciphertext.setObjectName("ciphertext")
        self.plaintext = QtWidgets.QLabel(Form)
        self.plaintext.setGeometry(QtCore.QRect(100, 260, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.plaintext.setFont(font)
        self.plaintext.setObjectName("plaintext")
        self.time_tt = QtWidgets.QLabel(Form)
        self.time_tt.setGeometry(QtCore.QRect(100, 180, 461, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.time_tt.setFont(font)
        self.time_tt.setObjectName("time_tt")
        self.end_time = QtWidgets.QLabel(Form)
        self.end_time.setGeometry(QtCore.QRect(100, 410, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.end_time.setFont(font)
        self.end_time.setObjectName("end_time")
        self.key = QtWidgets.QDateEdit(Form)
        self.key.setGeometry(QtCore.QRect(500, 70, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.key.setFont(font)
        self.key.setCalendarPopup(True)
        self.key.setTimeSpec(QtCore.Qt.LocalTime)
        self.key.setObjectName("key")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.data_ming.setDisplayFormat(_translate("Form", "yyyy/MM/dd HH:mm:ss"))
        self.ciphertext.setText(_translate("Form", "密文："))
        self.plaintext.setText(_translate("Form", "明文："))
        self.time_tt.setText(_translate("Form", "时间戳："))
        self.end_time.setText(_translate("Form", "解密的时间："))
        self.key.setDisplayFormat(_translate("Form", "yyyy-MM-dd"))
