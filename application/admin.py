# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\secondwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
from commonfunctions import *
from cartoonization import *
from attendance import *

import re

class admin_form(object):
    def setupUi(self, Form , name):
        Form.setObjectName("Form")
        Form.resize(711, 435)
        self.mw = Form #mw is short for Main Window 

        self.user = name

        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.power2 = QtWidgets.QPushButton(Form)
        self.power2.setObjectName("power2")
        self.gridLayout.addWidget(self.power2, 1, 1, 1, 1)

        self.num7 = QtWidgets.QPushButton(Form)
        self.num7.setObjectName("num7")
        self.gridLayout.addWidget(self.num7, 2, 0, 1, 1)

        self.num4 = QtWidgets.QPushButton(Form)
        self.num4.setObjectName("num4")
        self.gridLayout.addWidget(self.num4, 3, 0, 1, 1)

        self.power3 = QtWidgets.QPushButton(Form)
        self.power3.setObjectName("power3")
        self.gridLayout.addWidget(self.power3, 0, 1, 1, 1)

        self.neg = QtWidgets.QPushButton(Form)
        self.neg.setObjectName("neg")
        self.gridLayout.addWidget(self.neg, 5, 0, 1, 1)

        self.mul = QtWidgets.QPushButton(Form)
        self.mul.setObjectName("mul")
        self.gridLayout.addWidget(self.mul, 2, 3, 1, 1)

        self.num2 = QtWidgets.QPushButton(Form)
        self.num2.setObjectName("num2")
        self.gridLayout.addWidget(self.num2, 4, 1, 1, 1)

        self.num1 = QtWidgets.QPushButton(Form)
        self.num1.setObjectName("num1")
        self.gridLayout.addWidget(self.num1, 4, 0, 1, 1)

        self.inverse = QtWidgets.QPushButton(Form)
        self.inverse.setObjectName("inverse")
        self.gridLayout.addWidget(self.inverse, 1, 0, 1, 1)

        self.divide = QtWidgets.QPushButton(Form)
        self.divide.setObjectName("divide")
        self.gridLayout.addWidget(self.divide, 1, 3, 1, 1)

        self.eq = QtWidgets.QPushButton(Form)
        self.eq.setObjectName("eq")
        self.gridLayout.addWidget(self.eq, 5, 3, 1, 1)

        self.AC = QtWidgets.QPushButton(Form)
        self.AC.setObjectName("AC")
        self.gridLayout.addWidget(self.AC, 0, 2, 1, 1)

        self.num5 = QtWidgets.QPushButton(Form)
        self.num5.setObjectName("num5")
        self.gridLayout.addWidget(self.num5, 3, 1, 1, 1)

        self.num0 = QtWidgets.QPushButton(Form)
        self.num0.setObjectName("num0")
        self.gridLayout.addWidget(self.num0, 5, 1, 1, 1)

        self.back = QtWidgets.QPushButton(Form)
        self.back.setObjectName("back")
        self.gridLayout.addWidget(self.back, 0, 3, 1, 1)

        self.add = QtWidgets.QPushButton(Form)
        self.add.setObjectName("add")
        self.gridLayout.addWidget(self.add, 4, 3, 1, 1)

        self.sqrt = QtWidgets.QPushButton(Form)
        self.sqrt.setObjectName("sqrt")
        self.gridLayout.addWidget(self.sqrt, 1, 2, 1, 1)

        self.num8 = QtWidgets.QPushButton(Form)
        self.num8.setObjectName("num8")
        self.gridLayout.addWidget(self.num8, 2, 1, 1, 1)

        self.num3 = QtWidgets.QPushButton(Form)
        self.num3.setObjectName("num3")
        self.gridLayout.addWidget(self.num3, 4, 2, 1, 1)

        self.point = QtWidgets.QPushButton(Form)
        self.point.setObjectName("point")
        self.gridLayout.addWidget(self.point, 5, 2, 1, 1)

        self.num9 = QtWidgets.QPushButton(Form)
        self.num9.setObjectName("num9")
        self.gridLayout.addWidget(self.num9, 2, 2, 1, 1)

        self.percent = QtWidgets.QPushButton(Form)
        self.percent.setObjectName("percent")
        self.gridLayout.addWidget(self.percent, 0, 0, 1, 1)

        self.sub = QtWidgets.QPushButton(Form)
        self.sub.setObjectName("sub")
        self.gridLayout.addWidget(self.sub, 3, 3, 1, 1)

        self.num6 = QtWidgets.QPushButton(Form)
        self.num6.setObjectName("num6")
        self.gridLayout.addWidget(self.num6, 3, 2, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 3, 1)

        self.frame = QtWidgets.QLabel(Form)
        self.frame.setObjectName("frame")
        self.gridLayout_3.addWidget(self.frame, 0, 1, 1, 2)




        self.add_user = QtWidgets.QPushButton(Form)
        self.add_user.setObjectName("add_user")
        self.gridLayout_3.addWidget(self.add_user, 1, 1, 1, 1)

        self.usersList = QtWidgets.QListWidget(Form)
        self.usersList.setObjectName("usersList")
        self.gridLayout_3.addWidget(self.usersList, 1, 2, 2, 1)

        self.del_user = QtWidgets.QPushButton(Form)
        self.del_user.setObjectName("del_user")
        self.gridLayout_3.addWidget(self.del_user, 2, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.num0.clicked.connect(self.show) #0
        self.num1.clicked.connect(self.show) #1
        self.num2.clicked.connect(self.show)#2
        self.num3.clicked.connect(self.show)#3
        self.num4.clicked.connect(self.show)#4
        self.num5.clicked.connect(self.show)#5
        self.num6.clicked.connect(self.show)#6
        self.num7.clicked.connect(self.show)#7
        self.num8.clicked.connect(self.show)#8
        self.num9.clicked.connect(self.show)#9

        self.add.clicked.connect(self.show)#+
        self.sub.clicked.connect(self.show)#-
        self.mul.clicked.connect(self.show)#x
        self.divide.clicked.connect(self.show)#/

        self.point.clicked.connect(self.show)#.
        self.back.clicked.connect(self.show)#<=
        self.eq.clicked.connect(self.show)#=
        self.neg.clicked.connect(self.show)#+/-

        self.AC.clicked.connect(self.show)#AC
        self.power3.clicked.connect(self.show)#x^3
        self.percent.clicked.connect(self.show)#%

        self.inverse.clicked.connect(self.show)#1/x
        self.power2.clicked.connect(self.show)#x^2
        self.sqrt.clicked.connect(self.show)#sqrt

        self.text=''
        self.textEdit.setFontPointSize(24)
        self.processed=False



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "App(Calculator)"))
        self.power2.setText(_translate("Form", "x^2"))
        self.num7.setText(_translate("Form", "7"))
        self.num4.setText(_translate("Form", "4"))
        self.power3.setText(_translate("Form", "x^3"))
        self.neg.setText(_translate("Form", "+/-"))
        self.mul.setText(_translate("Form", "*"))
        self.num2.setText(_translate("Form", "2"))
        self.num1.setText(_translate("Form", "1"))
        self.inverse.setText(_translate("Form", "1/x"))
        self.divide.setText(_translate("Form", "/"))
        self.eq.setText(_translate("Form", "="))
        self.AC.setText(_translate("Form", "AC"))
        self.num5.setText(_translate("Form", "5"))
        self.num0.setText(_translate("Form", "0"))
        self.back.setText(_translate("Form", "Backspace"))
        self.add.setText(_translate("Form", "+"))
        self.sqrt.setText(_translate("Form", "sqrt"))
        self.num8.setText(_translate("Form", "8"))
        self.num3.setText(_translate("Form", "3"))
        self.point.setText(_translate("Form", "."))
        self.num9.setText(_translate("Form", "9"))
        self.percent.setText(_translate("Form", "%"))
        self.sub.setText(_translate("Form", "-"))
        self.num6.setText(_translate("Form", "6"))
        self.frame.setText(_translate("Form", "Avatar"))
        self.add_user.setText(_translate("Form", "Add User"))
        self.del_user.setText(_translate("Form", "Delete User"))
        self.usersList.setSortingEnabled(True)


    def process(self):
        try:
            inp=self.text
            inp = re.sub(r"\.(?![0-9])","", inp)
            val = eval(inp, {'__builtins__':None})
            self.text=str(val)
        except Exception as e:
            self.text = str(e)
        self.processed = True
			
		
		
    def show(self):
        self.textEdit.setFontPointSize(24)
        self.text = self.textEdit.toPlainText()
        
        num_list = [str(num) for num in [0,1,2,3,4,5,6,7,8,9,'.']]
        op_list = ['+','-','*','/','%']
        
        c_or_ce_list = ['AC']
        func_list=['1/x','x^2','sqrt','+/-','x^3']
        
        if self.mw.sender().text()!='Backspace':
            if self.mw.sender().text() in num_list :
                if self.processed == True:
                    self.text=''
                self.text+=self.mw.sender().text()
                self.processed = False
            
            if self.mw.sender().text() in op_list :
                
                self.text+=self.mw.sender().text()
                self.processed = False
            
            if self.mw.sender().text() =='=':
                self.process()
            if self.mw.sender().text() in c_or_ce_list:
                self.text=''
                self.processed = False
            if self.mw.sender().text() in func_list:
                if self.mw.sender().text() == func_list[0]:
                    try:
                        self.text= str(1/eval(self.text))
                    except Exception as e: 
                        self.text=str(e)
                    self.processed = False
                if self.mw.sender().text() == func_list[1]:
                    self.text= str(eval(self.text)**2)
                    self.processed = False
                if self.mw.sender().text() == func_list[2]:
                    self.text= str(eval(self.text)**0.5)
                    self.processed = False
                if self.mw.sender().text() == func_list[3]:
                    self.text= str(-1*eval(self.text))	
                    self.processed = False
                if self.mw.sender().text() == func_list[4]:
                    self.text= str(eval(self.text)**3)
                    self.processed = False
            
                
        else:
            self.text = self.text[0:len(self.text)-1]
            
        self.textEdit.setText(self.text)
        imgloc = os.path.join('.','data', self.user, self.user +".jpg")
        #imgloc = ".\\data\\"+self.user+"\\"+self.user+".jpg"
        img = cv2.imread(imgloc)
        img = cv2.resize(img,(365,350))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.frame.setPixmap(QPixmap.fromImage(qImg))






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = admin_form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())