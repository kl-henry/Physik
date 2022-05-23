from PySide2.QtGui import QDoubleValidator
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

from PySide2.QtWidgets import QDialog
from matplotlib import pyplot as plt
from scipy.special import factorial

from dialogQuantenHarmonischerOszillator_ui import Ui_dlgQuantenHarmonischerOszillator
from utilities.messageBoxes import show_warning


def get_potential(q):
    """Return potential energy on scaled oscillator displacement grid q."""
    return q ** 2 / 2


class dlgQuantenHarmonischerOszillator(QDialog, Ui_dlgQuantenHarmonischerOszillator):
    def __init__(self):
        # print("dlgQuantenHarmonischerOszillator Enter")
        super(dlgQuantenHarmonischerOszillator, self).__init__()

        self.setupUi(self)

        self.dialogHeight = self.frameGeometry().height()
        self.dialogWidth = self.frameGeometry().width()

        floatValidator = QDoubleValidator(0.0, 90.0, 2)

        self.windowResized = None
        self.PotentialFaktor = None
        self.displayWaveFunction = False
        self.ax = None
        self.EnergyLevel = None
        self.potential = None
        self.Hr = None
        # Normalization constant and energy for vibrational state v
        self.N = lambda v: 1. / np.sqrt(np.sqrt(np.pi) * 2 ** v * factorial(v))
        self.get_E = lambda v: v + 0.5
        self.lePotentialFaktorInput.setValidator(floatValidator)
        # Some appearance settings
        # Pad the q-axis on each side of the maximum turning points by this fraction
        self.QPAD_FRAC = 1.3
        # Scale the wavefunctions by this much, so they don't overlap
        self.SCALING = 0.7
        # Colours of the positive and negative parts of the wavefunction

        self.pbBerechne.clicked.connect(self.berechne)
        self.pbEingabe.clicked.connect(self.datenEingabe)
        self.pbGraphik.clicked.connect(self.show_Graph)

    def make_Hr(self):
        """Return a list of np.poly1d objects representing Hermite polynomials."""
        # Define the Hermite polynomials up to order VMAX by recursion:
        # H_[v] = 2qH_[v-1] - 2(v-1)H_[v-2]
        Hr = [None] * (self.EnergyLevel + 1)
        Hr[0] = np.poly1d([1., ])
        Hr[1] = np.poly1d([2., 0.])
        for v in range(2, self.EnergyLevel + 1):
            Hr[v] = Hr[1] * Hr[v - 1] - 2 * (v - 1) * Hr[v - 2]
        return Hr

    def get_psi(self, v, q):
        """Return the harmonic oscillator wavefunction for level v on grid q."""
        return self.N(v) * self.Hr[v](q) * np.exp(-q * q / 2.)

    def get_turning_points(self, v):
        """Return the classical turning points for state v."""
        qmax = np.sqrt(2. * self.get_E(v + 0.5))
        return -qmax, qmax

    def berechne(self):
        # print("dlgQuantenHarmonischerOszillator: enter berechne")
        if self.lePotentialFaktorInput.text() == "":
            show_warning(self=None, title="Warning", text="Daten unvollständig")
        else:
            self.PotentialFaktor = float(self.lePotentialFaktorInput.text())
            self.EnergyLevel = int(self.spNoofEnergieNiveaus.text())
            self.displayWaveFunction = self.rbPsiSquare.isChecked()

        self.leNoofEnergieNiveaus.setText(str(self.EnergyLevel+1))
        self.leStatus.setText("Fertig")
        self.lbGraphExtensionTitel.setText("Harmonischer Quanten Oszillator")
        # print("dlgQuantenHarmonischerOszillator: berechne displayWaveFunction=", self.displayWaveFunction)
        # print("dlgQuantenHarmonischerOszillator: ende berechne")

    def datenEingabe(self):
        # print("dlgQuantenHarmonischerOszillator: enter datenEingabe")
        self.gbDatenEingabe.setEnabled(True)
        self.lbPotentialFaktor.setEnabled(True)
        self.lePotentialFaktorInput.setEnabled(True)
        self.lbAnzahlEnergieniveaus.setEnabled(True)
        self.spNoofEnergieNiveaus.setEnabled(True)

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

    def plot_func(self, q, f, scaling=1, yoffset=0):
        """Plot f*scaling with offset yoffset.

        The curve above the offset is filled with COLOUR1; the curve below is
        filled with COLOUR2.

        """
        # print("dlgQuantenHarmonischerOszillator: plot_func f, q", len(f), len(q))
        COLOUR1 = (0.6196, 0.0039, 0.2588, 1.0)
        COLOUR2 = (0.3686, 0.3098, 0.6353, 1.0)
        self.ax.plot(q, f * scaling + yoffset, color=COLOUR1)
        self.ax.fill_between(q, f * scaling + yoffset, yoffset, f > 0.,
                             color=COLOUR1, alpha=0.5)
        self.ax.fill_between(q, f * scaling + yoffset, yoffset, f < 0.,
                             color=COLOUR2, alpha=0.5)

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
            self.Hr = self.make_Hr()
            qmin, qmax = self.get_turning_points(self.EnergyLevel)
            xmin, xmax = self.QPAD_FRAC * qmin, self.QPAD_FRAC * qmax
            q = np.linspace(qmin, qmax, 500)
            V = get_potential(q)

            self.ax.plot(q, V, color='k', linewidth=1.5)
            # Plot each of the wavefunctions (or probability distributions) up to VMAX.
            E_v = 0
            for v in range(self.EnergyLevel + 1):
                psi_v = self.get_psi(v, q)
                E_v = self.get_E(v)
                # print("dlgQuantenHarmonischerOszillator: show_Graph psi_v, q", len(psi_v), len(q))
                if self.displayWaveFunction:
                    self.plot_func(q, psi_v ** 2, yoffset=E_v)
                else:
                    self.plot_func(q, psi_v, yoffset=E_v)
                # The energy, E = (v+0.5).hbar.omega.
                self.ax.text(s=r'$\frac{{{}}}{{2}}\hbar\omega$'.format(2 * v + 1), x=qmax + 0.2,
                             y=E_v, va='center')
                # Label the vibrational levels.
                self.ax.text(s=r'$v={}$'.format(v), x=qmin - 0.2, y=E_v, va='center', ha='right')

            # The top of the plot, plus a bit.
            ymax = E_v + 0.5

            if self.displayWaveFunction:
                ylabel = r'$|\psi(q)|^2$'
            else:
                ylabel = r'$\psi(q)$'
            self.ax.text(s=ylabel, x=0, y=ymax, va='bottom', ha='center')

            self.ax.set_xlabel('$q$')
            self.ax.set_xlim(xmin, xmax)
            self.ax.set_ylim(0, ymax)
            self.ax.spines['left'].set_position('center')
            self.ax.set_yticks([])
            self.ax.spines['top'].set_visible(False)
            self.ax.spines['right'].set_visible(False)

            self.lyGraph.addWidget(self.toolbar)
            self.lyGraph.addWidget(self.canvas)
