# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogLissajous.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgLissajous(object):
    def setupUi(self, dlgLissajous):
        if not dlgLissajous.objectName():
            dlgLissajous.setObjectName(u"dlgLissajous")
        dlgLissajous.resize(598, 454)
        self.pbBerechne = QPushButton(dlgLissajous)
        self.pbBerechne.setObjectName(u"pbBerechne")
        self.pbBerechne.setGeometry(QRect(10, 250, 84, 34))
        self.layoutWidget = QWidget(dlgLissajous)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 410, 571, 36))
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

        self.verticalLayoutWidget = QWidget(dlgLissajous)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(660, 80, 391, 361))
        self.lyGraph = QVBoxLayout(self.verticalLayoutWidget)
        self.lyGraph.setObjectName(u"lyGraph")
        self.lyGraph.setContentsMargins(0, 0, 0, 0)
        self.gbDatenEingabe = QGroupBox(dlgLissajous)
        self.gbDatenEingabe.setObjectName(u"gbDatenEingabe")
        self.gbDatenEingabe.setEnabled(False)
        self.gbDatenEingabe.setGeometry(QRect(10, 60, 571, 181))
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
        self.hlyLissajous = QHBoxLayout(self.layoutWidget_3)
        self.hlyLissajous.setSpacing(0)
        self.hlyLissajous.setObjectName(u"hlyLissajous")
        self.hlyLissajous.setContentsMargins(0, 0, 0, 0)
        self.lbOmega1 = QLabel(self.layoutWidget_3)
        self.lbOmega1.setObjectName(u"lbOmega1")

        self.hlyLissajous.addWidget(self.lbOmega1)

        self.leOmega1Input = QLineEdit(self.layoutWidget_3)
        self.leOmega1Input.setObjectName(u"leOmega1Input")
        self.leOmega1Input.setEnabled(False)

        self.hlyLissajous.addWidget(self.leOmega1Input)

        self.lbOmega2 = QLabel(self.layoutWidget_3)
        self.lbOmega2.setObjectName(u"lbOmega2")

        self.hlyLissajous.addWidget(self.lbOmega2)

        self.leOmega2Input = QLineEdit(self.layoutWidget_3)
        self.leOmega2Input.setObjectName(u"leOmega2Input")
        self.leOmega2Input.setEnabled(False)

        self.hlyLissajous.addWidget(self.leOmega2Input)

        self.lbLaufzeit_2 = QLabel(self.layoutWidget_3)
        self.lbLaufzeit_2.setObjectName(u"lbLaufzeit_2")

        self.hlyLissajous.addWidget(self.lbLaufzeit_2)

        self.spLaufzeitInput = QSpinBox(self.layoutWidget_3)
        self.spLaufzeitInput.setObjectName(u"spLaufzeitInput")
        self.spLaufzeitInput.setEnabled(False)
        self.spLaufzeitInput.setMinimum(10)
        self.spLaufzeitInput.setMaximum(100)

        self.hlyLissajous.addWidget(self.spLaufzeitInput)

        self.lbIntervalle_2 = QLabel(self.layoutWidget_3)
        self.lbIntervalle_2.setObjectName(u"lbIntervalle_2")

        self.hlyLissajous.addWidget(self.lbIntervalle_2)

        self.spIntervalleInput = QSpinBox(self.layoutWidget_3)
        self.spIntervalleInput.setObjectName(u"spIntervalleInput")
        self.spIntervalleInput.setEnabled(False)
        self.spIntervalleInput.setMinimum(100)
        self.spIntervalleInput.setMaximum(1000)

        self.hlyLissajous.addWidget(self.spIntervalleInput)

        self.layoutWidget_4 = QWidget(self.gbDatenEingabe)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 80, 331, 38))
        self.hlyLissajous_2 = QHBoxLayout(self.layoutWidget_4)
        self.hlyLissajous_2.setSpacing(0)
        self.hlyLissajous_2.setObjectName(u"hlyLissajous_2")
        self.hlyLissajous_2.setContentsMargins(0, 0, 0, 0)
        self.lbPhase1 = QLabel(self.layoutWidget_4)
        self.lbPhase1.setObjectName(u"lbPhase1")

        self.hlyLissajous_2.addWidget(self.lbPhase1)

        self.lePhase1Input = QLineEdit(self.layoutWidget_4)
        self.lePhase1Input.setObjectName(u"lePhase1Input")
        self.lePhase1Input.setEnabled(False)

        self.hlyLissajous_2.addWidget(self.lePhase1Input)

        self.lbPhase2 = QLabel(self.layoutWidget_4)
        self.lbPhase2.setObjectName(u"lbPhase2")

        self.hlyLissajous_2.addWidget(self.lbPhase2)

        self.lePhase2Input = QLineEdit(self.layoutWidget_4)
        self.lePhase2Input.setObjectName(u"lePhase2Input")
        self.lePhase2Input.setEnabled(False)

        self.hlyLissajous_2.addWidget(self.lePhase2Input)

        self.layoutWidget_5 = QWidget(self.gbDatenEingabe)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(10, 130, 331, 38))
        self.hlyLissajous_3 = QHBoxLayout(self.layoutWidget_5)
        self.hlyLissajous_3.setSpacing(0)
        self.hlyLissajous_3.setObjectName(u"hlyLissajous_3")
        self.hlyLissajous_3.setContentsMargins(0, 0, 0, 0)
        self.lbAmplitude1 = QLabel(self.layoutWidget_5)
        self.lbAmplitude1.setObjectName(u"lbAmplitude1")

        self.hlyLissajous_3.addWidget(self.lbAmplitude1)

        self.leAmplitude1Input = QLineEdit(self.layoutWidget_5)
        self.leAmplitude1Input.setObjectName(u"leAmplitude1Input")
        self.leAmplitude1Input.setEnabled(False)

        self.hlyLissajous_3.addWidget(self.leAmplitude1Input)

        self.lbAmplitude2 = QLabel(self.layoutWidget_5)
        self.lbAmplitude2.setObjectName(u"lbAmplitude2")

        self.hlyLissajous_3.addWidget(self.lbAmplitude2)

        self.leAmplitude2Input = QLineEdit(self.layoutWidget_5)
        self.leAmplitude2Input.setObjectName(u"leAmplitude2Input")
        self.leAmplitude2Input.setEnabled(False)

        self.hlyLissajous_3.addWidget(self.leAmplitude2Input)

        self.pbEingabe = QPushButton(dlgLissajous)
        self.pbEingabe.setObjectName(u"pbEingabe")
        self.pbEingabe.setGeometry(QRect(10, 20, 121, 34))
        self.line = QFrame(dlgLissajous)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(630, 10, 20, 441))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.lbGraphExtensionTitel = QLabel(dlgLissajous)
        self.lbGraphExtensionTitel.setObjectName(u"lbGraphExtensionTitel")
        self.lbGraphExtensionTitel.setGeometry(QRect(660, 30, 321, 31))
        self.lbGraphExtensionTitel.setStyleSheet(u"QLabel{\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.gbErgbnis = QGroupBox(dlgLissajous)
        self.gbErgbnis.setObjectName(u"gbErgbnis")
        self.gbErgbnis.setGeometry(QRect(10, 290, 571, 101))
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
        self.layoutWidget1.setGeometry(QRect(20, 40, 529, 36))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lbT1 = QLabel(self.layoutWidget1)
        self.lbT1.setObjectName(u"lbT1")

        self.horizontalLayout_11.addWidget(self.lbT1)

        self.leT1Input = QLineEdit(self.layoutWidget1)
        self.leT1Input.setObjectName(u"leT1Input")
        self.leT1Input.setEnabled(False)

        self.horizontalLayout_11.addWidget(self.leT1Input)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)

        self.lbT2 = QLabel(self.layoutWidget1)
        self.lbT2.setObjectName(u"lbT2")

        self.horizontalLayout_10.addWidget(self.lbT2)

        self.leT2Input = QLineEdit(self.layoutWidget1)
        self.leT2Input.setObjectName(u"leT2Input")
        self.leT2Input.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.leT2Input)


        self.retranslateUi(dlgLissajous)
        self.buttonBox.accepted.connect(dlgLissajous.accept)

        QMetaObject.connectSlotsByName(dlgLissajous)
    # setupUi

    def retranslateUi(self, dlgLissajous):
        dlgLissajous.setWindowTitle(QCoreApplication.translate("dlgLissajous", u"Lissajous Figuren", None))
        self.pbBerechne.setText(QCoreApplication.translate("dlgLissajous", u"Berechne", None))
        self.pbGraphik.setText(QCoreApplication.translate("dlgLissajous", u"Graph >>>", None))
        self.gbDatenEingabe.setTitle(QCoreApplication.translate("dlgLissajous", u"Daten Eingabe", None))
