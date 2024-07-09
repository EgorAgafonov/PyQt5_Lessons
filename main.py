from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu
import sys


class MainWindow(QMainWindow):
    """"""
    
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('ТекстРед')
        self.setGeometry(300, 250, 350, 200)
        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)
        self.createMenuBar()

    def createMenuBar(self):
        """"""
        # Создаем полоску основного меню:
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        # Создаем вкладку "Файл" на полосе основного меню:
        file_tab = QMenu("&Файл", self)
        self.menuBar.addMenu(file_tab)

        # Добавляем опцию "Открыть" во вкладке "Файл" основного меню:
        file_tab_open = file_tab.addMenu('&Открыть')
        file_tab_save = file_tab.addMenu('&Сохранить')


def application():
    """"""

    app = QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
    mw = MainWindow()
    mw.show()
    app.exec_()


if __name__ == "__main__":
    application()


