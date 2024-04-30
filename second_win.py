from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout, QLineEdit
from instr import *
from final_win import FinalWin
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont

class EXperiment():
    def __init__(self,age,test1,test2,test3):
        self.age=age
        self.test1=test1
        self.test2=test2
        self.test3=test3


class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()



    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)



    def initUI(self):
        self.button_next=QPushButton(txt_test_next)
        self.button_test1=QPushButton(txt_test_button1)
        self.button_test2=QPushButton(txt_test_button2)
        self.button_test3=QPushButton(txt_test_button3)


        self.text1=QLabel(txt_test1)
        self.text2=QLabel(txt_test2)
        self.text3=QLabel(txt_test3)
        self.text_timer=QLabel(txt_text_timer)
        self.test_name=QLabel(txt_test_name )
        self.test_years=QLabel(txt_test_years)

        self.line_name=QLineEdit(txt_line_name)
        self.line_years=QLineEdit(txt_line_years)
        self.line_test1=QLineEdit(txt_line_test1)
        self.line_test2=QLineEdit(txt_line_test2)
        self.line_test3=QLineEdit(txt_line_test3)
        

        self.lineV1=QVBoxLayout()
        self.lineV2=QVBoxLayout()
        self.lineH=QHBoxLayout()

        self.lineV2.addWidget(self.text_timer,alignment=Qt.AlignRight)
    
        self.lineV1.addWidget(self.test_name,alignment=Qt.AlignLeft)
        self.lineV1.addWidget(self.line_name,alignment=Qt.AlignLeft)
        self.lineV1.addWidget(self.test_years,alignment=Qt.AlignLeft)
        self.lineV1.addWidget(self.line_test1,alignment=Qt.AlignLeft)
        self.lineV1.addWidget(self.text1,alignment=Qt.AlignLeft)
        self.lineV1.addWidget(self.button_test1,alignment=Qt.AlignLeft)
        self.lineV1.addWidget(self.line_years,alignment=Qt.AlignLeft)
        self.lineV1.addWidget(self.text2,alignment=Qt.AlignLeft)
        self.lineV1.addWidget(self.button_test2,alignment=Qt.AlignLeft)
        self.lineV1.addWidget(self.text3,alignment=Qt.AlignLeft)
        self.lineV1.addWidget(self.button_test3,alignment=Qt.AlignLeft)
        self.lineV1.addWidget(self.line_test2,alignment=Qt.AlignLeft)
        self.lineV1.addWidget(self.line_test3,alignment=Qt.AlignLeft)
        self.lineV1.addWidget(self.button_next,alignment=Qt.AlignCenter)
        
        
        
        
        
        
        self.lineV1.addWidget(self.line_test2,alignment=Qt.AlignLeft)
        self.lineV1.addWidget(self.line_test3,alignment=Qt.AlignLeft)
        self.lineH.addLayout(self.lineV1)
        self.lineH.addLayout(self.lineV2)
        self.setLayout(self.lineH)

    def next_click(self):
        self.hide()
        self.exp= EXperiment(int(self.line_years.text()),self.line_test1.text(),self.line_test2.text(),self.line_test3.text())
        self.final=FinalWin(self.exp)
        


    def connects(self):
        self.button_next.clicked.connect(self.next_click)
        self.button_test1.clicked.connect(self.test_timer)
        self.button_test2.clicked.connect(self.test_timer2)
        self.button_test3.clicked.connect(self.test_timer3)

    def test_timer(self):
        global time
        time=QTime(0,0,15)
        self.timer=QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time=time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont('Times',36,QFont.Bold))
        self.text_timer.setStyleSheet('color:rgb(0,0,0)')
        if time.toString(('hh:mm:ss'))=='00:00:00':
            self.timer.stop()

    def test_timer2(self):
        global time
        time=QTime(0,0,30)
        self.timer=QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)


    def timer2Event(self):
        global time 
        time=time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss')[6:8])
        self.text_timer.setFont(QFont('Times',36,QFont.Bold))
        self.text_timer.setStyleSheet('color:rgb(0,0,0)')
        if time.toString(('hh:mm:ss'))== '00:00:00':
            self.timer.stop()

    def test_timer3(self):
        global time
        time=QTime(0,1,00)
        self.timer=QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
   
   
    def timer3Event(self):
        global time 
        time=time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont('Times',36,QFont.Bold))
        self.text_timer.setStyleSheet('color:rgb(168,228,160)')
        if int(time.toString(('hh:mm:ss')[6:8]))>=45:
            self.text_timer.setStyleSheet('color:rgb(168,228,160)')

        elif int(time.toString(('hh:mm:ss')[6:8]))<=15:
            self.text_timer.setStyleSheet('color:rgb(168,228,160)')
        
        else:
            self.text_timer.setStyleSheet('color:rgb(0,0,0)')

        if time.toString(('hh:mm:ss'))== '00:00:00':
            self.timer.stop()


        


    

    


    
















    
