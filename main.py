from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
import sys
from api import PetFriends
import sys
import os


class MainWindow(object):
    def setupUi(self, mw):
        mw.setObjectName("mw")
        mw.resize(790, 580)
        mw.setStyleSheet("background-color: rgb(200, 200, 200);")
        mw.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(mw)
        self.centralwidget.setObjectName("centralwidget")
        self.result_field = QtWidgets.QTextEdit(self.centralwidget)
        self.result_field.setGeometry(QtCore.QRect(10, 10, 381, 561))
        self.result_field.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                        "background-color: rgb(255, 255, 255);")
        self.result_field.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.result_field.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.result_field.setLineWidth(3)
        self.result_field.setReadOnly(True)
        self.result_field.setObjectName("result_field")
        self.post_label = QtWidgets.QLabel(self.centralwidget)
        self.post_label.setGeometry(QtCore.QRect(410, 10, 381, 31))
        self.post_label.setAlignment(QtCore.Qt.AlignCenter)
        self.post_label.setObjectName("post_label")
        self.url_label = QtWidgets.QLabel(self.centralwidget)
        self.url_label.setGeometry(QtCore.QRect(410, 60, 41, 21))
        self.url_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.url_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.url_label.setObjectName("url_label")
        self.url_field = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.url_field.setGeometry(QtCore.QRect(450, 60, 331, 21))
        self.url_field.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "font: 8pt \"MS Shell Dlg 2\";")
        self.url_field.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.url_field.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.url_field.setObjectName("url_field")
        self.path_field = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.path_field.setGeometry(QtCore.QRect(450, 90, 331, 21))
        self.path_field.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 8pt \"MS Shell Dlg 2\";")
        self.path_field.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.path_field.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.path_field.setObjectName("path_field")
        self.path_label = QtWidgets.QLabel(self.centralwidget)
        self.path_label.setGeometry(QtCore.QRect(410, 90, 41, 21))
        self.path_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.path_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.path_label.setObjectName("path_label")
        self.token_field = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.token_field.setGeometry(QtCore.QRect(450, 120, 331, 21))
        self.token_field.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "font: 8pt \"MS Shell Dlg 2\";")
        self.token_field.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.token_field.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.token_field.setObjectName("token_field")
        self.token_label = QtWidgets.QLabel(self.centralwidget)
        self.token_label.setGeometry(QtCore.QRect(410, 120, 41, 21))
        self.token_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.token_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.token_label.setObjectName("token_label")
        self.params_label = QtWidgets.QLabel(self.centralwidget)
        self.params_label.setGeometry(QtCore.QRect(410, 40, 371, 16))
        self.params_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.params_label.setAlignment(QtCore.Qt.AlignCenter)
        self.params_label.setObjectName("params_label")
        self.body_label = QtWidgets.QLabel(self.centralwidget)
        self.body_label.setGeometry(QtCore.QRect(410, 150, 371, 16))
        self.body_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.body_label.setAlignment(QtCore.Qt.AlignCenter)
        self.body_label.setObjectName("body_label")
        self.name_field = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.name_field.setGeometry(QtCore.QRect(450, 170, 331, 21))
        self.name_field.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 8pt \"MS Shell Dlg 2\";")
        self.name_field.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.name_field.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.name_field.setObjectName("name_field")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(410, 170, 41, 21))
        self.name_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.name_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.name_label.setObjectName("name_label")
        self.breed_field = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.breed_field.setGeometry(QtCore.QRect(450, 200, 331, 21))
        self.breed_field.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "font: 8pt \"MS Shell Dlg 2\";")
        self.breed_field.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.breed_field.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.breed_field.setObjectName("breed_field")
        self.breed_label = QtWidgets.QLabel(self.centralwidget)
        self.breed_label.setGeometry(QtCore.QRect(410, 200, 41, 21))
        self.breed_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.breed_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.breed_label.setObjectName("breed_label")
        self.age_field = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.age_field.setGeometry(QtCore.QRect(450, 230, 331, 21))
        self.age_field.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "font: 8pt \"MS Shell Dlg 2\";")
        self.age_field.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.age_field.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.age_field.setObjectName("age_field")
        self.age_label = QtWidgets.QLabel(self.centralwidget)
        self.age_label.setGeometry(QtCore.QRect(410, 230, 41, 21))
        self.age_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.age_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.age_label.setObjectName("age_label")
        self.send_btn = QtWidgets.QPushButton(self.centralwidget)
        self.send_btn.setGeometry(QtCore.QRect(410, 300, 75, 41))
        self.send_btn.setStyleSheet("background-color: rgb(0, 170, 0);\n"
                                    "color: rgb(255, 255, 255);")
        self.send_btn.setObjectName("send_btn")
        self.select_btn = QtWidgets.QPushButton(self.centralwidget)
        self.select_btn.setGeometry(QtCore.QRect(470, 260, 75, 23))
        self.select_btn.setObjectName("select_btn")
        self.response_field = QtWidgets.QTextEdit(self.centralwidget)
        self.response_field.setGeometry(QtCore.QRect(410, 360, 371, 211))
        self.response_field.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
                                          "background-color: rgb(255, 255, 255);")
        self.response_field.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.response_field.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.response_field.setLineWidth(1)
        self.response_field.setReadOnly(True)
        self.response_field.setObjectName("response_field")
        self.vert_scroll_bar = QtWidgets.QScrollBar(self.centralwidget)
        self.vert_scroll_bar.setGeometry(QtCore.QRect(380, 10, 16, 561))
        self.vert_scroll_bar.setSingleStep(0)
        self.vert_scroll_bar.setPageStep(1)
        self.vert_scroll_bar.setProperty("value", 0)
        self.vert_scroll_bar.setSliderPosition(0)
        self.vert_scroll_bar.setOrientation(QtCore.Qt.Vertical)
        self.vert_scroll_bar.setObjectName("vert_scroll_bar")
        self.photo_field = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.photo_field.setGeometry(QtCore.QRect(560, 260, 221, 21))
        self.photo_field.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                       "font: 8pt \"MS Shell Dlg 2\";")
        self.photo_field.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.photo_field.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.photo_field.setReadOnly(True)
        self.photo_field.setObjectName("photo_field")
        self.petphoto_label = QtWidgets.QLabel(self.centralwidget)
        self.petphoto_label.setGeometry(QtCore.QRect(410, 260, 51, 21))
        self.petphoto_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.petphoto_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.petphoto_label.setObjectName("petphoto_label")
        self.clear_res_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_res_btn.setGeometry(QtCore.QRect(500, 300, 91, 41))
        self.clear_res_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(0, 85, 127);")
        self.clear_res_btn.setObjectName("clear_res_btn")
        mw.setCentralWidget(self.centralwidget)
        self.add_actions_btn()
        self.clipboard = QtWidgets.QApplication.clipboard()
        self.clipboard.setImage(QtGui.QImage())
        self.retranslateUi(mw)
        QtCore.QMetaObject.connectSlotsByName(mw)

    def retranslateUi(self, mw):
        _translate = QtCore.QCoreApplication.translate
        mw.setWindowTitle(_translate("mw", "Petfriends.skillfactory.ru (REST API)"))
        self.post_label.setText(_translate("mw",
                                           "<html><head/><body><p><span style=\" font-size:11pt; "
                                           "font-weight:600;\">POST - create_pet_with_photo</span></p></body></html>"))
        self.url_label.setText(_translate("mw", "URL:"))
        self.path_label.setText(_translate("mw", "Path:"))
        self.token_label.setText(_translate("mw", "Token:"))
        self.params_label.setText(_translate("mw", "Parameters"))
        self.body_label.setText(_translate("mw", "Body (data of pet)"))
        self.name_label.setText(_translate("mw", "Name:"))
        self.breed_label.setText(_translate("mw", "Breed:"))
        self.age_label.setText(_translate("mw", "Age:"))
        self.send_btn.setText(_translate("mw", "SEND"))
        self.select_btn.setText(_translate("mw", "SELECT.."))
        self.petphoto_label.setText(_translate("mw", "Pet photo:"))
        self.clear_res_btn.setText(_translate("mw", "CLEAR RESULT"))

    def add_actions_btn(self):
        self.select_btn.clicked.connect(self.select_photo)
        # self.send_btn.clicked.connect(self.send_request)
        # self.clear_res_btn.clicked.connect(self.clear_fields)

    def select_photo(self):

        action = self.sender()

        if action.text() == 'SELECT..':
            fname = QFileDialog.getOpenFileName(self)[0]
            try:
                with open(fname, 'rb') as f:
                    print(os.path.dirname(f))

            except FileNotFoundError:
                print("Файл не выбран.")

    # def send_request(self):
    #
    #
    # def clear_fields(self):
    #     self.result_field.clear()
    #     self.response_field.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
    ui = MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
