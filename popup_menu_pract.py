from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog
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
        file_tab.addAction('Открыть', self.action_clicked)
        file_tab.addAction('Сохранить', self.action_clicked)

    @QtCore.pyqtSlot()
    def action_clicked(self):
        """"""

        action = self.sender()

        if action.text() == 'Открыть':
            fname = QFileDialog.getOpenFileName(self)[0]
            try:
                with open(fname, 'r', encoding='utf-8') as f:
                    data = f.read()
                    self.text_edit.setText(data)
            except FileNotFoundError:
                print("Файл не выбран.")

        elif action.text() == 'Сохранить':
            fname = QFileDialog.getSaveFileName(self)[0]
            try:
                with open(fname, 'w', encoding='utf-8') as f:
                    text = self.text_edit.toPlainText()
                    f.write(text)
            except FileNotFoundError:
                print("Файл не выбран.")

        else:
            pass


def application():
    """"""

    app = QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
    mw = MainWindow()
    mw.show()
    app.exec_()
