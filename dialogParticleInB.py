import math

from PySide2.QtGui import QDoubleValidator
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

from PySide2.QtWidgets import QDialog
from matplotlib import pyplot as plt

from dialogParticleInB_ui import Ui_dlgParticleInB
from utilities.messageBoxes import show_warning


class dlgParticleInB(QDialog, Ui_dlgParticleInB):
    def __init__(self):
        # print("dlgLissajous Enter")
        super(dlgParticleInB, self).__init__()


        self.setupUi(self)

        self.dialogHeight = self.frameGeometry().height()
        self.dialogWidth = self.frameGeometry().width()

        floatValidator = QDoubleValidator(0.0, 90.0, 2)

        self.windowResized = None
        self.Winkel = None
        self.V0Input = None
        self.LarmorFrequenz = None
        self.t = None
        self.yt = None
        self.xt = None
        self.zt = None

        self.leLarmorFrequenzInput.setValidator(floatValidator)
        self.leV0Input.setValidator(floatValidator)

        self.pbEingabe.clicked.connect(self.datenEingabe)
        self.pbBerechne.clicked.connect(self.berechne)
        self.pbGraphik.clicked.connect(self.show_Graph)

    def berechne(self):
        # print("dlgParticleInB: enter berechne")
        if self.leLarmorFrequenzInput.text() == "" or self.leV0Input.text() == "":
            show_warning(self=None, title="Warning", text="Daten unvollständig")
        else:
            self.LarmorFrequenz = float(self.leLarmorFrequenzInput.text())
            self.V0Input = float(self.leV0Input.text())
            self.Winkel = int(self.spWinkelInput.text())

            theta = (math.pi / 180.0) * self.Winkel
            v0y = self.V0Input * math.cos(theta)
            v0z = self.V0Input * math.sin(theta)
            x0 = -1 * v0y / self.LarmorFrequenz
            stepOfHelix = v0z * 2.0 * math.pi / self.LarmorFrequenz

            self.t = np.linspace(0, int(self.spLaufzeitInput.text()), int(self.spIntervalleInput.text()))
            # print("dlgParticleInB: berechne len(t) = ", len(self.t), -1 * int(self.spLaufzeitInput.text()))

            self.leStartRichtung.setText(f"{x0:.5f}")
            self.leStepOfHelix.setText(f"{stepOfHelix:.5f}" + " [m*s]")
            self.leKreisRadius.setText(f"{abs(x0):.5f}" + " [m]")

            self.xt = x0 * np.cos(self.LarmorFrequenz * self.t)
            self.yt = -1 * x0 * np.sin(self.LarmorFrequenz * self.t)
            self.zt = v0z * self.t

            # print(f"dlgParticleInB: berechne xt, yt ", self.xt, self.yt)

    def datenEingabe(self):
        print("dlgParticleInB: enter datenEingabe")
        # utilities.app_utilities.datenEingabe(self, self.gbDatenEingabe.objectName())
        self.gbDatenEingabe.setEnabled(True)
        self.lbLarmorFrequenz.setEnabled(True)
        self.spIntervalleInput.setEnabled(True)
        self.spLaufzeitInput.setEnabled(True)
        self.leLarmorFrequenzInput.setEnabled(True)
        self.leV0Input.setEnabled(True)
        self.spWinkelInput.setEnabled(True)

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
        # print("dlgParticleInB: show_Graph Start")
        if self.windowResized:
            self.resize(self.dialogWidth, self.dialogHeight)
            self.windowResized = False
            self.pbGraphik.setText("Graph >>>")
            # print("dlgLissajous: show_Graph Frame Widget Count: ", self.lyGraph.count())
            for i in reversed(range(self.lyGraph.count())):
                self.lyGraph.itemAt(i).widget().deleteLater()
        else:
            ax = self._init_graph()

            ax.plot(self.t, self.xt, '-r', linewidth=2, label='vx')
            ax.plot(self.t, self.yt, '-b', label='vy')
            ax.plot(self.t, self.zt, '-g', label='vz')

            plt.grid(True)
            ax.legend(loc='lower right')
            self.lyGraph.addWidget(self.toolbar)
            self.lyGraph.addWidget(self.canvas)

            self.lbGraphExtensionTitel.setText(f"Particle im Magnetfeld: LarmorFrequenz={self.LarmorFrequenz:.2f}")
            # self.canvas.draw()
