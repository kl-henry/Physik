import math

from PySide2.QtGui import QDoubleValidator
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

from PySide2.QtWidgets import QDialog
from matplotlib import pyplot as plt

import utilities.messageBoxes
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
        self.lePotentialHeightInput.setValidator(floatValidator)
        self.leXKreisInput.setValidator(floatValidator)
        self.leYKreisInput.setValidator(floatValidator)
        self.leRadiusKreisInput.setValidator(floatValidator)
        self.leThetaInput.setValidator(floatValidator)
        self.leV0Input.setValidator(floatValidator)

        self.pbBerechne.clicked.connect(self.berechne)
        self.pbEingabe.clicked.connect(self.datenEingabe)
        self.pbGraphik.clicked.connect(self.show_Graph)

    def berechne(self):
        # print("dlgMinigolf: enter berechne")
        if self.lePotentialWidthInput.text() == "" or self.lePotentialHeightInput.text() == "" or \
                self.leXKreisInput.text == "" or self.leYKreisInput.text == "" \
                or self.leV0Input.text == "" or self.leThetaInput.text == "":
            show_warning(self=None, title="Warning", text="Daten unvollständig")
        else:
            laengePotential = float(self.lePotentialWidthInput.text())
            hoehePotential = float(self.lePotentialHeightInput.text())
            v0 = float(self.leV0Input.text())
            xKreis = float(self.leXKreisInput.text())
            yKreis = float(self.leYKreisInput.text())
            rKreis = float(self.leRadiusKreisInput.text())
            theta = float(self.leThetaInput.text())

            x0x = 0
            x0y = hoehePotential / 2
            self.t = np.linspace(0, int(self.spLaufzeitInput.text()), int(self.spIntervalleInput.text()))
            self.leZeitintervall.setText(str(len(self.t)))

            x = x0x
            y = x0y
            theta = math.radians(theta)
            v0x = v0 * math.cos(theta)
            v0y = v0 * math.sin(theta)
            vx = v0x
            vy = v0y
            r2 = rKreis * rKreis
            nx = 0
            ny = 0
            text = ""
            self.xt = []
            self.yt = []
            self.vx = []
            self.vy = []
            dt = self.t[1] - self.t[0]
            count = len(self.t)
            for i in range(count):
                x = x + vx * dt
                y = y + vy * dt
                if x > laengePotential:
                    vx = -1 * vx
                    nx = nx + 1
                if y < 0.0 or y > hoehePotential:
                    vy = -1 * vy
                    ny = ny + 1
                print(f"dlgMinigolf: berechne x: {x:2.4f}, y {y:2.4f}")
                if x < 0.0:
                    text = "Kein Treffer"
                    print(text)
                    break
                if (x - xKreis) * (x - xKreis) + (y - yKreis) * (y - yKreis) <= r2:
                    text = "Treffer"
                    print(text)
                    break
                self.xt.append(x)
                self.yt.append(y)
                self.vx.append(vx)
                self.vy.append(vy)
                print(f"dlgMinigolf: berechne x: {len(self.xt):d}, y {len(self.yt):d}")
            self.xt = np.array(self.xt)
            self.yt = np.array(self.yt)
            self.vy = np.array(self.vx)
            self.vy = np.array(self.vy)

            self.leStatus.setText(f"Fertig! {dt:2.4f}")
            self.lbGraphExtensionTitel.setText(text)
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
        self.lePotentialHeightInput.setEnabled(True)
        self.leXKreisInput.setEnabled(True)
        self.leYKreisInput.setEnabled(True)
        self.leV0Input.setEnabled(True)
        self.leRadiusKreisInput.setEnabled(True)
        self.leThetaInput.setEnabled(True)

        self.lePotentialWidthInput.setText("10")
        self.lePotentialHeightInput.setText("5")
        self.leXKreisInput.setText("8")
        self.leYKreisInput.setText("2.5")
        self.leV0Input.setText("3")
        self.leRadiusKreisInput.setText("1")
        self.leThetaInput.setText("45")

    def _init_graph(self):
        self.resize(self.dialogWidth + 480, self.dialogHeight)
        self.windowResized = True
        self.pbGraphik.setText("Graph <<<")
        # print("show_Graph: type(a), type(i), type(f):", type(a), type(i), type(f))
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.figure.clear()
        ax111 = plt.subplot()
        self.figure.tight_layout(h_pad=3)
        return ax111

    def show_Graph(self):
        # print("dlgMinigolf: show_Graph Start")
        if self.windowResized:
            self.resize(self.dialogWidth, self.dialogHeight)
            self.windowResized = False
            self.pbGraphik.setText("Graph >>>")
            self.lyGraph.itemAt(0).widget().deleteLater()
            self.lyGraph.itemAt(1).widget().deleteLater()
        else:
            ax1 = self._init_graph()

            ax1.plot(self.t, self.xt, '-r', linewidth=2, label='x')
            # ax1.plot(self.t, self.yt, dashes=[30, 5, 10, 5], label='y')

            plt.grid(True)
            ax1.legend(loc='lower right')

            self.lyGraph.addWidget(self.toolbar)
            self.lyGraph.addWidget(self.canvas)

            # self.canvas.draw()
