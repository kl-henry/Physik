import math

from PySide2.QtGui import QDoubleValidator
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import scipy.constants
from PySide2.QtWidgets import QDialog
from matplotlib import pyplot as plt

from dialog1_dim_Box_ui import Ui_dlg_Win_1_dim_box
from utilities.messageBoxes import show_warning


class dlg1_dim_Box(QDialog, Ui_dlg_Win_1_dim_box):
    def __init__(self):
        # print("dlg1_dim_Box Enter")
        super(dlg1_dim_Box, self).__init__()
        self.setupUi(self)

        self.dialogHeight = self.frameGeometry().height()
        self.dialogWidth = self.frameGeometry().width()

        self.windowResized = None
        self.yt = None
        self.xt = None
        self.vy = None

        floatValidator = QDoubleValidator(0, 100, 3)
        self.lePotentialWidthInput.setValidator(floatValidator)
        self.leX0Input.setValidator(floatValidator)
        self.leY0Input.setValidator(floatValidator)
        self.leV0xInput.setValidator(floatValidator)
        self.leV0yInput.setValidator(floatValidator)

        self.pbBerechne.clicked.connect(self.berechne)
        self.pbEingabe.clicked.connect(self.datenEingabe)
        self.pbGraphik.clicked.connect(self.show_Graph)

    def berechne(self):
        # print("dlg1_dim_Box: enter berechne")
        if self.lePotentialWidthInput.text() == "" or self.leX0Input.text == "" or self.leY0Input.text == "" \
                or self.leV0xInput.text == "" or self.leV0yInput.text == "":
            show_warning(self=None, title="Warning", text="Daten unvollständig")
        else:
            laenge = float(self.lePotentialWidthInput.text())

            # print(f"dlg1_dim_Box: berechne xt, theta: ", self.xt, theta)
            # print(f"dlg1_dim_Box: berechne xt, yt, vy: ", self.xt, self.yt, self.vy)

    def datenEingabe(self):
        # print("dlg1_dim_Box: enter datenEingabe")
        self.gbDatenEingabe.setEnabled(True)
        self.spIntervalleInput.setEnabled(True)
        self.spLaufzeitInput.setEnabled(True)
        self.lePotentialWidthInput.setEnabled(True)
        self.leX0Input.setEnabled(True)
        self.leY0Input.setEnabled(True)
        self.leV0xInput.setEnabled(True)
        self.leV0yInput.setEnabled(True)

    def _init_graph(self):
        self.resize(self.dialogWidth + 480, self.dialogHeight)
        self.windowResized = True
        self.pbGraphik.setText("Graph <<<")
        # print("show_Graph: type(a), type(i), type(f):", type(a), type(i), type(f))
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        return ax

    def show_Graph(self):
        # print("dlgWinLineareRegression: show_Graph Start")
        if self.windowResized:
            self.resize(self.dialogWidth, self.dialogHeight)
            self.windowResized = False
            self.pbGraphik.setText("Graph >>>")
            self.lyGraph.itemAt(0).widget().deleteLater()
            self.lyGraph.itemAt(1).widget().deleteLater()
        else:
            ax = self._init_graph()

            ax.plot(self.xt, self.yt, '-r', linewidth=2, label='Ausl.')

            ax.plot(self.xt, self.vy, dashes=[30, 5, 10, 5], label='Geschw.')
            plt.grid(True)
            ax.legend(loc='lower right')
            self.lyGraph.addWidget(self.toolbar)
            self.lyGraph.addWidget(self.canvas)


            # self.canvas.draw()
