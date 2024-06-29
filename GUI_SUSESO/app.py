# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'video.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2

import mediapipe as mp
import cv2
import numpy as np
import csv
import os
import pandas as pd
import time

# para seleccionar ruta de video
import tkinter as tk
from tkinter import filedialog

from PIL import Image, ImageTk


mp_drawing = mp.solutions.drawing_utils # utilidades para dibujar de mediapipe
mp_pose = mp.solutions.pose # importa la estimacion de postura


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
        self.botonCARGAR.clicked.connect(self.start_video)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def start_video(self):
        self.Work = Work()
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

class Work(QThread):
    Imageupd = pyqtSignal(QImage)
    def run(self):
        
        def calculate_angle(a,b,c):
            a = np.array(a) #proximal
            b = np.array(b) #joint
            c = np.array(c) #distal
            
            radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
            angle = np.abs(radians*180.0/np.pi)
            
            if angle >180.0:
                angle = 360-angle
            return angle
        
        # funcion para calculo del Centro de masa
        def calculate_center_of_mass(landmarks):
            x_values = [landmark.x for landmark in landmarks]
            y_values = [landmark.y for landmark in landmarks]
            z_values = [landmark.z for landmark in landmarks]
            center_x = sum(x_values) / len(landmarks)
            center_y = sum(y_values) / len(landmarks)
            center_z = sum(z_values) / len(landmarks)
            return center_x, center_y, center_z
        
        root = tk.Tk()
        root.withdraw()
        
        # Muestra un cuadro de diálogo para seleccionar un archivo de video
        file_path = filedialog.askopenfilename(
            title='Seleccionar archivo de video',
            filetypes=(('Archivos de video', '*.mp4 *.avi *.mov'), ('Todos los archivos', '*.*'))
        )
        if file_path:
            cap = cv2.VideoCapture(file_path)
        #cap = cv2.VideoCapture(0) # linea para usar webcam
        #cap = cv2.VideoCapture('/media/jose/DataDisk/Ubuntu/OpencvProject/VideosEnzo/Sagital1.MP4') # indicar ruta de video
        
        fps = cap.get(cv2.CAP_PROP_FPS)
        duracion = cap.get(cv2.CAP_PROP_FRAME_COUNT) / fps
        largo = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        vectorTiempo = np.arange(largo)
        
        # vectores vacios para ir agregando resultados
        
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
        
        #  para escribir un video, requiere de altura y ancho
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        out = cv2.VideoWriter('output03062023.avi',cv2.VideoWriter_fourcc('M','J','P','G'), fps, (800,600))

        #la siguiente linea pone como condicion que tan seguro esta del estimador
        com = False
        #start_time = time.time()
        p = 0
        q = 0
        

        with mp_pose.Pose(min_detection_confidence = 0.8, min_tracking_confidence=0.8) as pose:
            while cap.isOpened():
                ret, frame = cap.read() # frame es la imagen
                #check imagen
                if ret:
                    
                    frame = cv2.resize(frame,(800,600)) # esto permite cambiar tamaño de las imegenes del video generado
                    # detectar pose y dibujarla
                    # cambio de BGR a RGB
                    # opencv trabaja en formato BGR, asi que hay que cambiar el orden del array de colores
                    
                    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
            #        image.flags.writeable = False # para salvar memoria
                    
                    # deteccion
                    results = pose.process(image) 
                    
                    # solucionar esta linea, crea doble sujeto
            #        image.flags.writeable = True
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                    
                    
                    try:
                        landmarks = results.pose_landmarks.landmark
                        
                        # obtener coordenadas de centros de rotacion            
                        Right_Shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                        Right_Hip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
                        Right_Knee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
                        Right_Ankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
                        Right_Heel = [landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value].y]
                        Right_Toe = [landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].y]
                        Left_Shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                        Left_Hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                        Left_Knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                        Left_Ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
                        Left_Heel = [landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].y]
                        Left_Toe = [landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].x,landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].y]
                        # hay que corregir COM, ya que esta fijo en los ejes
                        # de momento podria hacer una ecuacion que normalice en base altura y ancho de la persona
                        #COMx = (Right_Hip[0] + Left_Hip[0])/2
                        #COMy = (Right_Hip[1] + Left_Hip[1])/2
                        center_x, center_y, center_z = calculate_center_of_mass(landmarks)
                        com = True
                        # calcular tiempo
                        #end_time = time.time()
                        #time_lapsed = end_time - start_time
                        
                        # calcular angulos EEII
                        Right_Hip_angle = calculate_angle(Right_Shoulder,Right_Hip,Right_Knee)
                        Right_Knee_angle = calculate_angle(Right_Hip,Right_Knee,Right_Ankle)
                        Right_Ankle_angle = calculate_angle(Right_Knee,Right_Heel,Right_Toe)
                        Left_Hip_angle = calculate_angle(Left_Shoulder,Left_Hip,Left_Knee)
                        Left_Knee_angle = calculate_angle(Left_Hip,Left_Knee,Left_Ankle)
                        Left_Ankle_angle = calculate_angle(Left_Knee,Left_Heel,Left_Toe)
                       
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
                    
                    
                    # Dibujar estimador, centros de rotacion y segmento en formato BGR
                    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                              mp_drawing.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=2),
                                              mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2)) 
                    
                    if com == True:
                       ## print('dibujo COM')
                        
                        cv2.circle(image, np.multiply([center_x,center_y],[800,600]).astype(int), 7, (0,255,255), -1)
                    
                    else:
                        pass
                    out.write(image)
                    #print('out')
                    #cv2.imshow("Analisis de Marcha SUSESO", image) #plotea imagen
                    #cv2.waitKey(1)
    
    
                    Image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    #flip = cv2.flip(Image, 1)
                    convertir_QT = QImage(Image.data, Image.shape[1], Image.shape[0], QImage.Format_RGB888)
                    pic = convertir_QT.scaled(800,600, Qt.KeepAspectRatio)
                    self.Imageupd.emit(pic)
                        
                    
                    
                    #if cv2.waitKey(10) & 0xFF == ord('q'):
                    #    break
                
                else:
                    break
                
            cap.release()
            out.release()
     #       cv2.destroyAllWindows()
            
        d = {'Time': tiempo ,'Right_Hip_angle': RHip_angle ,'Right_Knee_angle': RKnee_angle, 'Right_Ankle_angle': RAnkle_angle,'Left_Hip_angle': LHip_angle ,'Left_Knee_angle': LKnee_angle, 'Left_Ankle_angle': LAnkle_angle, 'COMX': VCOMx, 'COMY': VCOMy}
        df = pd.DataFrame(data=d) 
        df.to_csv('MarchaSagital.csv') #GUARDAR EN CSV PARA FACILITAR ANALISIS DE FASES

            
            
            
            

                
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
