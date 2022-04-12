import math

from PySide2.QtGui import QDoubleValidator
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import scipy.constants
from PySide2.QtWidgets import QDialog
from matplotlib import pyplot as plt

from dialogSchieferWurf_ui import Ui_dlgSchieferWurf
from utilities.messageBoxes import show_warning
from vector_rechnung.angle_Vectors import angleBetween
from vector_rechnung.mag_vector import magVectors


class dlgSchieferWurf(QDialog, Ui_dlgSchieferWurf):
    def __init__(self):
        # print("dlgSchieferWurf Enter")
        super(dlgSchieferWurf, self).__init__()


        self.setupUi(self)

        self.dialogHeight = self.frameGeometry().height()
        self.dialogWidth = self.frameGeometry().width()

        floatValidator = QDoubleValidator(0.0, 90.0, 2)

        self.windowResized = None
        self.xt = None
        self.yt = None
        self.v0y = None
        self.v0x = None
        self.yt_plus = None
        self.xt_plus = None
        self.yt_minus = None
        self.xt_minus = None
        self.ax = None
        self.t = None
        self.k_air = None

        self.leV0xInput.setValidator(floatValidator)
        self.leV0yInput.setValidator(floatValidator)
        self.leLuftwiderstandInput.setValidator(floatValidator)

        self.pbBerechne.clicked.connect(self.berechne)
        self.pbEingabe.clicked.connect(self.datenEingabe)
        self.pbGraphik.clicked.connect(self.show_Graph)

    def berechne(self):
        # print("dlgSchieferWurf: enter berechne")
        if self.leV0xInput.text() == "" or self.leV0yInput.text() == "":
            show_warning(self=None, title="Warning", text="Daten unvollständig")
        else:
            self.k_air = 0.0  # float(self.leLuftwiderstandInput.text())
            self.v0x = float(self.leV0xInput.text())
            self.v0y = float(self.leV0yInput.text())
            theta = angleBetween((1, 0), (self.v0x, self.v0y))
            self.leWinkel.setText(f"theta= {theta:.3f}")
            # self.t = np.linspace(0, int(self.spLaufzeitInput.text()), int(self.spIntervalleInput.text()))
            v0 = magVectors((self.v0x, self.v0y))

            theta = np.radians(theta)
            coeff1 = -0.5 * scipy.constants.g
            coeff2 = v0 * math.sin(theta)
            roots = np.roots([coeff1, coeff2])
            self.t = np.linspace(0, int(roots[0]+1), int(self.spIntervalleInput.text()))

            # print(f"dlgSchieferWurf:berechne coeff1: {coeff1:.3f}")
            # print(f"dlgSchieferWurf:berechne coeff2: {coeff2:.3f}")
            # print(f"dlgSchieferWurf:berechne roots: ", roots)
            self.xt = v0 * math.cos(theta) * self.t
            self.yt = -0.5 * scipy.constants.g * self.t * self.t + v0 * math.sin(theta) * self.t
            self.xt_minus = v0 * math.cos(theta-0.10) * self.t
            self.yt_minus = -0.5 * scipy.constants.g * self.t * self.t + v0 * math.sin(theta-0.10) * self.t
            self.xt_plus = v0 * math.cos(theta+0.20) * self.t
            self.yt_plus = -0.5 * scipy.constants.g * self.t * self.t + v0 * math.sin(theta+0.20) * self.t

            self.lbGraphExtensionTitel.setText(f"rot: {np.degrees(theta):.3f}, "
                                               f"blau: {np.degrees(theta+0.2):.3f}, "
                                               f"grün : {np.degrees(theta-0.1):.3f}")
            # print("dlgSchieferWurf:berechne v0: ", v0)
            # print("dlgSchieferWurf:berechne g: ", scipy.constants.g)
            # print("dlgSchieferWurf:berechne xt: ", self.xt)
            # print("dlgSchieferWurf:berechne yt: ", self.yt)

    def datenEingabe(self):
        # print("dlgSchieferWurf: enter datenEingabe")
        self.gbDatenEingabe.setEnabled(True)
        self.spIntervalleInput.setEnabled(True)
        self.spLaufzeitInput.setEnabled(True)
        self.lbLuftwiderstand.setEnabled(True)
        self.leV0xInput.setEnabled(True)
        self.leV0yInput.setEnabled(True)
        self.leLuftwiderstandInput.setEnabled(True)

        self.leV0xInput.setText("10")
        self.leV0yInput.setText("20")
        self.spLaufzeitInput.setValue(2)
        self.spIntervalleInput.setValue(20)

    def _init_graph(self):
        # print("dlgSchieferWurf _init_graph enter")
        self.resize(self.dialogWidth + 480, self.dialogHeight)
        self.windowResized = True
        self.pbGraphik.setText("Graph <<<")

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.figure.clear()
        # ---------------------------------------
        # fig, ax = plt.subplots(figsize=(8, 5))
        # set the x-spine
        ax = self.figure.add_subplot(111)
        ax.spines['left'].set_position('zero')

        # turn off the right spine/ticks
        ax.spines['right'].set_color('none')
        ax.yaxis.tick_left()

        # set the y-spine
        ax.spines['bottom'].set_position('zero')

        # turn off the top spine/ticks
        ax.spines['top'].set_color('none')
        ax.xaxis.tick_bottom()
        # ---------------------------------------
        # ax = self.figure.add_subplot(111)
        # print("_init_graph ax: ", ax)
        return ax

    def show_Graph(self):
        print("dlgSchieferWurf: show_Graph Start")
        if self.windowResized:
            self.resize(self.dialogWidth, self.dialogHeight)
            self.windowResized = False
            self.pbGraphik.setText("Graph >>>")
            for i in reversed(range(self.lyGraph.count())):
                self.lyGraph.itemAt(i).widget().deleteLater()
        else:
            self.ax = self._init_graph()

            self.ax.set_ylabel('$y(t)$', fontsize=14)
            self.ax.set_xlabel('$t$', fontsize=14)
            # self.ax.set_xlim(0, 90)

            self.ax.plot(self.t, self.yt, '-r', linewidth=2)
            self.ax.plot(self.t, self.yt_minus, '.g', linewidth=2)
            self.ax.plot(self.t, self.yt_plus, '.b', linewidth=2)

            # self.ax.plot(self.xt, self.vy, dashes=[30, 5, 10, 5], label=self.label_2)
            plt.grid(True)
            # self.ax.legend(loc='lower right')
            self.lyGraph.addWidget(self.toolbar)
            self.lyGraph.addWidget(self.canvas)
            # print("dlgSchieferWurf show_Graph: list children: ", self.lyGraph.findChildren(QWidget))
            # self.canvas.draw()
