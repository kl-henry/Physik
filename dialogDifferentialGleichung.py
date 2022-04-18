import numpy as np
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PySide2.QtWidgets import QDialog
from matplotlib import pyplot as plt
from scipy.integrate import odeint

from dialogDifferentialGleichung_ui import Ui_dlgDifferentialGleichung
from utilities.messageBoxes import show_warning


class dlgDifferentialGleichung(QDialog, Ui_dlgDifferentialGleichung):
    def __init__(self):
        # print("dlgDifferentialGleichung Enter")
        super(dlgDifferentialGleichung, self).__init__()
        self.setupUi(self)

        self.dialogHeight = self.frameGeometry().height()
        self.dialogWidth = self.frameGeometry().width()

        self.windowResized = None
        self.x = None
        self.y = None  # array for Euler method
        self.y_mod = None  # array for Modified Euler method
        self.y_rk2 = None  # array for RK2 method
        self.y_rk4 = None  # array for RK4 method
        self.y_odeint = None  # array for odeint method

        self.f = lambda y, x: (y + x) / (y - x)  # Slope function

        self.pbBerechne.clicked.connect(self.berechne)
        self.pbEingabe.clicked.connect(self.datenEingabe)
        self.pbGraphik.clicked.connect(self.show_Graph)

    def model(self, y, x):
        slope = self.f(y, x)  # f(x,y) may be replaced by appropriate value according to the problem
        return slope

    def eulerFunc(self, y, x, h):
        y_new = y + self.model(y, x) * h
        return y_new

    def eulerModFunc(self, y, x, h):
        k1 = self.model(y, x)  # slope at (x, y)
        y_p = y + k1 * h  # predicted 'y' value at 'x+h' based on 'k1'
        k2 = self.model(y_p, x + h)  # slope at (x+h, y+h)
        k_avg = (k1 + k2) / 2  # average of the slopes at 'k1' and 'k2'
        y_c = y + k_avg * h  # corrected 'y' value at 'x+h' based on 'k_avg'
        return y_c

    def rk2Func(self, y, x, h):
        k1 = self.model(y, x)
        k2 = self.model(y + k1 * h / 2, x + h / 2)
        y_new = y + k2 * h
        return y_new

    def rk4Func(self, y, x, h):
        k1 = self.model(y, x)
        k2 = self.model(y + k1 * h / 2, x + h / 2)
        k3 = self.model(y + k2 * h / 2, x + h / 2)
        k4 = self.model(y + k3 * h, x + h)
        k_avg = (k1 + 2 * (k2 + k3) + k4) / 6
        y_new = y + k_avg * h
        return y_new

    def berechne(self):
        # print("dlgDifferentialGleichung: enter berechne")
        if self.leStartwertInput.text() == "":
            show_warning(self=None, title="Warning", text="Daten unvollständig")
        else:
            print(f"dlgDifferentialGleichung: berechne")
            x_init, x_final = 0, 0.6
            step_size = int(self.spSchrittweiteInput.text())/10
            self.leAnzahlSchritte.setText(str(step_size))
            self.x = np.arange(x_init, x_final + step_size, step_size)
            self.y = np.zeros(len(self.x))  # array for Euler method
            self.y_mod = np.zeros(len(self.x))  # array for Modified Euler method
            self.y_rk2 = np.zeros(len(self.x))  # array for RK2 method
            self.y_rk4 = np.zeros(len(self.x))  # array for RK4 method
            self.y_odeint = np.zeros(len(self.x))  # array for odeint method

            # Initialize your variables
            self.y[0] = 1
            self.y_mod[0] = 1
            self.y_rk2[0] = 1
            self.y_rk4[0] = 1
            self.y_odeint[0] = 1

            h = step_size
            for i in range(len(self.x) - 1):
                self.y[i + 1] = self.eulerFunc(self.y[i], self.x[i], h)
                self.y_mod[i + 1] = self.eulerModFunc(self.y_mod[i], self.x[i], h)
                self.y_rk2[i + 1] = self.rk2Func(self.y_rk2[i], self.x[i], h)
                self.y_rk4[i + 1] = self.rk4Func(self.y_rk2[i], self.x[i], h)
            self.y0 = self.y[0]
            sol = odeint(self.model, self.y0, self.x)
            self.y_odeint = sol[:, 0]
            self.leStatus.setText("Fertig")

    def datenEingabe(self):
        # print("dlgDifferentialGleichung: enter datenEingabe")
        self.gbDatenEingabe.setEnabled(True)
        self.leStartwertInput.setEnabled(True)
        self.spSchrittweiteInput.setEnabled(True)

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
        # print("dlgDifferentialGleichung: show_Graph Start")
        if self.windowResized:
            self.resize(self.dialogWidth, self.dialogHeight)
            self.windowResized = False
            self.pbGraphik.setText("Graph >>>")
            self.lyGraph.itemAt(0).widget().deleteLater()
            self.lyGraph.itemAt(1).widget().deleteLater()
        else:
            ax = self._init_graph()

            ax.plot(self.x, self.y, ls=':', marker='^', markersize=10, color='red', label='Euler method')
            ax.plot(self.x, self.y_mod, ls=':', marker='*', markersize=10, color='blue', label='ModifiedEuler method')
            ax.plot(self.x, self.y_rk2, ls=':', marker='o', markersize=10, color='green', label='RK2 method')
            ax.plot(self.x, self.y_rk4, ls=':', marker='<', markersize=10, color='orange', label='RK4 method')
            ax.plot(self.x, self.y_odeint, ls=':', marker='^', markersize=10, color='purple', label='odeint method')
            plt.xlabel('x', fontsize=14)
            plt.ylabel('y(x)', fontsize=14)
            plt.title('Comaparison of Euler, Modified Euler, RK2, RK4 and odeint Method', fontsize=16)
            plt.legend(frameon=False, loc='best')
            self.lyGraph.addWidget(self.toolbar)
            self.lyGraph.addWidget(self.canvas)
