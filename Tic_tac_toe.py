import os
import sys
import random as rd
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
os.system("cls")
class Tic_tac_toe(QMainWindow):
    check=False
    def __init__(self):
  
        super().__init__()
        self.setGeometry(40,450,800,450)
        self.setWindowTitle("X O o'yini")
        self.setFont(QFont("Calibri",22))
        self.setWindowIcon(QIcon("C:\\Users\\Asus Vivobook\\Downloads\\Tic_tac.ico"))

        self.lb1=QLabel("Player1 :",self)
        self.lb2=QLabel("Player2 :",self)
        self.lb3=QLabel(self)
        self.lb3.setFont(QFont("Calibri",22))
        self.lb3.setVisible(False)

        self.lb1.setGeometry(400,30,130,50)
        self.lb2.setGeometry(400,80,130,50)

        self.qb1=QCheckBox(self)
        self.qb2=QCheckBox(self)

        self.qb1.setGeometry(700,40,30,30)
        self.qb2.setGeometry(700,100,30,30)
        self.qb1.setFont(QFont("Calibri",28))
        self.qb2.setFont(QFont("Calibri",28))


        self.ln1=QLineEdit(self)
        self.ln2=QLineEdit(self)

        self.ln1.setGeometry(550,40,140,40)
        self.ln1.setAlignment(Qt.AlignCenter)
        self.ln2.setGeometry(550,100,140,40)
        self.ln2.setAlignment(Qt.AlignCenter)

        self.btn1=QPushButton(" With Computer",self)
        self.btn2=QPushButton("New game",self)
        self.btn3=QPushButton(" Start game ",self)
        self.btn4=QPushButton(" Start game ",self)

        self.btn1.setGeometry(450,150,250,50)
        self.btn1.setStyleSheet('''
                            background-color:blue;
                            color: yellow;
                            border-radius: solid;
                            border-radius: 15px;
                                ''')
        self.btn2.setGeometry(470,210,200,50)
        self.btn2.setStyleSheet('''
                            background-color:blue;
                            color: yellow;
                            border-radius: solid;
                            border-radius: 15px;
                                ''')
        self.btn3.setGeometry(470,270,200,50)
        self.btn3.setStyleSheet('''
                            background-color:blue;
                            color: yellow;
                            border-radius: solid;
                            border-radius: 15px;
                                ''')
        self.btn4.setGeometry(470,270,200,50)
        self.btn4.setStyleSheet('''
                            background-color:blue;
                            color: yellow;
                            border-radius: solid;
                            border-radius: 15px;
                                ''')
        self.btn4.setVisible(False)
        self.lb3.setGeometry(200,330,800,50)
        self.b1=QPushButton("",self)
        self.b2=QPushButton("",self)
        self.b3=QPushButton("",self)
        self.b4=QPushButton("",self)
        self.b5=QPushButton("",self)
        self.b6=QPushButton("",self)
        self.b7=QPushButton("",self)
        self.b8=QPushButton("",self)
        self.b9=QPushButton("",self)

        self.ls=[self.b1,self.b2,self.b3,self.b4,self.b5,self.b6,self.b7,self.b8,self.b9]

        self.b1.setVisible(False)
        self.b2.setVisible(False)
        self.b3.setVisible(False)
        self.b4.setVisible(False)
        self.b5.setVisible(False)
        self.b6.setVisible(False)
        self.b7.setVisible(False)
        self.b8.setVisible(False)
        self.b9.setVisible(False)

        self.b1.setGeometry(0,0,100,100)
        self.b2.setGeometry(100,0,100,100)
        self.b3.setGeometry(200,0,100,100)
        
        self.b4.setGeometry(0,100,100,100)
        self.b5.setGeometry(100,100,100,100)
        self.b6.setGeometry(200,100,100,100)

        self.b7.setGeometry(0,200,100,100)
        self.b8.setGeometry(100,200,100,100)
        self.b9.setGeometry(200,200,100,100)

        self.b1.setStyleSheet("background-color:blue;")
        self.b2.setStyleSheet("background-color:blue;")
        self.b3.setStyleSheet("background-color:blue;")
        self.b4.setStyleSheet("background-color:blue;")
        self.b5.setStyleSheet("background-color:blue;")
        self.b6.setStyleSheet("background-color:blue;")
        self.b7.setStyleSheet("background-color:blue;")
        self.b8.setStyleSheet("background-color:blue;")
        self.b9.setStyleSheet("background-color:blue;")

        self.btn1.clicked.connect(self.computer_game)
        self.btn2.clicked.connect(self.reverse)
        self.btn3.clicked.connect(self.start)
    def reverse(self):
        self.wn=Tic_tac_toe()
        self.wn.check=False
        self.wn.show()
        self.hide()
    def start(self):
        if ((self.qb1.isChecked()==False) or (self.qb2.isChecked()==False)):
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("O'yin boshlashda xatolik qildingiz!!!")
            msg.setIcon(QMessageBox.Critical)
            msg.show()    
            self.b1.setVisible(False)
            self.b2.setVisible(False)
            self.b3.setVisible(False)
            self.b4.setVisible(False)
            self.b5.setVisible(False)
            self.b6.setVisible(False)
            self.b7.setVisible(False)
            self.b8.setVisible(False)
            self.b9.setVisible(False)
        else:
            self.b1.setVisible(True)
            self.b2.setVisible(True)
            self.b3.setVisible(True)
            self.b4.setVisible(True)
            self.b5.setVisible(True)
            self.b6.setVisible(True)
            self.b7.setVisible(True)
            self.b8.setVisible(True)
            self.b9.setVisible(True)

            self.ls=[self.b1,self.b2,self.b3,self.b4,self.b5,self.b6,self.b7,self.b8,self.b9]

            self.b1.clicked.connect(self.change_btn1)
            self.b2.clicked.connect(self.change_btn2)
            self.b3.clicked.connect(self.change_btn3)
            self.b4.clicked.connect(self.change_btn4)
            self.b5.clicked.connect(self.change_btn5)
            self.b6.clicked.connect(self.change_btn6)
            self.b7.clicked.connect(self.change_btn7)
            self.b8.clicked.connect(self.change_btn8)
            self.b9.clicked.connect(self.change_btn9)
    def computer_game(self):
        self.lb2.setVisible(False)
        self.ln2.setVisible(False)
        self.qb2.setVisible(False)
        self.btn3.setVisible(False)
        self.btn4.setVisible(True)
        self.btn4.clicked.connect(self.start_for_computer)
    def start_for_computer(self):
        if self.qb1.isChecked():
            self.b1.setVisible(True)
            self.b2.setVisible(True)
            self.b3.setVisible(True)
            self.b4.setVisible(True)
            self.b5.setVisible(True)
            self.b6.setVisible(True)
            self.b7.setVisible(True)
            self.b8.setVisible(True)
            self.b9.setVisible(True)


        
            self.b1.clicked.connect(self.comp_1)
            self.b2.clicked.connect(self.comp_2)
            self.b3.clicked.connect(self.comp_3)
            self.b4.clicked.connect(self.comp_4)
            self.b5.clicked.connect(self.comp_5)
            self.b6.clicked.connect(self.comp_6)
            self.b7.clicked.connect(self.comp_7)
            self.b8.clicked.connect(self.comp_8)
            self.b9.clicked.connect(self.comp_9)
      

        else:
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("O'yin boshlashda xatolik qildingiz!!!")
            msg.setIcon(QMessageBox.Critical)
            msg.show()

    def comp_1(self):
        if self.b1.text()=="" and Tic_tac_toe.check==False:
            self.b1.setFont(QFont("Consolas",32))
            self.b1.setStyleSheet("background-color: blue;color: rgb(0,49,83);")
            self.b1.setText("X")
            Tic_tac_toe.check_buttons_for_computer(self)
            Tic_tac_toe.check=True
        else:   
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Xato qildingiz!!!")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
        Tic_tac_toe.for_computer(self)

    def comp_2(self):
        if self.b2.text()=="" and Tic_tac_toe.check==False:
            self.b2.setFont(QFont("Consolas",32))
            self.b2.setStyleSheet("background-color: blue;color: rgb(0,49,83);")
            self.b2.setText("X")
            Tic_tac_toe.check_buttons_for_computer(self)
            Tic_tac_toe.check=True
        else:   
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Xato qildingiz!!!")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
        Tic_tac_toe.for_computer(self)
    def comp_3(self):
        if self.b3.text()=="" and Tic_tac_toe.check==False:
            self.b3.setFont(QFont("Consolas",32))
            self.b3.setStyleSheet("background-color: blue;color: rgb(0,49,83);")
            self.b3.setText("X")
            Tic_tac_toe.check_buttons_for_computer(self)
            Tic_tac_toe.check=True
        else:   
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Xato qildingiz!!!")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
        Tic_tac_toe.for_computer(self)
    def comp_4(self):
        if self.b4.text()=="" and Tic_tac_toe.check==False:
            self.b4.setFont(QFont("Consolas",32))
            self.b4.setStyleSheet("background-color: blue;color: rgb(0,49,83);")
            self.b4.setText("X")
            Tic_tac_toe.check_buttons_for_computer(self)
            Tic_tac_toe.check=True
        else:   
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Xato qildingiz!!!")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
        Tic_tac_toe.for_computer(self)
    def comp_5(self):
        if self.b5.text()=="" and Tic_tac_toe.check==False:
            self.b5.setFont(QFont("Consolas",32))
            self.b5.setStyleSheet("background-color: blue;color: rgb(0,49,83);")
            self.b5.setText("X")
            Tic_tac_toe.check_buttons_for_computer(self)
            Tic_tac_toe.check=True
        else:   
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Xato qildingiz!!!")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
        Tic_tac_toe.for_computer(self)
    def comp_6(self):
        if self.b6.text()=="" and Tic_tac_toe.check==False:
            self.b6.setFont(QFont("Consolas",32))
            self.b6.setStyleSheet("background-color: blue;color: rgb(0,49,83);")
            self.b6.setText("X")
            Tic_tac_toe.check_buttons_for_computer(self)
            Tic_tac_toe.check=True
        else:   
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Xato qildingiz!!!")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
        Tic_tac_toe.for_computer(self)
    def comp_7(self):
        if self.b7.text()=="" and Tic_tac_toe.check==False:
            self.b7.setFont(QFont("Consolas",32))
            self.b7.setStyleSheet("background-color: blue;color: rgb(0,49,83);")
            self.b7.setText("X")
            Tic_tac_toe.check_buttons_for_computer(self)
            Tic_tac_toe.check=True
        else:   
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Xato qildingiz!!!")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
        Tic_tac_toe.for_computer(self)
    def comp_8(self):
        if self.b8.text()=="" and Tic_tac_toe.check==False:
            self.b8.setFont(QFont("Consolas",32))
            self.b8.setStyleSheet("background-color: blue;color: rgb(0,49,83);")
            self.b8.setText("X")
            Tic_tac_toe.check_buttons_for_computer(self)
            Tic_tac_toe.check=True
        else:   
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Xato qildingiz!!!")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
        Tic_tac_toe.for_computer(self)
    def comp_9(self):
        if self.b9.text()=="" and Tic_tac_toe.check==False:
            self.b9.setFont(QFont("Consolas",32))
            self.b9.setStyleSheet("background-color: blue;color: rgb(0,49,83);")
            self.b9.setText("X")
            Tic_tac_toe.check_buttons_for_computer(self)
            Tic_tac_toe.check=True
        else:   
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Xato qildingiz!!!")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
        Tic_tac_toe.for_computer(self)

    def for_computer(self):
        chk=True
        kk=None
        while chk==True:
            kk=rd.choice(self.ls)
            if kk.text()=="":
                kk.setStyleSheet("background-color: blue;color: red;")
                kk.setFont(QFont("Consolas",32))
                kk.setText("O")
                Tic_tac_toe.check_buttons_for_computer(self)
                Tic_tac_toe.check=False
                chk=False
    def check_buttons_for_computer(self):
         if (self.b1.text()=="X"and self.b2.text()=="X" and self.b3.text()=="X")or (self.b1.text()=="X" and self.b4.text()=="X" and self.b7.text()=="X")or(self.b1.text()=="X" and self.b5.text()=="X" and self.b9.text()=="X")or(self.b4.text()=="X" and self.b5.text()=="X" and self.b6.text()=="X")or(self.b7.text()=="X" and self.b8.text()=="X" and self.b9.text()=="X")or(self.b3.text()=="X" and self.b6.text()=="X" and self.b9.text()=="X"):
            self.lb3.setText(f"O'yin Tugadi! G'olib:{self.ln1.text()} nomli o'yinchi")
            self.lb3.setVisible(True)
            return
         elif(self.b1.text()=="O"and self.b2.text()=="O" and self.b3.text()=="O")or (self.b1.text()=="O" and self.b4.text()=="O" and self.b7.text()=="O")or(self.b1.text()=="O" and self.b5.text()=="O" and self.b9.text()=="O")or(self.b4.text()=="O" and self.b5.text()=="O" and self.b6.text()=="O")or(self.b7.text()=="O" and self.b8.text()=="O" and self.b9.text()=="O")or(self.b3.text()=="O" and self.b6.text()=="O" and self.b9.text()=="O"):
                self.lb3.setText(f"O'yin Tugadi! G'olib:Kompyuter !!!")
                self.lb3.setVisible(True)
                return
    def change_btn1(self):
        if self.b1.text()=="" and Tic_tac_toe.check==False:
            self.b1.setFont(QFont("Consolas",32))
            self.b1.setStyleSheet("background-color: blue;color: rgb(0,49,83);")
            self.b1.setText("X")
            Tic_tac_toe.check_buttons(self)
            Tic_tac_toe.check=True
        elif self.b1.text()=="" and Tic_tac_toe.check==True:
            self.b1.setFont(QFont("Consolas",32))
            self.b1.setStyleSheet("background-color: blue;color: red;")
            self.b1.setText("O")
            Tic_tac_toe.check_buttons(self)
            Tic_tac_toe.check=False
        else:
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Xato qildingiz!!!")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
    def change_btn2(self):
        if self.b2.text()=="" and Tic_tac_toe.check==False:
            self.b2.setFont(QFont("Consolas",32))
            self.b2.setStyleSheet("background-color: blue;color: rgb(0,49,83);")
            self.b2.setText("X")
            Tic_tac_toe.check_buttons(self)
            Tic_tac_toe.check=True
        elif self.b2.text()=="" and Tic_tac_toe.check==True:
            self.b2.setFont(QFont("Consolas",32))
            self.b2.setStyleSheet("background-color: blue;color: red;")
            self.b2.setText("O")
            Tic_tac_toe.check_buttons(self)
            Tic_tac_toe.check=False
        else:
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Xato qildingiz!!!")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
    def change_btn3(self):
        if self.b3.text()=="" and Tic_tac_toe.check==False:
            self.b3.setFont(QFont("Consolas",32))
            self.b3.setStyleSheet("background-color: blue;color: rgb(0,49,83);")
            self.b3.setText("X")
            Tic_tac_toe.check_buttons(self)
            Tic_tac_toe.check=True
        elif self.b3.text()=="" and Tic_tac_toe.check==True:
            self.b3.setFont(QFont("Consolas",32))
            self.b3.setStyleSheet("background-color: blue;color: red;")
            self.b3.setText("O")
            Tic_tac_toe.check_buttons(self)
            Tic_tac_toe.check=False
        else:
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Xato qildingiz!!!")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
    def change_btn4(self):
        if self.b4.text()=="" and Tic_tac_toe.check==False:
            self.b4.setFont(QFont("Consolas",32))
            self.b4.setStyleSheet("background-color: blue;color: rgb(0,49,83);")
            self.b4.setText("X")
            Tic_tac_toe.check_buttons(self)
            Tic_tac_toe.check=True
        elif self.b4.text()=="" and Tic_tac_toe.check==True:
            self.b4.setFont(QFont("Consolas",32))
            self.b4.setStyleSheet("background-color: blue;color: red;")
            self.b4.setText("O")
            Tic_tac_toe.check_buttons(self)
            Tic_tac_toe.check=False
        else:
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Xato qildingiz!!!")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
    def change_btn5(self):
        if self.b5.text()=="" and Tic_tac_toe.check==False:
            self.b5.setFont(QFont("Consolas",32))
            self.b5.setStyleSheet("background-color: blue;color: rgb(0,49,83);")
            self.b5.setText("X")
            Tic_tac_toe.check_buttons(self)
            Tic_tac_toe.check=True
        elif self.b5.text()=="" and Tic_tac_toe.check==True:
            self.b5.setFont(QFont("Consolas",32))
            self.b5.setStyleSheet("background-color: blue;color: red;")
            self.b5.setText("O")
            Tic_tac_toe.check_buttons(self)
            Tic_tac_toe.check=False
        else:
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Xato qildingiz!!!")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
    def change_btn6(self):
        if self.b6.text()=="" and Tic_tac_toe.check==False:
            self.b6.setFont(QFont("Consolas",32))
            self.b6.setStyleSheet("background-color: blue;color: rgb(0,49,83);")
            self.b6.setText("X")
            Tic_tac_toe.check_buttons(self)
            Tic_tac_toe.check=True
        elif self.b6.text()=="" and Tic_tac_toe.check==True:
            self.b6.setFont(QFont("Consolas",32))
            self.b6.setStyleSheet("background-color: blue;color: red;")
            self.b6.setText("O")
            Tic_tac_toe.check_buttons(self)
            Tic_tac_toe.check=False
        else:
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Xato qildingiz!!!")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
    def change_btn7(self):
        if self.b7.text()=="" and Tic_tac_toe.check==False:
            self.b7.setFont(QFont("Consolas",32))
            self.b7.setStyleSheet("background-color: blue;color: rgb(0,49,83);")
            self.b7.setText("X")
            Tic_tac_toe.check_buttons(self)
            Tic_tac_toe.check=True
        elif self.b7.text()=="" and Tic_tac_toe.check==True:
            self.b7.setFont(QFont("Consolas",32))
            self.b7.setStyleSheet("background-color: blue;color: red;")
            self.b7.setText("O")
            Tic_tac_toe.check_buttons(self)
            Tic_tac_toe.check=False
        else:
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Xato qildingiz!!!")
            msg.setIcon(QMessageBox.Critical)
            msg.show()

    def change_btn8(self):
        if self.b8.text()=="" and Tic_tac_toe.check==False:
            self.b8.setFont(QFont("Consolas",32))
            self.b8.setStyleSheet("background-color: blue;color: rgb(0,49,83);")
            self.b8.setText("X")
            Tic_tac_toe.check_buttons(self)
            Tic_tac_toe.check=True
        elif self.b8.text()=="" and Tic_tac_toe.check==True:
            self.b8.setFont(QFont("Consolas",32))
            self.b8.setStyleSheet("background-color: blue;color: red;")
            self.b8.setText("O")
            Tic_tac_toe.check_buttons(self)
            Tic_tac_toe.check=False
        else:
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Xato qildingiz!!!")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
    def change_btn9(self):
        if self.b9.text()=="" and Tic_tac_toe.check==False:
            self.b9.setFont(QFont("Consolas",32))
            self.b9.setStyleSheet("background-color: blue;color: rgb(0,49,83);")
            self.b9.setText("X")
            Tic_tac_toe.check_buttons(self)
            Tic_tac_toe.check=True
        elif self.b9.text()=="" and Tic_tac_toe.check==True:
            self.b9.setFont(QFont("Consolas",32))
            self.b9.setStyleSheet("background-color: blue;color: red;")
            self.b9.setText("O")
            Tic_tac_toe.check_buttons(self)
            Tic_tac_toe.check=False
        else:
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Xato qildingiz!!!")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
    def check_buttons(self):
        if (self.b1.text()=="X"and self.b2.text()=="X" and self.b3.text()=="X")or (self.b1.text()=="X" and self.b4.text()=="X" and self.b7.text()=="X")or(self.b1.text()=="X" and self.b5.text()=="X" and self.b9.text()=="X")or(self.b4.text()=="X" and self.b5.text()=="X" and self.b6.text()=="X")or(self.b7.text()=="X" and self.b8.text()=="X" and self.b9.text()=="X")or(self.b3.text()=="X" and self.b6.text()=="X" and self.b9.text()=="X"):
            self.lb3.setText(f"O'yin Tugadi! G'olib:{self.ln1.text()} nomli o'yinchi")
            self.lb3.setVisible(True)
            return
           
        elif(self.b1.text()=="O"and self.b2.text()=="O" and self.b3.text()=="O")or (self.b1.text()=="O" and self.b4.text()=="O" and self.b7.text()=="O")or(self.b1.text()=="O" and self.b5.text()=="O" and self.b9.text()=="O")or(self.b4.text()=="O" and self.b5.text()=="O" and self.b6.text()=="O")or(self.b7.text()=="O" and self.b8.text()=="O" and self.b9.text()=="O")or(self.b3.text()=="O" and self.b6.text()=="O" and self.b9.text()=="O"):
            self.lb3.setText(f"O'yin Tugadi! G'olib:{self.ln2.text()} nomli o'yinchi")
            self.lb3.setVisible(True)
            return
if __name__=="__main__":
    app=QApplication(sys.argv)
    mn=Tic_tac_toe()
    mn.show()
    sys.exit(app.exec_())
