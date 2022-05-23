# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogRadioactiveDecay.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgRadioactiveDecay(object):
    def setupUi(self, dlgRadioactiveDecay):
        if not dlgRadioactiveDecay.objectName():
            dlgRadioactiveDecay.setObjectName(u"dlgRadioactiveDecay")
        dlgRadioactiveDecay.resize(605, 454)
        self.pbBerechne = QPushButton(dlgRadioactiveDecay)
        self.pbBerechne.setObjectName(u"pbBerechne")
        self.pbBerechne.setGeometry(QRect(10, 170, 84, 34))
        self.layoutWidget = QWidget(dlgRadioactiveDecay)
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

        self.verticalLayoutWidget = QWidget(dlgRadioactiveDecay)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(660, 80, 391, 361))
        self.lyGraph = QVBoxLayout(self.verticalLayoutWidget)
        self.lyGraph.setObjectName(u"lyGraph")
        self.lyGraph.setContentsMargins(0, 0, 0, 0)
        self.gbDatenEingabe = QGroupBox(dlgRadioactiveDecay)
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
        self.lbAnfangsmenge = QLabel(self.layoutWidget_3)
        self.lbAnfangsmenge.setObjectName(u"lbAnfangsmenge")
        self.lbAnfangsmenge.setEnabled(False)

        self.hlySchieferWurf.addWidget(self.lbAnfangsmenge)

        self.leAnfangsmengeInput = QLineEdit(self.layoutWidget_3)
        self.leAnfangsmengeInput.setObjectName(u"leAnfangsmengeInput")
        self.leAnfangsmengeInput.setEnabled(False)
        self.leAnfangsmengeInput.setMaximumSize(QSize(998, 16777215))
        self.leAnfangsmengeInput.setMaxLength(100)

        self.hlySchieferWurf.addWidget(self.leAnfangsmengeInput)

        self.lbHalbwertszeit = QLabel(self.layoutWidget_3)
        self.lbHalbwertszeit.setObjectName(u"lbHalbwertszeit")
        self.lbHalbwertszeit.setEnabled(False)

        self.hlySchieferWurf.addWidget(self.lbHalbwertszeit)

        self.leHalbwertszeitInput = QLineEdit(self.layoutWidget_3)
        self.leHalbwertszeitInput.setObjectName(u"leHalbwertszeitInput")
        self.leHalbwertszeitInput.setEnabled(False)
        self.leHalbwertszeitInput.setMaximumSize(QSize(998, 16777215))
        self.leHalbwertszeitInput.setMaxLength(100)

        self.hlySchieferWurf.addWidget(self.leHalbwertszeitInput)

        self.pbEingabe = QPushButton(dlgRadioactiveDecay)
        self.pbEingabe.setObjectName(u"pbEingabe")
        self.pbEingabe.setGeometry(QRect(10, 20, 121, 34))
        self.line = QFrame(dlgRadioactiveDecay)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(630, 10, 20, 441))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.lbGraphExtensionTitel = QLabel(dlgRadioactiveDecay)
        self.lbGraphExtensionTitel.setObjectName(u"lbGraphExtensionTitel")
        self.lbGraphExtensionTitel.setGeometry(QRect(660, 30, 321, 31))
        self.lbGraphExtensionTitel.setStyleSheet(u"QLabel{\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.gbErgbnis = QGroupBox(dlgRadioactiveDecay)
        self.gbErgbnis.setObjectName(u"gbErgbnis")
        self.gbErgbnis.setGeometry(QRect(10, 210, 571, 81))
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

        self.leInverseHalbwertszeit = QLineEdit(self.layoutWidget1)
        self.leInverseHalbwertszeit.setObjectName(u"leInverseHalbwertszeit")
        self.leInverseHalbwertszeit.setEnabled(False)

        self.horizontalLayout_11.addWidget(self.leInverseHalbwertszeit)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)

        self.lbStatus = QLabel(self.layoutWidget1)
        self.lbStatus.setObjectName(u"lbStatus")

        self.horizontalLayout_10.addWidget(self.lbStatus)

        self.leStatus = QLineEdit(self.layoutWidget1)
        self.leStatus.setObjectName(u"leStatus")
        self.leStatus.setEnabled(False)

        self.horizontalLayout_10.addWidget(self.leStatus)

        self.gbBeispiele = QGroupBox(dlgRadioactiveDecay)
        self.gbBeispiele.setObjectName(u"gbBeispiele")
        self.gbBeispiele.setEnabled(True)
        self.gbBeispiele.setGeometry(QRect(10, 290, 571, 91))
        self.gbBeispiele.setStyleSheet(u"QGroupBox {\n"
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
        self.layoutWidget_4 = QWidget(self.gbBeispiele)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 30, 531, 41))
        self.hlySchieferWurf_2 = QHBoxLayout(self.layoutWidget_4)
        self.hlySchieferWurf_2.setSpacing(0)
        self.hlySchieferWurf_2.setObjectName(u"hlySchieferWurf_2")
        self.hlySchieferWurf_2.setContentsMargins(0, 0, 0, 0)
        self.lbElement = QLabel(self.layoutWidget_4)
        self.lbElement.setObjectName(u"lbElement")
        self.lbElement.setEnabled(True)

        self.hlySchieferWurf_2.addWidget(self.lbElement)

        self.cbElemente = QComboBox(self.layoutWidget_4)
        self.cbElemente.setObjectName(u"cbElemente")

        self.hlySchieferWurf_2.addWidget(self.cbElemente)

        self.lbStrahlung = QLabel(self.layoutWidget_4)
        self.lbStrahlung.setObjectName(u"lbStrahlung")

        self.hlySchieferWurf_2.addWidget(self.lbStrahlung)

        self.pteStrahlungsarten = QPlainTextEdit(self.layoutWidget_4)
        self.pteStrahlungsarten.setObjectName(u"pteStrahlungsarten")

        self.hlySchieferWurf_2.addWidget(self.pteStrahlungsarten)

        self.lbHalbwertszeit_2 = QLabel(self.layoutWidget_4)
        self.lbHalbwertszeit_2.setObjectName(u"lbHalbwertszeit_2")
        self.lbHalbwertszeit_2.setEnabled(True)

        self.hlySchieferWurf_2.addWidget(self.lbHalbwertszeit_2)

        self.pteHalbwertszeit = QPlainTextEdit(self.layoutWidget_4)
        self.pteHalbwertszeit.setObjectName(u"pteHalbwertszeit")

        self.hlySchieferWurf_2.addWidget(self.pteHalbwertszeit)


        self.retranslateUi(dlgRadioactiveDecay)
        self.buttonBox.accepted.connect(dlgRadioactiveDecay.accept)

        QMetaObject.connectSlotsByName(dlgRadioactiveDecay)
    # setupUi

    def retranslateUi(self, dlgRadioactiveDecay):
        dlgRadioactiveDecay.setWindowTitle(QCoreApplication.translate("dlgRadioactiveDecay", u"Radioaktiver Zerfall", None))
        self.pbBerechne.setText(QCoreApplication.translate("dlgRadioactiveDecay", u"Berechne", None))
        self.pbGraphik.setText(QCoreApplication.translate("dlgRadioactiveDecay", u"Graph >>>", None))
        self.gbDatenEingabe.setTitle(QCoreApplication.translate("dlgRadioactiveDecay", u"Daten Eingabe", None))
