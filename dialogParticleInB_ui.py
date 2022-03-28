# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogParticleInB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgParticleInB(object):
    def setupUi(self, dlgParticleInB):
        if not dlgParticleInB.objectName():
            dlgParticleInB.setObjectName(u"dlgParticleInB")
        dlgParticleInB.resize(598, 454)
        self.pbBerechne = QPushButton(dlgParticleInB)
        self.pbBerechne.setObjectName(u"pbBerechne")
        self.pbBerechne.setGeometry(QRect(10, 170, 84, 34))
        self.layoutWidget = QWidget(dlgParticleInB)
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

        self.verticalLayoutWidget = QWidget(dlgParticleInB)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(660, 80, 391, 361))
        self.lyGraph = QVBoxLayout(self.verticalLayoutWidget)
        self.lyGraph.setObjectName(u"lyGraph")
        self.lyGraph.setContentsMargins(0, 0, 0, 0)
        self.pbVergleich = QPushButton(self.verticalLayoutWidget)
        self.pbVergleich.setObjectName(u"pbVergleich")

        self.lyGraph.addWidget(self.pbVergleich)

        self.gbDatenEingabe = QGroupBox(dlgParticleInB)
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
        self.layoutWidget_3.setGeometry(QRect(10, 30, 551, 38))
        self.hlyParticleInB = QHBoxLayout(self.layoutWidget_3)
        self.hlyParticleInB.setSpacing(0)
        self.hlyParticleInB.setObjectName(u"hlyParticleInB")
        self.hlyParticleInB.setContentsMargins(0, 0, 0, 0)
        self.lbLarmorFrequenz = QLabel(self.layoutWidget_3)
        self.lbLarmorFrequenz.setObjectName(u"lbLarmorFrequenz")
        self.lbLarmorFrequenz.setEnabled(False)

        self.hlyParticleInB.addWidget(self.lbLarmorFrequenz)

        self.leLarmorFrequenzInput = QLineEdit(self.layoutWidget_3)
        self.leLarmorFrequenzInput.setObjectName(u"leLarmorFrequenzInput")
        self.leLarmorFrequenzInput.setEnabled(False)
        self.leLarmorFrequenzInput.setMaximumSize(QSize(998, 16777215))
        self.leLarmorFrequenzInput.setMaxLength(100)

        self.hlyParticleInB.addWidget(self.leLarmorFrequenzInput)

        self.lbV0 = QLabel(self.layoutWidget_3)
        self.lbV0.setObjectName(u"lbV0")

        self.hlyParticleInB.addWidget(self.lbV0)

        self.leV0Input = QLineEdit(self.layoutWidget_3)
        self.leV0Input.setObjectName(u"leV0Input")
        self.leV0Input.setEnabled(False)

        self.hlyParticleInB.addWidget(self.leV0Input)

        self.lbWinkel = QLabel(self.layoutWidget_3)
        self.lbWinkel.setObjectName(u"lbWinkel")

        self.hlyParticleInB.addWidget(self.lbWinkel)

        self.spWinkelInput = QSpinBox(self.layoutWidget_3)
        self.spWinkelInput.setObjectName(u"spWinkelInput")
        self.spWinkelInput.setEnabled(False)
        self.spWinkelInput.setMinimum(0)
        self.spWinkelInput.setMaximum(90)

        self.hlyParticleInB.addWidget(self.spWinkelInput)

        self.lbLaufzeit = QLabel(self.layoutWidget_3)
        self.lbLaufzeit.setObjectName(u"lbLaufzeit")

        self.hlyParticleInB.addWidget(self.lbLaufzeit)

        self.spLaufzeitInput = QSpinBox(self.layoutWidget_3)
        self.spLaufzeitInput.setObjectName(u"spLaufzeitInput")
        self.spLaufzeitInput.setEnabled(False)
        self.spLaufzeitInput.setMinimum(1)
        self.spLaufzeitInput.setMaximum(60)

        self.hlyParticleInB.addWidget(self.spLaufzeitInput)

        self.lbIntervalle = QLabel(self.layoutWidget_3)
        self.lbIntervalle.setObjectName(u"lbIntervalle")

        self.hlyParticleInB.addWidget(self.lbIntervalle)

        self.spIntervalleInput = QSpinBox(self.layoutWidget_3)
        self.spIntervalleInput.setObjectName(u"spIntervalleInput")
        self.spIntervalleInput.setEnabled(False)
        self.spIntervalleInput.setMinimum(10)
        self.spIntervalleInput.setMaximum(1000)

        self.hlyParticleInB.addWidget(self.spIntervalleInput)

        self.pbEingabe = QPushButton(dlgParticleInB)
        self.pbEingabe.setObjectName(u"pbEingabe")
        self.pbEingabe.setGeometry(QRect(10, 20, 121, 34))
        self.line = QFrame(dlgParticleInB)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(630, 10, 20, 441))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.lbGraphExtensionTitel = QLabel(dlgParticleInB)
        self.lbGraphExtensionTitel.setObjectName(u"lbGraphExtensionTitel")
        self.lbGraphExtensionTitel.setGeometry(QRect(660, 30, 321, 31))
        self.lbGraphExtensionTitel.setStyleSheet(u"QLabel{\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.gbErgebnis = QGroupBox(dlgParticleInB)
        self.gbErgebnis.setObjectName(u"gbErgebnis")
        self.gbErgebnis.setGeometry(QRect(10, 230, 571, 141))
        self.gbErgebnis.setStyleSheet(u"QGroupBox {\n"
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
        self.layoutWidget1 = QWidget(self.gbErgebnis)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 40, 529, 36))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lbStartRichtung = QLabel(self.layoutWidget1)
        self.lbStartRichtung.setObjectName(u"lbStartRichtung")

        self.horizontalLayout_10.addWidget(self.lbStartRichtung)

        self.leStartRichtung = QLineEdit(self.layoutWidget1)
        self.leStartRichtung.setObjectName(u"leStartRichtung")
        self.leStartRichtung.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.leStartRichtung)

        self.lbStepOfHelix = QLabel(self.layoutWidget1)
        self.lbStepOfHelix.setObjectName(u"lbStepOfHelix")

        self.horizontalLayout_10.addWidget(self.lbStepOfHelix)

        self.leStepOfHelix = QLineEdit(self.layoutWidget1)
        self.leStepOfHelix.setObjectName(u"leStepOfHelix")
        self.leStepOfHelix.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.leStepOfHelix)

        self.layoutWidget2 = QWidget(self.gbErgebnis)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 90, 529, 34))
        self.horizontalLayout_13 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.lbKreisRadius = QLabel(self.layoutWidget2)
        self.lbKreisRadius.setObjectName(u"lbKreisRadius")

        self.horizontalLayout_13.addWidget(self.lbKreisRadius)

        self.leKreisRadius = QLineEdit(self.layoutWidget2)
        self.leKreisRadius.setObjectName(u"leKreisRadius")
        self.leKreisRadius.setEnabled(False)

        self.horizontalLayout_13.addWidget(self.leKreisRadius)


        self.retranslateUi(dlgParticleInB)
        self.buttonBox.accepted.connect(dlgParticleInB.accept)

        QMetaObject.connectSlotsByName(dlgParticleInB)
    # setupUi

    def retranslateUi(self, dlgParticleInB):
        dlgParticleInB.setWindowTitle(QCoreApplication.translate("dlgParticleInB", u"Teilchen im Magnetfeld", None))
        self.pbBerechne.setText(QCoreApplication.translate("dlgParticleInB", u"Berechne", None))
        self.pbGraphik.setText(QCoreApplication.translate("dlgParticleInB", u"Graph >>>", None))
        self.pbVergleich.setText(QCoreApplication.translate("dlgParticleInB", u"Vergleich mit/ohne Luftwiderstand", None))
        self.gbDatenEingabe.setTitle(QCoreApplication.translate("dlgParticleInB", u"Daten Eingabe", None))
        self.lbLarmorFrequenz.setText(QCoreApplication.translate("dlgParticleInB", u"Larmor Frequenz:", None))
