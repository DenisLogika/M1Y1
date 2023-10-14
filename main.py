import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from password import Ui_MainWindow

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.password = Ui_MainWindow()
        self.password.setupUi(self)

def generation():
    digital = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

btn_OK.connect.clicked(generation)

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
