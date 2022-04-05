# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogMinigolf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgMinigolf(object):
    def setupUi(self, dlgMinigolf):
        if not dlgMinigolf.objectName():
            dlgMinigolf.setObjectName(u"dlgMinigolf")
        dlgMinigolf.resize(596, 454)
        self.pbBerechne = QPushButton(dlgMinigolf)
        self.pbBerechne.setObjectName(u"pbBerechne")
        self.pbBerechne.setGeometry(QRect(10, 210, 84, 34))
        self.layoutWidget = QWidget(dlgMinigolf)
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

        self.verticalLayoutWidget = QWidget(dlgMinigolf)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(660, 80, 391, 361))
        self.lyGraph = QVBoxLayout(self.verticalLayoutWidget)
        self.lyGraph.setObjectName(u"lyGraph")
        self.lyGraph.setContentsMargins(0, 0, 0, 0)
        self.gbDatenEingabe = QGroupBox(dlgMinigolf)
        self.gbDatenEingabe.setObjectName(u"gbDatenEingabe")
        self.gbDatenEingabe.setEnabled(False)
        self.gbDatenEingabe.setGeometry(QRect(10, 60, 571, 130))
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
        self.layoutWidget_3.setGeometry(QRect(10, 30, 551, 41))
        self.hlyMinigolf_Box = QHBoxLayout(self.layoutWidget_3)
        self.hlyMinigolf_Box.setSpacing(0)
        self.hlyMinigolf_Box.setObjectName(u"hlyMinigolf_Box")
        self.hlyMinigolf_Box.setContentsMargins(0, 0, 0, 0)
        self.lbPotentialWidth = QLabel(self.layoutWidget_3)
        self.lbPotentialWidth.setObjectName(u"lbPotentialWidth")
        self.lbPotentialWidth.setEnabled(False)

        self.hlyMinigolf_Box.addWidget(self.lbPotentialWidth)

        self.lePotentialWidthInput = QLineEdit(self.layoutWidget_3)
        self.lePotentialWidthInput.setObjectName(u"lePotentialWidthInput")
        self.lePotentialWidthInput.setEnabled(False)
        self.lePotentialWidthInput.setMaximumSize(QSize(998, 16777215))
        self.lePotentialWidthInput.setMaxLength(100)

        self.hlyMinigolf_Box.addWidget(self.lePotentialWidthInput)

        self.lbPotentialHeight = QLabel(self.layoutWidget_3)
        self.lbPotentialHeight.setObjectName(u"lbPotentialHeight")
        self.lbPotentialHeight.setEnabled(False)

        self.hlyMinigolf_Box.addWidget(self.lbPotentialHeight)

        self.lePotentialHeightInput = QLineEdit(self.layoutWidget_3)
        self.lePotentialHeightInput.setObjectName(u"lePotentialHeightInput")
        self.lePotentialHeightInput.setEnabled(False)
        self.lePotentialHeightInput.setMaximumSize(QSize(998, 16777215))
        self.lePotentialHeightInput.setMaxLength(100)

        self.hlyMinigolf_Box.addWidget(self.lePotentialHeightInput)

        self.lbLaufzeit_2 = QLabel(self.layoutWidget_3)
        self.lbLaufzeit_2.setObjectName(u"lbLaufzeit_2")

        self.hlyMinigolf_Box.addWidget(self.lbLaufzeit_2)

        self.spLaufzeitInput = QSpinBox(self.layoutWidget_3)
        self.spLaufzeitInput.setObjectName(u"spLaufzeitInput")
        self.spLaufzeitInput.setEnabled(False)
        self.spLaufzeitInput.setMinimum(1)
        self.spLaufzeitInput.setMaximum(60)

        self.hlyMinigolf_Box.addWidget(self.spLaufzeitInput)

        self.lbIntervalle_2 = QLabel(self.layoutWidget_3)
        self.lbIntervalle_2.setObjectName(u"lbIntervalle_2")

        self.hlyMinigolf_Box.addWidget(self.lbIntervalle_2)

        self.spIntervalleInput = QSpinBox(self.layoutWidget_3)
        self.spIntervalleInput.setObjectName(u"spIntervalleInput")
        self.spIntervalleInput.setEnabled(False)
        self.spIntervalleInput.setMinimum(10)
        self.spIntervalleInput.setMaximum(1000)

        self.hlyMinigolf_Box.addWidget(self.spIntervalleInput)

        self.layoutWidget_4 = QWidget(self.gbDatenEingabe)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 80, 551, 41))
        self.hlyMinigolf_Box_2 = QHBoxLayout(self.layoutWidget_4)
        self.hlyMinigolf_Box_2.setSpacing(0)
        self.hlyMinigolf_Box_2.setObjectName(u"hlyMinigolf_Box_2")
        self.hlyMinigolf_Box_2.setContentsMargins(0, 0, 0, 0)
        self.lbXKreis = QLabel(self.layoutWidget_4)
        self.lbXKreis.setObjectName(u"lbXKreis")

        self.hlyMinigolf_Box_2.addWidget(self.lbXKreis)

        self.leXKreisInput = QLineEdit(self.layoutWidget_4)
        self.leXKreisInput.setObjectName(u"leXKreisInput")
        self.leXKreisInput.setEnabled(False)

        self.hlyMinigolf_Box_2.addWidget(self.leXKreisInput)

        self.lbYKreis = QLabel(self.layoutWidget_4)
        self.lbYKreis.setObjectName(u"lbYKreis")

        self.hlyMinigolf_Box_2.addWidget(self.lbYKreis)

        self.leYKreisInput = QLineEdit(self.layoutWidget_4)
        self.leYKreisInput.setObjectName(u"leYKreisInput")
        self.leYKreisInput.setEnabled(False)

        self.hlyMinigolf_Box_2.addWidget(self.leYKreisInput)

        self.lbRaduisKreis = QLabel(self.layoutWidget_4)
        self.lbRaduisKreis.setObjectName(u"lbRaduisKreis")

        self.hlyMinigolf_Box_2.addWidget(self.lbRaduisKreis)

        self.leRadiusKreisInput = QLineEdit(self.layoutWidget_4)
        self.leRadiusKreisInput.setObjectName(u"leRadiusKreisInput")
        self.leRadiusKreisInput.setEnabled(False)

        self.hlyMinigolf_Box_2.addWidget(self.leRadiusKreisInput)

        self.lbV0 = QLabel(self.layoutWidget_4)
        self.lbV0.setObjectName(u"lbV0")

        self.hlyMinigolf_Box_2.addWidget(self.lbV0)

        self.leV0Input = QLineEdit(self.layoutWidget_4)
        self.leV0Input.setObjectName(u"leV0Input")
        self.leV0Input.setEnabled(False)

        self.hlyMinigolf_Box_2.addWidget(self.leV0Input)

        self.lbTheta = QLabel(self.layoutWidget_4)
        self.lbTheta.setObjectName(u"lbTheta")

        self.hlyMinigolf_Box_2.addWidget(self.lbTheta)

        self.leThetaInput = QLineEdit(self.layoutWidget_4)
        self.leThetaInput.setObjectName(u"leThetaInput")
        self.leThetaInput.setEnabled(False)

        self.hlyMinigolf_Box_2.addWidget(self.leThetaInput)

        self.pbEingabe = QPushButton(dlgMinigolf)
        self.pbEingabe.setObjectName(u"pbEingabe")
        self.pbEingabe.setGeometry(QRect(10, 20, 121, 34))
        self.line = QFrame(dlgMinigolf)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(630, 10, 20, 441))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.lbGraphExtensionTitel = QLabel(dlgMinigolf)
        self.lbGraphExtensionTitel.setObjectName(u"lbGraphExtensionTitel")
        self.lbGraphExtensionTitel.setGeometry(QRect(660, 30, 321, 31))
        self.lbGraphExtensionTitel.setStyleSheet(u"QLabel{\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.gbErgbnis = QGroupBox(dlgMinigolf)
        self.gbErgbnis.setObjectName(u"gbErgbnis")
        self.gbErgbnis.setGeometry(QRect(10, 270, 571, 101))
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
        self.lbIntervallLaenge = QLabel(self.layoutWidget1)
        self.lbIntervallLaenge.setObjectName(u"lbIntervallLaenge")

        self.horizontalLayout_11.addWidget(self.lbIntervallLaenge)

        self.leZeitintervall = QLineEdit(self.layoutWidget1)
        self.leZeitintervall.setObjectName(u"leZeitintervall")
        self.leZeitintervall.setEnabled(False)

        self.horizontalLayout_11.addWidget(self.leZeitintervall)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)

        self.lbStatus = QLabel(self.layoutWidget1)
        self.lbStatus.setObjectName(u"lbStatus")

        self.horizontalLayout_10.addWidget(self.lbStatus)

        self.leStatus = QLineEdit(self.layoutWidget1)
        self.leStatus.setObjectName(u"leStatus")
        self.leStatus.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.leStatus)

