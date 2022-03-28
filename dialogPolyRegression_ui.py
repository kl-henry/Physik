# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogPolyRegression.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dlgPolyRegression(object):
    def setupUi(self, dlgPolyRegression):
        if not dlgPolyRegression.objectName():
            dlgPolyRegression.setObjectName(u"dlgPolyRegression")
        dlgPolyRegression.resize(603, 459)
        self.layoutWidget = QWidget(dlgPolyRegression)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 160, 561, 81))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbX_Werte = QLabel(self.layoutWidget)
        self.lbX_Werte.setObjectName(u"lbX_Werte")

        self.verticalLayout_2.addWidget(self.lbX_Werte)

        self.lbY_Werte = QLabel(self.layoutWidget)
        self.lbY_Werte.setObjectName(u"lbY_Werte")

        self.verticalLayout_2.addWidget(self.lbY_Werte)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.leX_Werte = QLineEdit(self.layoutWidget)
        self.leX_Werte.setObjectName(u"leX_Werte")
        self.leX_Werte.setReadOnly(True)

        self.verticalLayout.addWidget(self.leX_Werte)

        self.leY_Werte = QLineEdit(self.layoutWidget)
        self.leY_Werte.setObjectName(u"leY_Werte")
        self.leY_Werte.setReadOnly(True)

        self.verticalLayout.addWidget(self.leY_Werte)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.gbErgebnis = QGroupBox(dlgPolyRegression)
        self.gbErgebnis.setObjectName(u"gbErgebnis")
        self.gbErgebnis.setGeometry(QRect(10, 290, 361, 110))
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
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF0ECE, stop: 1 #FFFFFF);\n"
"}")
        self.frErgebnis = QFrame(self.gbErgebnis)
        self.frErgebnis.setObjectName(u"frErgebnis")
        self.frErgebnis.setGeometry(QRect(20, 19, 301, 81))
        self.horizontalLayout_2 = QHBoxLayout(self.frErgebnis)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.lbSteigung = QLabel(self.frErgebnis)
        self.lbSteigung.setObjectName(u"lbSteigung")

        self.verticalLayout_3.addWidget(self.lbSteigung)

        self.lbSchnittpunkt = QLabel(self.frErgebnis)
        self.lbSchnittpunkt.setObjectName(u"lbSchnittpunkt")

        self.verticalLayout_3.addWidget(self.lbSchnittpunkt)

        self.lbFehler = QLabel(self.frErgebnis)
        self.lbFehler.setObjectName(u"lbFehler")

        self.verticalLayout_3.addWidget(self.lbFehler)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbSteigungErgebnis = QLabel(self.frErgebnis)
        self.lbSteigungErgebnis.setObjectName(u"lbSteigungErgebnis")
        self.lbSteigungErgebnis.setAutoFillBackground(False)
        self.lbSteigungErgebnis.setStyleSheet(u"background-color: lightgreen;")

        self.verticalLayout_4.addWidget(self.lbSteigungErgebnis)

        self.lbSchnittpunktErbegnis = QLabel(self.frErgebnis)
        self.lbSchnittpunktErbegnis.setObjectName(u"lbSchnittpunktErbegnis")
        self.lbSchnittpunktErbegnis.setStyleSheet(u"background-color: lightgreen;")

        self.verticalLayout_4.addWidget(self.lbSchnittpunktErbegnis)

        self.lbFehlerErgebnis = QLabel(self.frErgebnis)
        self.lbFehlerErgebnis.setObjectName(u"lbFehlerErgebnis")
        self.lbFehlerErgebnis.setAutoFillBackground(False)
        self.lbFehlerErgebnis.setStyleSheet(u"background-color: lightgreen;")

        self.verticalLayout_4.addWidget(self.lbFehlerErgebnis)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.frPolynomErgebnis = QFrame(self.gbErgebnis)
        self.frPolynomErgebnis.setObjectName(u"frPolynomErgebnis")
        self.frPolynomErgebnis.setGeometry(QRect(20, 19, 301, 81))
        self.verticalLayout_5 = QVBoxLayout(self.frPolynomErgebnis)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbPolynomErgebnis = QLabel(self.frPolynomErgebnis)
        self.lbPolynomErgebnis.setObjectName(u"lbPolynomErgebnis")

        self.verticalLayout_5.addWidget(self.lbPolynomErgebnis)

        self.textEdit = QTextEdit(self.frPolynomErgebnis)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_5.addWidget(self.textEdit)

        self.pbBerechne = QPushButton(dlgPolyRegression)
        self.pbBerechne.setObjectName(u"pbBerechne")
        self.pbBerechne.setGeometry(QRect(10, 250, 84, 34))
        self.layoutWidget1 = QWidget(dlgPolyRegression)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 410, 555, 36))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pbBeispiel = QPushButton(self.layoutWidget1)
        self.pbBeispiel.setObjectName(u"pbBeispiel")

        self.horizontalLayout_3.addWidget(self.pbBeispiel)

        self.horizontalSpacer_3 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.horizontalSpacer_2 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.pbGraphik = QPushButton(self.layoutWidget1)
        self.pbGraphik.setObjectName(u"pbGraphik")

        self.horizontalLayout_3.addWidget(self.pbGraphik)

        self.horizontalSpacer = QSpacerItem(98, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.buttonBox = QDialogButtonBox(self.layoutWidget1)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.horizontalLayout_3.addWidget(self.buttonBox)

        self.verticalLayoutWidget = QWidget(dlgPolyRegression)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(660, 80, 391, 361))
        self.lyGraph = QVBoxLayout(self.verticalLayoutWidget)
        self.lyGraph.setObjectName(u"lyGraph")
        self.lyGraph.setContentsMargins(0, 0, 0, 0)
        self.gbDatenEingabe = QGroupBox(dlgPolyRegression)
        self.gbDatenEingabe.setObjectName(u"gbDatenEingabe")
        self.gbDatenEingabe.setEnabled(False)
        self.gbDatenEingabe.setGeometry(QRect(10, 60, 561, 91))
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
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF0ECE, stop: 1 #FFFFFF);\n"
"}")
        self.layoutWidget2 = QWidget(self.gbDatenEingabe)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 30, 541, 38))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbGraphTitle = QLabel(self.layoutWidget2)
        self.lbGraphTitle.setObjectName(u"lbGraphTitle")

        self.horizontalLayout_4.addWidget(self.lbGraphTitle)

        self.leGraphTitleInput = QLineEdit(self.layoutWidget2)
        self.leGraphTitleInput.setObjectName(u"leGraphTitleInput")
        self.leGraphTitleInput.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.leGraphTitleInput)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbXWert = QLabel(self.layoutWidget2)
        self.lbXWert.setObjectName(u"lbXWert")

        self.horizontalLayout_5.addWidget(self.lbXWert)

        self.leXInput = QLineEdit(self.layoutWidget2)
        self.leXInput.setObjectName(u"leXInput")
        self.leXInput.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.leXInput)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.lbYWert = QLabel(self.layoutWidget2)
        self.lbYWert.setObjectName(u"lbYWert")

        self.horizontalLayout_6.addWidget(self.lbYWert)

        self.leYInput = QLineEdit(self.layoutWidget2)
        self.leYInput.setObjectName(u"leYInput")
        self.leYInput.setEnabled(False)

        self.horizontalLayout_6.addWidget(self.leYInput)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)

        self.pbUebernehmen = QPushButton(self.layoutWidget2)
        self.pbUebernehmen.setObjectName(u"pbUebernehmen")
        self.pbUebernehmen.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.pbUebernehmen)

        self.pbEingabe = QPushButton(dlgPolyRegression)
        self.pbEingabe.setObjectName(u"pbEingabe")
        self.pbEingabe.setGeometry(QRect(10, 20, 121, 34))
        self.line = QFrame(dlgPolyRegression)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(630, 10, 20, 441))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.lbGraphExtensionTitel = QLabel(dlgPolyRegression)
        self.lbGraphExtensionTitel.setObjectName(u"lbGraphExtensionTitel")
        self.lbGraphExtensionTitel.setGeometry(QRect(660, 30, 321, 31))
        self.lbGraphExtensionTitel.setStyleSheet(u"QLabel{\n"
"    border: 2px solid green;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.frPolynomDegree = QFrame(dlgPolyRegression)
        self.frPolynomDegree.setObjectName(u"frPolynomDegree")
        self.frPolynomDegree.setGeometry(QRect(100, 241, 211, 51))
        self.frPolynomDegree.setFrameShape(QFrame.Box)
        self.frPolynomDegree.setFrameShadow(QFrame.Raised)
        self.formLayoutWidget = QWidget(self.frPolynomDegree)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 191, 34))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lbPolynomGrad = QLabel(self.formLayoutWidget)
        self.lbPolynomGrad.setObjectName(u"lbPolynomGrad")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbPolynomGrad)

        self.sbPolyDegree = QSpinBox(self.formLayoutWidget)
        self.sbPolyDegree.setObjectName(u"sbPolyDegree")
        self.sbPolyDegree.setMinimum(1)
        self.sbPolyDegree.setMaximum(10)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.sbPolyDegree)


        self.retranslateUi(dlgPolyRegression)
        self.buttonBox.accepted.connect(dlgPolyRegression.accept)

        QMetaObject.connectSlotsByName(dlgPolyRegression)
    # setupUi

    def retranslateUi(self, dlgPolyRegression):
        dlgPolyRegression.setWindowTitle(QCoreApplication.translate("dlgPolyRegression", u"Lineare Regression", None))
        self.lbX_Werte.setText(QCoreApplication.translate("dlgPolyRegression", u"X Werte:", None))
        self.lbY_Werte.setText(QCoreApplication.translate("dlgPolyRegression", u"Y Werte:", None))
        self.gbErgebnis.setTitle(QCoreApplication.translate("dlgPolyRegression", u"Ergebnis", None))
        self.lbSteigung.setText(QCoreApplication.translate("dlgPolyRegression", u"Steigung:", None))
        self.lbSchnittpunkt.setText(QCoreApplication.translate("dlgPolyRegression", u"Schnittpunkt:", None))
        self.lbFehler.setText(QCoreApplication.translate("dlgPolyRegression", u"Fehler:", None))
        self.lbSteigungErgebnis.setText(QCoreApplication.translate("dlgPolyRegression", u"Steigung a", None))
        self.lbSchnittpunktErbegnis.setText(QCoreApplication.translate("dlgPolyRegression", u"Schnittpunkt b", None))
        self.lbFehlerErgebnis.setText(QCoreApplication.translate("dlgPolyRegression", u"Fehler Score", None))
        self.lbPolynomErgebnis.setText(QCoreApplication.translate("dlgPolyRegression", u"resultierendes Polynom:", None))
        self.pbBerechne.setText(QCoreApplication.translate("dlgPolyRegression", u"Berechne", None))
        self.pbBeispiel.setText(QCoreApplication.translate("dlgPolyRegression", u"Beispiel (Millikan)", None))
        self.pbGraphik.setText(QCoreApplication.translate("dlgPolyRegression", u"Graph >>>", None))
        self.gbDatenEingabe.setTitle(QCoreApplication.translate("dlgPolyRegression", u"Daten Eingabe", None))
        self.lbGraphTitle.setText(QCoreApplication.translate("dlgPolyRegression", u"Grafik Titel:", None))
        self.lbXWert.setText(QCoreApplication.translate("dlgPolyRegression", u"X:", None))
        self.lbYWert.setText(QCoreApplication.translate("dlgPolyRegression", u"Y:", None))
        self.pbUebernehmen.setText(QCoreApplication.translate("dlgPolyRegression", u"\u00dcbernehmen", None))
        self.pbEingabe.setText(QCoreApplication.translate("dlgPolyRegression", u"Dateneingabe", None))
        self.lbGraphExtensionTitel.setText(QCoreApplication.translate("dlgPolyRegression", u"Graphik Titel", None))
        self.lbPolynomGrad.setText(QCoreApplication.translate("dlgPolyRegression", u"Grad des Polynoms:", None))
    # retranslateUi

