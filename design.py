# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 470)
        MainWindow.setStyleSheet("background-color: #fcf0ca;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_well = QtWidgets.QPushButton(self.centralwidget)
        self.button_well.setGeometry(QtCore.QRect(10, 420, 131, 41))
        self.button_well.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"background-color: #bde0ff;\n"
"font: 75 bold 18pt \"FreeSerif\";\n"
"\n"
"")
        self.button_well.setObjectName("button_well")
        self.button_lizard = QtWidgets.QPushButton(self.centralwidget)
        self.button_lizard.setGeometry(QtCore.QRect(150, 420, 131, 41))
        self.button_lizard.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"background-color: #bde0ff;\n"
"font: 75 bold 18pt \"FreeSerif\";\n"
"\n"
"")
        self.button_lizard.setObjectName("button_lizard")
        self.button_spock = QtWidgets.QPushButton(self.centralwidget)
        self.button_spock.setGeometry(QtCore.QRect(290, 420, 131, 41))
        self.button_spock.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"background-color: #bde0ff;\n"
"font: 75 bold 18pt \"FreeSerif\";\n"
"\n"
"")
        self.button_spock.setObjectName("button_spock")
        self.design_line = QtWidgets.QFrame(self.centralwidget)
        self.design_line.setGeometry(QtCore.QRect(0, 350, 441, 16))
        self.design_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.design_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.design_line.setObjectName("design_line")
        self.button_stone = QtWidgets.QPushButton(self.centralwidget)
        self.button_stone.setGeometry(QtCore.QRect(10, 370, 131, 41))
        self.button_stone.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"background-color: #bde0ff;\n"
"font: 75 bold 18pt \"FreeSerif\";\n"
"\n"
"")
        self.button_stone.setObjectName("button_stone")
        self.button_scissors = QtWidgets.QPushButton(self.centralwidget)
        self.button_scissors.setGeometry(QtCore.QRect(150, 370, 131, 41))
        self.button_scissors.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"background-color: #bde0ff;\n"
"font: 75 bold 18pt \"FreeSerif\";\n"
"\n"
"")
        self.button_scissors.setObjectName("button_scissors")
        self.button_papers = QtWidgets.QPushButton(self.centralwidget)
        self.button_papers.setGeometry(QtCore.QRect(290, 370, 131, 41))
        self.button_papers.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"background-color: #bde0ff;\n"
"font: 75 bold 18pt \"FreeSerif\";\n"
"\n"
"")
        self.button_papers.setObjectName("button_papers")
        self.design_label = QtWidgets.QLabel(self.centralwidget)
        self.design_label.setGeometry(QtCore.QRect(10, 70, 420, 270))
        self.design_label.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"border-style: outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width: 1px;\n"
"")
        self.design_label.setText("")
        self.design_label.setObjectName("design_label")
        self.design_label2 = QtWidgets.QLabel(self.centralwidget)
        self.design_label2.setGeometry(QtCore.QRect(40, 40, 101, 21))
        self.design_label2.setStyleSheet("font: 75 12pt \"FreeSerif\";")
        self.design_label2.setObjectName("design_label2")
        self.user_score = QtWidgets.QLCDNumber(self.centralwidget)
        self.user_score.setGeometry(QtCore.QRect(140, 40, 64, 21))
        self.user_score.setObjectName("user_score")
        self.computer_score = QtWidgets.QLCDNumber(self.centralwidget)
        self.computer_score.setGeometry(QtCore.QRect(240, 40, 64, 21))
        self.computer_score.setObjectName("computer_score")
        self.design_label3 = QtWidgets.QLabel(self.centralwidget)
        self.design_label3.setGeometry(QtCore.QRect(310, 40, 81, 21))
        self.design_label3.setStyleSheet("font: 75 12pt \"FreeSerif\";")
        self.design_label3.setObjectName("design_label3")
        self.design_label2_2 = QtWidgets.QLabel(self.centralwidget)
        self.design_label2_2.setGeometry(QtCore.QRect(160, 10, 121, 21))
        self.design_label2_2.setStyleSheet("font: 75 16pt \"FreeSerif\";")
        self.design_label2_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.design_label2_2.setObjectName("design_label2_2")
        self.design_label5 = QtWidgets.QLabel(self.centralwidget)
        self.design_label5.setGeometry(QtCore.QRect(20, 110, 81, 21))
        self.design_label5.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"font: 75 16pt \"FreeSerif\";")
        self.design_label5.setObjectName("design_label5")
        self.user_change = QtWidgets.QLineEdit(self.centralwidget)
        self.user_change.setGeometry(QtCore.QRect(20, 140, 401, 25))
        self.user_change.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 1px;")
        self.user_change.setAlignment(QtCore.Qt.AlignCenter)
        self.user_change.setReadOnly(True)
        self.user_change.setObjectName("user_change")
        self.design_label4 = QtWidgets.QLabel(self.centralwidget)
        self.design_label4.setGeometry(QtCore.QRect(20, 240, 81, 21))
        self.design_label4.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"font: 75 16pt \"FreeSerif\";")
        self.design_label4.setObjectName("design_label4")
        self.computer_change = QtWidgets.QLineEdit(self.centralwidget)
        self.computer_change.setGeometry(QtCore.QRect(20, 270, 401, 25))
        self.computer_change.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 1px;")
        self.computer_change.setAlignment(QtCore.Qt.AlignCenter)
        self.computer_change.setReadOnly(True)
        self.computer_change.setObjectName("computer_change")
        self.button_done = QtWidgets.QPushButton(self.centralwidget)
        self.button_done.setGeometry(QtCore.QRect(170, 190, 100, 30))
        self.button_done.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"font: 75 18pt \"FreeSerif\";\n"
"background-color: rgb(238, 238, 236);")
        self.button_done.setObjectName("button_done")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_well.setText(_translate("MainWindow", "Колодец"))
        self.button_lizard.setText(_translate("MainWindow", "Ящерица"))
        self.button_spock.setText(_translate("MainWindow", "Спок"))
        self.button_stone.setText(_translate("MainWindow", "Камень"))
        self.button_scissors.setText(_translate("MainWindow", "Ножницы"))
        self.button_papers.setText(_translate("MainWindow", "Бумага"))
        self.design_label2.setText(_translate("MainWindow", "Пользователь"))
        self.design_label3.setText(_translate("MainWindow", "Компьютер"))
        self.design_label2_2.setText(_translate("MainWindow", "- Cчёт игры -"))
        self.design_label5.setText(_translate("MainWindow", "Ваш ход:"))
        self.design_label4.setText(_translate("MainWindow", "Мой ход:"))
        self.button_done.setText(_translate("MainWindow", "Готово"))
