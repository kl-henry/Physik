import numpy as np
import matplotlib.pyplot as plt

from PySide2.QtGui import QDoubleValidator, QIntValidator
from PySide2.QtWidgets import QDialog
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


from sklearn.linear_model import LinearRegression

from dialogPolyRegression_ui import Ui_dlgPolyRegression
from utilities import messageBoxes


class dlgWinPolyRegression(QDialog, Ui_dlgPolyRegression):
    def __init__(self, polynomial=False):

        print("dlgWinLineareRegression Enter")
        super(dlgWinPolyRegression, self).__init__()
        self.setupUi(self)
        self.polynomial = polynomial
        if self.polynomial:
            self.setWindowTitle(u"Polynom Regression")
            self.pbBeispiel.setText("Beispiel")
            self.frErgebnis.hide()
            self.frPolynomDegree.show()
            self.frPolynomErgebnis.show()
        else:
            self.frPolynomDegree.hide()
            self.frPolynomErgebnis.hide()
            self.frErgebnis.show()

        self.x = []
        self.y = []
        self.f = []
        self.calc_values = []
        self.num_graphs = 1
        self.windowResized = False
        self.y_str = None
        self.x_str = None
        self.selectBeispiel = False
        self.polyDegree = 0

        self.toolbar = None
        self.canvas = None
        self.figure = None

        self.dialogHeight = self.frameGeometry().height()
        self.dialogWidth = self.frameGeometry().width()

        self.pbBerechne.setEnabled(False)
        self.pbGraphik.setEnabled(False)
        self.leX_Werte.setEnabled(False)
        self.leY_Werte.setEnabled(False)

        self.leXInput.setValidator(QDoubleValidator(999999, -999999, 8))
        self.leYInput.setValidator(QDoubleValidator(999999, -999999, 8))

        self.pbBeispiel.clicked.connect(self.Beispiel_Regression)
        self.pbBerechne.clicked.connect(self.berechne_Regression)
        self.pbGraphik.clicked.connect(self.show_Graph)
        self.pbEingabe.clicked.connect(self.daten_Eingabe)
        self.pbUebernehmen.clicked.connect(self.daten_Uebernehmen)

    def Beispiel_Regression(self):
        # print("dlgWinLineareRegression: Beispiel_Regression Enter")
        self.selectBeispiel = True
        if self.polynomial:
            self.Beispiel_Polynomial()
        else:
            self.Beispiel_Millikan()

    def _polyReg(self):
        # print("dlgWinLineareRegression: _polyReg Enter")
        # Polynomial mit Scikit-Learn
        self.x = self.x.flatten()
        self.polyDegree = int(self.sbPolyDegree.text())
        print("dlgWinLineareRegression: _polyReg type(self.x", type(self.x), self.x.shape, self.polyDegree)
        y_fit = np.polyfit(self.x, self.y, self.polyDegree)

        return y_fit

    def _linReg(self):
        # print("dlgWinLineareRegression: _linReg Enter")
        # lineare Regression mit Scikit-Learn
        self.x = self.x.reshape(-1, 1)
        reg = LinearRegression()
        reg.fit(self.x, self.y)
        # Coefficient of determination
        r_squared = reg.score(self.x, self.y)
        # print(r_squared)

        # slope
        slope = reg.coef_
        # print("_linReg, slope: ", slope)

        # intercept
        intercept = reg.intercept_
        # print("_linReg, intercept: ", intercept)

        y_pred = reg.predict(self.x)
        y_pred = y_pred.flatten()
        # print("_linReg, y_pred, y_pred.shape: ", y_pred, y_pred.shape)

        return slope[0], intercept, y_pred, r_squared

    def berechne_Regression(self):
        # print("dlgWinLineareRegression: berechne_Regression Enter")
        x = self.leX_Werte.text()
        y = self.leY_Werte.text()
        x = x.split(",")
        y = y.split(",")
        self.x = np.array(x, np.float)
        self.y = np.array(y, np.float)

        if len(x) == 0 or len(y) == 0:
            messageBoxes.show_warning(text="Zu wenig Parameter")
        else:
            if self.polynomial:
                self.f = self._polyReg()
                print("dlgWinLineareRegression: berechne_Regression polynomial: f", self.f)
                self.lbSteigungErgebnis.setText("")
                self.lbSchnittpunktErbegnis.setText("")
                self.lbFehlerErgebnis.setText(str(""))
                polynomString = "f(x) = "
                for i in range(self.polyDegree, -1, -1):
                    polynomString = polynomString + "{:.5f}*x^{:d} + ".format(self.f[i], i)
                self.textEdit.setText(polynomString)
            else:
                a, i, self.f, r_sq = self._linReg()
                self.lbSteigungErgebnis.setText(str(a))
                self.lbSchnittpunktErbegnis.setText(str(i))
                self.lbFehlerErgebnis.setText(str(r_sq))
            self.pbGraphik.setEnabled(True)

    def Beispiel_Millikan(self):
        # Millikan Messdaten
        k = np.array([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
        q = np.array(
            [6.558, 8.206, 9.880, 11.50, 13.14, 14.81, 16.40, 18.04, 19.68, 21.32, 22.96, 24.60, 26.24, 27.88, 29.52])

        self.aufbereiten_Messwerte(k, q)
        self.lbGraphExtensionTitel.setText("Millikan Messwerte")

    def Beispiel_Polynomial(self):
        # Beispiel Messdaten
        x_d = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
        y_d = np.array([0, 0.8, 0.9, 0.1, -0.6, -0.8, -1, -0.9, -0.4])

        self.aufbereiten_Messwerte(x_d, y_d)
        self.lbGraphExtensionTitel.setText("Beispiel Messwerte Polynom")

    def aufbereiten_Messwerte(self, x, y):
        k_str_elem = [str(element) for element in x]
        k_str = ",".join(k_str_elem)
        self.leX_Werte.setText(k_str)
        q_str_elem = [str(element) for element in y]
        q_str = ",".join(q_str_elem)
        self.leY_Werte.setText(q_str)
        self.pbBerechne.setEnabled(True)

    def show_Graph(self):
        # print("dlgWinLineareRegression: show_Graph Start")
        if self.windowResized:
            self.resize(self.dialogWidth, self.dialogHeight)
            self.windowResized = False
            self.pbGraphik.setText("Graph >>>")
            self.lyGraph.itemAt(0).widget().deleteLater()
            self.lyGraph.itemAt(1).widget().deleteLater()
        else:
            if not self.polynomial:
                if len(self.f) == 0:
                    self.berechne_Regression()
                ax = self._init_graph()

                ax.plot(self.x, self.y, 'or', linewidth=2, label='Messwerte')

                ax.plot(self.x, self.f, dashes=[30, 5, 10, 5], label='Regression')
                plt.grid(True)
                ax.legend(loc='lower right')
                self.lyGraph.addWidget(self.toolbar)
                self.lyGraph.addWidget(self.canvas)
                if not self.selectBeispiel:
                    self.lbGraphExtensionTitel.setText(self.leGraphTitleInput.text())

                # self.canvas.draw()
            else:
                if len(self.f) == 0:
                    self.berechne_Regression()
                ax = self._init_graph()

                ax.title.set_text("Polynom {0:d}. Grades".format(self.polyDegree))
                ax.plot(self.x, self.y, 'or', linewidth=2, label='Messwerte')

                ax.plot(self.x, np.polyval(self.f, self.x), dashes=[30, 5, 10, 5], label='Regression')
                plt.grid(True)
                ax.legend(loc='lower right')
                self.lyGraph.addWidget(self.toolbar)
                self.lyGraph.addWidget(self.canvas)
                if not self.selectBeispiel:
                    self.lbGraphExtensionTitel.setText(self.leGraphTitleInput.text())

    def _init_graph(self):
        self.resize(1084, 459)
        self.windowResized = True
        self.pbGraphik.setText("Graph <<<")
        # print("show_Graph: type(a), type(i), type(f):", type(a), type(i), type(f))
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        return ax

    def daten_Eingabe(self):
        # print("dlgWinLineareRegression: daten_Eingabe Start")
        self.selectBeispiel = False
        self.leX_Werte.setEnabled(True)
        self.leY_Werte.setEnabled(True)
        self.gbDatenEingabe.setEnabled(True)
        self.pbUebernehmen.setEnabled(True)
        self.leXInput.setEnabled(True)
        self.leYInput.setEnabled(True)
        self.leGraphTitleInput.setEnabled(True)
        self.pbBerechne.setEnabled(True)
        self.leX_Werte.setText("")
        self.leY_Werte.setText("")
        self.x_str = ""
        self.y_str = ""

    def daten_Uebernehmen(self):
        # print("dlgWinLineareRegression: daten_Uebernehmen Start")
        if self.leXInput.text() == "" or self.leYInput.text() == "":
            messageBoxes.show_warning(self, text="X oder Y fehlt")
        else:
            x_value = self.leXInput.text().replace(",", ".")
            y_value = self.leYInput.text().replace(",", ".")
            if len(self.x_str) > 0:
                self.x_str = self.x_str + "," + x_value
                self.y_str = self.y_str + "," + y_value
            else:
                self.x_str = x_value
                self.y_str = y_value
            # print("dlgWinLineareRegression: daten_Uebernehmen: len(x)= ", len(self.x_str))
            # print("dlgWinLineareRegression: daten_Uebernehmen self.x, self.y", self.x, self.y)
            self.leX_Werte.setText(str(self.x_str))
            self.leY_Werte.setText(str(self.y_str))
            self.leXInput.setText("")
            self.leYInput.setText("")
