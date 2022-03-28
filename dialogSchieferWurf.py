import math

from PySide2.QtCore import QCoreApplication
from PySide2.QtGui import QDoubleValidator
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import scipy.constants
from PySide2.QtWidgets import QDialog, QPushButton
from matplotlib import pyplot as plt

from dialogSchieferWurf_ui import Ui_dlgSchieferWurf
from utilities.messageBoxes import show_warning


class dlgSchieferWurf(QDialog, Ui_dlgSchieferWurf):
    def __init__(self):
        # print("dlgEinfachesPendel Enter")
        super(dlgSchieferWurf, self).__init__()

        self.ax = None
        self.setupUi(self)

        self.dialogHeight = self.frameGeometry().height()
        self.dialogWidth = self.frameGeometry().width()

        floatValidator = QDoubleValidator(0.0, 90.0, 2)

        self.windowResized = None
        self.xt = None
        self.yt = None
        self.vx = None
        self.vy = None
        self.label_1 = None
        self.label_2 = None
        self.vy_ohne = None
        self.vx_ohne = None
        self.yt_ohne = None
        self.xt_ohne = None
        self.vy_mit = None
        self.vx_mit = None
        self.yt_mit = None
        self.xt_mit = None

        self.leV0Input.setValidator(floatValidator)
        self.leWinkelInput.setValidator(floatValidator)
        self.leLuftwiderstandInput.setValidator(floatValidator)
        self.pbBerechne.clicked.connect(self.berechne)
        self.pbEingabe.clicked.connect(self.datenEingabe)
        self.pbGraphik.clicked.connect(self.show_Graph)

    def berechne(self):
        # print("dlgEinfachesPendel: enter berechne")
        if self.leV0Input.text() == "" or self.leWinkelInput.text() == "":
            show_warning(self=None, title="Warning", text="Daten unvollständig")
        else:
            if self.leLuftwiderstandInput.text() == "":
                k_air = 0.0
                air_resistance = False
            else:
                k_air = float(self.leLuftwiderstandInput.text())
                air_resistance = True
            theta = float(self.leWinkelInput.text())
            theta = (math.pi / 180.0) * theta
            v0 = float(self.leV0Input.text())
            v0x = v0 * math.cos(theta)
            v0y = v0 * math.sin(theta)
            intervalle = int(self.spIntervalleInput.text())
            # print(f"dlgSchieferWurf: berechne {intervalle:d}")
            t = np.linspace(0, int(self.spLaufzeitInput.text()), int(self.spIntervalleInput.text()))

            # print(f"dlgSchieferWurf: berechne {theta:.5f} (rad) {v0:.5f} "
            #       f"{v0x:.5f}, {v0y:.5f}")

            self.leV0x.setText(f"{v0x:.5f}")
            self.leV0y.setText(f"{v0y:.5f}")

            # Rechnung mit Luftwiderstand k_air
            self.xt_mit = (v0x / k_air) * (1.0 - np.exp((-1 * k_air * t)))
            self.yt_mit = (1.0 / k_air) * (v0y + (scipy.constants.g / k_air)) * (1.0 - np.exp((-1 * k_air * t))) \
                          - (scipy.constants.g / k_air) * t
            self.vx_mit = v0x * np.exp(-1.0 * k_air * t)
            self.vy_mit = (v0y + (scipy.constants.g / k_air)) * np.exp(-1.0 * k_air * t) - (
                    scipy.constants.g / k_air)
            # Rechnung ohne Luftwiderstand
            self.xt_ohne = v0x * t
            self.yt_ohne = v0y * t - 0.5 * scipy.constants.g * t * t
            self.vx_ohne = v0x
            self.vy_ohne = v0y - scipy.constants.g * t
            if air_resistance:
                print(f"dlgSchieferWurf: berechne air_resistance = True")
                self.xt = self.xt_mit
                self.yt = self.yt_mit
                self.vx = self.vx_mit
                self.vy = self.vy_mit
                self.lbGraphExtensionTitel.setText("Schiefer Wurf mit Luftwiderstand")
            else:
                print(f"dlgSchieferWurf: berechne air_resistance = False")
                self.xt = self.xt_ohne
                self.yt = self.yt_ohne
                self.vx = self.vx_ohne
                self.vy = self.vy_ohne
                self.lbGraphExtensionTitel.setText("Schiefer Wurf ohne Luftwiderstand")

            self.label_1 = "Pos."
            self.label_2 = "Geschw."

            # print(f"dlgSchieferWurf: berechne x = ", self.xt)
            # print(f"dlgSchieferWurf: berechne y = ", self.yt)

    def datenEingabe(self):
        # print("dlgEinfachesPendel: enter datenEingabe")
        self.gbDatenEingabe.setEnabled(True)
        self.spIntervalleInput.setEnabled(True)
        self.spLaufzeitInput.setEnabled(True)
        self.leWinkelInput.setEnabled(True)
        self.leV0Input.setEnabled(True)
        self.leLuftwiderstandInput.setEnabled(True)

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
        self.pbVergleich = QPushButton(self.verticalLayoutWidget)
        self.pbVergleich.setObjectName(u"pbVergleich")
        self.pbVergleich.setText(
            QCoreApplication.translate("dlgSchieferWurf", u"Vergleich mit/ohne Luftwiderstand", None))
        self.pbVergleich.clicked.connect(self.vergleich)
        return ax

    def show_Graph(self):
        # print("dlgWinLineareRegression: show_Graph Start")
        if self.windowResized:
            self.resize(self.dialogWidth, self.dialogHeight)
            self.windowResized = False
            self.pbGraphik.setText("Graph >>>")
            for i in reversed(range(self.lyGraph.count())):
                self.lyGraph.itemAt(i).widget().deleteLater()
        else:
            self.ax = self._init_graph()

            self.ax.plot(self.xt, self.yt, '-r', linewidth=2, label=self.label_1)

            self.ax.plot(self.xt, self.vy, dashes=[30, 5, 10, 5], label=self.label_2)
            plt.grid(True)
            self.ax.legend(loc='lower right')
            self.lyGraph.addWidget(self.toolbar)
            self.lyGraph.addWidget(self.canvas)
            self.lyGraph.addWidget(self.pbVergleich)
            self.pbVergleich.setEnabled(True)
            # print("show_Graph: list children: ", self.lyGraph.findChildren(QWidget))
            # self.canvas.draw()

    def vergleich(self):
        print("dlgWinLineareRegression: vergleich Start")
        self.ax.plot(self.xt_ohne, self.yt_ohne, '-g', linewidth=2, label=self.label_1)
        self.canvas.draw()
