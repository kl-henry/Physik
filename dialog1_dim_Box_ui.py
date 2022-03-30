# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog1_dim_Box.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlg_Win_1_dim_box(object):
    def setupUi(self, dlg_Win_1_dim_box):
        if not dlg_Win_1_dim_box.objectName():
            dlg_Win_1_dim_box.setObjectName(u"dlg_Win_1_dim_box")
        dlg_Win_1_dim_box.resize(598, 454)
        self.pbBerechne = QPushButton(dlg_Win_1_dim_box)
        self.pbBerechne.setObjectName(u"pbBerechne")
        self.pbBerechne.setGeometry(QRect(10, 170, 84, 34))
        self.layoutWidget = QWidget(dlg_Win_1_dim_box)
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

        self.verticalLayoutWidget = QWidget(dlg_Win_1_dim_box)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(660, 80, 391, 361))
        self.lyGraph = QVBoxLayout(self.verticalLayoutWidget)
        self.lyGraph.setObjectName(u"lyGraph")
        self.lyGraph.setContentsMargins(0, 0, 0, 0)
        self.pbVergleich = QPushButton(self.verticalLayoutWidget)
        self.pbVergleich.setObjectName(u"pbVergleich")

        self.lyGraph.addWidget(self.pbVergleich)

        self.gbDatenEingabe = QGroupBox(dlg_Win_1_dim_box)
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
        self.hlySchieferWurf = QHBoxLayout(self.layoutWidget_3)
        self.hlySchieferWurf.setSpacing(0)
        self.hlySchieferWurf.setObjectName(u"hlySchieferWurf")
        self.hlySchieferWurf.setContentsMargins(0, 0, 0, 0)
        self.lbPotentialWidth = QLabel(self.layoutWidget_3)
        self.lbPotentialWidth.setObjectName(u"lbPotentialWidth")
        self.lbPotentialWidth.setEnabled(False)

        self.hlySchieferWurf.addWidget(self.lbPotentialWidth)

        self.lePotentialWidthInput = QLineEdit(self.layoutWidget_3)
        self.lePotentialWidthInput.setObjectName(u"lePotentialWidthInput")
        self.lePotentialWidthInput.setEnabled(False)
        self.lePotentialWidthInput.setMaximumSize(QSize(998, 16777215))
        self.lePotentialWidthInput.setMaxLength(100)

        self.hlySchieferWurf.addWidget(self.lePotentialWidthInput)

        self.lbV0 = QLabel(self.layoutWidget_3)
        self.lbV0.setObjectName(u"lbV0")

        self.hlySchieferWurf.addWidget(self.lbV0)

        self.leV0Input = QLineEdit(self.layoutWidget_3)
        self.leV0Input.setObjectName(u"leV0Input")
        self.leV0Input.setEnabled(False)

        self.hlySchieferWurf.addWidget(self.leV0Input)

        self.lbX0 = QLabel(self.layoutWidget_3)
        self.lbX0.setObjectName(u"lbX0")

        self.hlySchieferWurf.addWidget(self.lbX0)

        self.leX0Input = QLineEdit(self.layoutWidget_3)
        self.leX0Input.setObjectName(u"leX0Input")
        self.leX0Input.setEnabled(False)

        self.hlySchieferWurf.addWidget(self.leX0Input)

        self.lbLaufzeit_2 = QLabel(self.layoutWidget_3)
        self.lbLaufzeit_2.setObjectName(u"lbLaufzeit_2")

        self.hlySchieferWurf.addWidget(self.lbLaufzeit_2)

        self.spLaufzeitInput = QSpinBox(self.layoutWidget_3)
        self.spLaufzeitInput.setObjectName(u"spLaufzeitInput")
        self.spLaufzeitInput.setEnabled(False)
        self.spLaufzeitInput.setMinimum(1)
        self.spLaufzeitInput.setMaximum(60)

        self.hlySchieferWurf.addWidget(self.spLaufzeitInput)

        self.lbIntervalle_2 = QLabel(self.layoutWidget_3)
        self.lbIntervalle_2.setObjectName(u"lbIntervalle_2")

        self.hlySchieferWurf.addWidget(self.lbIntervalle_2)

        self.spIntervalleInput = QSpinBox(self.layoutWidget_3)
        self.spIntervalleInput.setObjectName(u"spIntervalleInput")
        self.spIntervalleInput.setEnabled(False)
        self.spIntervalleInput.setMinimum(10)
        self.spIntervalleInput.setMaximum(1000)

        self.hlySchieferWurf.addWidget(self.spIntervalleInput)

        self.pbEingabe = QPushButton(dlg_Win_1_dim_box)
        self.pbEingabe.setObjectName(u"pbEingabe")
        self.pbEingabe.setGeometry(QRect(10, 20, 121, 34))
        self.line = QFrame(dlg_Win_1_dim_box)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(630, 10, 20, 441))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.lbGraphExtensionTitel = QLabel(dlg_Win_1_dim_box)
        self.lbGraphExtensionTitel.setObjectName(u"lbGraphExtensionTitel")
        self.lbGraphExtensionTitel.setGeometry(QRect(660, 30, 321, 31))
        self.lbGraphExtensionTitel.setStyleSheet(u"QLabel{\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.gbErgbnis = QGroupBox(dlg_Win_1_dim_box)
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


        self.retranslateUi(dlg_Win_1_dim_box)
        self.buttonBox.accepted.connect(dlg_Win_1_dim_box.accept)

        QMetaObject.connectSlotsByName(dlg_Win_1_dim_box)
    # setupUi

    def retranslateUi(self, dlg_Win_1_dim_box):
        dlg_Win_1_dim_box.setWindowTitle(QCoreApplication.translate("dlg_Win_1_dim_box", u"Teilchen im 1 dim. Potential", None))
        self.pbBerechne.setText(QCoreApplication.translate("dlg_Win_1_dim_box", u"Berechne", None))
        self.pbGraphik.setText(QCoreApplication.translate("dlg_Win_1_dim_box", u"Graph >>>", None))
        self.pbVergleich.setText(QCoreApplication.translate("dlg_Win_1_dim_box", u"Vergleich mit/ohne Luftwiderstand", None))
        self.gbDatenEingabe.setTitle(QCoreApplication.translate("dlg_Win_1_dim_box", u"Daten Eingabe", None))
        self.lbPotentialWidth.setText(QCoreApplication.translate("dlg_Win_1_dim_box", u"L\u00e4nge des Potentials:", None))
#if QT_CONFIG(tooltip)
        self.lbV0.setToolTip(QCoreApplication.translate("dlg_Win_1_dim_box", u"<html><head/><body><p>Anfangsgeschwingikeit [m/s]</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lbV0.setText(QCoreApplication.translate("dlg_Win_1_dim_box", u"v0:", None))
#if QT_CONFIG(tooltip)
        self.leV0Input.setToolTip(QCoreApplication.translate("dlg_Win_1_dim_box", u"<html><head/><body><p>Anfangsgeschwingikeit [m/s]</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lbX0.setText(QCoreApplication.translate("dlg_Win_1_dim_box", u"X0:", None))
        self.lbLaufzeit_2.setText(QCoreApplication.translate("dlg_Win_1_dim_box", u"Laufzeit:", None))
        self.lbIntervalle_2.setText(QCoreApplication.translate("dlg_Win_1_dim_box", u"Intervalle:", None))
        self.pbEingabe.setText(QCoreApplication.translate("dlg_Win_1_dim_box", u"Dateneingabe", None))
        self.lbGraphExtensionTitel.setText(QCoreApplication.translate("dlg_Win_1_dim_box", u"Graphik Titel", None))
        self.gbErgbnis.setTitle(QCoreApplication.translate("dlg_Win_1_dim_box", u"Ergebnis", None))
        self.lbIntervallLaenge.setText(QCoreApplication.translate("dlg_Win_1_dim_box", u"Zeitintervall:", None))
        self.lbStatus.setText(QCoreApplication.translate("dlg_Win_1_dim_box", u"Status:", None))
    # retranslateUi

