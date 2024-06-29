#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QInputDialog, QFileDialog, QProgressBar, QVBoxLayout

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import cv2
import mediapipe as mp
import numpy as np
import pandas as pd

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(986, 936)
        MainWindow.setStyleSheet("QWidget#centralwidget{background-color: rgb(85,170,127);}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelVIDEO = QtWidgets.QLabel(self.centralwidget)
        self.labelVIDEO.setGeometry(QtCore.QRect(90, 150, 800, 600))
        self.labelVIDEO.setStyleSheet("background-color: rgb(255,255,255)")
        self.labelVIDEO.setText("")
        self.labelVIDEO.setObjectName("labelVIDEO")
        self.botonCARGAR = QtWidgets.QPushButton(self.centralwidget)
        self.botonCARGAR.setGeometry(QtCore.QRect(190, 800, 201, 71))
        self.botonCARGAR.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(211, 215, 207);")
        self.botonCARGAR.setObjectName("botonCARGAR")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(540, 800, 251, 71))
        self.pushButton.setObjectName("pushButton")
        self.labelLOGO = QtWidgets.QLabel(self.centralwidget)
        self.labelLOGO.setGeometry(QtCore.QRect(310, 20, 131, 121))
        self.labelLOGO.setStyleSheet("background-image: url(:/prefijoNuevo/Logo_ACHS.png);")
        self.labelLOGO.setText("")
        self.labelLOGO.setPixmap(QtGui.QPixmap(":/prefijoNuevo/Logo_ACHS.png"))
        self.labelLOGO.setScaledContents(True)
        self.labelLOGO.setObjectName("labelLOGO")
        self.labelLOGO2 = QtWidgets.QLabel(self.centralwidget)
        self.labelLOGO2.setGeometry(QtCore.QRect(520, 10, 241, 131))
        self.labelLOGO2.setStyleSheet("background-image: url(:/prefijoNuevo/LOGO_SUSESO.png);")
        self.labelLOGO2.setText("")
        self.labelLOGO2.setPixmap(QtGui.QPixmap(":/prefijoNuevo/LOGO_SUSESO.png"))
        self.labelLOGO2.setScaledContents(True)
        self.labelLOGO2.setObjectName("labelLOGO2")
