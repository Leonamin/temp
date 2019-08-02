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
        MainWindow.resize(425, 517)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 421, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 330, 421, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.commandLine = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.commandLine.setText("")
        self.commandLine.setObjectName("commandLine")
        self.verticalLayout_2.addWidget(self.commandLine)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.paddingLbl = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.paddingLbl.setMaximumSize(QtCore.QSize(70, 50))
        self.paddingLbl.setStyleSheet("")
        self.paddingLbl.setText("")
        self.paddingLbl.setObjectName("paddingLbl")
        self.horizontalLayout_2.addWidget(self.paddingLbl)
        self.statusLbl = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.statusLbl.setMaximumSize(QtCore.QSize(70, 50))
        self.statusLbl.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.statusLbl.setObjectName("statusLbl")
        self.horizontalLayout_2.addWidget(self.statusLbl)
        self.paddingLbl_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.paddingLbl_2.setMaximumSize(QtCore.QSize(70, 50))
        self.paddingLbl_2.setStyleSheet("")
        self.paddingLbl_2.setText("")
        self.paddingLbl_2.setObjectName("paddingLbl_2")
        self.horizontalLayout_2.addWidget(self.paddingLbl_2)
        self.paddingLbl_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.paddingLbl_3.setMaximumSize(QtCore.QSize(70, 50))
        self.paddingLbl_3.setStyleSheet("")
        self.paddingLbl_3.setText("")
        self.paddingLbl_3.setObjectName("paddingLbl_3")
        self.horizontalLayout_2.addWidget(self.paddingLbl_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.camToggleBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.camToggleBtn.setMaximumSize(QtCore.QSize(70, 50))
        self.camToggleBtn.setObjectName("camToggleBtn")
        self.horizontalLayout.addWidget(self.camToggleBtn)
        self.gpioToggleBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.gpioToggleBtn.setMaximumSize(QtCore.QSize(70, 50))
        self.gpioToggleBtn.setObjectName("gpioToggleBtn")
        self.horizontalLayout.addWidget(self.gpioToggleBtn)
        self.sendCommandBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.sendCommandBtn.setMaximumSize(QtCore.QSize(70, 50))
        self.sendCommandBtn.setObjectName("sendCommandBtn")
        self.horizontalLayout.addWidget(self.sendCommandBtn)
        self.quitBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.quitBtn.setMaximumSize(QtCore.QSize(70, 50))
        self.quitBtn.setObjectName("quitBtn")
        self.horizontalLayout.addWidget(self.quitBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 425, 28))
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
        self.statusLbl.setText(_translate("MainWindow", "LOW"))
        self.camToggleBtn.setText(_translate("MainWindow", "On"))
        self.gpioToggleBtn.setText(_translate("MainWindow", "GPIO 18"))
        self.sendCommandBtn.setText(_translate("MainWindow", "Send"))
        self.quitBtn.setText(_translate("MainWindow", "Quit"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
