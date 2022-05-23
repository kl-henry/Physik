from PySide2.QtWidgets import QDialog, QTableWidgetItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

from dialogSimSonnensystem_ui import Ui_dlgSimSonnensystem


class point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class dlgSimSonnensystem(QDialog, Ui_dlgSimSonnensystem):
    def __init__(self, parent=None):
        super(dlgSimSonnensystem, self).__init__(parent)
        self.windowResized = None
        self.setupUi(self)

        self.dialogHeight = self.frameGeometry().height()
        self.dialogWidth = self.frameGeometry().width()


        # planet data(location(m), mass(kg), velocity(m / s)
        solarSystemObjects = {
            "sun": [0, 0, 0, 2e30,0, 0, 0],
            "mercury": [0, 5.7e10, 0, 3.285e23, 47000, 0, 0],
            "venus": [0, 1.1e11, 0, 4.8e24, 35000, 0, 0],
            "earth": [0, 1.5e11, 0, 6e24, 30000, 0, 0],
            "mars": [0, 2.2e11, 0, 2.4e24, 24000, 0, 0],
            "jupiter": [0, 7.7e11, 0, 1e28, 13000, 0, 0],
            "saturn": [0, 1.4e12, 0, 5.7e26, 9000, 0, 0],
            "uranus": [0, 2.8e12, 0, 8.7e25, 6835, 0, 0],
            "neptune": [0, 4.5e12, 0, 1e26, 5477, 0, 0],
            "pluto": [0, 3.7e12, 0, 1.3e22, 4748, 0, 0]
        }
        self.twSolarSystemObjects.setHorizontalHeaderLabels(["Name", "Position(m) x", "Position(m) y", "Position(m) z", "Masse [kg]",
                                                              "Geschw.[m/s] x", "Geschw.[m/s] y", "Geschw.[m/s] z"])
        row = 0
        for n, key in enumerate(solarSystemObjects):
            self.twSolarSystemObjects.setRowCount(n + 1)
            newitem = QTableWidgetItem(key)
            print(key, str(n))
            self.twSolarSystemObjects.setItem(n, 0, newitem)
            for col, item in enumerate(solarSystemObjects[key]):
                newitem = QTableWidgetItem(str(item))
                print("newitem = ", item)
                self.twSolarSystemObjects.setItem(n, col+1, newitem)
            row += 1

        self.twSolarSystemObjects.resizeColumnsToContents()
        self.twSolarSystemObjects.resizeRowsToContents()

        self.pbBerechne.clicked.connect(self.berechne)

    def berechne(self):
        print("dlgWinTest: berechne Enter")
        rows = sorted(set(index.row() for index in
                          self.twSolarSystemObjects.selectedIndexes()))
        for row in rows:
            print('dlgWinTest: berechne Row %d is selected' % row)

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

    def show_Graph(self):
        # print("dlgSimSonnensystem: show_Graph Start")
        if self.windowResized:
            self.resize(self.dialogWidth, self.dialogHeight)
            self.windowResized = False
            self.pbGraphik.setText("Graph >>>")
            self.lyGraph.itemAt(0).widget().deleteLater()
            self.lyGraph.itemAt(1).widget().deleteLater()
        else:
            ax = self._init_graph()

            ax.plot(self.x, self.y, 'or', linewidth=2, label='Messwerte')

            ax.plot(self.x, self.f, dashes=[30, 5, 10, 5], label='Regression')
            plt.grid(True)
            ax.legend(loc='lower right')
            self.lyGraph.addWidget(self.toolbar)
            self.lyGraph.addWidget(self.canvas)

            # self.canvas.draw()
