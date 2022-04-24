# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogQuantenHarmonischerOszillator.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgQuantenHarmonischerOszillator(object):
    def setupUi(self, dlgQuantenHarmonischerOszillator):
        if not dlgQuantenHarmonischerOszillator.objectName():
            dlgQuantenHarmonischerOszillator.setObjectName(u"dlgQuantenHarmonischerOszillator")
        dlgQuantenHarmonischerOszillator.resize(605, 454)
        self.pbBerechne = QPushButton(dlgQuantenHarmonischerOszillator)
        self.pbBerechne.setObjectName(u"pbBerechne")
        self.pbBerechne.setGeometry(QRect(10, 170, 84, 34))
        self.layoutWidget = QWidget(dlgQuantenHarmonischerOszillator)
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

        self.verticalLayoutWidget = QWidget(dlgQuantenHarmonischerOszillator)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(660, 80, 391, 361))
        self.lyGraph = QVBoxLayout(self.verticalLayoutWidget)
        self.lyGraph.setObjectName(u"lyGraph")
        self.lyGraph.setContentsMargins(0, 0, 0, 0)
        self.gbDatenEingabe = QGroupBox(dlgQuantenHarmonischerOszillator)
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
        self.layoutWidget_3.setGeometry(QRect(10, 20, 531, 50))
        self.hlySchieferWurf = QHBoxLayout(self.layoutWidget_3)
        self.hlySchieferWurf.setSpacing(0)
        self.hlySchieferWurf.setObjectName(u"hlySchieferWurf")
        self.hlySchieferWurf.setContentsMargins(0, 0, 0, 0)
        self.lbPotentialFaktor = QLabel(self.layoutWidget_3)
        self.lbPotentialFaktor.setObjectName(u"lbPotentialFaktor")
        self.lbPotentialFaktor.setEnabled(False)

        self.hlySchieferWurf.addWidget(self.lbPotentialFaktor)

        self.lePotentialFaktorInput = QLineEdit(self.layoutWidget_3)
        self.lePotentialFaktorInput.setObjectName(u"lePotentialFaktorInput")
        self.lePotentialFaktorInput.setEnabled(False)
        self.lePotentialFaktorInput.setMaximumSize(QSize(998, 16777215))
        self.lePotentialFaktorInput.setMaxLength(100)

        self.hlySchieferWurf.addWidget(self.lePotentialFaktorInput)

        self.lbAnzahlEnergieniveaus = QLabel(self.layoutWidget_3)
        self.lbAnzahlEnergieniveaus.setObjectName(u"lbAnzahlEnergieniveaus")
        self.lbAnzahlEnergieniveaus.setEnabled(False)

        self.hlySchieferWurf.addWidget(self.lbAnzahlEnergieniveaus)

        self.spNoofEnergieNiveaus = QSpinBox(self.layoutWidget_3)
        self.spNoofEnergieNiveaus.setObjectName(u"spNoofEnergieNiveaus")
        self.spNoofEnergieNiveaus.setMinimum(1)
        self.spNoofEnergieNiveaus.setMaximum(6)

        self.hlySchieferWurf.addWidget(self.spNoofEnergieNiveaus)

        self.pbEingabe = QPushButton(dlgQuantenHarmonischerOszillator)
        self.pbEingabe.setObjectName(u"pbEingabe")
        self.pbEingabe.setGeometry(QRect(10, 20, 121, 34))
        self.line = QFrame(dlgQuantenHarmonischerOszillator)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(630, 10, 20, 441))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.lbGraphExtensionTitel = QLabel(dlgQuantenHarmonischerOszillator)
        self.lbGraphExtensionTitel.setObjectName(u"lbGraphExtensionTitel")
        self.lbGraphExtensionTitel.setGeometry(QRect(660, 30, 321, 31))
        self.lbGraphExtensionTitel.setStyleSheet(u"QLabel{\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.gbErgbnis = QGroupBox(dlgQuantenHarmonischerOszillator)
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
        self.lbBerechnung = QLabel(self.layoutWidget1)
        self.lbBerechnung.setObjectName(u"lbBerechnung")

        self.horizontalLayout_11.addWidget(self.lbBerechnung)

        self.leNoofEnergieNiveaus = QLineEdit(self.layoutWidget1)
        self.leNoofEnergieNiveaus.setObjectName(u"leNoofEnergieNiveaus")
        self.leNoofEnergieNiveaus.setEnabled(False)

        self.horizontalLayout_11.addWidget(self.leNoofEnergieNiveaus)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)

        self.lbStatus = QLabel(self.layoutWidget1)
        self.lbStatus.setObjectName(u"lbStatus")

        self.horizontalLayout_10.addWidget(self.lbStatus)

        self.leStatus = QLineEdit(self.layoutWidget1)
        self.leStatus.setObjectName(u"leStatus")
        self.leStatus.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.leStatus)

        self.gbDarstellung = QGroupBox(dlgQuantenHarmonischerOszillator)
        self.gbDarstellung.setObjectName(u"gbDarstellung")
        self.gbDarstellung.setGeometry(QRect(10, 320, 201, 80))
        self.gbDarstellung.setStyleSheet(u"QGroupBox {\n"
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
        self.rbPsi = QRadioButton(self.gbDarstellung)
        self.rbPsi.setObjectName(u"rbPsi")
        self.rbPsi.setGeometry(QRect(20, 30, 61, 22))
        icon = QIcon()
        icon.addFile(u"../../Apps/PycharmProjects/Physik/icons8-psi-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.rbPsi.setIcon(icon)
        self.rbPsi.setIconSize(QSize(32, 16))
        self.rbPsiSquare = QRadioButton(self.gbDarstellung)
        self.rbPsiSquare.setObjectName(u"rbPsiSquare")
        self.rbPsiSquare.setGeometry(QRect(100, 30, 71, 22))
        self.rbPsiSquare.setIcon(icon)
        self.rbPsiSquare.setChecked(True)

        self.retranslateUi(dlgQuantenHarmonischerOszillator)
        self.buttonBox.accepted.connect(dlgQuantenHarmonischerOszillator.accept)

        QMetaObject.connectSlotsByName(dlgQuantenHarmonischerOszillator)
    # setupUi

    def retranslateUi(self, dlgQuantenHarmonischerOszillator):
        dlgQuantenHarmonischerOszillator.setWindowTitle(QCoreApplication.translate("dlgQuantenHarmonischerOszillator", u"harmonischer Quanten Oszillator", None))
        self.pbBerechne.setText(QCoreApplication.translate("dlgQuantenHarmonischerOszillator", u"Berechne", None))
        self.pbGraphik.setText(QCoreApplication.translate("dlgQuantenHarmonischerOszillator", u"Graph >>>", None))
        self.gbDatenEingabe.setTitle(QCoreApplication.translate("dlgQuantenHarmonischerOszillator", u"Daten Eingabe", None))
#if QT_CONFIG(tooltip)
        self.lbPotentialFaktor.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lbPotentialFaktor.setText(QCoreApplication.translate("dlgQuantenHarmonischerOszillator", u"Potential Faktor q (V=q*x^2):", None))
#if QT_CONFIG(tooltip)
        self.lePotentialFaktorInput.setToolTip(QCoreApplication.translate("dlgQuantenHarmonischerOszillator", u"Potentialbreite", None))
#endif // QT_CONFIG(tooltip)
        self.lePotentialFaktorInput.setText(QCoreApplication.translate("dlgQuantenHarmonischerOszillator", u"1", None))
#if QT_CONFIG(tooltip)
        self.lbAnzahlEnergieniveaus.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lbAnzahlEnergieniveaus.setText(QCoreApplication.translate("dlgQuantenHarmonischerOszillator", u"Anzahl Energieniveaus:", None))
        self.pbEingabe.setText(QCoreApplication.translate("dlgQuantenHarmonischerOszillator", u"Dateneingabe", None))
        self.lbGraphExtensionTitel.setText(QCoreApplication.translate("dlgQuantenHarmonischerOszillator", u"Graphik Titel", None))
        self.gbErgbnis.setTitle(QCoreApplication.translate("dlgQuantenHarmonischerOszillator", u"Ergebnis", None))
        self.lbBerechnung.setText(QCoreApplication.translate("dlgQuantenHarmonischerOszillator", u"Anzahl Energieniveaus:", None))
        self.lbStatus.setText(QCoreApplication.translate("dlgQuantenHarmonischerOszillator", u"Status:", None))
        self.gbDarstellung.setTitle(QCoreApplication.translate("dlgQuantenHarmonischerOszillator", u"Darstellung", None))
        self.rbPsi.setText("")
        self.rbPsiSquare.setText(QCoreApplication.translate("dlgQuantenHarmonischerOszillator", u"**2", None))
    # retranslateUi

