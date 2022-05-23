# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogSimSonnensystem.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgSimSonnensystem(object):
    def setupUi(self, dlgSimSonnensystem):
        if not dlgSimSonnensystem.objectName():
            dlgSimSonnensystem.setObjectName(u"dlgSimSonnensystem")
        dlgSimSonnensystem.resize(605, 454)
        self.pbBerechne = QPushButton(dlgSimSonnensystem)
        self.pbBerechne.setObjectName(u"pbBerechne")
        self.pbBerechne.setGeometry(QRect(10, 340, 84, 34))
        self.layoutWidget = QWidget(dlgSimSonnensystem)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 410, 555, 36))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pbGraphik = QPushButton(self.layoutWidget)
        self.pbGraphik.setObjectName(u"pbGraphik")

        self.horizontalLayout_3.addWidget(self.pbGraphik)

        self.horizontalSpacer = QSpacerItem(98, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.buttonBox = QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.horizontalLayout_3.addWidget(self.buttonBox)

        self.verticalLayoutWidget = QWidget(dlgSimSonnensystem)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(660, 80, 391, 361))
        self.lyGraph = QVBoxLayout(self.verticalLayoutWidget)
        self.lyGraph.setObjectName(u"lyGraph")
        self.lyGraph.setContentsMargins(0, 0, 0, 0)
        self.line = QFrame(dlgSimSonnensystem)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(630, 10, 20, 441))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.lbGraphExtensionTitel = QLabel(dlgSimSonnensystem)
        self.lbGraphExtensionTitel.setObjectName(u"lbGraphExtensionTitel")
        self.lbGraphExtensionTitel.setGeometry(QRect(660, 30, 321, 31))
        self.lbGraphExtensionTitel.setStyleSheet(u"QLabel{\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.twSolarSystemObjects = QTableWidget(dlgSimSonnensystem)
        if (self.twSolarSystemObjects.columnCount() < 8):
            self.twSolarSystemObjects.setColumnCount(8)
        if (self.twSolarSystemObjects.rowCount() < 1):
            self.twSolarSystemObjects.setRowCount(1)
        self.twSolarSystemObjects.setObjectName(u"twSolarSystemObjects")
        self.twSolarSystemObjects.setGeometry(QRect(10, 20, 581, 311))
        self.twSolarSystemObjects.setRowCount(1)
        self.twSolarSystemObjects.setColumnCount(8)
        self.twSolarSystemObjects.horizontalHeader().setDefaultSectionSize(69)

        self.retranslateUi(dlgSimSonnensystem)
        self.buttonBox.accepted.connect(dlgSimSonnensystem.accept)

        QMetaObject.connectSlotsByName(dlgSimSonnensystem)
    # setupUi

    def retranslateUi(self, dlgSimSonnensystem):
        dlgSimSonnensystem.setWindowTitle(QCoreApplication.translate("dlgSimSonnensystem", u"Simualtion des Sonnensystems", None))
        self.pbBerechne.setText(QCoreApplication.translate("dlgSimSonnensystem", u"Berechne", None))
        self.pbGraphik.setText(QCoreApplication.translate("dlgSimSonnensystem", u"Graph >>>", None))
        self.lbGraphExtensionTitel.setText(QCoreApplication.translate("dlgSimSonnensystem", u"Graphik Titel", None))
    # retranslateUi

