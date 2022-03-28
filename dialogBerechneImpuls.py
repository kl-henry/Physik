from PySide2.QtWidgets import QDialog

from dialogBerechneImpuls_ui import Ui_dlgBerechneImpuls


class dlgWinBerechneImpuls(QDialog, Ui_dlgBerechneImpuls):
    def __init__(self):
        print("dlgWinBerechneImpuls Enter")
        super(dlgWinBerechneImpuls, self).__init__()
        self.setupUi(self)
        self.pbBerechne.clicked.connect(self.berechne)

    def berechne(self):
        print("dlgWinBerechneImpuls: berechne Enter")
        m = float(self.leMasse.text())
        v = float(self.leGeschwindigkeit.text())
        self.leImpulsErgebnis.setText(str(m*v))