#if QT_CONFIG(tooltip)
        self.leLarmorFrequenzInput.setToolTip(QCoreApplication.translate("dlgParticleInB", u"<html><head/><body><p>Frequenz der <a href=\"https://flexikon.doccheck.com/de/index.php?title=Pr%C3%A4zessionsbewegung&amp;action=edit&amp;redlink=1\"><span style=\" text-decoration: underline; color:#2980b9;\">Pr\u00e4zessionsbewegung</span></a> eines <a href=\"https://flexikon.doccheck.com/de/Elementarteilchen\"><span style=\" text-decoration: underline; color:#2980b9;\">Elementarteilchens</span></a> in einem externen <a href=\"https://flexikon.doccheck.com/de/Magnetfeld\"><span style=\" text-decoration: underline; color:#2980b9;\">Magnetfeld (Omega = B*q/m,  position x0 = \u2212v0y / omega)</span></a></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lbV0.setToolTip(QCoreApplication.translate("dlgParticleInB", u"<html><head/><body><p>Anfangsgeschwingikeit [m/s]</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lbV0.setText(QCoreApplication.translate("dlgParticleInB", u"v0:", None))
#if QT_CONFIG(tooltip)
        self.leV0Input.setToolTip(QCoreApplication.translate("dlgParticleInB", u"<html><head/><body><p>Anfangsgeschwingikeit [m/s]</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lbWinkel.setText(QCoreApplication.translate("dlgParticleInB", u"Winkel:", None))
        self.lbLaufzeit.setText(QCoreApplication.translate("dlgParticleInB", u"Laufzeit:", None))
        self.lbIntervalle.setText(QCoreApplication.translate("dlgParticleInB", u"Intervalle:", None))
        self.pbEingabe.setText(QCoreApplication.translate("dlgParticleInB", u"Dateneingabe", None))
        self.lbGraphExtensionTitel.setText(QCoreApplication.translate("dlgParticleInB", u"Graphik Titel", None))
        self.gbErgebnis.setTitle(QCoreApplication.translate("dlgParticleInB", u"Ergebnis", None))
        self.lbStartRichtung.setText(QCoreApplication.translate("dlgParticleInB", u"Start Richtung:", None))
        self.lbStepOfHelix.setText(QCoreApplication.translate("dlgParticleInB", u"step of helix : s=v0z *T= :", None))
        self.lbKreisRadius.setText(QCoreApplication.translate("dlgParticleInB", u"xy Ebene: KreisMittelpunkt ( 0 , 0 ), Radius=:", None))
    # retranslateUi

