import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from password import Ui_MainWindow
import random

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_generate.clicked.connect(self.generate)
    
    def generate(self):
        s_number = '0123456789'
        s_alphabet = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        pas = ''
        if self.ui.cb_numbers.isChecked():
            for i in range(30):
                pas = pas + random.choice(s_number)
        if self.ui.cb_alphabet.isChecked():
            for i in range(30):
                pas = pas + random.choice(s_alphabet)
        if self.ui.cb_numbers.isChecked() and self.ui.cb_alphabet.isChecked():
            for i in range(30):
                pas = pas + random.choice(s_number + s_alphabet)
        self.ui.result.setText(pas)

app = QApplication([])
ex = Widget()

ex.show()
app.exec_()