#if QT_CONFIG(tooltip)
        self.lbOmega1.setToolTip(QCoreApplication.translate("dlgLissajous", u"<html><head/><body><p>Frequenz 1 [1/s]</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lbOmega1.setText(QCoreApplication.translate("dlgLissajous", u"Omega1:", None))
#if QT_CONFIG(tooltip)
        self.leOmega1Input.setToolTip(QCoreApplication.translate("dlgLissajous", u"<html><head/><body><p>Kresifrequenz 1 [1/s]</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lbOmega2.setToolTip(QCoreApplication.translate("dlgLissajous", u"<html><head/><body><p>Frequenz 2 [1/s]</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lbOmega2.setText(QCoreApplication.translate("dlgLissajous", u"Omega2:", None))
#if QT_CONFIG(tooltip)
        self.leOmega2Input.setToolTip(QCoreApplication.translate("dlgLissajous", u"<html><head/><body><p>Kreisfrequenz 2 [1/s]</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lbLaufzeit_2.setText(QCoreApplication.translate("dlgLissajous", u"Laufzeit:", None))
        self.lbIntervalle_2.setText(QCoreApplication.translate("dlgLissajous", u"Intervalle:", None))
#if QT_CONFIG(tooltip)
        self.lbPhase1.setToolTip(QCoreApplication.translate("dlgLissajous", u"<html><head/><body><p>Phase 1 [1/s]</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lbPhase1.setText(QCoreApplication.translate("dlgLissajous", u"Phase1:", None))
#if QT_CONFIG(tooltip)
        self.lePhase1Input.setToolTip(QCoreApplication.translate("dlgLissajous", u"<html><head/><body><p>Phase 1 [1/s]</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lePhase1Input.setText(QCoreApplication.translate("dlgLissajous", u"0", None))
#if QT_CONFIG(tooltip)
        self.lbPhase2.setToolTip(QCoreApplication.translate("dlgLissajous", u"<html><head/><body><p>Phase 2 [1/s]</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lbPhase2.setText(QCoreApplication.translate("dlgLissajous", u"Phase2:", None))
#if QT_CONFIG(tooltip)
        self.lePhase2Input.setToolTip(QCoreApplication.translate("dlgLissajous", u"<html><head/><body><p>Phase 2 [1/s]</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lePhase2Input.setText(QCoreApplication.translate("dlgLissajous", u"0", None))
#if QT_CONFIG(tooltip)
        self.lbAmplitude1.setToolTip(QCoreApplication.translate("dlgLissajous", u"<html><head/><body><p>Amplitude 1 [1/s]</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lbAmplitude1.setText(QCoreApplication.translate("dlgLissajous", u"Amplitude1:", None))
#if QT_CONFIG(tooltip)
        self.leAmplitude1Input.setToolTip(QCoreApplication.translate("dlgLissajous", u"<html><head/><body><p>Amplitude1 [1/s]</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.leAmplitude1Input.setText(QCoreApplication.translate("dlgLissajous", u"1", None))
#if QT_CONFIG(tooltip)
        self.lbAmplitude2.setToolTip(QCoreApplication.translate("dlgLissajous", u"<html><head/><body><p>Amplitude 2 [1/s]</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lbAmplitude2.setText(QCoreApplication.translate("dlgLissajous", u"Amplitude2:", None))
#if QT_CONFIG(tooltip)
        self.leAmplitude2Input.setToolTip(QCoreApplication.translate("dlgLissajous", u"<html><head/><body><p>Amplitude 2 [1/s]</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.leAmplitude2Input.setText(QCoreApplication.translate("dlgLissajous", u"1", None))
        self.pbEingabe.setText(QCoreApplication.translate("dlgLissajous", u"Dateneingabe", None))
        self.lbGraphExtensionTitel.setText(QCoreApplication.translate("dlgLissajous", u"Graphik Titel", None))
        self.gbErgbnis.setTitle(QCoreApplication.translate("dlgLissajous", u"Ergebnis", None))
        self.lbT1.setText(QCoreApplication.translate("dlgLissajous", u"T1:", None))
#if QT_CONFIG(tooltip)
        self.leT1Input.setToolTip(QCoreApplication.translate("dlgLissajous", u"<html><head/><body><p>Winkelgeschwindigkeit 1 in rad</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lbT2.setText(QCoreApplication.translate("dlgLissajous", u"T2:", None))
#if QT_CONFIG(tooltip)
        self.leT2Input.setToolTip(QCoreApplication.translate("dlgLissajous", u"<html><head/><body><p>Winkelgeschwindigkeit 2 in rad</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

