# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_physik.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Physik(object):
    def setupUi(self, Physik):
        if not Physik.objectName():
            Physik.setObjectName(u"Physik")
        Physik.resize(619, 537)
        self.action_Schlie_en = QAction(Physik)
        self.action_Schlie_en.setObjectName(u"action_Schlie_en")
        self.action_Impuls = QAction(Physik)
        self.action_Impuls.setObjectName(u"action_Impuls")
        self.actionVektorrechnung = QAction(Physik)
        self.actionVektorrechnung.setObjectName(u"actionVektorrechnung")
        self.action = QAction(Physik)
        self.action.setObjectName(u"action")
        self.actionLineare_Regression = QAction(Physik)
        self.actionLineare_Regression.setObjectName(u"actionLineare_Regression")
        self.actionkleinste_Quadrate_Polynom = QAction(Physik)
        self.actionkleinste_Quadrate_Polynom.setObjectName(u"actionkleinste_Quadrate_Polynom")
        self.action_ber = QAction(Physik)
        self.action_ber.setObjectName(u"action_ber")
        self.actionTest = QAction(Physik)
        self.actionTest.setObjectName(u"actionTest")
        self.actionEinfaches_Pendel = QAction(Physik)
        self.actionEinfaches_Pendel.setObjectName(u"actionEinfaches_Pendel")
        self.actionSchiefer_Wurf = QAction(Physik)
        self.actionSchiefer_Wurf.setObjectName(u"actionSchiefer_Wurf")
        self.actionLissajous_Figuren = QAction(Physik)
        self.actionLissajous_Figuren.setObjectName(u"actionLissajous_Figuren")
        self.actiongeladenes_Teichen_im_Magnetfeld = QAction(Physik)
        self.actiongeladenes_Teichen_im_Magnetfeld.setObjectName(u"actiongeladenes_Teichen_im_Magnetfeld")
        self.actionMinigolf = QAction(Physik)
        self.actionMinigolf.setObjectName(u"actionMinigolf")
        self.centralwidget = QWidget(Physik)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbMain = QLabel(self.centralwidget)
        self.lbMain.setObjectName(u"lbMain")
        self.lbMain.setGeometry(QRect(40, 30, 531, 411))
        self.lbMain.setPixmap(QPixmap(u"formula.png"))
        Physik.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Physik)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 619, 30))
        self.menu_Datei = QMenu(self.menubar)
        self.menu_Datei.setObjectName(u"menu_Datei")
        self.menuMechanik = QMenu(self.menubar)
        self.menuMechanik.setObjectName(u"menuMechanik")
        self.menu_ber = QMenu(self.menubar)
        self.menu_ber.setObjectName(u"menu_ber")
        self.menuMathematik = QMenu(self.menubar)
        self.menuMathematik.setObjectName(u"menuMathematik")
        self.menuInterpolation = QMenu(self.menuMathematik)
        self.menuInterpolation.setObjectName(u"menuInterpolation")
        self.menuElektrodynamik = QMenu(self.menubar)
        self.menuElektrodynamik.setObjectName(u"menuElektrodynamik")
        self.menuSimulation = QMenu(self.menubar)
        self.menuSimulation.setObjectName(u"menuSimulation")
        Physik.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Physik)
        self.statusbar.setObjectName(u"statusbar")
        Physik.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_Datei.menuAction())
        self.menubar.addAction(self.menuMechanik.menuAction())
        self.menubar.addAction(self.menuElektrodynamik.menuAction())
        self.menubar.addAction(self.menuMathematik.menuAction())
        self.menubar.addAction(self.menuSimulation.menuAction())
        self.menubar.addAction(self.menu_ber.menuAction())
        self.menu_Datei.addAction(self.action_Schlie_en)
        self.menuMechanik.addAction(self.action_Impuls)
        self.menuMechanik.addAction(self.actionEinfaches_Pendel)
        self.menuMechanik.addAction(self.actionSchiefer_Wurf)
        self.menuMechanik.addAction(self.actionLissajous_Figuren)
        self.menu_ber.addAction(self.action_ber)
        self.menu_ber.addAction(self.actionTest)
        self.menuMathematik.addAction(self.actionVektorrechnung)
        self.menuMathematik.addAction(self.menuInterpolation.menuAction())
        self.menuInterpolation.addAction(self.actionLineare_Regression)
        self.menuInterpolation.addAction(self.actionkleinste_Quadrate_Polynom)
        self.menuElektrodynamik.addAction(self.actiongeladenes_Teichen_im_Magnetfeld)
        self.menuSimulation.addAction(self.actionMinigolf)

        self.retranslateUi(Physik)
        self.action_Schlie_en.triggered.connect(Physik.close)

        QMetaObject.connectSlotsByName(Physik)
    # setupUi

    def retranslateUi(self, Physik):
        Physik.setWindowTitle(QCoreApplication.translate("Physik", u"Physik", None))
        self.action_Schlie_en.setText(QCoreApplication.translate("Physik", u"&Schlie\u00dfen", None))
        self.action_Impuls.setText(QCoreApplication.translate("Physik", u"&Impuls", None))
        self.actionVektorrechnung.setText(QCoreApplication.translate("Physik", u"Vektorrechnung", None))
        self.action.setText(QCoreApplication.translate("Physik", u"Methode der kleinsten Quadrate", None))
        self.actionLineare_Regression.setText(QCoreApplication.translate("Physik", u"Lineare Regression (Aitken)", None))
        self.actionkleinste_Quadrate_Polynom.setText(QCoreApplication.translate("Physik", u"kleinste Quadrate (Polynom)", None))
        self.action_ber.setText(QCoreApplication.translate("Physik", u"\u00dcber", None))
        self.actionTest.setText(QCoreApplication.translate("Physik", u"Test", None))
        self.actionEinfaches_Pendel.setText(QCoreApplication.translate("Physik", u"Einfaches Pendel", None))
        self.actionSchiefer_Wurf.setText(QCoreApplication.translate("Physik", u"Schiefer Wurf", None))
        self.actionLissajous_Figuren.setText(QCoreApplication.translate("Physik", u"Lissajous Figuren", None))
        self.actiongeladenes_Teichen_im_Magnetfeld.setText(QCoreApplication.translate("Physik", u"geladenes Teichen im Magnetfeld", None))
        self.actionMinigolf.setText(QCoreApplication.translate("Physik", u"Minigolf", None))
        self.lbMain.setText("")
        self.menu_Datei.setTitle(QCoreApplication.translate("Physik", u"&Datei", None))
        self.menuMechanik.setTitle(QCoreApplication.translate("Physik", u"Mechanik", None))
        self.menu_ber.setTitle(QCoreApplication.translate("Physik", u"\u00dcber", None))
        self.menuMathematik.setTitle(QCoreApplication.translate("Physik", u"Mathematik", None))
        self.menuInterpolation.setTitle(QCoreApplication.translate("Physik", u"Interpolation", None))
        self.menuElektrodynamik.setTitle(QCoreApplication.translate("Physik", u"Elektrodynamik", None))
        self.menuSimulation.setTitle(QCoreApplication.translate("Physik", u"Simulation", None))
    # retranslateUi

