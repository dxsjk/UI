# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ad.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.sure = QtWidgets.QPushButton(Form)
        self.sure.setGeometry(QtCore.QRect(400, 150, 93, 28))
        self.sure.setObjectName("sure")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.sure.setText(_translate("Form", "PushButton"))


