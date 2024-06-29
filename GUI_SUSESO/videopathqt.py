# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'video.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QInputDialog, QFileDialog
import cv2


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(993, 907)
        MainWindow.setStyleSheet("QWidget#centralwidget{background-color: rgb(85,170,127);}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelVIDEO = QtWidgets.QLabel(self.centralwidget)
        self.labelVIDEO.setGeometry(QtCore.QRect(90, 120, 800, 600))
        self.labelVIDEO.setStyleSheet("background-color: rgb(255,255,255)")
        self.labelVIDEO.setText("")
        self.labelVIDEO.setObjectName("labelVIDEO")
        self.botonCARGAR = QtWidgets.QPushButton(self.centralwidget)
        self.botonCARGAR.setGeometry(QtCore.QRect(190, 750, 201, 71))
        self.botonCARGAR.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(211, 215, 207);")
        self.botonCARGAR.setObjectName("botonCARGAR")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(540, 750, 251, 71))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 993, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.pushButton.clicked.connect(self.cancel)
        self.botonCARGAR.clicked.connect(self.pushBotton_handler)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def start_video(self, path):
        self.Work = Work(path)
        self.Work.start()
        self.Work.Imageupd.connect(self.Imageupd_slot)
        
    def Imageupd_slot(self, Image):
        self.labelVIDEO.setPixmap(QPixmap.fromImage(Image))
        
    def cancel(self):
        self.labelVIDEO.clear()
        self.Work.stop()
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.botonCARGAR.setText(_translate("MainWindow", "Cargar video"))
        self.pushButton.setText(_translate("MainWindow", "Resultados"))
        
    def pushBotton_handler(self):
        path = self.open_dialog_box()
        if path:
            self.start_video(path)
        
    def open_dialog_box(self):
        filename, _ = QFileDialog.getOpenFileName()
        return filename
    

class Work(QThread):
    Imageupd = pyqtSignal(QImage)
    
    def __init__(self, path):
        super().__init__()
        self.path = path
    
    def run(self):
        self.hilo_corriendo = True
        cap = cv2.VideoCapture(self.path)
        
                
        fps = cap.get(cv2.CAP_PROP_FPS)
        duracion = cap.get(cv2.CAP_PROP_FRAME_COUNT) / fps
        largo = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        vectorTiempo = np.arange(largo)
        print(fps)
        
        
        while self.hilo_corriendo:
            ret, frame = cap.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                #flip = cv2.flip(Image, 1)
                convertir_QT = QImage(Image.data, Image.shape[1], Image.shape[0], QImage.Format_RGB888)
                pic = convertir_QT.scaled(800, 600, Qt.KeepAspectRatio)
                self.Imageupd.emit(pic)
        
    def stop(self):
        self.hilo_corriendo = False
        self.quit()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())