from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class MainWindow(qtw.QWidget):
    """Основной класс калькулятора"""

    def __init__(self):
        super().__init__()
        self.result_field = qtw.QLineEdit()
        self.result_field.setReadOnly(True)
        self.result_field.setStyleSheet("color: white;  background-color: black")
        self.setWindowTitle('Калькулятор')
        self.setLayout(qtw.QVBoxLayout())
        self.layout().addWidget(qtw.QWidget())
        self.keypad()
        self.temp_nums = []
        self.fin_nums = []
        self.show()

    def keypad(self):
        """Создание кнопок калькулятора и сетки для их размещения внутри MainWindow """

        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())
        container.setStyleSheet("color: black;  background-color: teal")
        # Create buttons objects
        btn_result = qtw.QPushButton('ВВОД', clicked=self.func_result)
        btn_clear = qtw.QPushButton('СБРОС', clicked=self.clear_calc)
        btn_9 = qtw.QPushButton('9', clicked=lambda: self.num_press('9'))
        btn_8 = qtw.QPushButton('8', clicked=lambda: self.num_press('8'))
        btn_7 = qtw.QPushButton('7', clicked=lambda: self.num_press('7'))
        btn_6 = qtw.QPushButton('6', clicked=lambda: self.num_press('6'))
        btn_5 = qtw.QPushButton('5', clicked=lambda: self.num_press('5'))
        btn_4 = qtw.QPushButton('4', clicked=lambda: self.num_press('4'))
        btn_3 = qtw.QPushButton('3', clicked=lambda: self.num_press('3'))
        btn_2 = qtw.QPushButton('2', clicked=lambda: self.num_press('2'))
        btn_1 = qtw.QPushButton('1', clicked=lambda: self.num_press('1'))
        btn_0 = qtw.QPushButton('0', clicked=lambda: self.num_press('0'))
        btn_plus = qtw.QPushButton('+', clicked=lambda: self.func_press('+'))
        btn_mins = qtw.QPushButton('-', clicked=lambda: self.func_press('-'))
        btn_mult = qtw.QPushButton('*', clicked=lambda: self.func_press('*'))
        btn_divd = qtw.QPushButton('÷', clicked=lambda: self.func_press('/'))

        # Adding buttons(widgets) to the layout
        container.layout().addWidget(self.result_field, 0, 0, 1, 4, )
        container.layout().addWidget(btn_result, 1, 0, 1, 2)
        container.layout().addWidget(btn_clear, 1, 2, 1, 2)
        container.layout().addWidget(btn_9, 2, 0)
        container.layout().addWidget(btn_8, 2, 1)
        container.layout().addWidget(btn_7, 2, 2)
        container.layout().addWidget(btn_plus, 2, 3)
        container.layout().addWidget(btn_6, 3, 0)
        container.layout().addWidget(btn_5, 3, 1)
        container.layout().addWidget(btn_4, 3, 2)
        container.layout().addWidget(btn_mins, 3, 3)
        container.layout().addWidget(btn_3, 4, 0)
        container.layout().addWidget(btn_2, 4, 1)
        container.layout().addWidget(btn_1, 4, 2)
        container.layout().addWidget(btn_mult, 4, 3)
        container.layout().addWidget(btn_0, 5, 0, 1, 3)
        container.layout().addWidget(btn_divd, 5, 3)
        self.layout().addWidget(container)

    def num_press(self, key_number):
        """Метод обработки числовых символов калькулятора"""

        self.temp_nums.append(key_number)  # добавление в список строкового значения числа, "указанного на кнопке"
        temp_string = ''.join(self.temp_nums)  # создание переменной содержащей одну объединенную строку из элементов
        # списка self.temp_nums
        if self.fin_nums:
            self.result_field.setText(''.join(self.fin_nums) + temp_string)
        else:
            self.result_field.setText(temp_string)

    def func_press(self, operator):
        """Метод обработки знаков операторов числовых выражений калькулятора"""

        temp_string = ''.join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append(operator)
        self.temp_nums = []
        self.result_field.setText(''.join(self.fin_nums))

    def func_result(self):
        """Метод для расчета результата числового выражения калькулятора"""

        fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
        result_string = eval(fin_string)
        fin_string += '='
        fin_string += str(result_string)
        self.result_field.setText(fin_string)

    def clear_calc(self):
        """Метод для очистки поля ввода калькулятора(удаляет из него все символы)"""

        self.result_field.clear()
        self.temp_nums = []
        self.fin_nums = []

#
# if __name__ == '__main__':
#     app = qtw.QApplication([])
#     mw = MainWindow()
#     app.setStyle(qtw.QStyleFactory.create("Fusion"))
#     app.exec_()
