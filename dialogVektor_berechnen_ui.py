# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogVektor_berechnen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgVektorRechnung(object):
    def setupUi(self, dlgVektorRechnung):
        if not dlgVektorRechnung.objectName():
            dlgVektorRechnung.setObjectName(u"dlgVektorRechnung")
        dlgVektorRechnung.resize(573, 294)
        self.buttonBox = QDialogButtonBox(dlgVektorRechnung)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(260, 230, 271, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.layoutWidget = QWidget(dlgVektorRechnung)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 30, 521, 181))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.gbVektoren = QGroupBox(self.layoutWidget)
        self.gbVektoren.setObjectName(u"gbVektoren")
        self.layoutWidget1 = QWidget(self.gbVektoren)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 61, 131, 110))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbX = QLabel(self.layoutWidget1)
        self.lbX.setObjectName(u"lbX")

        self.horizontalLayout_2.addWidget(self.lbX)

        self.leX = QLineEdit(self.layoutWidget1)
        self.leX.setObjectName(u"leX")

        self.horizontalLayout_2.addWidget(self.leX)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbY = QLabel(self.layoutWidget1)
        self.lbY.setObjectName(u"lbY")

        self.horizontalLayout_3.addWidget(self.lbY)

        self.leY = QLineEdit(self.layoutWidget1)
        self.leY.setObjectName(u"leY")

        self.horizontalLayout_3.addWidget(self.leY)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbZ = QLabel(self.layoutWidget1)
        self.lbZ.setObjectName(u"lbZ")

        self.horizontalLayout_4.addWidget(self.lbZ)

        self.leZ = QLineEdit(self.layoutWidget1)
        self.leZ.setObjectName(u"leZ")

        self.horizontalLayout_4.addWidget(self.leZ)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_8.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbX_2 = QLabel(self.layoutWidget1)
        self.lbX_2.setObjectName(u"lbX_2")

        self.horizontalLayout_5.addWidget(self.lbX_2)

        self.leX_2 = QLineEdit(self.layoutWidget1)
        self.leX_2.setObjectName(u"leX_2")

        self.horizontalLayout_5.addWidget(self.leX_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbY_2 = QLabel(self.layoutWidget1)
        self.lbY_2.setObjectName(u"lbY_2")

        self.horizontalLayout_6.addWidget(self.lbY_2)

        self.leY_2 = QLineEdit(self.layoutWidget1)
        self.leY_2.setObjectName(u"leY_2")

        self.horizontalLayout_6.addWidget(self.leY_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lbZ_2 = QLabel(self.layoutWidget1)
        self.lbZ_2.setObjectName(u"lbZ_2")

        self.horizontalLayout_7.addWidget(self.lbZ_2)

        self.leZ_2 = QLineEdit(self.layoutWidget1)
        self.leZ_2.setObjectName(u"leZ_2")

        self.horizontalLayout_7.addWidget(self.leZ_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_8.addLayout(self.verticalLayout_3)


        self.horizontalLayout.addWidget(self.gbVektoren)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pbAdd = QPushButton(self.layoutWidget)
        self.pbAdd.setObjectName(u"pbAdd")

        self.verticalLayout.addWidget(self.pbAdd)

        self.pbEinheitsVektor = QPushButton(self.layoutWidget)
        self.pbEinheitsVektor.setObjectName(u"pbEinheitsVektor")

        self.verticalLayout.addWidget(self.pbEinheitsVektor)

        self.pbWinkel = QPushButton(self.layoutWidget)
        self.pbWinkel.setObjectName(u"pbWinkel")

        self.verticalLayout.addWidget(self.pbWinkel)

        self.pbBetrag = QPushButton(self.layoutWidget)
        self.pbBetrag.setObjectName(u"pbBetrag")

        self.verticalLayout.addWidget(self.pbBetrag)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.gbErgebnis = QGroupBox(self.layoutWidget)
        self.gbErgebnis.setObjectName(u"gbErgebnis")
        self.layoutWidget2 = QWidget(self.gbErgebnis)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(50, 30, 81, 142))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lbErgebnis = QLabel(self.layoutWidget2)
        self.lbErgebnis.setObjectName(u"lbErgebnis")

        self.verticalLayout_5.addWidget(self.lbErgebnis)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lbX_3 = QLabel(self.layoutWidget2)
        self.lbX_3.setObjectName(u"lbX_3")

        self.horizontalLayout_9.addWidget(self.lbX_3)

        self.leX_3 = QLineEdit(self.layoutWidget2)
        self.leX_3.setObjectName(u"leX_3")

        self.horizontalLayout_9.addWidget(self.leX_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lbY_3 = QLabel(self.layoutWidget2)
        self.lbY_3.setObjectName(u"lbY_3")

        self.horizontalLayout_10.addWidget(self.lbY_3)

        self.leY_3 = QLineEdit(self.layoutWidget2)
        self.leY_3.setObjectName(u"leY_3")

        self.horizontalLayout_10.addWidget(self.leY_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lbZ_3 = QLabel(self.layoutWidget2)
        self.lbZ_3.setObjectName(u"lbZ_3")

        self.horizontalLayout_11.addWidget(self.lbZ_3)

        self.leZ_3 = QLineEdit(self.layoutWidget2)
        self.leZ_3.setObjectName(u"leZ_3")

        self.horizontalLayout_11.addWidget(self.leZ_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.horizontalLayout.addWidget(self.gbErgebnis)


        self.retranslateUi(dlgVektorRechnung)
        self.buttonBox.accepted.connect(dlgVektorRechnung.accept)

        QMetaObject.connectSlotsByName(dlgVektorRechnung)
    # setupUi

    def retranslateUi(self, dlgVektorRechnung):
        dlgVektorRechnung.setWindowTitle(QCoreApplication.translate("dlgVektorRechnung", u"Vektor Rechnung", None))
        self.gbVektoren.setTitle(QCoreApplication.translate("dlgVektorRechnung", u"Vektoren", None))
        self.lbX.setText(QCoreApplication.translate("dlgVektorRechnung", u"X:", None))
        self.lbY.setText(QCoreApplication.translate("dlgVektorRechnung", u"Y:", None))
        self.lbZ.setText(QCoreApplication.translate("dlgVektorRechnung", u"Z:", None))
        self.lbX_2.setText(QCoreApplication.translate("dlgVektorRechnung", u"X:", None))
        self.lbY_2.setText(QCoreApplication.translate("dlgVektorRechnung", u"Y:", None))
        self.lbZ_2.setText(QCoreApplication.translate("dlgVektorRechnung", u"Z:", None))
        self.pbAdd.setText(QCoreApplication.translate("dlgVektorRechnung", u"Addieren", None))
        self.pbEinheitsVektor.setText(QCoreApplication.translate("dlgVektorRechnung", u"Einheitsvektor", None))
        self.pbWinkel.setText(QCoreApplication.translate("dlgVektorRechnung", u"Winkel", None))
        self.pbBetrag.setText(QCoreApplication.translate("dlgVektorRechnung", u"Betrag", None))
        self.gbErgebnis.setTitle(QCoreApplication.translate("dlgVektorRechnung", u"Ergebnis", None))
        self.lbErgebnis.setText("")
        self.lbX_3.setText(QCoreApplication.translate("dlgVektorRechnung", u"X:", None))
        self.lbY_3.setText(QCoreApplication.translate("dlgVektorRechnung", u"Y:", None))
        self.lbZ_3.setText(QCoreApplication.translate("dlgVektorRechnung", u"Z:", None))
    # retranslateUi

