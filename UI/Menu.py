# Form implementation generated from reading ui file 'Menu.ui'
#
# Created by: PyQt6 MainWindow.ui code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget
from qt_material import apply_stylesheet

class Menu_Form(QWidget):
    def setupUi(self, Form):
        apply_stylesheet(Form, theme='light_blue.xml')
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        Form.resize(1280, 720)
        font = QtGui.QFont()
        font.setPointSize(12)
        Form.setFont(font)
        Form.setStyleSheet("QLineEdit{\n"
"    border:0px; margin:10px;\n"
"     margin-left:50px;\n"
"     margin-right:50px;\n"
"     border-bottom: 2px solid #B3B3B3;\n"
"     font-family: \"Microsoft Yahei\";\n"
"     font-size:    20px;\n"
"     font-wight: blod;\n"
"}\n"
"\n"
"QLineEdit:Focus{\n"
"    border-bottom: 3px soild  #E680BD\n"
"}")
        Form.setStyleSheet("#Form{border-image:url(Background.png);}")
        self.User_Manager = QtWidgets.QPushButton(parent=Form)
        self.User_Manager.setGeometry(QtCore.QRect(400, 200, 120, 41))
        self.User_Manager.setObjectName("User_Manager")
        self.Student_Manager = QtWidgets.QPushButton(parent=Form)
        self.Student_Manager.setGeometry(QtCore.QRect(400, 350, 120, 40))
        self.Student_Manager.setObjectName("Student_Manager")
        self.Teacher_Manager = QtWidgets.QPushButton(parent=Form)
        self.Teacher_Manager.setGeometry(QtCore.QRect(400, 500, 120, 40))
        self.Teacher_Manager.setObjectName("Teacher_Manager")
        self.Canteen_Manager = QtWidgets.QPushButton(parent=Form)
        self.Canteen_Manager.setGeometry(QtCore.QRect(700, 500, 120, 40))
        self.Canteen_Manager.setObjectName("Canteen_Manager")
        self.Things_Manager = QtWidgets.QPushButton(parent=Form)
        self.Things_Manager.setGeometry(QtCore.QRect(700, 200, 120, 40))
        self.Things_Manager.setObjectName("Things_Manager")
        self.Teach_Manager = QtWidgets.QPushButton(parent=Form)
        self.Teach_Manager.setGeometry(QtCore.QRect(700, 350, 120, 40))
        self.Teach_Manager.setObjectName("Teach_Manager")
        self.Exit = QtWidgets.QPushButton(parent=Form)
        self.Exit.setGeometry(QtCore.QRect(600, 600, 120, 40))
        self.Exit.setObjectName("Exit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "基于ChatGPT的幼儿园管理系统"))
        self.User_Manager.setText(_translate("Form", "账号管理"))
        self.Student_Manager.setText(_translate("Form", "学生信息管理"))
        self.Teacher_Manager.setText(_translate("Form", "教职工信息管理"))
        self.Canteen_Manager.setText(_translate("Form", "食堂管理"))
        self.Things_Manager.setText(_translate("Form", "物资管理"))
        self.Teach_Manager.setText(_translate("Form", "教学管理"))
        self.Exit.setText(_translate("Form", "退出"))
