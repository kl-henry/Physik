import sqlite3

from PySide2.QtGui import QDoubleValidator, QIntValidator
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

from PySide2.QtWidgets import QDialog
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp

from dialogRadioactiveDecay_ui import Ui_dlgRadioactiveDecay
from utilities.messageBoxes import show_warning


class dlgRadioactiveDecay(QDialog, Ui_dlgRadioactiveDecay):
    def __init__(self):
        # print("dlgRadioactiveDecay Enter")
        super(dlgRadioactiveDecay, self).__init__()

        self.setupUi(self)

        self.Anfangsmenge = None
        self.Halbwertszeit = None
        self.Element = None
        self.inverseHalftime = None
        self.t = None
        self.ax = None
        self.rows = None

        self.dialogHeight = self.frameGeometry().height()
        self.dialogWidth = self.frameGeometry().width()

        floatValidator = QDoubleValidator(0.0, 90.0, 2)
        self.leHalbwertszeitInput.setValidator(floatValidator)

        intValidator = QIntValidator()
        self.leHalbwertszeitInput.setValidator(intValidator)

        self.windowResized = None

        conn = sqlite3.connect('/home/hhill/PycharmProjects/Physik/RadioactiveDecay.db')
        c = conn.cursor()

        c.execute('''SELECT * FROM elements;''')
        self.rows = c.fetchall()
        for row in self.rows:
            # print(row)
            cbText = f"{row[4]} {row[1]:d}"
            # print(cbText)
            self.cbElemente.addItem(cbText)

        self.pbBerechne.clicked.connect(self.berechne)
        self.pbEingabe.clicked.connect(self.datenEingabe)
        self.pbGraphik.clicked.connect(self.show_Graph)
        self.cbElemente.currentIndexChanged.connect(self.zeigeBeispiel)

    def berechne(self):
        # print("dlgQuantenHarmonischerOszillator: enter berechne")
        if self.leAnfangsmengeInput.text() == "" or self.leHalbwertszeitInput.text() == "":
            show_warning(self=None, title="Warning", text="Daten unvollständig")
        else:
            self.Anfangsmenge = float(self.leAnfangsmengeInput.text())
            self.Halbwertszeit = int(self.leHalbwertszeitInput.text())
            self.inverseHalftime = 1 / self.Halbwertszeit
            self.Element = self.cbElemente.currentText()

            t_init, t_final, step_size = 0, self.Halbwertszeit * 2, 1
            self.t = np.arange(t_init, t_final, step_size)

            self.leInverseHalbwertszeit.setText(f"{self.inverseHalftime:.3f}")
            self.leStatus.setText("Fertig")
            self.lbGraphExtensionTitel.setText("Radioaktiver Zerfall")
            # print("dlgQuantenHarmonischerOszillator: berechne displayWaveFunction=", self.displayWaveFunction)
            # print("dlgQuantenHarmonischerOszillator: ende berechne")

    def datenEingabe(self):
        # print("dlgQuantenHarmonischerOszillator: enter datenEingabe")
        self.gbDatenEingabe.setEnabled(True)
        self.lbAnfangsmenge.setEnabled(True)
        self.leAnfangsmengeInput.setEnabled(True)
        self.lbHalbwertszeit.setEnabled(True)
        self.leHalbwertszeitInput.setEnabled(True)

    def _init_graph(self):
        # print("dlgQuantenHarmonischerOszillator _init_graph enter")
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
        # print("dlgQuantenHarmonischerOszillator: show_Graph Start")
        if self.windowResized:
            self.resize(self.dialogWidth, self.dialogHeight)
            self.windowResized = False
            self.pbGraphik.setText("Graph >>>")
            for i in reversed(range(self.lyGraph.count())):
                self.lyGraph.itemAt(i).widget().deleteLater()
        else:
            self.ax = self._init_graph()

            def model(t, N):  # order of the argument is very important; first independent and then dependent variable
                return -self.inverseHalftime * N

            sol = solve_ivp(model, t_span=(self.t[0], self.t[-1]), y0=([self.Anfangsmenge]), t_eval=self.t)

            t = sol.t
            N = sol.y.T

            self.ax.plot(t, N, ls='--', color='green', label='Parent nucleus')
            self.ax.plot(t, self.Anfangsmenge - N, ls='--', color='orange', label='Daughter nucleus')
            self.ax.legend()
            # self.ax.plot(q, V, color='k', linewidth=1.5)
            # # print("dlgQuantenHarmonischerOszillator: show_Graph psi_v, q", len(psi_v), len(q))
            # self.plot_func(q, psi_v ** 2, yoffset=E_v)
            # # The energy, E = (v+0.5).hbar.omega.
            # self.ax.text(s=r'$\frac{{{}}}{{2}}\hbar\omega$'.format(2 * v + 1), x=qmax + 0.2,
            #              y=E_v, va='center')
            # # Label the vibrational levels.
            # self.ax.text(s=r'$v={}$'.format(v), x=qmin - 0.2, y=E_v, va='center', ha='right')
            #
            # # The top of the plot, plus a bit.
            # ylabel = r'$|\psi(q)|^2$'
            # self.ax.text(s=ylabel, x=0, y=ymax, va='bottom', ha='center')
            #
            # self.ax.set_xlabel('$q$')
            # self.ax.set_xlim(xmin, xmax)
            # self.ax.set_ylim(0, ymax)
            # self.ax.spines['left'].set_position('center')
            # self.ax.set_yticks([])
            # self.ax.spines['top'].set_visible(False)
            # self.ax.spines['right'].set_visible(False)

            self.lyGraph.addWidget(self.toolbar)
            self.lyGraph.addWidget(self.canvas)

    def zeigeBeispiel(self):
        print("dialogRadioactiveDecay zeigeBeispiel Start")
        cbIndex = self.cbElemente.currentIndex()
        # print(f"dialogRadioactiveDecay zeigeBeispiel Index= {cbIndex:d}")
        self.pteStrahlungsarten.insertPlainText(self.rows[cbIndex-1][3])
        self.pteHalbwertszeit.insertPlainText(self.rows[cbIndex-1][2])
