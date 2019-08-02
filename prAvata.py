# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prAvata.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(180, 50, 421, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(250, 479, 319, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.camToggleBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.camToggleBtn.setMaximumSize(QtCore.QSize(70, 50))
        self.camToggleBtn.setObjectName("camToggleBtn")
        self.horizontalLayout.addWidget(self.camToggleBtn)
        self.gpioToggleBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.gpioToggleBtn.setMaximumSize(QtCore.QSize(70, 50))
        self.gpioToggleBtn.setObjectName("gpioToggleBtn")
        self.horizontalLayout.addWidget(self.gpioToggleBtn)
        self.sendCommandBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.sendCommandBtn.setMaximumSize(QtCore.QSize(70, 50))
        self.sendCommandBtn.setObjectName("sendCommandBtn")
        self.horizontalLayout.addWidget(self.sendCommandBtn)
        self.quitBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.quitBtn.setMaximumSize(QtCore.QSize(70, 50))
        self.quitBtn.setObjectName("quitBtn")
        self.horizontalLayout.addWidget(self.quitBtn)
        self.commandLine = QtWidgets.QLineEdit(self.centralwidget)
        self.commandLine.setGeometry(QtCore.QRect(250, 390, 281, 25))
        self.commandLine.setText("")
        self.commandLine.setObjectName("commandLine")
        self.statusLbl = QtWidgets.QLabel(self.centralwidget)
        self.statusLbl.setGeometry(QtCore.QRect(600, 440, 61, 41))
        self.statusLbl.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.statusLbl.setObjectName("statusLbl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.camToggleBtn.setText(_translate("MainWindow", "On"))
        self.gpioToggleBtn.setText(_translate("MainWindow", "GPIO 18"))
        self.sendCommandBtn.setText(_translate("MainWindow", "Send"))
        self.quitBtn.setText(_translate("MainWindow", "Quit"))
        self.statusLbl.setText(_translate("MainWindow", "LOW"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
