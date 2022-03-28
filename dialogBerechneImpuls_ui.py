# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogBerechneImpuls.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgBerechneImpuls(object):
    def setupUi(self, dlgBerechneImpuls):
        if not dlgBerechneImpuls.objectName():
            dlgBerechneImpuls.setObjectName(u"dlgBerechneImpuls")
        dlgBerechneImpuls.resize(310, 303)
        self.buttonBox = QDialogButtonBox(dlgBerechneImpuls)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 241, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.pbBerechne = QPushButton(dlgBerechneImpuls)
        self.pbBerechne.setObjectName(u"pbBerechne")
        self.pbBerechne.setGeometry(QRect(30, 120, 88, 34))
        self.layoutWidget = QWidget(dlgBerechneImpuls)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 40, 241, 34))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbMasse = QLabel(self.layoutWidget)
        self.lbMasse.setObjectName(u"lbMasse")

        self.horizontalLayout.addWidget(self.lbMasse)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.leMasse = QLineEdit(self.layoutWidget)
        self.leMasse.setObjectName(u"leMasse")
        self.leMasse.setStyleSheet(u"QLineEdit { background-color: yellow }")

        self.horizontalLayout.addWidget(self.leMasse)

        self.layoutWidget1 = QWidget(dlgBerechneImpuls)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 80, 241, 34))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbGeschwindigkeit = QLabel(self.layoutWidget1)
        self.lbGeschwindigkeit.setObjectName(u"lbGeschwindigkeit")

        self.horizontalLayout_2.addWidget(self.lbGeschwindigkeit)

        self.leGeschwindigkeit = QLineEdit(self.layoutWidget1)
        self.leGeschwindigkeit.setObjectName(u"leGeschwindigkeit")
        self.leGeschwindigkeit.setStyleSheet(u"QLineEdit { background-color: yellow }")

        self.horizontalLayout_2.addWidget(self.leGeschwindigkeit)

        self.layoutWidget2 = QWidget(dlgBerechneImpuls)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(30, 160, 241, 34))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lbImpuls = QLabel(self.layoutWidget2)
        self.lbImpuls.setObjectName(u"lbImpuls")

        self.horizontalLayout_3.addWidget(self.lbImpuls)

        self.leImpulsErgebnis = QLineEdit(self.layoutWidget2)
        self.leImpulsErgebnis.setObjectName(u"leImpulsErgebnis")
        self.leImpulsErgebnis.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.leImpulsErgebnis)


        self.retranslateUi(dlgBerechneImpuls)
        self.buttonBox.accepted.connect(dlgBerechneImpuls.accept)

        QMetaObject.connectSlotsByName(dlgBerechneImpuls)
    # setupUi

    def retranslateUi(self, dlgBerechneImpuls):
        dlgBerechneImpuls.setWindowTitle(QCoreApplication.translate("dlgBerechneImpuls", u"Berechne Impuls", None))
        self.pbBerechne.setText(QCoreApplication.translate("dlgBerechneImpuls", u"Berechnen", None))
        self.lbMasse.setText(QCoreApplication.translate("dlgBerechneImpuls", u"Masse m:", None))
        self.lbGeschwindigkeit.setText(QCoreApplication.translate("dlgBerechneImpuls", u"Geschwindigkeit v:", None))
        self.lbImpuls.setText(QCoreApplication.translate("dlgBerechneImpuls", u"Impuls [Hy]:", None))
    # retranslateUi

