# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogEinfachesPendel.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgEinfachesPendel(object):
    def setupUi(self, dlgEinfachesPendel):
        if not dlgEinfachesPendel.objectName():
            dlgEinfachesPendel.setObjectName(u"dlgEinfachesPendel")
        dlgEinfachesPendel.resize(598, 454)
        self.pbBerechne = QPushButton(dlgEinfachesPendel)
        self.pbBerechne.setObjectName(u"pbBerechne")
        self.pbBerechne.setGeometry(QRect(10, 170, 84, 34))
        self.layoutWidget = QWidget(dlgEinfachesPendel)
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

        self.verticalLayoutWidget = QWidget(dlgEinfachesPendel)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(660, 80, 391, 361))
        self.lyGraph = QVBoxLayout(self.verticalLayoutWidget)
        self.lyGraph.setObjectName(u"lyGraph")
        self.lyGraph.setContentsMargins(0, 0, 0, 0)
        self.gbDatenEingabe = QGroupBox(dlgEinfachesPendel)
        self.gbDatenEingabe.setObjectName(u"gbDatenEingabe")
        self.gbDatenEingabe.setEnabled(False)
        self.gbDatenEingabe.setGeometry(QRect(10, 60, 571, 91))
        self.gbDatenEingabe.setStyleSheet(u"QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #00E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left; /* position at the top left */\n"
"    padding: 0 3px;\n"
"color: black;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF0ECE, stop: 1 #FFFFFF);\n"
"}")
        self.layoutWidget1 = QWidget(self.gbDatenEingabe)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 30, 553, 38))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbPendLength = QLabel(self.layoutWidget1)
        self.lbPendLength.setObjectName(u"lbPendLength")

        self.horizontalLayout_4.addWidget(self.lbPendLength)

        self.lePendLengthInput = QLineEdit(self.layoutWidget1)
        self.lePendLengthInput.setObjectName(u"lePendLengthInput")
        self.lePendLengthInput.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.lePendLengthInput)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbTheta = QLabel(self.layoutWidget1)
        self.lbTheta.setObjectName(u"lbTheta")

        self.horizontalLayout_5.addWidget(self.lbTheta)

        self.leAuslenkungInput = QLineEdit(self.layoutWidget1)
        self.leAuslenkungInput.setObjectName(u"leAuslenkungInput")
        self.leAuslenkungInput.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.leAuslenkungInput)

        self.lbLaufzeit = QLabel(self.layoutWidget1)
        self.lbLaufzeit.setObjectName(u"lbLaufzeit")

        self.horizontalLayout_5.addWidget(self.lbLaufzeit)

        self.spLaufzeitInput = QSpinBox(self.layoutWidget1)
        self.spLaufzeitInput.setObjectName(u"spLaufzeitInput")
        self.spLaufzeitInput.setMinimum(1)
        self.spLaufzeitInput.setMaximum(60)

        self.horizontalLayout_5.addWidget(self.spLaufzeitInput)

        self.lbIntervalle = QLabel(self.layoutWidget1)
        self.lbIntervalle.setObjectName(u"lbIntervalle")

        self.horizontalLayout_5.addWidget(self.lbIntervalle)

        self.spIntervalleInput = QSpinBox(self.layoutWidget1)
        self.spIntervalleInput.setObjectName(u"spIntervalleInput")
        self.spIntervalleInput.setMinimum(10)
        self.spIntervalleInput.setMaximum(1000)

        self.horizontalLayout_5.addWidget(self.spIntervalleInput)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)

        self.pbEingabe = QPushButton(dlgEinfachesPendel)
        self.pbEingabe.setObjectName(u"pbEingabe")
        self.pbEingabe.setGeometry(QRect(10, 20, 121, 34))
        self.line = QFrame(dlgEinfachesPendel)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(630, 10, 20, 441))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.lbGraphExtensionTitel = QLabel(dlgEinfachesPendel)
        self.lbGraphExtensionTitel.setObjectName(u"lbGraphExtensionTitel")
        self.lbGraphExtensionTitel.setGeometry(QRect(660, 30, 321, 31))
        self.lbGraphExtensionTitel.setStyleSheet(u"QLabel{\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.gbErgbnis = QGroupBox(dlgEinfachesPendel)
        self.gbErgbnis.setObjectName(u"gbErgbnis")
        self.gbErgbnis.setGeometry(QRect(10, 230, 571, 101))
        self.gbErgbnis.setStyleSheet(u"QGroupBox {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #00E0E0, stop: 1 #FFFFFF);\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left; /* position at the top left */\n"
"    padding: 0 3px;\n"
"color: black;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF0ECE, stop: 1 #FFFFFF);\n"
"}")
        self.layoutWidget_2 = QWidget(self.gbErgbnis)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 40, 531, 38))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")

        self.horizontalLayout_8.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lbFrequenz = QLabel(self.layoutWidget_2)
        self.lbFrequenz.setObjectName(u"lbFrequenz")

        self.horizontalLayout_11.addWidget(self.lbFrequenz)

        self.leFrequenz = QLineEdit(self.layoutWidget_2)
        self.leFrequenz.setObjectName(u"leFrequenz")
        self.leFrequenz.setEnabled(False)

        self.horizontalLayout_11.addWidget(self.leFrequenz)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)

        self.lbSchwingungsDauer = QLabel(self.layoutWidget_2)
        self.lbSchwingungsDauer.setObjectName(u"lbSchwingungsDauer")

        self.horizontalLayout_10.addWidget(self.lbSchwingungsDauer)

        self.leSchwingungsDauer = QLineEdit(self.layoutWidget_2)
        self.leSchwingungsDauer.setObjectName(u"leSchwingungsDauer")
        self.leSchwingungsDauer.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.leSchwingungsDauer)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_10)


        self.retranslateUi(dlgEinfachesPendel)
        self.buttonBox.accepted.connect(dlgEinfachesPendel.accept)

        QMetaObject.connectSlotsByName(dlgEinfachesPendel)
    # setupUi

    def retranslateUi(self, dlgEinfachesPendel):
        dlgEinfachesPendel.setWindowTitle(QCoreApplication.translate("dlgEinfachesPendel", u"Einfaches Pendel", None))
        self.pbBerechne.setText(QCoreApplication.translate("dlgEinfachesPendel", u"Berechne", None))
        self.pbGraphik.setText(QCoreApplication.translate("dlgEinfachesPendel", u"Graph >>>", None))
        self.gbDatenEingabe.setTitle(QCoreApplication.translate("dlgEinfachesPendel", u"Daten Eingabe", None))
        self.lbPendLength.setText(QCoreApplication.translate("dlgEinfachesPendel", u"Pendel L\u00e4nge:", None))
        self.lbTheta.setText(QCoreApplication.translate("dlgEinfachesPendel", u"Auslenkung:", None))
        self.lbLaufzeit.setText(QCoreApplication.translate("dlgEinfachesPendel", u"Laufzeit:", None))
        self.lbIntervalle.setText(QCoreApplication.translate("dlgEinfachesPendel", u"Intervalle:", None))
        self.pbEingabe.setText(QCoreApplication.translate("dlgEinfachesPendel", u"Dateneingabe", None))
        self.lbGraphExtensionTitel.setText(QCoreApplication.translate("dlgEinfachesPendel", u"Graphik Titel", None))
        self.gbErgbnis.setTitle(QCoreApplication.translate("dlgEinfachesPendel", u"Ergebnis", None))
        self.lbFrequenz.setText(QCoreApplication.translate("dlgEinfachesPendel", u"Frequenz:", None))
        self.lbSchwingungsDauer.setText(QCoreApplication.translate("dlgEinfachesPendel", u"Schwingungsdauer:", None))
    # retranslateUi

