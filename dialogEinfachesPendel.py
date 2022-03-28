import math

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import scipy.constants
from PySide2.QtWidgets import QDialog
from matplotlib import pyplot as plt

from dialogEinfachesPendel_ui import Ui_dlgEinfachesPendel
from utilities.messageBoxes import show_warning


class dlgEinfachesPendel(QDialog, Ui_dlgEinfachesPendel):
    def __init__(self):
        # print("dlgEinfachesPendel Enter")
        super(dlgEinfachesPendel, self).__init__()
        self.setupUi(self)

        self.dialogHeight = self.frameGeometry().height()
        self.dialogWidth = self.frameGeometry().width()

        self.windowResized = None
        self.yt = None
        self.xt = None
        self.vy = None

        self.pbBerechne.clicked.connect(self.berechne)
        self.pbEingabe.clicked.connect(self.datenEingabe)
        self.pbGraphik.clicked.connect(self.show_Graph)

    def berechne(self):
        # print("dlgEinfachesPendel: enter berechne")
        if self.lePendLengthInput.text() == "" or self.leAuslenkungInput.text == "" :
            show_warning(self=None, title="Warning", text="Daten unvollständig")
        else:
            laenge = float(self.lePendLengthInput.text())
            omega = math.sqrt(scipy.constants.g / laenge)
            period = (math.pi * 2.0) / omega

            # print(f"dlgEinfachesPendel: berechne Frequenz, Periode {omega:.5f} {period:.5f} "
            #       f"(g: {scipy.constants.g:.5f})")

            self.leFrequenz.setText(f"{omega:.5f}" + " [Hz]")
            self.leSchwingungsDauer.setText(f"{period:.5f}" + " [s]")

            theta0 = float(self.leAuslenkungInput.text())
            self.xt = np.linspace(0, int(self.spLaufzeitInput.text()), int(self.spIntervalleInput.text()))
            theta = theta0 * np.cos(self.xt)
            theta_dt = -1 * omega * theta0 * np.sin(self.xt)

            self.yt = -1 * laenge * np.cos(theta)
            # vx = laenge * theta_dt * np.cos(theta)
            self.vy = laenge * theta_dt * np.sin(theta)

            # print(f"dlgEinfachesPendel: berechne xt, theta: ", self.xt, theta)
            # print(f"dlgEinfachesPendel: berechne xt, yt, vy: ", self.xt, self.yt, self.vy)

    def datenEingabe(self):
        # print("dlgEinfachesPendel: enter datenEingabe")
        self.gbDatenEingabe.setEnabled(True)
        self.spIntervalleInput.setEnabled(True)
        self.spLaufzeitInput.setEnabled(True)
        self.lePendLengthInput.setEnabled(True)
        self.leAuslenkungInput.setEnabled(True)

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
