from PySide2.QtWidgets import QMessageBox


def show_about(title="AboutBox", text="This is about application"):
    QMessageBox.about(title, text)


def show_warning(self=None, title="Warning", text="This is Warning"):
    QMessageBox.warning(self, title, text)


def show_info(title="Info", text="This is Information"):
    QMessageBox.information(title, text)


def show_question(title="Question MessageBox", text="Do You Like Pyside2"):
    reply = QMessageBox.question(title, text, QMessageBox.Yes | QMessageBox.No)

    if reply == QMessageBox.Yes:
        print("I Like Pyside2")

    elif reply == QMessageBox.No:
        print("I Dont Like Pyside2")
