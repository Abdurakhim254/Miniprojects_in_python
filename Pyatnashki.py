import os
import random
os.system("cls")
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class pyatnashki(QMainWindow):
    numbers = []
    urinish = 0
    
    def __init__(self):
        super().__init__()
        self.setGeometry(250,100,1000,600)
        self.setMaximumSize(1000,600)
        self.setMinimumSize(1000,600)
        self.setWindowIcon(QIcon("C:/Users/User/Downloads/pyatnashki.ico"))
        self.setWindowTitle("Bekorsozlikdan o'yin yaratdim")
        
        self.btn1 = QPushButton("1",self)
        self.btn1.setGeometry(50,50,100,100)
        self.btn1.setFont(QFont("Poor Richard",45))
        self.btn1.setStyleSheet("background-color: rgb(0,20,168); color: rgb(0,255,0)")
        self.btn1.clicked.connect(self.btn1_click)
        
        self.btn2 = QPushButton("2",self)
        self.btn2.setGeometry(152,50,100,100)
        self.btn2.setFont(QFont("Poor Richard",45))
        self.btn2.setStyleSheet("background-color: rgb(0,20,168); color: rgb(0,255,0)")
        self.btn2.clicked.connect(self.btn2_click)
        
        self.btn3 = QPushButton("3",self)
        self.btn3.setGeometry(254,50,100,100)
        self.btn3.setFont(QFont("Poor Richard",45))
        self.btn3.setStyleSheet("background-color: rgb(0,20,168); color: rgb(0,255,0)")
        self.btn3.clicked.connect(self.btn3_click)
        
        self.btn4 = QPushButton("4",self)
        self.btn4.setGeometry(356,50,100,100)
        self.btn4.setFont(QFont("Poor Richard",45))
        self.btn4.setStyleSheet("background-color: rgb(0,20,168); color: rgb(0,255,0)")
        self.btn4.clicked.connect(self.btn4_click)
  
        self.btn5 = QPushButton("5",self)
        self.btn5.setGeometry(50,152,100,100)
        self.btn5.setFont(QFont("Poor Richard",45))
        self.btn5.setStyleSheet("background-color: rgb(0,20,168); color: rgb(0,255,0)")
        self.btn5.clicked.connect(self.btn5_click)
        
        self.btn6 = QPushButton("6",self)
        self.btn6.setGeometry(152,152,100,100)
        self.btn6.setFont(QFont("Poor Richard",45))
        self.btn6.setStyleSheet("background-color: rgb(0,20,168); color: rgb(0,255,0)")
        self.btn6.clicked.connect(self.btn6_click)
        
        self.btn7 = QPushButton("7",self)
        self.btn7.setGeometry(254,152,100,100)
        self.btn7.setFont(QFont("Poor Richard",45))
        self.btn7.setStyleSheet("background-color: rgb(0,20,168); color: rgb(0,255,0)")
        self.btn7.clicked.connect(self.btn7_click)
        
        self.btn8 = QPushButton("8",self)
        self.btn8.setGeometry(356,152,100,100)
        self.btn8.setFont(QFont("Poor Richard",45))
        self.btn8.setStyleSheet("background-color: rgb(0,20,168); color: rgb(0,255,0)")
        self.btn8.clicked.connect(self.btn8_click)
          
        self.btn9 = QPushButton("9",self)
        self.btn9.setGeometry(50,254,100,100)
        self.btn9.setFont(QFont("Poor Richard",45))
        self.btn9.setStyleSheet("background-color: rgb(0,20,168); color: rgb(0,255,0)")
        self.btn9.clicked.connect(self.btn9_click)
        
        self.btn10 = QPushButton("10",self)
        self.btn10.setGeometry(152,254,100,100)
        self.btn10.setFont(QFont("Poor Richard",45))
        self.btn10.setStyleSheet("background-color: rgb(0,20,168); color: rgb(0,255,0)")
        self.btn10.clicked.connect(self.btn10_click)
        
        self.btn11 = QPushButton("11",self)
        self.btn11.setGeometry(254,254,100,100)
        self.btn11.setFont(QFont("Poor Richard",45))
        self.btn11.setStyleSheet("background-color: rgb(0,20,168); color: rgb(0,255,0)")
        self.btn11.clicked.connect(self.btn11_click)
        
        self.btn12 = QPushButton("12",self)
        self.btn12.setGeometry(356,254,100,100)
        self.btn12.setFont(QFont("Poor Richard",45))
        self.btn12.setStyleSheet("background-color: rgb(0,20,168); color: rgb(0,255,0)")
        self.btn12.clicked.connect(self.btn12_click)

        self.btn13 = QPushButton("13",self)
        self.btn13.setGeometry(50,356,100,100)
        self.btn13.setFont(QFont("Poor Richard",45))
        self.btn13.setStyleSheet("background-color: rgb(0,20,168); color: rgb(0,255,0)")
        self.btn13.clicked.connect(self.btn13_click)
        
        self.btn14 = QPushButton("14",self)
        self.btn14.setGeometry(152,356,100,100)
        self.btn14.setFont(QFont("Poor Richard",45))
        self.btn14.setStyleSheet("background-color: rgb(0,20,168); color: rgb(0,255,0)")
        self.btn14.clicked.connect(self.btn14_click)
        
        self.btn15 = QPushButton("15",self)
        self.btn15.setGeometry(254,356,100,100)
        self.btn15.setFont(QFont("Poor Richard",45))
        self.btn15.setStyleSheet("background-color: rgb(0,20,168); color: rgb(0,255,0)")
        self.btn15.clicked.connect(self.btn15_click)
        
        self.btn16 = QPushButton("",self)
        self.btn16.setGeometry(356,356,100,100)
        self.btn16.setFont(QFont("Poor Richard",45))
        self.btn16.setStyleSheet("background-color: rgb(0,20,168); color: rgb(0,255,0)")
        self.btn16.clicked.connect(self.btn16_click)

        self.ls1 = [self.btn1,self.btn2,self.btn3,self.btn4,
                    self.btn5,self.btn6,self.btn7,self.btn8,
                    self.btn9,self.btn10,self.btn11,self.btn12,
                    self.btn13,self.btn14,self.btn15]
        
        self.tablo1 = QLabel("Urinishlar soni <<< ",self)
        self.tablo1.setGeometry(500,225,300,50)
        self.tablo1.setFont(QFont("Calibri",22))
        self.tablo1.setStyleSheet("color: red;")
        
        self.tablo2 = QSpinBox(self)
        self.tablo2.setGeometry(805,225,150,50)
        self.tablo2.setStyleSheet("color: rgb(0,255,0); background-color: rgb(0,0,0);")
        self.tablo2.setFont(QFont("Consolas",24))
        self.tablo2.setMaximum(999)
        self.tablo2.setEnabled(False)
        
        self.new_game()
        
    
    def btn15_click(self):
        pyatnashki.urinish += 1
        if self.btn14.text() == "":
            self.btn14.setText(self.btn15.text())
            self.btn15.setText("")
        elif self.btn11.text() == "":
            self.btn11.setText(self.btn15.text())
            self.btn15.setText("")
        elif self.btn16.text() == "":
            self.btn16.setText(self.btn15.text())
            self.btn15.setText("")
        else:
            pyatnashki.urinish -= 1
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Siljitishni iloji nes")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
        
        self.tablo2.setValue(pyatnashki.urinish)
        self.check_game()
    
    def btn2_click(self):
        pyatnashki.urinish += 1
        if self.btn1.text() == "":
            self.btn1.setText(self.btn2.text())
            self.btn2.setText("")
        elif self.btn3.text() == "":
            self.btn3.setText(self.btn2.text())
            self.btn2.setText("")
        elif self.btn6.text() == "":
            self.btn6.setText(self.btn2.text())
            self.btn2.setText("")
        else:
            pyatnashki.urinish -= 1
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Siljitishni iloji nes")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
        
        self.tablo2.setValue(pyatnashki.urinish)
        self.check_game()
    
    def btn3_click(self):
        pyatnashki.urinish += 1
        if self.btn2.text() == "":
            self.btn2.setText(self.btn3.text())
            self.btn3.setText("")
        elif self.btn4.text() == "":
            self.btn4.setText(self.btn3.text())
            self.btn3.setText("")
        elif self.btn7.text() == "":
            self.btn7.setText(self.btn3.text())
            self.btn3.setText("")
        else:
            pyatnashki.urinish -= 1
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Siljitishni iloji nes")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
        
        self.tablo2.setValue(pyatnashki.urinish)
        self.check_game()
    
    def btn5_click(self):
        pyatnashki.urinish += 1
        if self.btn1.text() == "":
            self.btn1.setText(self.btn5.text())
            self.btn5.setText("")
        elif self.btn6.text() == "":
            self.btn6.setText(self.btn5.text())
            self.btn5.setText("")
        elif self.btn9.text() == "":
            self.btn9.setText(self.btn5.text())
            self.btn5.setText("")
        else:
            pyatnashki.urinish -= 1
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Siljitishni iloji nes")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
        
        self.tablo2.setValue(pyatnashki.urinish)
        self.check_game()
    
    def btn8_click(self):
        pyatnashki.urinish += 1
        if self.btn4.text() == "":
            self.btn4.setText(self.btn8.text())
            self.btn8.setText("")
        elif self.btn7.text() == "":
            self.btn7.setText(self.btn8.text())
            self.btn8.setText("")
        elif self.btn12.text() == "":
            self.btn12.setText(self.btn8.text())
            self.btn8.setText("")
        else:
            pyatnashki.urinish -= 1
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Siljitishni iloji nes")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
        
        self.tablo2.setValue(pyatnashki.urinish)
        self.check_game()
    
    def btn9_click(self):
        pyatnashki.urinish += 1
        if self.btn5.text() == "":
            self.btn5.setText(self.btn9.text())
            self.btn9.setText("")
        elif self.btn10.text() == "":
            self.btn10.setText(self.btn9.text())
            self.btn9.setText("")
        elif self.btn13.text() == "":
            self.btn13.setText(self.btn9.text())
            self.btn9.setText("")
        else:
            pyatnashki.urinish -= 1
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Siljitishni iloji nes")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
        
        self.tablo2.setValue(pyatnashki.urinish)
        self.check_game()
    
    def btn12_click(self):
        pyatnashki.urinish += 1
        if self.btn11.text() == "":
            self.btn11.setText(self.btn12.text())
            self.btn12.setText("")
        elif self.btn8.text() == "":
            self.btn8.setText(self.btn12.text())
            self.btn12.setText("")
        elif self.btn16.text() == "":
            self.btn16.setText(self.btn12.text())
            self.btn12.setText("")
        else:
            pyatnashki.urinish -= 1
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Siljitishni iloji nes")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
        
        self.tablo2.setValue(pyatnashki.urinish)
        self.check_game()
        
    def btn14_click(self):
        pyatnashki.urinish += 1
        if self.btn13.text() == "":
            self.btn13.setText(self.btn14.text())
            self.btn14.setText("")
        elif self.btn10.text() == "":
            self.btn10.setText(self.btn14.text())
            self.btn14.setText("")
        elif self.btn15.text() == "":
            self.btn15.setText(self.btn14.text())
            self.btn14.setText("")
        else:
            pyatnashki.urinish -= 1
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Siljitishni iloji nes")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
        
        self.tablo2.setValue(pyatnashki.urinish)
        self.check_game()
        
    def btn1_click(self):
        pyatnashki.urinish += 1
        if self.btn2.text() == "":
            self.btn2.setText(self.btn1.text())
            self.btn1.setText("")
        elif self.btn5.text() == "":
            self.btn5.setText(self.btn1.text())
            self.btn1.setText("")
        else:
            pyatnashki.urinish -= 1
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Siljitishni iloji nes")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
        
        self.tablo2.setValue(pyatnashki.urinish)
        self.check_game()
        
    def btn6_click(self):
        pyatnashki.urinish+=1
        if self.btn5.text()=="":
            self.btn5.setText(self.btn6.text())
            self.btn6.setText("")
        elif self.btn2.text()=="":
            self.btn2.setText(self.btn6.text())
            self.btn6.setText("")
        elif self.btn7.text()=="":
            self.btn7.setText(self.btn6.text())
            self.btn6.setText("")
        elif self.btn10.text()=="":
            self.btn10.setText(self.btn6.text())
            self.btn6.setText("")
        else:
            pyatnashki.urinish -= 1
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Siljitishni iloji nes")
            msg.setIcon(QMessageBox.Critical)
            msg.show()   
    def btn7_click(self):
        pyatnashki.urinish+=1
        if self.btn6.text()=="":
            self.btn6.setText(self.btn7.text())
            self.btn7.setText("")
        elif self.btn3.text()=="":
            self.btn3.setText(self.btn7.text())
            self.btn7.setText("")
        elif self.btn8.text()=="":
            self.btn8.setText(self.btn7.text())
            self.btn7.setText("")
        elif self.btn11.text()=="":
            self.btn11.setText(self.btn7.text())
            self.btn7.setText("")  
        else:
            pyatnashki.urinish -= 1
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Siljitishni iloji nes")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
    def  btn10_click(self):
        pyatnashki.urinish+=1
        if self.btn11.text()=="":
            self.btn11.setText(self.btn10.text())
            self.btn10.setText("")
        elif self.btn9.text()=="":
            self.btn9.setText(self.btn10.text())
            self.btn10.setText("")
        elif self.btn6.text()=="":
            self.btn6.setText(self.btn10.text())
            self.btn10.setText("")
        elif self.btn14.text()=="":
            self.btn14.setText(self.btn10.text())
            self.btn10.setText("")
        else:
            pyatnashki.urinish -= 1
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Siljitishni iloji nes")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
    
    def btn11_click(self):
        pyatnashki.urinish+=1
        if self.btn10.text()=="":
            self.btn10.setText(self.btn11.text())
            self.btn11.setText("")
        elif self.btn12.text()=="":
            self.btn12.setText(self.btn11.text())
            self.btn11.setText("")
        elif self.btn7.text()=="":
            self.btn7.setText(self.btn11.text())
            self.btn11.setText("")
        elif self.btn15.text()=="":
            self.btn15.setText(self.btn11.text())
            self.btn11.setText("")
        else:
            pyatnashki.urinish -= 1
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Siljitishni iloji nes")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
    def btn4_click(self):
        pyatnashki.urinish += 1
        if self.btn3.text() == "":
            self.btn3.setText(self.btn4.text())
            self.btn4.setText("")
        elif self.btn8.text() == "":
            self.btn8.setText(self.btn4.text())
            self.btn4.setText("")
        else:
            pyatnashki.urinish -= 1
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Siljitishni iloji nes")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
        
        self.tablo2.setValue(pyatnashki.urinish)
        self.check_game()
    
    def btn13_click(self):
        pyatnashki.urinish += 1
        if self.btn9.text() == "":
            self.btn9.setText(self.btn13.text())
            self.btn13.setText("")
        elif self.btn14.text() == "":
            self.btn14.setText(self.btn13.text())
            self.btn13.setText("")
        else:
            pyatnashki.urinish -= 1
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Siljitishni iloji nes")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
        
        self.tablo2.setValue(pyatnashki.urinish)
        self.check_game()
    
    def btn16_click(self):
        pyatnashki.urinish += 1
        if self.btn12.text() == "":
            self.btn12.setText(self.btn16.text())
            self.btn16.setText("")
        elif self.btn15.text() == "":
            self.btn15.setText(self.btn16.text())
            self.btn16.setText("")
        else:
            pyatnashki.urinish -= 1
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText("Siljitishni iloji nes")
            msg.setIcon(QMessageBox.Critical)
            msg.show()
        
        self.tablo2.setValue(pyatnashki.urinish)
        self.check_game()
        
    def new_game(self):
        st = set()
        while len(st) != 15:
            st.add(random.randint(1,15))
        pyatnashki.ls = list(st)
        random.shuffle(pyatnashki.ls)
        print(st)
        for x,y in zip(self.ls1,pyatnashki.ls):
            x.setText(str(y))
        
    def check_game(self):
        check = False
        for x in range(len(self.ls1)):
            if str(x + 1) == self.ls1[x].text():
                continue
            else:
                check = True
                break
        if check == False:
            msg = QMessageBox(self)
            msg.setFont(QFont("Calibri",20))
            msg.setText(f"Siz {pyatnashki.urinish} martada yutdingiz!!!")
            msg.setIcon(QMessageBox.Critical)
            msg.show()

            


if __name__ == "__main__":
    spp = QApplication(sys.argv) 
    game = pyatnashki()
    game.show()
    sys.exit(spp.exec_())