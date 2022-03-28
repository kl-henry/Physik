import math

from PySide2.QtGui import QDoubleValidator
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import scipy.constants
from PySide2.QtWidgets import QDialog
from matplotlib import pyplot as plt

from dialogLissajous_ui import Ui_dlgLissajous
from utilities.messageBoxes import show_warning


class dlgLissajous(QDialog, Ui_dlgLissajous):
    def __init__(self):
        # print("dlgLissajous Enter")
        super(dlgLissajous, self).__init__()


        self.setupUi(self)

        self.dialogHeight = self.frameGeometry().height()
        self.dialogWidth = self.frameGeometry().width()

        floatValidator = QDoubleValidator(0.0, 90.0, 2)

        self.windowResized = None
        self.t = None
        self.yt = None
        self.xt = None
        self.omega2 = None
        self.omega1 = None

        self.leOmega1Input.setValidator(floatValidator)
        self.leOmega2Input.setValidator(floatValidator)
        self.lePhase1Input.setValidator(floatValidator)
        self.lePhase2Input.setValidator(floatValidator)
        self.leAmplitude1Input.setValidator(floatValidator)
        self.leAmplitude2Input.setValidator(floatValidator)

        self.pbBerechne.clicked.connect(self.berechne)
        self.pbEingabe.clicked.connect(self.datenEingabe)
        self.pbGraphik.clicked.connect(self.show_Graph)

    def berechne(self):
        # print("dlgLissajous: enter berechne")
        if self.leOmega1Input.text() == "" or self.leOmega2Input.text == "":
            show_warning(self=None, title="Warning", text="Daten unvollständig")
        else:
            self.omega1 = float(self.leOmega1Input.text())
            self.omega2 = float(self.leOmega2Input.text())
            phase1 = float(self.lePhase1Input.text())
            phase2 = float(self.lePhase2Input.text())
            amplitude1 = float(self.leAmplitude1Input.text())
            amplitude2 = float(self.leAmplitude2Input.text())

            period1 = (math.pi * 2.0) / self.omega1
            period2 = (math.pi * 2.0) / self.omega2

            self.t = np.linspace(-1 * int(self.spLaufzeitInput.text()),
                                 int(self.spLaufzeitInput.text()), int(self.spIntervalleInput.text()))
            # print("dlgLissajous:  berechne len(t) = ", len(self.t), -1 * int(self.spLaufzeitInput.text()))
            self.leT1Input.setText(f"{period1:.5f}" + " [s]")
            self.leT2Input.setText(f"{period2:.5f}" + " [s]")

            self.xt = amplitude1 * np.cos(self.omega1 * self.t + phase1)
            self.yt = amplitude2 * np.sin(self.omega2 * self.t + phase2)

            # print(f"dlgLissajous: berechne xt, yt ", self.xt, self.yt)

    def datenEingabe(self):
        # print("dlgLissajous: enter datenEingabe")
        self.gbDatenEingabe.setEnabled(True)
        self.spIntervalleInput.setEnabled(True)
        self.spLaufzeitInput.setEnabled(True)
        self.leOmega1Input.setEnabled(True)
        self.leOmega2Input.setEnabled(True)
        self.lePhase1Input.setEnabled(True)
        self.lePhase2Input.setEnabled(True)
        self.leAmplitude1Input.setEnabled(True)
        self.leAmplitude2Input.setEnabled(True)

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
        # print("dlgLissajous: show_Graph Start")
        if self.windowResized:
            self.resize(self.dialogWidth, self.dialogHeight)
            self.windowResized = False
            self.pbGraphik.setText("Graph >>>")
            # print("dlgLissajous: show_Graph Frame Widget Count: ", self.lyGraph.count())
            for i in reversed(range(self.lyGraph.count())):
                self.lyGraph.itemAt(i).widget().deleteLater()
        else:
            ax = self._init_graph()

            ax.plot(self.xt, self.yt, '-r', linewidth=2, label='O1')

            # ax.plot(self.t, self.yt, dashes=[30, 5, 10, 5], label='O2')
            plt.grid(True)
            # ax.legend(loc='lower right')
            self.lyGraph.addWidget(self.toolbar)
            self.lyGraph.addWidget(self.canvas)

            self.lbGraphExtensionTitel.setText(f"Lissajous mit {self.omega1:.2f} und {self.omega2:.2f}")
            # self.canvas.draw()
