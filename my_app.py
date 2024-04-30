from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout 
from instr import *
from second_win import TestWin

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()



    def initUI(self):
        self.hello_text=QLabel(txt_hello)
        self.instruction=QLabel(txt_instruction)
        self.button=QPushButton(txt_next,self)

        self.line=QVBoxLayout()
        self.line.addWidget(self.hello_text,alignment=Qt.AlignLeft)
        self.line.addWidget( self.instruction,alignment=Qt.AlignLeft)
        self.line.addWidget(self.button,alignment=Qt.AlignCenter)
        self.setLayout(self.line)
    
    def connects(self):
        self.button.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw=TestWin()
        
    
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)

app=QApplication([])
mw=MainWindow()
app.exec_()