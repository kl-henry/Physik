# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogTest.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgTest(object):
    def setupUi(self, dlgTest):
        if not dlgTest.objectName():
            dlgTest.setObjectName(u"dlgTest")
        dlgTest.resize(733, 302)
        self.buttonBox = QDialogButtonBox(dlgTest)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(170, 240, 201, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.pbBerechne = QPushButton(dlgTest)
        self.pbBerechne.setObjectName(u"pbBerechne")
        self.pbBerechne.setGeometry(QRect(30, 240, 88, 34))
        self.verticalLayoutWidget = QWidget(dlgTest)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 30, 160, 191))
        self.vl_1 = QVBoxLayout(self.verticalLayoutWidget)
        self.vl_1.setObjectName(u"vl_1")
        self.vl_1.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.vl_1.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.vl_1.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.vl_1.addWidget(self.pushButton)

        self.verticalLayoutWidget_2 = QWidget(dlgTest)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(400, 30, 311, 191))
        self.lyGraph = QVBoxLayout(self.verticalLayoutWidget_2)
        self.lyGraph.setObjectName(u"lyGraph")
        self.lyGraph.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget_3 = QWidget(dlgTest)
        self.verticalWidget_3.setObjectName(u"verticalWidget_3")
        self.verticalWidget_3.setGeometry(QRect(210, 30, 160, 191))
        self.vl_2 = QVBoxLayout(self.verticalWidget_3)
        self.vl_2.setObjectName(u"vl_2")
        self.pushButton_4 = QPushButton(self.verticalWidget_3)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.vl_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.verticalWidget_3)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.vl_2.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.verticalWidget_3)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.vl_2.addWidget(self.pushButton_6)


        self.retranslateUi(dlgTest)
        self.buttonBox.accepted.connect(dlgTest.accept)
        self.buttonBox.rejected.connect(dlgTest.reject)

        QMetaObject.connectSlotsByName(dlgTest)
    # setupUi

    def retranslateUi(self, dlgTest):
        dlgTest.setWindowTitle(QCoreApplication.translate("dlgTest", u"Test Dialog", None))
        self.pbBerechne.setText(QCoreApplication.translate("dlgTest", u"Berechne", None))
        self.pushButton_3.setText(QCoreApplication.translate("dlgTest", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("dlgTest", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("dlgTest", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("dlgTest", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("dlgTest", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("dlgTest", u"PushButton", None))
    # retranslateUi

