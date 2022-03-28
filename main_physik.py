from PySide2.QtWidgets import QMainWindow

from dialogBerechneImpuls import dlgWinBerechneImpuls
from dialogEinfachesPendel import dlgEinfachesPendel
from dialogLissajous import dlgLissajous
from dialogParticleInB import dlgParticleInB
from dialogPolyRegression import dlgWinPolyRegression
from dialogSchieferWurf import dlgSchieferWurf
from dialogTest import dlgWinTest
from dialogVektor_berechnen import dlgWinVektor_berechnen
from main_physik_ui import Ui_Physik


class MainWindow(QMainWindow, Ui_Physik):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.action_Impuls.triggered.connect(self.dlg_BerechneImpuls)
        self.actionVektorrechnung.triggered.connect(self.dlg_BerechneVektoren)
        self.actionLineare_Regression.triggered.connect(self.dlg_LineareRegression)
        self.actionkleinste_Quadrate_Polynom.triggered.connect(self.dlg_PolynomRegression)
        self.actionEinfaches_Pendel.triggered.connect(self.dlg_EinfachesPendel)
        self.actionSchiefer_Wurf.triggered.connect(self.dlg_SchieferWurf)
        self.actionLissajous_Figuren.triggered.connect(self.dlg_Lissajous)
        self.actiongeladenes_Teichen_im_Magnetfeld.triggered.connect(self.dlg_ParticleInB)
        self.actionTest.triggered.connect(self.dlg_Test)

        self.show()

    @staticmethod
    def dlg_BerechneImpuls():
        # print("MainWindow: dlg_BerechneImpuls")
        dlgWin = dlgWinBerechneImpuls()
        dlgWin.exec_()

    @staticmethod
    def dlg_BerechneVektoren():
        # print("MainWindow: dlg_BerechneVektoren")
        dlgWin = dlgWinVektor_berechnen()
        dlgWin.exec_()

    @staticmethod
    def dlg_LineareRegression():
        # print("MainWindow: dlg_LineareRegression")
        dlgWin = dlgWinPolyRegression()
        dlgWin.exec_()

    @staticmethod
    def dlg_PolynomRegression():
        # print("MainWindow: dlg_PolynomRegression")
        dlgWin = dlgWinPolyRegression(polynomial=True)
        dlgWin.exec_()

    @staticmethod
    def dlg_EinfachesPendel():
        # print("MainWindow: dlgEinfachesPendel")
        dlgWin = dlgEinfachesPendel()
        dlgWin.exec_()

    @staticmethod
    def dlg_SchieferWurf():
        # print("MainWindow: dlg_SchieferWurf")
        dlgWin = dlgSchieferWurf()
        dlgWin.exec_()

    @staticmethod
    def dlg_Lissajous():
        # print("MainWindow: dlg_Lissajous")
        dlgWin = dlgLissajous()
        dlgWin.exec_()

    @staticmethod
    def dlg_ParticleInB():
        # print("MainWindow: dlg_ParticleInB")
        dlgWin = dlgParticleInB()
        dlgWin.exec_()

    @staticmethod
    def dlg_Test():
        print("MainWindow: dlg_Test")
        dlgWin = dlgWinTest()
        dlgWin.exec_()
