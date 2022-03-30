#!/usr/bin/python3
# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication

from main_physik import MainWindow


if __name__ == '__main__':
    # print("Main Enter")
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit(ret)