#if QT_CONFIG(shortcut)
        self.lbPotentialWidth.setBuddy(self.lePotentialWidthInput)
        self.lbPotentialHeight.setBuddy(self.lePotentialWidthInput)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(dlgMinigolf)
        self.buttonBox.accepted.connect(dlgMinigolf.accept)

        QMetaObject.connectSlotsByName(dlgMinigolf)
    # setupUi

    def retranslateUi(self, dlgMinigolf):
        dlgMinigolf.setWindowTitle(QCoreApplication.translate("dlgMinigolf", u"Simulation: Minigolf", None))
        self.pbBerechne.setText(QCoreApplication.translate("dlgMinigolf", u"Berechne", None))
        self.pbGraphik.setText(QCoreApplication.translate("dlgMinigolf", u"Graph >>>", None))
        self.gbDatenEingabe.setTitle(QCoreApplication.translate("dlgMinigolf", u"Daten Eingabe", None))
        self.lbPotentialWidth.setText(QCoreApplication.translate("dlgMinigolf", u"L\u00e4nge Potential:", None))
        self.lbPotentialHeight.setText(QCoreApplication.translate("dlgMinigolf", u"H\u00f6he Potential:", None))
        self.lbLaufzeit_2.setText(QCoreApplication.translate("dlgMinigolf", u"Laufzeit:", None))
        self.lbIntervalle_2.setText(QCoreApplication.translate("dlgMinigolf", u"Intervalle:", None))
        self.lbXKreis.setText(QCoreApplication.translate("dlgMinigolf", u"X Kreis:", None))
        self.lbYKreis.setText(QCoreApplication.translate("dlgMinigolf", u"Y Kreis:", None))
        self.lbRaduisKreis.setText(QCoreApplication.translate("dlgMinigolf", u"R Kreis:", None))