#        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
#        self.progressBar.setGeometry(QtCore.QRect(90, 750, 801, 23))
#        self.progressBar.setProperty("value", 0)
#        self.progressBar.setObjectName("progressBar")
        self.labelCARGANDO = QtWidgets.QLabel(self.centralwidget)
        self.labelCARGANDO.setGeometry(QtCore.QRect(90, 750, 800, 23))
        self.labelCARGANDO.setStyleSheet("background-color: rgb(255,255,255)")
        self.labelCARGANDO.setText("DEBES CARGAR UN VIDEO")
        self.labelCARGANDO.setObjectName("labelCARGANDO")

        self.w = QtWidgets.QLabel(self.centralwidget)
        self.w.setGeometry(QtCore.QRect(540, 800, 251, 71))
        self.w.setStyleSheet("background-color: rgb(255,255,255)")
        #self.w.setText("Abrir PDF")
        self.w.setObjectName("")
        
        path = r"/media/jose/DataDisk/Ubuntu/OpencvProject/PDF/informe3.pdf"

        url = bytearray(QUrl.fromLocalFile(path).toEncoded()).decode() # file:///C:/Users/Shaurya/Documents/To%20be%20saved/hello.pdf
        text = "<a href={}>Abrir PDF> </a>".format(url)
        self.w.setText(text)
        self.w.setOpenExternalLinks(True)



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 986, 22))
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
        self.labelCARGANDO.setText("PROCESANDO VIDEO")
        
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
        
        
     

    def calculate_angle(self,a,b,c):
        a = np.array(a) #proximal
        b = np.array(b) #joint
        c = np.array(c) #distal
    
        radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
        angle = np.abs(radians*180.0/np.pi)
    
        if angle >180.0:
            angle = 360-angle
        return angle
    
    
    def run(self):
        self.hilo_corriendo = True
        mp_drawing = mp.solutions.drawing_utils # utilidades para dibujar de mediapipe
        mp_pose = mp.solutions.pose # importa la estimacion de postura
                        
        RHip_angle = []
        RKnee_angle = []
        RAnkle_angle = []
        LHip_angle = []
        LKnee_angle = []
        LAnkle_angle = []
        VCOMx = []
        VCOMy = []
        tiempo = []
        RightHeelTrajectoryX = []
        RightHeelTrajectoryY = []
        LeftHeelTrajectoryX = []
        LeftHeelTrajectoryY = []
        RightToeTrajectoryX = []
        RightToeTrajectoryY = []
        LeftToeTrajectoryX = []
        LeftToeTrajectoryY = []
        
        RHip_angleB = []
        RKnee_angleB = []
        RAnkle_angleB = []
        LHip_angleB = []
        LKnee_angleB = []
        LAnkle_angleB = []
        VCOMxB = []
        VCOMyB = []
        tiempoB = []
        noTiempoB = []
        RightHeelTrajectoryXB = []
        RightHeelTrajectoryYB = []
        LeftHeelTrajectoryXB = []
        LeftHeelTrajectoryYB = []
        RightToeTrajectoryXB = []
        RightToeTrajectoryYB = []
        LeftToeTrajectoryXB = []
        LeftToeTrajectoryYB = []
        cap = cv2.VideoCapture(self.path)
        mpDraw = mp.solutions.drawing_utils
        mpPose = mp.solutions.pose
        pose = mpPose.Pose()
        
        fps = cap.get(cv2.CAP_PROP_FPS)
        duracion = cap.get(cv2.CAP_PROP_FRAME_COUNT) / fps
        largo = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        vectorTiempo = np.arange(largo)
        
        # siguiente linea es para la barra de progreso
        
        
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        #fps = 30
        out = cv2.VideoWriter('videoRESULTADO.avi',cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width,frame_height))
        com = False
        p = 0
        q = 0
        
        
        while True:
            success, img = cap.read()

            try:
        
                imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                results = pose.process(imgRGB)
            except:
              print('1')
              break
        

            
            if results.pose_landmarks:
                mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        
                try:
                    landmarks = results.pose_landmarks.landmark
            
                            # obtener coordenadas de centros de rotacion
                    Right_Shoulder = [landmarks[mpPose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mpPose.PoseLandmark.RIGHT_SHOULDER.value].y]
                    Right_Hip = [landmarks[mpPose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mpPose.PoseLandmark.RIGHT_HIP.value].y]
                    Right_Knee = [landmarks[mpPose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[mpPose.PoseLandmark.RIGHT_KNEE.value].y]
                    Right_Ankle = [landmarks[mpPose.PoseLandmark.RIGHT_ANKLE.value].x,landmarks[mpPose.PoseLandmark.RIGHT_ANKLE.value].y]
                    Right_Heel = [landmarks[mpPose.PoseLandmark.RIGHT_HEEL.value].x,landmarks[mpPose.PoseLandmark.RIGHT_HEEL.value].y]
                    Right_Toe = [landmarks[mpPose.PoseLandmark.RIGHT_FOOT_INDEX.value].x,landmarks[mpPose.PoseLandmark.RIGHT_FOOT_INDEX.value].y]
                    Left_Shoulder = [landmarks[mpPose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mpPose.PoseLandmark.LEFT_SHOULDER.value].y]
                    Left_Hip = [landmarks[mpPose.PoseLandmark.LEFT_HIP.value].x,landmarks[mpPose.PoseLandmark.LEFT_HIP.value].y]
                    Left_Knee = [landmarks[mpPose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mpPose.PoseLandmark.LEFT_KNEE.value].y]
                    Left_Ankle = [landmarks[mpPose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mpPose.PoseLandmark.LEFT_ANKLE.value].y]
                    Left_Heel = [landmarks[mpPose.PoseLandmark.LEFT_HEEL.value].x,landmarks[mpPose.PoseLandmark.LEFT_HEEL.value].y]
                    Left_Toe = [landmarks[mpPose.PoseLandmark.LEFT_FOOT_INDEX.value].x,landmarks[mpPose.PoseLandmark.LEFT_FOOT_INDEX.value].y]
                            # hay que corregir COM, ya que esta fijo en los ejes
                            # de momento podria hacer una ecuacion que normalice en base altura y ancho de la persona
                            #COMx = (Right_Hip[0] + Left_Hip[0])/2
                            #COMy = (Right_Hip[1] + Left_Hip[1])/2
                            # calcular tiempo
            #        end_time = time.time()
            #        time_lapsed = end_time - start_time
                    center_x, center_y, center_z = calculate_center_of_mass(landmarks)
                    com = True
            
                            # calcular angulos EEII
                    Right_Hip_angle = self.calculate_angle(Right_Shoulder,Right_Hip,Right_Knee)
                    Right_Knee_angle = self.calculate_angle(Right_Hip,Right_Knee,Right_Ankle)
                    Right_Ankle_angle = self.calculate_angle(Right_Knee,Right_Heel,Right_Toe)
                    Left_Hip_angle = self.calculate_angle(Left_Shoulder,Left_Hip,Left_Knee)
                    Left_Knee_angle = self.calculate_angle(Left_Hip,Left_Knee,Left_Ankle)
                    Left_Ankle_angle = self.calculate_angle(Left_Knee,Left_Heel,Left_Toe)
                            #print(Right_Ankle_angle)
                            # cv2.putText(image, str(Knee_angle),
                            #             tuple(np.multiply(Right_Knee, [640, 480]).astype(int)),
                            #                   cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)
                            #             #
                    RHip_angle.append(180 - Right_Hip_angle)
                    RKnee_angle.append(180 - Right_Knee_angle)
                    RAnkle_angle.append(90 - Right_Ankle_angle)
                    LHip_angle.append(180 - Left_Hip_angle)
                    LKnee_angle.append(180 - Left_Knee_angle)
                    LAnkle_angle.append(90 - Left_Ankle_angle)
                    tiempo.append(vectorTiempo[p] / fps)
                    RightHeelTrajectoryX.append(Right_Heel[0])
                    RightHeelTrajectoryY.append(Right_Heel[1])
                    LeftHeelTrajectoryX.append(Left_Heel[0])
                    LeftHeelTrajectoryY.append(Left_Heel[1])
                    RightToeTrajectoryX.append(Right_Toe[0])
                    RightToeTrajectoryY.append(Right_Toe[1])
                    LeftToeTrajectoryX.append(Left_Toe[0])
                    LeftToeTrajectoryY.append(Left_Toe[1])
    
    
                    VCOMx.append(center_x)
                    VCOMy.append(center_y)
                    
                    
                    RHip_angleB.append(180 - Right_Hip_angle)
                    RKnee_angleB.append(180 - Right_Knee_angle)
                    RAnkle_angleB.append(90 - Right_Ankle_angle)
                    LHip_angleB.append(180 - Left_Hip_angle)
                    LKnee_angleB.append(180 - Left_Knee_angle)
                    LAnkle_angleB.append(90 - Left_Ankle_angle)
                    tiempoB.append(vectorTiempo[q] / fps)
                    RightHeelTrajectoryXB.append(Right_Heel[0])
                    RightHeelTrajectoryYB.append(Right_Heel[1])
                    LeftHeelTrajectoryXB.append(Left_Heel[0])
                    LeftHeelTrajectoryYB.append(Left_Heel[1])
                    RightToeTrajectoryXB.append(Right_Toe[0])
                    RightToeTrajectoryYB.append(Right_Toe[1])
                    LeftToeTrajectoryXB.append(Left_Toe[0])
                    LeftToeTrajectoryYB.append(Left_Toe[1])
    
    
                    VCOMxB.append(center_x)
                    VCOMyB.append(center_y)
                    
                    p = p + 1
                    q = q + 1
        
                except:
                    RHip_angle.append(0)
                    RKnee_angle.append(0)
                    RAnkle_angle.append(0)
                    LHip_angle.append(0)
                    LKnee_angle.append(0)
                    LAnkle_angle.append(0)
                    tiempo.append(vectorTiempo[p] / fps)
                    noTiempoB.append(vectorTiempo[p] / fps)
                    RightHeelTrajectoryX.append(0)
                    RightHeelTrajectoryY.append(0)
                    LeftHeelTrajectoryX.append(0)
                    LeftHeelTrajectoryY.append(0)
                    RightToeTrajectoryX.append(0)
                    RightToeTrajectoryY.append(0)
                    LeftToeTrajectoryX.append(0)
                    LeftToeTrajectoryY.append(0)
    
    
                    VCOMx.append(0)
                    VCOMy.append(0)
                    
                    
                    p = p + 1
                    
                    pass


        
        
        # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
        
            out.write(img)
        
          #  cTime = time.time()
          #  fps = 1/(cTime - pTime)
          #  pTime = cTime
        
        #    cv2.imshow('Image', img)
        #    cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
        #    cv2.waitKey(1)
        
        cap.release()
        out.release()
        cv2.destroyAllWindows()
        
            
        d = {'Time': tiempo ,'Right_Hip_angle': RHip_angle ,'Right_Knee_angle': RKnee_angle, 'Right_Ankle_angle': RAnkle_angle,'Left_Hip_angle': LHip_angle ,'Left_Knee_angle': LKnee_angle, 'Left_Ankle_angle': LAnkle_angle, 'COMX': VCOMx, 'COMY': VCOMy}
        df = pd.DataFrame(data=d) 
        df.to_csv('MarchaSagital.csv') #GUARDAR EN CSV PARA FACILITAR ANALISIS DE FASES
          
        
        
        
        cap2 = cv2.VideoCapture('videoRESULTADO.avi')
        
        fps2 = cap2.get(cv2.CAP_PROP_FPS)
        duracion2 = cap2.get(cv2.CAP_PROP_FRAME_COUNT) / fps2
        largo2 = cap2.get(cv2.CAP_PROP_FRAME_COUNT)
        vectorTiempo2 = np.arange(largo)
        
        frame_width2 = int(cap2.get(3))
        frame_height2 = int(cap2.get(4))
        

        
        while self.hilo_corriendo:
            ret, frame = cap2.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                flip = Image
                convertir_QT = QImage(flip.data, flip.shape[1], flip.shape[0], QImage.Format_RGB888)
                pic = convertir_QT.scaled(800, 600, Qt.KeepAspectRatio)
                self.Imageupd.emit(pic)
                self.msleep(1000//30)
        
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