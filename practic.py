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

        # Result field
        self.result_field = qtw.QLineEdit(self)
        self.result_field.setReadOnly(True)
        self.result_field.move(150, 50)
        self.result_field.setFixedWidth(200)

        # Text object
        self.main_text = qtw.QLabel(self)
        self.main_text.setText('Тестовая надпись в основном окне')
        self.main_text.move(150, 20)
        self.main_text.adjustSize()

        # Result button object
        self.btn_res = qtw.QPushButton(self)
        self.btn_res.move(100, 90)
        self.btn_res.setText('Укажите логин и пароль \nпользователя')
        self.btn_res.setFixedWidth(200)
        self.btn_res.clicked.connect(self._show_result)

        # Clear button object
        self.btn_clr = qtw.QPushButton(self)
        self.btn_res.move(150, 90)
        self.btn_res.setText('Очистить поле вывода')
        self.btn_res.setFixedWidth(200)
        self.btn_res.clicked.connect(self._show_result)

    def _show_result(self):
        """"""

        result = "Данные отсутствуют"
        self.result_field.setText(result)








def run_application():
    """"""

    app = qtw.QApplication(sys.argv)
    app.setStyle(qtw.QStyleFactory.create("Fusion"))
    mw = MainWindow()
    mw.show()
    app.exec_()


run_application()



