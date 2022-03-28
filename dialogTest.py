from PySide2.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide2.QtWidgets import QDialog, QPushButton, QVBoxLayout, QWidget, QDialogButtonBox, QFrame, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random

import utilities.app_utilities
from dialogTest_ui import Ui_dlgTest


class dlgWinTest(QDialog, Ui_dlgTest):
    def __init__(self, parent=None):
        super(dlgWinTest, self).__init__(parent)
        self.setupUi(self)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        self.lbTest = QLabel('Test')

        self.lyGraph.addWidget(self.toolbar)
        self.lyGraph.addWidget(self.canvas)
        self.lyGraph.addWidget(self.button)
        self.lyGraph.addWidget(self.lbTest)

        self.pbBerechne.clicked.connect(self.berechne)
        self.pushButton.clicked.connect(self.button_1)
        self.pushButton_6.clicked.connect(self.button_6)

    def plot(self):
        print("Test: plot Enter")
        data = [random.random() for i in range(10)]
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(data, '*-')
        self.canvas.draw()

    def berechne(self):
        print("dlgWinTest: berechne Enter")
        if self.verticalWidget_3.isVisible():
            self.verticalWidget_3.hide()
        else:
            self.verticalWidget_3.show()

    def button_1(self):
        print("dlgWinTest: button_1 Enter")
        utilities.app_utilities.datenEingabe(self)

    def button_6(self):
        print("dlgWinTest: button_6 Enter")
