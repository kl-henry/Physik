from PySide2.QtWidgets import QLineEdit, QLabel


def datenEingabe(myWidget, widgetName=None):
    print("utilities.app_utilities: enter datenEingabe: ", myWidget.objectName())

    widgets = myWidget.children()

    print("utilities.app_utilities: datenEingabe: widgets= ", widgets)
    for widget in widgets:
        print("in Loop %s - %s" % (widget.objectName(), str(type(widget))))
        if widget.objectName() == widgetName:
            widgets_1 = widget.children()
            print("utilities.app_utilities:  in Loop Sub: widgets_1= ", widgets_1, len(widgets_1))
            if len(widgets_1) == 1:
                widgets_count = widgets_1.count()
                print("in Loop2 %s - %d" % (widgets_1.objectName(), widgets_count))
