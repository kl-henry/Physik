# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogSchieferWurf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgSchieferWurf(object):
    def setupUi(self, dlgSchieferWurf):
        if not dlgSchieferWurf.objectName():
            dlgSchieferWurf.setObjectName(u"dlgSchieferWurf")
        dlgSchieferWurf.resize(598, 454)
        self.pbBerechne = QPushButton(dlgSchieferWurf)
        self.pbBerechne.setObjectName(u"pbBerechne")
        self.pbBerechne.setGeometry(QRect(10, 170, 84, 34))
        self.layoutWidget = QWidget(dlgSchieferWurf)
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

        self.verticalLayoutWidget = QWidget(dlgSchieferWurf)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(660, 80, 391, 361))
        self.lyGraph = QVBoxLayout(self.verticalLayoutWidget)
        self.lyGraph.setObjectName(u"lyGraph")
        self.lyGraph.setContentsMargins(0, 0, 0, 0)
        # self.pbVergleich = QPushButton(self.verticalLayoutWidget)
        # self.pbVergleich.setObjectName(u"pbVergleich")
        #
        # self.lyGraph.addWidget(self.pbVergleich)

        self.gbDatenEingabe = QGroupBox(dlgSchieferWurf)
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
        self.lbLuftwiderstand = QLabel(self.layoutWidget_3)
        self.lbLuftwiderstand.setObjectName(u"lbLuftwiderstand")
        self.lbLuftwiderstand.setEnabled(False)

        self.hlySchieferWurf.addWidget(self.lbLuftwiderstand)

        self.leLuftwiderstandInput = QLineEdit(self.layoutWidget_3)
        self.leLuftwiderstandInput.setObjectName(u"leLuftwiderstandInput")
        self.leLuftwiderstandInput.setEnabled(False)
        self.leLuftwiderstandInput.setMaximumSize(QSize(998, 16777215))
        self.leLuftwiderstandInput.setMaxLength(100)

        self.hlySchieferWurf.addWidget(self.leLuftwiderstandInput)

        self.lbV0 = QLabel(self.layoutWidget_3)
        self.lbV0.setObjectName(u"lbV0")

        self.hlySchieferWurf.addWidget(self.lbV0)

        self.leV0Input = QLineEdit(self.layoutWidget_3)
        self.leV0Input.setObjectName(u"leV0Input")
        self.leV0Input.setEnabled(False)

        self.hlySchieferWurf.addWidget(self.leV0Input)

        self.lbWinkel = QLabel(self.layoutWidget_3)
        self.lbWinkel.setObjectName(u"lbWinkel")

        self.hlySchieferWurf.addWidget(self.lbWinkel)

        self.leWinkelInput = QLineEdit(self.layoutWidget_3)
        self.leWinkelInput.setObjectName(u"leWinkelInput")
        self.leWinkelInput.setEnabled(False)

        self.hlySchieferWurf.addWidget(self.leWinkelInput)

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

        self.pbEingabe = QPushButton(dlgSchieferWurf)
        self.pbEingabe.setObjectName(u"pbEingabe")
        self.pbEingabe.setGeometry(QRect(10, 20, 121, 34))
        self.line = QFrame(dlgSchieferWurf)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(630, 10, 20, 441))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.lbGraphExtensionTitel = QLabel(dlgSchieferWurf)
        self.lbGraphExtensionTitel.setObjectName(u"lbGraphExtensionTitel")
        self.lbGraphExtensionTitel.setGeometry(QRect(660, 30, 321, 31))
        self.lbGraphExtensionTitel.setStyleSheet(u"QLabel{\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.gbErgbnis = QGroupBox(dlgSchieferWurf)
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
        self.lbV0x = QLabel(self.layoutWidget1)
        self.lbV0x.setObjectName(u"lbV0x")

        self.horizontalLayout_11.addWidget(self.lbV0x)

        self.leV0x = QLineEdit(self.layoutWidget1)
        self.leV0x.setObjectName(u"leV0x")
        self.leV0x.setEnabled(False)

        self.horizontalLayout_11.addWidget(self.leV0x)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)

        self.lbV0y = QLabel(self.layoutWidget1)
        self.lbV0y.setObjectName(u"lbV0y")

        self.horizontalLayout_10.addWidget(self.lbV0y)

        self.leV0y = QLineEdit(self.layoutWidget1)
        self.leV0y.setObjectName(u"leV0y")
        self.leV0y.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.leV0y)


        self.retranslateUi(dlgSchieferWurf)
        self.buttonBox.accepted.connect(dlgSchieferWurf.accept)

        QMetaObject.connectSlotsByName(dlgSchieferWurf)
    # setupUi

    def retranslateUi(self, dlgSchieferWurf):
        dlgSchieferWurf.setWindowTitle(QCoreApplication.translate("dlgSchieferWurf", u"Schiefer Wurf mit Luftwiderstand", None))
        self.pbBerechne.setText(QCoreApplication.translate("dlgSchieferWurf", u"Berechne", None))
        self.pbGraphik.setText(QCoreApplication.translate("dlgSchieferWurf", u"Graph >>>", None))
        # self.pbVergleich.setText(QCoreApplication.translate("dlgSchieferWurf", u"Vergleich mit/ohne Luftwiderstand", None))
        self.gbDatenEingabe.setTitle(QCoreApplication.translate("dlgSchieferWurf", u"Daten Eingabe", None))
        self.lbLuftwiderstand.setText(QCoreApplication.translate("dlgSchieferWurf", u"Luftwiderstand:", None))
#if QT_CONFIG(tooltip)
        self.lbV0.setToolTip(QCoreApplication.translate("dlgSchieferWurf", u"<html><head/><body><p>Anfangsgeschwingikeit [m/s]</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lbV0.setText(QCoreApplication.translate("dlgSchieferWurf", u"v0:", None))
#if QT_CONFIG(tooltip)
        self.leV0Input.setToolTip(QCoreApplication.translate("dlgSchieferWurf", u"<html><head/><body><p>Anfangsgeschwingikeit [m/s]</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lbWinkel.setText(QCoreApplication.translate("dlgSchieferWurf", u"Winkel:", None))
        self.lbLaufzeit_2.setText(QCoreApplication.translate("dlgSchieferWurf", u"Laufzeit:", None))
        self.lbIntervalle_2.setText(QCoreApplication.translate("dlgSchieferWurf", u"Intervalle:", None))
        self.pbEingabe.setText(QCoreApplication.translate("dlgSchieferWurf", u"Dateneingabe", None))
        self.lbGraphExtensionTitel.setText(QCoreApplication.translate("dlgSchieferWurf", u"Graphik Titel", None))
        self.gbErgbnis.setTitle(QCoreApplication.translate("dlgSchieferWurf", u"Ergebnis", None))
        self.lbV0x.setText(QCoreApplication.translate("dlgSchieferWurf", u"v0x:", None))
        self.lbV0y.setText(QCoreApplication.translate("dlgSchieferWurf", u"v0y:", None))
    # retranslateUi

