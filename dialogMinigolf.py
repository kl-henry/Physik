import math

from PySide2.QtGui import QDoubleValidator
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

from PySide2.QtWidgets import QDialog
from matplotlib import pyplot as plt

from dialogMinigolf_ui import Ui_dlgMinigolf
from utilities.messageBoxes import show_warning


class dlgMinigolf(QDialog, Ui_dlgMinigolf):
    def __init__(self):
        # print("dlgMinigolf Enter")
        super(dlgMinigolf, self).__init__()
        self.setupUi(self)

        self.dialogHeight = self.frameGeometry().height()
        self.dialogWidth = self.frameGeometry().width()

        self.windowResized = None
        self.yt = None
        self.xt = None
        self.vx = None
        self.vy = None
        self.t = None

        floatValidator = QDoubleValidator(0, 100, 3)
        self.lePotentialWidthInput.setValidator(floatValidator)
        self.lePotentialHeightInpu.setValidator(floatValidator)
        self.leXKreisInput.setValidator(floatValidator)
        self.leYKreisInput.setValidator(floatValidator)
        self.leYRadiusKreisInput.setValidator(floatValidator)
        self.leThetaInput.setValidator(floatValidator)
        self.leV0xInput.setValidator(floatValidator)

        self.pbBerechne.clicked.connect(self.berechne)
        self.pbEingabe.clicked.connect(self.datenEingabe)
        self.pbGraphik.clicked.connect(self.show_Graph)

    def berechne(self):
        # print("dlgMinigolf: enter berechne")
        if self.lePotentialWidthInput.text() == "" or self.leX0xInput.text == "" or self.leX0yInput.text == "" \
                or self.leV0xInput.text == "" or self.leV0yInput.text == "":
            show_warning(self=None, title="Warning", text="Daten unvollständig")
        else:
            laenge = float(self.lePotentialWidthInput.text())
            x0x = float(self.leX0xInput.text())
            x0y = float(self.leX0yInput.text())
            v0x = float(self.leV0xInput.text())
            v0y = float(self.leV0yInput.text())
            self.t = np.linspace(0, int(self.spLaufzeitInput.text()), int(self.spIntervalleInput.text()))

            self.leZeitintervall.setText(str(len(self.t)))

            t0 = 0
            x = x0x
            y = x0y
            vx = v0x
            vy = v0y
            nx = 0
            ny = 0
            self.xt = []
            self.yt = []
            self.vx = []
            self.vy = []
            dt = self.t[1] - self.t[0]
            count = len(self.t)
            for i in range(count):
                x = x + vx * dt
                y = y + vy * dt
                if x < 0.0 or x > laenge:
                    vx = -1 * vx
                    nx = nx + 1
                if y < 0.0 or y > laenge:
                    vy = -1 * vy
                    ny = ny + 1
                self.xt.append(x)
                self.yt.append(y)
                self.vx.append(vx)
                self.vy.append(vy)
            self.xt = np.array(self.xt)
            self.yt = np.array(self.yt)
            self.vy = np.array(self.vx)
            self.vy = np.array(self.vy)

            self.leStatus.setText(f"Fertig! {dt:2.4f}")
            # print(f"dlgMinigolf: berechne xt, theta: ", self.xt, theta)
            # print(f"dlgMinigolf: berechne xt, yt, vy: ", self.xt, self.yt, self.vy)

    def datenEingabe(self):
        # print("dlgMinigolf: enter datenEingabe")
        self.gbDatenEingabe.setEnabled(True)
        self.spIntervalleInput.setEnabled(True)
        self.spLaufzeitInput.setEnabled(True)
        self.lbPotentialWidth.setEnabled(True)
        self.lbPotentialHeight.setEnabled(True)
        self.lePotentialWidthInput.setEnabled(True)
        self.lePotentialHeightInpu.setEnabled(True)
        self.leXKreisInput.setEnabled(True)
        self.leYKreisInput.setEnabled(True)
        self.leV0xInput.setEnabled(True)
        self.leYRadiusKreisInput.setEnabled(True)
        self.leThetaInput.setEnabled(True)


    def _init_graph(self):
        self.resize(self.dialogWidth + 480, self.dialogHeight)
        self.windowResized = True
        self.pbGraphik.setText("Graph <<<")
        # print("show_Graph: type(a), type(i), type(f):", type(a), type(i), type(f))
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.figure.clear()
        ax111 = plt.subplot(211)
        ax211 = plt.subplot(212)
        self.figure.tight_layout(h_pad=3)
        return ax111, ax211

    def show_Graph(self):
        # print("dlgMinigolf: show_Graph Start")
        if self.windowResized:
            self.resize(self.dialogWidth, self.dialogHeight)
            self.windowResized = False
            self.pbGraphik.setText("Graph >>>")
            self.lyGraph.itemAt(0).widget().deleteLater()
            self.lyGraph.itemAt(1).widget().deleteLater()
        else:
            ax1, ax2 = self._init_graph()

            ax1.plot(self.t, self.xt, '-r', linewidth=2, label='x')
            ax1.plot(self.t, self.yt, dashes=[30, 5, 10, 5], label='y')
            ax2.plot(self.t, self.vx, '-r', linewidth=2, label='vx')
            ax2.plot(self.t, self.vy, dashes=[30, 5, 10, 5], label='vy')

            plt.grid(True)
            ax1.legend(loc='lower right')
            ax2.legend(loc='lower right')
            self.lyGraph.addWidget(self.toolbar)
            self.lyGraph.addWidget(self.canvas)

            # self.canvas.draw()