#if QT_CONFIG(tooltip)
        self.lbAnfangsmenge.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lbAnfangsmenge.setText(QCoreApplication.translate("dlgRadioactiveDecay", u"Anfangsmenge N0:", None))
#if QT_CONFIG(tooltip)
        self.leAnfangsmengeInput.setToolTip(QCoreApplication.translate("dlgRadioactiveDecay", u"Potentialbreite", None))
#endif // QT_CONFIG(tooltip)
        self.leAnfangsmengeInput.setText(QCoreApplication.translate("dlgRadioactiveDecay", u"1000", None))
#if QT_CONFIG(tooltip)
        self.lbHalbwertszeit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lbHalbwertszeit.setText(QCoreApplication.translate("dlgRadioactiveDecay", u"Halbwertszeit (T):", None))
#if QT_CONFIG(tooltip)
        self.leHalbwertszeitInput.setToolTip(QCoreApplication.translate("dlgRadioactiveDecay", u"Potentialbreite", None))
#endif // QT_CONFIG(tooltip)
        self.leHalbwertszeitInput.setText(QCoreApplication.translate("dlgRadioactiveDecay", u"1000", None))
        self.pbEingabe.setText(QCoreApplication.translate("dlgRadioactiveDecay", u"Dateneingabe", None))
        self.lbGraphExtensionTitel.setText(QCoreApplication.translate("dlgRadioactiveDecay", u"Graphik Titel", None))
        self.gbErgbnis.setTitle(QCoreApplication.translate("dlgRadioactiveDecay", u"Ergebnis", None))
        self.lbBerechnung.setText(QCoreApplication.translate("dlgRadioactiveDecay", u"lambda (1/T):", None))
        self.lbStatus.setText(QCoreApplication.translate("dlgRadioactiveDecay", u"Status:", None))
        self.gbBeispiele.setTitle(QCoreApplication.translate("dlgRadioactiveDecay", u"Beispiele", None))
#if QT_CONFIG(tooltip)
        self.lbElement.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lbElement.setText(QCoreApplication.translate("dlgRadioactiveDecay", u"Element:", None))
        self.lbStrahlung.setText(QCoreApplication.translate("dlgRadioactiveDecay", u"Strahlungsarten:", None))
#if QT_CONFIG(tooltip)
        self.lbHalbwertszeit_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lbHalbwertszeit_2.setText(QCoreApplication.translate("dlgRadioactiveDecay", u"Halbwertszeit (T):", None))
    # retranslateUi