#if QT_CONFIG(tooltip)
        self.lbV0.setToolTip(QCoreApplication.translate("dlgMinigolf", u"<html><head/><body><p>Anfangsgeschwingikeit [m/s]</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lbV0.setText(QCoreApplication.translate("dlgMinigolf", u"v0:", None))
#if QT_CONFIG(tooltip)
        self.leV0Input.setToolTip(QCoreApplication.translate("dlgMinigolf", u"<html><head/><body><p>Anfangsgeschwingikeit [m/s]</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lbTheta.setToolTip(QCoreApplication.translate("dlgMinigolf", u"<html><head/><body><p>Anfangsgeschwingikeit [m/s]</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lbTheta.setText(QCoreApplication.translate("dlgMinigolf", u"Theta:", None))
#if QT_CONFIG(tooltip)
        self.leThetaInput.setToolTip(QCoreApplication.translate("dlgMinigolf", u"<html><head/><body><p>Anfangsgeschwingikeit [m/s]</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pbEingabe.setText(QCoreApplication.translate("dlgMinigolf", u"Dateneingabe", None))
        self.lbGraphExtensionTitel.setText(QCoreApplication.translate("dlgMinigolf", u"Graphik Titel", None))
        self.gbErgbnis.setTitle(QCoreApplication.translate("dlgMinigolf", u"Ergebnis", None))
        self.lbIntervallLaenge.setText(QCoreApplication.translate("dlgMinigolf", u"Zeitintervall:", None))
        self.lbStatus.setText(QCoreApplication.translate("dlgMinigolf", u"Status:", None))
    # retranslateUi

