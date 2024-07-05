from PyQt5 import QtWidgets as qtw
import sys
import tkinter


class MainWindow(qtw.QMainWindow):
    """"""

    def __init__(self):
        super(MainWindow, self).__init__()

        # Main window (one)
        self.setWindowTitle('Практика')
        self.setGeometry(960, 440, 500, 250)

        # Text object
        self.main_text = qtw.QLabel(self)
        self.main_text.setText('Тестовая надпись в основном окне')
        self.main_text.move(150, 20)
        self.main_text.adjustSize()

        # Button object
        self.btn = qtw.QPushButton(self)
        self.btn.move(150, 50)
        self.btn.setText('Укажите логин и пароль \nпользователя')
        self.btn.setFixedWidth(200)


def run_application():
    """"""

    app = qtw.QApplication(sys.argv)
    app.setStyle(qtw.QStyleFactory.create("Fusion"))
    mw = MainWindow()
    mw.show()
    app.exec_()


run_application()



