from PySide2.QtWidgets import QDialog

from dialogVektor_berechnen_ui import Ui_dlgVektorRechnung

from vector_rechnung.add_vectors import addVectors
from vector_rechnung.mag_vector import magVectors
from vector_rechnung.norm_vectors import normVectors
from vector_rechnung.angle_Vectors import angleBetween


class dlgWinVektor_berechnen(QDialog, Ui_dlgVektorRechnung):
    def __init__(self):
        print("dlgWinVektor_berechnen Enter")
        super(dlgWinVektor_berechnen, self).__init__()
        self.setupUi(self)

        self.pbAdd.clicked.connect(self.addiereVektoren)
        self.pbBetrag.clicked.connect(self.berechneBetrag)
        self.pbEinheitsVektor.clicked.connect(self.berechneEinheitsvektor)
        self.pbWinkel.clicked.connect(self.berechneWinkel)

    def addiereVektoren(self):
        # print("dlgWinVektor_berechnen: enter addiereVektoren")
        self.lbErgebnis.setText("Addition")
        v1 = (float(self.leX.text()), float(self.leY.text()), float(self.leZ.text()))
        v2 = (float(self.leX_2.text()), float(self.leY_2.text()), float(self.leZ_2.text()))

        v3 = addVectors(v1, v2)
        # print(v3)
        self.leX_3.setText("%.2f" % v3[0])
        self.leY_3.setText("%.2f" % v3[1])
        self.leZ_3.setText("%.2f" % v3[2])

    def berechneBetrag(self):
        # print("dlgWinVektor_berechnen: enter berechneBetrag")
        self.lbErgebnis.setText("Betrag")
        v1 = (float(self.leX.text()), float(self.leY.text()), float(self.leZ.text()))

        v3 = magVectors(v1)
        # print(v3)
        self.leX_3.setText("%.2f" % v3)
        self.leY_3.setText("")
        self.leZ_3.setText("")

    def berechneEinheitsvektor(self):
        # print("dlgWinVektor_berechnen: enter berechneEinheitsvektor")
        self.lbErgebnis.setText("Einheitsvektor")
        v1 = (float(self.leX.text()), float(self.leY.text()), float(self.leZ.text()))

        v3 = normVectors(v1)
        # print(v3)
        self.leX_3.setText("%.2f" % v3[0])
        self.leY_3.setText("%.2f" % v3[1])
        self.leZ_3.setText("%.2f" % v3[2])

    def berechneWinkel(self):
        print("dlgWinVektor_berechnen: enter berechneWinkel")
        self.lbErgebnis.setText("Winkel")
        v1 = (float(self.leX.text()), float(self.leY.text()))
        v2 = (float(self.leX_2.text()), float(self.leY_2.text()))

        v3 = angleBetween(v1, v2)
        print(v3)
        self.leX_3.setText("%.2f" % v3)
        self.leY_3.setText("")
        self.leZ_3.setText("")
