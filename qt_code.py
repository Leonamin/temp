# 출처 - https://github.com/ddd4117/GUI/blob/master/src/camera_test.py
# 수정 - webnautes

import cv2
import sys
import os
import RPi.GPIO as GPIO
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from prAvata import *

class ShowVideo(QtCore.QObject):

    camFlag = 0

    camera = cv2.VideoCapture(0)
    camera.set(3, 480)
    camera.set(4, 320)

    ret, image = camera.read()
    height, width = image.shape[:2]

    VideoSignal1 = QtCore.pyqtSignal(QtGui.QImage)
    VideoSignal2 = QtCore.pyqtSignal(QtGui.QImage)

    def __init__(self, parent=None):
        super(ShowVideo, self).__init__(parent)

    @QtCore.pyqtSlot()
    def startVideo(self):
        global image

        run_video = True
        while run_video:
            ret, image = self.camera.read()
            color_swapped_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            qt_image1 = QtGui.QImage(color_swapped_image.data,
                                    self.width,
                                    self.height,
                                    color_swapped_image.strides[0],
                                    QtGui.QImage.Format_RGB888)
            if self.camFlag:
                self.VideoSignal1.emit(qt_image1)

            loop = QtCore.QEventLoop()
            QtCore.QTimer.singleShot(1, loop.quit)
            loop.exec_()

    @QtCore.pyqtSlot()
    def camToggle(self):
        self.camFlag ^= 1


class ImageViewer(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)
        self.image = QtGui.QImage()
        self.setAttribute(QtCore.Qt.WA_OpaquePaintEvent)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.image)
        self.image = QtGui.QImage()

    def initUI(self):
        self.setWindowTitle('Test')

    @QtCore.pyqtSlot(QtGui.QImage)
    def setImage(self, image):
        if image.isNull():
            print("Viewer Dropped frame!")

        self.image = image
        if image.size() != self.size():
            self.setFixedSize(image.size())
        self.update()

class MainProgram(Ui_MainWindow, QtCore.QObject):
    gpioFlag = 0
    camFlag = 0
    camOnSig = QtCore.pyqtSignal()

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM) # We are accessing GPIOs according to their physical location
    pins = [18]
    GPIO.setup(pins, GPIO.OUT) # We have set our LED pin mode to output

    def initProgram(self):
        self.vidTr = QtCore.QThread()
        self.vidTr.start()
        self.vid = ShowVideo()
        self.vid.moveToThread(self.vidTr)

        self.image_viewer1 = ImageViewer()

        self.vid.VideoSignal1.connect(self.image_viewer1.setImage)

        self.verticalLayout.addWidget(self.image_viewer1)


        self.setupSig()
        self.emitSig()
    
    def setupSig(self):
        self.camOnSig.connect(self.vid.startVideo)
        self.camToggleBtn.clicked.connect(self.camToggle)
        self.gpioToggleBtn.clicked.connect(self.gpioToggle)
        self.sendCommandBtn.clicked.connect(self.sendCommand)
        self.quitBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)

    def emitSig(self):
        self.camOnSig.emit()

    def camToggle(self):
        self.camFlag ^= 1
        self.vid.camFlag = self.camFlag
        if self.camFlag:
            self.camToggleBtn.setText("Off")
        else:
            self.camToggleBtn.setText("On")

    def gpioToggle(self):
        self.gpioFlag ^= 1
        if self.gpioFlag:
            GPIO.output(18, GPIO.HIGH) # When it will start then LED will be OFF
            self.statusLbl.setText("HIGH")
            self.statusLbl.setStyleSheet("background-color: rgb(0, 255, 0)")
        else:
            GPIO.output(18, GPIO.LOW) # When it will start then LED will be OFF
            self.statusLbl.setText("LOW ")
            self.statusLbl.setStyleSheet("background-color: rgb(255, 0, 0)")

    def sendCommand(self):
        cmd = self.commandLine.text()
        os.system("echo \"%s\"" % cmd)
        print(cmd)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    #main 객체
    Main = MainProgram()
    Main.setupUi(MainWindow)
    Main.initProgram()

    MainWindow.show()
    sys.exit(app.exec_())