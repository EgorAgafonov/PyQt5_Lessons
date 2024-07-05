from PyQt5 import QtWidgets as qtw
import sys
import tkinter


def application():
    app = qtw.QApplication(sys.argv)
    mw = qtw.QMainWindow()
    mw.setWindowTitle('Практика')
    mw.setGeometry(960, 540, 500, 250)
    mw.setStyleSheet('Fusion')
    mw.show()
    sys.exit(app.exec_())


application()

