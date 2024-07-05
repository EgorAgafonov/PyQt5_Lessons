from PyQt5 import QtWidgets as qtw
import sys
import tkinter


def application():
    """"""

    app = qtw.QApplication(sys.argv)
    app.setStyle(qtw.QStyleFactory.create("Fusion"))

    # Main window (one)
    mw = qtw.QMainWindow()
    main_text = qtw.QLabel(mw)
    mw.setWindowTitle('Практика')
    mw.setGeometry(960, 440, 500, 250)

    # Text object
    main_text.setText('Тестовая надпись в основном окне')
    main_text.move(150, 20)
    main_text.adjustSize()

    # Button object
    btn = qtw.QPushButton(mw)
    btn.move(150, 50)
    btn.setText('Укажите логин и пароль \nпользователя')
    btn.setFixedWidth(200)

    mw.show()
    sys.exit(app.exec_())


application()

