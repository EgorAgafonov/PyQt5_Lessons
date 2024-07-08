from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()

        self.common_style = ("background-color: rgb(5, 185, 194); color: rgb(255, 255, 255); font: 24pt 'Tw Cen MT "
                             "Condensed Extra Bold';")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(300, 400)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.btn_enter = QtWidgets.QPushButton(self.centralwidget)
        self.btn_enter.setGeometry(QtCore.QRect(140, 320, 161, 80))
        self.btn_enter.setStyleSheet(self.common_style)
        self.btn_enter.setAutoDefault(False)
        self.btn_enter.setFlat(False)
        self.btn_enter.setObjectName("btn_enter")

        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(-10, 320, 151, 80))
        self.btn_0.setStyleSheet(self.common_style)
        self.btn_0.setAutoDefault(False)
        self.btn_0.setFlat(False)
        self.btn_0.setObjectName("btn_0")

        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 240, 101, 80))
        self.btn_7.setStyleSheet(self.common_style)
        self.btn_7.setAutoDefault(False)
        self.btn_7.setFlat(False)
        self.btn_7.setObjectName("btn_7")

        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(100, 240, 101, 80))
        self.btn_8.setStyleSheet(self.common_style)
        self.btn_8.setAutoDefault(False)
        self.btn_8.setFlat(False)
        self.btn_8.setObjectName("btn_8")

        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(200, 240, 111, 80))
        self.btn_9.setStyleSheet(self.common_style)
        self.btn_9.setAutoDefault(False)
        self.btn_9.setFlat(False)
        self.btn_9.setObjectName("btn_9")

        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(200, 160, 111, 80))
        self.btn_6.setStyleSheet(self.common_style)
        self.btn_6.setAutoDefault(False)
        self.btn_6.setFlat(False)
        self.btn_6.setObjectName("btn_6")

        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 160, 101, 80))
        self.btn_4.setStyleSheet(self.common_style)
        self.btn_4.setAutoDefault(False)
        self.btn_4.setFlat(False)
        self.btn_4.setObjectName("btn_4")

        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(100, 160, 101, 80))
        self.btn_5.setStyleSheet(self.common_style)
        self.btn_5.setAutoDefault(False)
        self.btn_5.setFlat(False)
        self.btn_5.setObjectName("btn_5")

        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 80, 101, 80))
        self.btn_1.setStyleSheet(self.common_style)
        self.btn_1.setAutoDefault(False)
        self.btn_1.setFlat(False)
        self.btn_1.setObjectName("btn_1")

        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(100, 80, 101, 80))
        self.btn_2.setStyleSheet(self.common_style)
        self.btn_2.setAutoDefault(False)
        self.btn_2.setFlat(False)
        self.btn_2.setObjectName("btn_2")

        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(200, 80, 111, 80))
        self.btn_3.setStyleSheet(self.common_style)
        self.btn_3.setAutoDefault(False)
        self.btn_3.setFlat(False)
        self.btn_3.setObjectName("btn_3")

        self.result_field = QtWidgets.QLineEdit(self.centralwidget)
        self.result_field.setGeometry(QtCore.QRect(0, -1, 301, 81))
        self.result_field.setStyleSheet("background-color: grey; color: rgb(255, 255, 255); font: 24pt 'Tw Cen MT "
                             "Condensed Extra Bold';")
        self.result_field.setInputMask("")
        self.result_field.setFrame(True)
        self.result_field.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.result_field.setReadOnly(True)
        self.result_field.setObjectName("result_field")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Тестовый проект"))
        self.btn_enter.setText(_translate("MainWindow", "="))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.result_field.setText(_translate("MainWindow", " 0"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
