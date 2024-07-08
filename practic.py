from PyQt5 import QtWidgets as qtw
import sys


class MainWindow(qtw.QMainWindow):
    """Класс с атрибутами и методами главного окна"""

    def __init__(self):
        super(MainWindow, self).__init__()

        # Main window (one)
        self.setWindowTitle('Практика')
        self.setGeometry(1300, 250, 315, 120)

        # Result field
        self.result_field = qtw.QLineEdit(self)
        self.result_field.setReadOnly(True)
        self.result_field.move(5, 50)
        self.result_field.setFixedWidth(305)
        self.result_field.setStyleSheet("color: white;  background-color: grey")

        # Text object
        self.main_text = qtw.QLabel(self)
        self.main_text.setText('Тестовая надпись в основном окне')
        self.main_text.move(80, 20)
        self.main_text.adjustSize()

        # Result button object
        self.btn_res = qtw.QPushButton(self)
        self.btn_res.move(5, 85)
        self.btn_res.setText('ENTER')
        self.btn_res.setFixedWidth(150)
        self.btn_res.clicked.connect(self._show_result)

        # Clear button object
        self.btn_clr = qtw.QPushButton(self)
        self.btn_clr.move(160, 85)
        self.btn_clr.setText('CLEAR')
        self.btn_clr.setFixedWidth(150)
        self.btn_clr.clicked.connect(self._clear_result)

    def _show_result(self):
        """Метод для отображения текста"""

        result = "Данные отсутствуют"
        self.result_field.setText(result)

    def _clear_result(self):
        """"""

        self.result_field.clear()


def run_application():
    """"""

    app = qtw.QApplication(sys.argv)
    app.setStyle(qtw.QStyleFactory.create("Fusion"))
    mw = MainWindow()
    mw.show()
    app.exec_()


run_application()
