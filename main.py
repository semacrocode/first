from instr import *
from second import *

from PyQt5.QtCore import Qt,QTime,QTimer,QLocale
from PyQt5.QtGui import  QDoubleValidator,QIntValidator,QFont
from PyQt5.QtWidgets import (
    QApplication,QWidget,
    QHBoxLayout ,QVBoxLayout,QGridLayout,
    QGroupBox,QRadioButton,
    QPushButton,QLabel,QListWidget,QLineEdit)



class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()


    def set_appear(self):
        self.setWindowTitle('проверка сердца')
        self.resize(800,450)
        self.move(0,0)

    def initUI(self):
        self.hello_text = QLabel('Добро пожаловать в программу по определению состояния здоровья!')
        self.intruction = QLabel(txt_instruction)
        self.btn_next = QPushButton('Начать')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text,alignment=Qt.AlignLeft)
        self.layout.addWidget(self.intruction,alignment=Qt.AlignLeft)
        self.layout.addWidget(self.btn_next,alignment=Qt.AlignCenter)
        self.setLayout(self.layout)






    def next_click(self):
        self.tw = TestWin()
        self.hide()


    def connects(self):
        self.btn_next.clicked.connect(self.next_click)


    def set_appear(self):
        self.setWindowTitle(txt_instruction)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)



def main():
    app = QApplication([])
    mw = MainWin()
    app.exec_()
main()




