# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogDifferentialGleichung.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgDifferentialGleichung(object):
    def setupUi(self, dlgDifferentialGleichung):
        if not dlgDifferentialGleichung.objectName():
            dlgDifferentialGleichung.setObjectName(u"dlgDifferentialGleichung")
        dlgDifferentialGleichung.resize(605, 454)
        self.pbBerechne = QPushButton(dlgDifferentialGleichung)
        self.pbBerechne.setObjectName(u"pbBerechne")
        self.pbBerechne.setGeometry(QRect(10, 170, 84, 34))
        self.layoutWidget = QWidget(dlgDifferentialGleichung)
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

        self.verticalLayoutWidget = QWidget(dlgDifferentialGleichung)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(660, 80, 391, 361))
        self.lyGraph = QVBoxLayout(self.verticalLayoutWidget)
        self.lyGraph.setObjectName(u"lyGraph")
        self.lyGraph.setContentsMargins(0, 0, 0, 0)
        self.gbDatenEingabe = QGroupBox(dlgDifferentialGleichung)
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
        self.layoutWidget_3 = QWidget(self.gbDatenEingabe)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 30, 552, 38))
        self.hlySchieferWurf = QHBoxLayout(self.layoutWidget_3)
        self.hlySchieferWurf.setSpacing(0)
        self.hlySchieferWurf.setObjectName(u"hlySchieferWurf")
        self.hlySchieferWurf.setContentsMargins(0, 0, 0, 0)
        self.lbStartWert = QLabel(self.layoutWidget_3)
        self.lbStartWert.setObjectName(u"lbStartWert")
        self.lbStartWert.setEnabled(False)

        self.hlySchieferWurf.addWidget(self.lbStartWert)

        self.leStartwertInput = QLineEdit(self.layoutWidget_3)
        self.leStartwertInput.setObjectName(u"leStartwertInput")
        self.leStartwertInput.setEnabled(False)
        self.leStartwertInput.setMaximumSize(QSize(998, 16777215))
        self.leStartwertInput.setMaxLength(100)

        self.hlySchieferWurf.addWidget(self.leStartwertInput)

        self.lbSchrittweite = QLabel(self.layoutWidget_3)
        self.lbSchrittweite.setObjectName(u"lbSchrittweite")

        self.hlySchieferWurf.addWidget(self.lbSchrittweite)

        self.spSchrittweiteInput = QSpinBox(self.layoutWidget_3)
        self.spSchrittweiteInput.setObjectName(u"spSchrittweiteInput")
        self.spSchrittweiteInput.setEnabled(False)
        self.spSchrittweiteInput.setMinimum(1)
        self.spSchrittweiteInput.setMaximum(10)
        self.spSchrittweiteInput.setSingleStep(1)
        self.spSchrittweiteInput.setValue(10)

        self.hlySchieferWurf.addWidget(self.spSchrittweiteInput)

        self.pbEingabe = QPushButton(dlgDifferentialGleichung)
        self.pbEingabe.setObjectName(u"pbEingabe")
        self.pbEingabe.setGeometry(QRect(10, 20, 121, 34))
        self.line = QFrame(dlgDifferentialGleichung)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(630, 10, 20, 441))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.lbGraphExtensionTitel = QLabel(dlgDifferentialGleichung)
        self.lbGraphExtensionTitel.setObjectName(u"lbGraphExtensionTitel")
        self.lbGraphExtensionTitel.setGeometry(QRect(660, 30, 321, 31))
        self.lbGraphExtensionTitel.setStyleSheet(u"QLabel{\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.gbErgbnis = QGroupBox(dlgDifferentialGleichung)
        self.gbErgbnis.setObjectName(u"gbErgbnis")
        self.gbErgbnis.setGeometry(QRect(10, 230, 571, 81))
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
        self.layoutWidget1 = QWidget(self.gbErgbnis)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 30, 529, 36))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lbAnzahl = QLabel(self.layoutWidget1)
        self.lbAnzahl.setObjectName(u"lbAnzahl")

        self.horizontalLayout_11.addWidget(self.lbAnzahl)

        self.leAnzahlSchritte = QLineEdit(self.layoutWidget1)
        self.leAnzahlSchritte.setObjectName(u"leAnzahlSchritte")
        self.leAnzahlSchritte.setEnabled(False)

        self.horizontalLayout_11.addWidget(self.leAnzahlSchritte)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)

        self.lbStatus = QLabel(self.layoutWidget1)
        self.lbStatus.setObjectName(u"lbStatus")

        self.horizontalLayout_10.addWidget(self.lbStatus)

        self.leStatus = QLineEdit(self.layoutWidget1)
        self.leStatus.setObjectName(u"leStatus")
        self.leStatus.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.leStatus)

        self.lbDGL = QLabel(dlgDifferentialGleichung)
        self.lbDGL.setObjectName(u"lbDGL")
        self.lbDGL.setGeometry(QRect(20, 320, 281, 18))
        self.teFormula = QTextEdit(dlgDifferentialGleichung)
        self.teFormula.setObjectName(u"teFormula")
        self.teFormula.setGeometry(QRect(10, 340, 561, 51))
        self.teFormula.setFrameShape(QFrame.NoFrame)

        self.retranslateUi(dlgDifferentialGleichung)
        self.buttonBox.accepted.connect(dlgDifferentialGleichung.accept)

        QMetaObject.connectSlotsByName(dlgDifferentialGleichung)
    # setupUi

    def retranslateUi(self, dlgDifferentialGleichung):
        dlgDifferentialGleichung.setWindowTitle(QCoreApplication.translate("dlgDifferentialGleichung", u"Differential Gleichung: Vergleich N\u00e4herungsmethoden", None))
        self.pbBerechne.setText(QCoreApplication.translate("dlgDifferentialGleichung", u"Berechne", None))
        self.pbGraphik.setText(QCoreApplication.translate("dlgDifferentialGleichung", u"Graph >>>", None))
        self.gbDatenEingabe.setTitle(QCoreApplication.translate("dlgDifferentialGleichung", u"Daten Eingabe", None))
        self.lbStartWert.setText(QCoreApplication.translate("dlgDifferentialGleichung", u"Startwert y(0):", None))
        self.leStartwertInput.setText(QCoreApplication.translate("dlgDifferentialGleichung", u"0.6", None))
        self.lbSchrittweite.setText(QCoreApplication.translate("dlgDifferentialGleichung", u"Schrittweite (x/10):", None))
        self.pbEingabe.setText(QCoreApplication.translate("dlgDifferentialGleichung", u"Dateneingabe", None))
        self.lbGraphExtensionTitel.setText(QCoreApplication.translate("dlgDifferentialGleichung", u"Graphik Titel", None))
        self.gbErgbnis.setTitle(QCoreApplication.translate("dlgDifferentialGleichung", u"Ergebnis", None))
        self.lbAnzahl.setText(QCoreApplication.translate("dlgDifferentialGleichung", u"Anzahl Schritte:", None))
        self.lbStatus.setText(QCoreApplication.translate("dlgDifferentialGleichung", u"Status:", None))
        self.lbDGL.setText(QCoreApplication.translate("dlgDifferentialGleichung", u"Diese Differentialgleichung wird berechnet:", None))
    # retranslateUi

