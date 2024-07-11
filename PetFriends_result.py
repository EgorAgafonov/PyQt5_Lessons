from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import requests

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(600, 330)
        main_window.setStyleSheet("font: 12pt \"Arial\";")
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.post_tab = QtWidgets.QTabWidget(self.centralwidget)
        self.post_tab.setGeometry(QtCore.QRect(0, 0, 600, 331))
        self.post_tab.setStyleSheet("background-color: rgb(199, 199, 199);")
        self.post_tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.post_tab.setElideMode(QtCore.Qt.ElideNone)
        self.post_tab.setDocumentMode(False)
        self.post_tab.setTabsClosable(False)
        self.post_tab.setTabBarAutoHide(False)
        self.post_tab.setObjectName("post_tab")
        self.get_tab = QtWidgets.QWidget()
        self.get_tab.setObjectName("get_tab")
        self.result_field = QtWidgets.QTextEdit(self.get_tab)
        self.result_field.setGeometry(QtCore.QRect(10, 40, 261, 241))
        self.result_field.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Arial\";")
        self.result_field.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.result_field.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.result_field.setReadOnly(True)
        self.result_field.setObjectName("result_field")
        self.label = QtWidgets.QLabel(self.get_tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 261, 21))
        self.label.setStyleSheet("color: rgb(0, 170, 0);")
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setObjectName("label")
        self.vert_line = QtWidgets.QFrame(self.get_tab)
        self.vert_line.setGeometry(QtCore.QRect(280, 10, 20, 271))
        self.vert_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.vert_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vert_line.setObjectName("vert_line")
        self.url_label = QtWidgets.QLabel(self.get_tab)
        self.url_label.setGeometry(QtCore.QRect(300, 10, 280, 41))
        self.url_label.setStyleSheet("font: 8pt \"Arial\";")
        self.url_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.url_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.url_label.setObjectName("url_label")
        self.url_input_field = QtWidgets.QLineEdit(self.get_tab)
        self.url_input_field.setGeometry(QtCore.QRect(349, 10, 231, 41))
        self.url_input_field.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.url_input_field.setObjectName("url_input_field")
        self.path_label = QtWidgets.QLabel(self.get_tab)
        self.path_label.setGeometry(QtCore.QRect(300, 70, 280, 41))
        self.path_label.setStyleSheet("font: 8pt \"Arial\";")
        self.path_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.path_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.path_label.setObjectName("path_label")
        self.path_input_field = QtWidgets.QLineEdit(self.get_tab)
        self.path_input_field.setGeometry(QtCore.QRect(349, 70, 231, 41))
        self.path_input_field.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.path_input_field.setObjectName("path_input_field")
        self.header_label = QtWidgets.QLabel(self.get_tab)
        self.header_label.setGeometry(QtCore.QRect(300, 130, 280, 41))
        self.header_label.setStyleSheet("font: 8pt \"Arial\";")
        self.header_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.header_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_label.setObjectName("header_label")
        self.header_input_field = QtWidgets.QLineEdit(self.get_tab)
        self.header_input_field.setGeometry(QtCore.QRect(349, 130, 231, 41))
        self.header_input_field.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.header_input_field.setObjectName("header_input_field")
        self.filter_label = QtWidgets.QLabel(self.get_tab)
        self.filter_label.setGeometry(QtCore.QRect(300, 190, 280, 41))
        self.filter_label.setStyleSheet("font: 8pt \"Arial\";")
        self.filter_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.filter_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.filter_label.setObjectName("filter_label")
        self.filter_input_field = QtWidgets.QLineEdit(self.get_tab)
        self.filter_input_field.setGeometry(QtCore.QRect(349, 190, 231, 41))
        self.filter_input_field.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";")
        self.filter_input_field.setObjectName("filter_input_field")
        self.send_btn = QtWidgets.QPushButton(self.get_tab)
        self.send_btn.setGeometry(QtCore.QRect(300, 250, 131, 31))
        self.send_btn.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.send_btn.setObjectName("send_btn")
        self.clear_btn = QtWidgets.QPushButton(self.get_tab)
        self.clear_btn.setGeometry(QtCore.QRect(450, 250, 131, 31))
        self.clear_btn.setStyleSheet("color: rgb(255, 255, 255);")
        self.clear_btn.setObjectName("clear_btn")
        self.post_tab.addTab(self.get_tab, "")
        self.post_tab1 = QtWidgets.QWidget()
        self.post_tab1.setStyleSheet("background-color: rgb(203, 203, 203);")
        self.post_tab1.setObjectName("post_tab1")
        self.post_tab.addTab(self.post_tab1, "")
        main_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_window)
        self.post_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "MainWindow"))
        self.label.setText(_translate("main_window", "Response:"))
        self.url_label.setText(_translate("main_window", " URL:"))
        self.path_label.setText(_translate("main_window", " Path:"))
        self.header_label.setText(_translate("main_window", "Header:"))
        self.filter_label.setText(_translate("main_window", " Filter:"))
        self.send_btn.setText(_translate("main_window", "SEND"))
        self.clear_btn.setText(_translate("main_window", "CLEAR"))
        self.post_tab.setTabText(self.post_tab.indexOf(self.get_tab), _translate("main_window", "GET"))
        self.post_tab.setTabText(self.post_tab.indexOf(self.post_tab1), _translate("main_window", "POST"))

    def get_pet_list(self):
        """"""

        url = str(self.url_input_field.text())
        path = str(self.path_input_field.text())
        token = str(self.header_input_field.text())
        filter = str(self.filter_input_field.text())

        headers = {'auth_key': token}
        filter = {'filter': filter}
        res = requests.get(url + path, headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text

        text =


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
