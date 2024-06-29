# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SUSESOvSEPT2.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

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
import time
import datetime

import jinja2
import pdfkit

from scipy.fft import fft, fftfreq # importa una parte de la libreria para calculo de fourier
from scipy import signal # importa parte de una libreria para manejo de se;ales
from scipy import integrate # importa libreria para calculo de integral
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

import ffmpeg # esta libreria se ocupa ya que videos de gopro tienen algunos
#problemas con opencv, segun los foros es un tema de sonido y formato.
#solucion momentanea es en base a esta libreria que permite correr ffmpeg 
#en python.



class Ui_MainWindow(object):
    def __init__(self):
        self.plano = 0  # Agregar la variable plano y definirla en el constructor


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1327, 936)
        MainWindow.setStyleSheet("QWidget#centralwidget{background-color: rgb(85,final2,127);}\n"
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
        self.pushButtonINFORME = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonINFORME.setGeometry(QtCore.QRect(540, 800, 251, 71))
        self.pushButtonINFORME.setAutoFillBackground(False)
        self.pushButtonINFORME.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(211, 215, 207);")
        self.pushButtonINFORME.setObjectName("pushButtonINFORME")
        
        self.labelLOGO = QtWidgets.QLabel(self.centralwidget)
        self.labelLOGO.setGeometry(QtCore.QRect(310, 20, 131, 121))
        self.labelLOGO.setStyleSheet("background-image: url(Logo_ACHS.png);")
        self.labelLOGO.setText("")
        self.labelLOGO.setPixmap(QtGui.QPixmap("Logo_ACHS.png"))
        self.labelLOGO.setScaledContents(True)
        self.labelLOGO.setObjectName("labelLOGO")
        self.labelLOGO2 = QtWidgets.QLabel(self.centralwidget)
        self.labelLOGO2.setGeometry(QtCore.QRect(520, 10, 241, 131))
        self.labelLOGO2.setStyleSheet("background-image: url(LOGO_SUSESO.png);")
        self.labelLOGO2.setText("")
        self.labelLOGO2.setPixmap(QtGui.QPixmap("LOGO_SUSESO.png"))
        self.labelLOGO2.setScaledContents(True)
        self.labelLOGO2.setObjectName("labelLOGO2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(90, 750, 801, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.lineNOMBRE = QtWidgets.QLineEdit(self.centralwidget)
        self.lineNOMBRE.setGeometry(QtCore.QRect(970, 310, 291, 31))
        self.lineNOMBRE.setObjectName("lineNOMBRE")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(970, 290, 300, 17))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEDAD = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEDAD.setGeometry(QtCore.QRect(970, 400, 291, 31))
        self.lineEDAD.setObjectName("lineEDAD")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(970, 470, 200, 17))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineDIAGNOSTICO = QtWidgets.QLineEdit(self.centralwidget)
        self.lineDIAGNOSTICO.setGeometry(QtCore.QRect(970, 490, 291, 31))
        self.lineDIAGNOSTICO.setObjectName("lineDIAGNOSTICO")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(970, 380, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(903, 140, 31, 631))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
#         self.pushButtonDATAPACIENTE = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButtonDATAPACIENTE.setEnabled(True)
#         self.pushButtonDATAPACIENTE.setGeometry(QtCore.QRect(970, 570, 191, 61))
#         self.pushButtonDATAPACIENTE.setAutoFillBackground(False)
#         self.pushButtonDATAPACIENTE.setStyleSheet("border-radius: 20px;\n"
# "background-color: rgb(211, 215, 207);")
#         self.pushButtonDATAPACIENTE.setAutoDefault(False)
#         self.pushButtonDATAPACIENTE.setObjectName("pushButtonDATAPACIENTE")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(870, 10, 161, 131))
        self.label_4.setStyleSheet("background-image: url(Logo_UCH.png);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Logo_UCH.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.botonSagital = QtWidgets.QPushButton(self.centralwidget)
        self.botonSagital.setGeometry(QtCore.QRect(210, 760, 161, 25))
        self.botonSagital.setObjectName("botonSagital")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 760, 161, 25))
        self.pushButton_2.setObjectName("pushButton_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1327, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.botonCARGAR.clicked.connect(self.cancel)
        self.botonCARGAR.clicked.connect(self.pushBotton_handler)
#        self.pushButtonINFORME.clicked.connect(lambda: self.abrir_pdf(ruta_salida))
#        self.pushButtonINFORME.clicked.connect(self.abrir_pdf)
#        self.pushButtonDATAPACIENTE.clicked.connect(self.cargarDATOSinforme)
        
        # Enlazar la función set_plano a los eventos de los botones
        self.botonSagital.clicked.connect(lambda: self.set_plano(0))
        self.pushButton_2.clicked.connect(lambda: self.set_plano(1))

        
    def start_video(self, path, nombre_usuario, edad_usuario, diagnostico_usuario, plano):
        self.Work = Work(path, nombre_usuario, edad_usuario, diagnostico_usuario, plano)
        self.Work.start()
        self.Work.Imageupd.connect(self.Imageupd_slot)
#        self.labelCARGANDO.setText("PROCESANDO VIDEO")
        
    def Imageupd_slot(self, Image):
        self.labelVIDEO.setPixmap(QPixmap.fromImage(Image))
        
    def cancel(self):
        self.labelVIDEO.clear()
        self.Work.stop()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.botonCARGAR.setText(_translate("MainWindow", "Cargar video"))
        self.pushButtonINFORME.setText(_translate("MainWindow", "Informe de resultados"))
        self.label.setText(_translate("MainWindow", "Nombre del usuario evaluado"))
        self.label_2.setText(_translate("MainWindow", "Diagnóstico médico"))
        self.label_3.setText(_translate("MainWindow", "Edad"))
        # self.pushButtonDATAPACIENTE.setText(_translate("MainWindow", "Cargar información"))
        self.botonSagital.setText(_translate("MainWindow", "Plano sagital"))
        self.pushButton_2.setText(_translate("MainWindow", "Plano frontal"))
       
    def pushBotton_handler(self):
        path = self.open_dialog_box()
        if path:
            nombre_usuario = self.lineNOMBRE.text()  # Obtener el contenido de lineNOMBRE
            edad_usuario = self.lineEDAD.text()
            diagnostico_usuario = self.lineDIAGNOSTICO.text()
            self.start_video(path, nombre_usuario, edad_usuario, diagnostico_usuario, self.plano)  # Pasa el nombre de usuario como argumento

        
    def open_dialog_box(self):
        filename, _ = QFileDialog.getOpenFileName()
        return filename
    
    def abrir_pdf(self, ruta_salida):
        # Ruta al archivo PDF que deseas abrir
        ruta_pdf = ruta_salida_final  # Utiliza la ruta de salida proporcionada como argumento
    
        # Abre el archivo PDF en el visor de PDF predeterminado
        QDesktopServices.openUrl(QUrl.fromLocalFile(ruta_pdf))
    
    # def update_progress(self, value):
    #         self.progressBar.setValue(value)
    
    def set_plano(self, valor):
        self.plano = valor
        print(self.plano)

class Work(QThread):
    Imageupd = pyqtSignal(QImage)
    
    def __init__(self, path, nombre_usuario, edad_usuario, diagnostico_usuario, plano):
        super().__init__()
        self.path = path
        self.nombre_usuario = nombre_usuario
        self.edad_usuario = edad_usuario
        self.diagnostico_usuario = diagnostico_usuario
        self.plano = plano
     # funcion para calculo del Centro de masa
    def calculate_center_of_mass(self,landmarks):
        x_values = [landmark.x for landmark in landmarks]
        y_values = [landmark.y for landmark in landmarks]
        z_values = [landmark.z for landmark in landmarks]
        center_x = sum(x_values) / len(landmarks)
        center_y = sum(y_values) / len(landmarks)
        center_z = sum(z_values) / len(landmarks)
        return center_x, center_y, center_z       
     

    def calculate_angle(self,a,b,c):
        a = np.array(a) #proximal
        b = np.array(b) #joint
        c = np.array(c) #distal
    
        radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
        angle = np.abs(radians*180.0/np.pi)
    
        if angle >180.0:
            angle = 360-angle
        return angle
    
    def crea_pdf(self,ruta_template, info, ruta_salida, rutacss=''):
        nombre_template = ruta_template.split('/')[-1]
        ruta_template = ruta_template.replace(nombre_template,'')
        
        env = jinja2.Environment(loader = jinja2.FileSystemLoader(ruta_template))
        template = env.get_template(nombre_template)
        html = template.render(info)
    
        options = {'page-size': 'Letter',
                   'margin-top': '0.5in',
                   'margin-right': '0.5in',
                   'margin-bottom': '0.5in',
                   'margin-left': '0.5in',
                   'encoding': 'UTF-8'}
    
        
        config = pdfkit.configuration(wkhtmltopdf = '/usr/bin/wkhtmltopdf')
        #ruta_salida = '/media/jose/DataDisk/Ubuntu/OpencvProject/PDF/informe4.pdf'
        # Obtenemos el timestamp actual en segundos como un número entero

        ruta_salida_final = '../PDF/' + ruta_salida
        
        pdfkit.from_string(html, ruta_salida_final, css=rutacss, options=options, configuration=config)
        QDesktopServices.openUrl(QUrl.fromLocalFile(ruta_salida_final))
        
    def convert_to_avi(self, input_file, output_file):
        ffmpeg.input(input_file).output(output_file, acodec='copy', vcodec='mpeg4').run()
    
    progressUpdated = pyqtSignal(int)  # Signal to update progress

    def run(self):
        self.hilo_corriendo = True
 #       print("Nombre del usuario:", self.nombre_usuario)
 #       print(self.plano)
        
        if self.plano == 0:
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
            
            input_video = self.path
            timestamp_video = int(time.time())
            
            # Convierte el timestamp a una cadena (string)
            timestamp_str_video = str(timestamp_video)
            output_video =  timestamp_str_video + 'SAGITAL.avi'

            self.convert_to_avi(input_video, output_video)

            print(f"Conversion completed: {input_video} -> {output_video}")
            
            #cap = cv2.VideoCapture(self.path)
            cap = cv2.VideoCapture(output_video)
            # Nuevos valores de calidad y fps deseados
            target_quality = 20  # Ajusta según tu preferencia (puedes experimentar con valores entre 0 y 100)
            target_fps = 200      # Ajusta según tu preferencia

            # Establece la calidad y fps deseados para la captura de video
            cap.set(cv2.CAP_PROP_FPS, target_fps)
            cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
#            cap.set(cv2.CAP_PROP_QUALITY, target_quality)

            
            mpDraw = mp.solutions.drawing_utils
            mpPose = mp.solutions.pose
            pose = mpPose.Pose()
            
            fps = cap.get(cv2.CAP_PROP_FPS)
            
#            fps = 20
            duracion = cap.get(cv2.CAP_PROP_FRAME_COUNT) / fps
            largo = cap.get(cv2.CAP_PROP_FRAME_COUNT)
            vectorTiempo = np.arange(largo)
            
            # siguiente linea es para la barra de progreso
            
            
            frame_width = int(cap.get(3))
            frame_height = int(cap.get(4))
            #fps = 30
            
            # Define la calidad y los fps deseados
            # target_quality = 20  # Ajusta según tu preferencia (puedes experimentar con valores entre 0 y 100)
            # target_fps = 15      # Ajusta según tu preferencia

            out = cv2.VideoWriter( timestamp_str_video +'RESULTADO.avi', cv2.VideoWriter_fourcc('M','J','P','G'), target_fps, (frame_width, frame_height))
            # Obtiene la información actualizada de calidad y fps
            fps = cap.get(cv2.CAP_PROP_FPS)
            quality = out.get(cv2.CAP_PROP_FOURCC)
            com = False
            p = 0
            q = 0
            cut = []
            
            a = 0
            while True:
                a = a + 1
     #           print (a)
    
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
                        print('inicio')
                        landmarks = results.pose_landmarks.landmark
                        print('landmark')
                
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
                #        print('antes de com')        
                        #center_x, center_y, center_z = self.calculate_center_of_mass(self,landmarks)
                #        print('despues com')
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
         #               print('apend bueno')
        
        
                        #VCOMx.append(center_x)
                        #VCOMy.append(center_y)
                        
                        
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
        
        
                        #VCOMxB.append(center_x)
                        #VCOMyB.append(center_y)
                        
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
        
        
                        # VCOMx.append(0)
                        # VCOMy.append(0)
                        cut.append(p)
                        
                        
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
            
                
            d = {'Time': tiempo ,'Right_Hip_angle': RHip_angle ,'Right_Knee_angle': RKnee_angle, 'Right_Ankle_angle': RAnkle_angle,'Left_Hip_angle': LHip_angle ,'Left_Knee_angle': LKnee_angle, 'Left_Ankle_angle': LAnkle_angle}
            df = pd.DataFrame(data=d) 
            df.to_csv('MarchaSagital.csv') #GUARDAR EN CSV PARA FACILITAR ANALISIS DE FASES
              
            
            fc1 = 5 # Cut-off frequency of the filter
            #w = fc / (fs / 2) # Normalize the frequency
            #b, a = signal.butter(4, w, 'low')
            b, a = signal.butter(N = 3, Wn = fc1 / (fps / 2), btype='lowpass')
            RHIP_FILT = signal.filtfilt(b, a, df.Right_Hip_angle)
            RKNEE_FILT = signal.filtfilt(b, a, df.Right_Knee_angle)
            RANKLE_FILT = signal.filtfilt(b, a, df.Right_Ankle_angle)
            LHIP_FILT = signal.filtfilt(b, a, df.Left_Hip_angle)
            LKNEE_FILT = signal.filtfilt(b, a, df.Left_Knee_angle)
            LANKLE_FILT = signal.filtfilt(b, a, df.Left_Ankle_angle)
            
            RightHeelTrajectoryX_filt = signal.filtfilt(b, a, RightHeelTrajectoryX)
            RightHeelTrajectoryY_filt = signal.filtfilt(b, a, RightHeelTrajectoryY)
            LeftHeelTrajectoryX_filt = signal.filtfilt(b, a, LeftHeelTrajectoryX)
            LeftHeelTrajectoryY_filt = signal.filtfilt(b, a, LeftHeelTrajectoryY)
            
            RightToeTrajectoryX_filt = signal.filtfilt(b, a, RightToeTrajectoryX)
            RightToeTrajectoryY_filt = signal.filtfilt(b, a, RightToeTrajectoryY)
            LeftToeTrajectoryX_filt = signal.filtfilt(b, a, LeftToeTrajectoryX)
            LeftToeTrajectoryY_filt = signal.filtfilt(b, a, LeftToeTrajectoryY)
            
            d2 = {'Time': tiempo , 'RHEEL_X': RightHeelTrajectoryX_filt, 'RHEEL_Y': RightHeelTrajectoryY_filt, 'LHEEL_X': LeftHeelTrajectoryX_filt, 'LHEEL_Y': LeftHeelTrajectoryY_filt, 'RTOE_X': RightToeTrajectoryX_filt, 'RTOE_Y': RightToeTrajectoryY_filt, 'LTOE_X': LeftToeTrajectoryX_filt, 'LTOE_Y': LeftToeTrajectoryY_filt}
            df2 = pd.DataFrame(data=d2) 
            df2.to_csv('KINEMATIC.csv') #GUARDAR EN CSV PARA FACILITAR ANALISIS DE FASES
    
            ventana = 5
            signal_conv_R = np.convolve(np.diff(RightHeelTrajectoryX_filt), np.ones(ventana) / float(ventana), 'same')
            signal_conv_L = np.convolve(np.diff(LeftHeelTrajectoryX_filt), np.ones(ventana) / float(ventana), 'same')
    
            umbral = 0.02
            apoyo = umbral * np.max(abs(signal_conv_R))
            apoyo2 = umbral * np.max(abs(signal_conv_L))
            tiempofaseapoyo = []
            fasesapoyo = []
            tiempofasebalanceo = []
            fasesbalanceo = []
            signalA = abs(signal_conv_R)
            
            tiempofaseapoyo2 = []
            fasesapoyo2 = []
            tiempofasebalanceo2 = []
            fasesbalanceo2 = []
            signalB = abs(signal_conv_L)
            
            largoSENAL2 = len(RHIP_FILT)
            inicio2 = int(0.5 * largoSENAL2)
            final2 = int(0.9 * largoSENAL2)
            
            for i in range (0,len(signalA)-1):
                if signalA[i] < apoyo:
                    tiempofaseapoyo.append(df.Time[i])
                    fasesapoyo.append(signalA[i])
                else:
                    tiempofasebalanceo.append(df.Time[i])
                    fasesbalanceo.append(signalA[i])
            
            for i in range (0,len(signalB)-1):
                if signalB[i] < apoyo2:
                    tiempofaseapoyo2.append(df.Time[i])
                    fasesapoyo2.append(signalB[i])
                else:
                    tiempofasebalanceo2.append(df.Time[i])
                    fasesbalanceo2.append(signalB[i])       
            

            
            print(cut)
    #        print(minimo1)
    #        print(maximo1)
            minimo1 = min(RHIP_FILT[inicio2:final2])
            maximo1 = max(RHIP_FILT[inicio2:final2])
            minimo2 = min(LHIP_FILT[inicio2:final2])
            maximo2 = max(LHIP_FILT[inicio2:final2])
            
    
            
            plt.figure(1)
            plt.plot(df.Time[inicio2:final2],RHIP_FILT[inicio2:final2], label = 'derecha')
            plt.plot(df.Time[inicio2:final2],LHIP_FILT[inicio2:final2], label = 'izquierda')
            plt.scatter(tiempofaseapoyo, [minimo1 - ( (maximo1 - minimo1) * 0.2 )] * len(fasesapoyo), color = 'red',marker = 's')
            plt.scatter(tiempofasebalanceo, [minimo1 - ( (maximo1 - minimo1) * 0.2 )] * len(fasesbalanceo), color = 'green',marker = 's')
            plt.scatter(tiempofaseapoyo2, [minimo1 - ( (maximo1 - minimo1) * 0.25 )] * len(fasesapoyo2), color = 'red',marker = 's')
            plt.scatter(tiempofasebalanceo2, [minimo1 - ( (maximo1 - minimo1) * 0.25 )] * len(fasesbalanceo2), color = 'green',marker = 's')
            plt.text(df.Time[165], minimo1 - ( (maximo1 - minimo1) * 0.2 ), "F. der")
            plt.text(df.Time[165], minimo1 - ( (maximo1 - minimo1) * 0.25 ), "F. izq")
            plt.xlabel('Tiempo [s]')
            plt.ylabel('Grados [º]')
            plt.title('Gráfico Plano Sagital cadera')
            plt.xlim(df.Time[inicio2], df.Time[final2]) 
            plt.legend()
            plt.savefig('plot1CADERA.png', dpi=300)  # Set the desired filename and DPI
            
            minimo1 = min(RHIP_FILT[inicio2:final2])
            maximo1 = max(RHIP_FILT[inicio2:final2])
            minimo2 = min(LHIP_FILT[inicio2:final2])
            maximo2 = max(LHIP_FILT[inicio2:final2])
            
            plt.figure(2)
            plt.plot(df.Time[inicio2:final2],RKNEE_FILT[inicio2:final2], label = 'derecha')
            plt.plot(df.Time[inicio2:final2],LKNEE_FILT[inicio2:final2], label = 'izquierda')
            plt.scatter(tiempofaseapoyo, [minimo1 -( (maximo1 - minimo1) * 0.2 )] * len(fasesapoyo), color = 'red',marker = 's')
            plt.scatter(tiempofasebalanceo, [minimo1 -( (maximo1 - minimo1) * 0.2 )] * len(fasesbalanceo), color = 'green',marker = 's')
            plt.scatter(tiempofaseapoyo2, [minimo1 -( (maximo1 - minimo1) * 0.25 )] * len(fasesapoyo2), color = 'red',marker = 's')
            plt.scatter(tiempofasebalanceo2, [minimo1 -( (maximo1 - minimo1) * 0.25 )] * len(fasesbalanceo2), color = 'green',marker = 's')
            plt.text(df.Time[[165]], minimo1 - ( (maximo1 - minimo1) * 0.2 ), "F. der")
            plt.text(df.Time[[165]], minimo1 - ( (maximo1 - minimo1) * 0.25 ), "F. izq")
            
            plt.xlabel('Tiempo [s]')
            plt.ylabel('Grados [º]')
            plt.title('Gráfico Plano Sagital rodilla')
            plt.legend()
            plt.xlim(df.Time[inicio2], df.Time[final2]) 
            plt.savefig('plotRODILLA.png', dpi=300)  # Set the desired filename and DPI
            
            
            minimo1 = min(RANKLE_FILT[inicio2:final2])
            minimo2 = min(LANKLE_FILT[inicio2:final2])
            maximo1 = max(RANKLE_FILT[inicio2:final2])
            maximo2 = max(LANKLE_FILT[inicio2:final2])
            plt.figure(3)
            plt.plot(df.Time[inicio2:final2],RANKLE_FILT[inicio2:final2], label = 'derecha')
            plt.plot(df.Time[inicio2:final2],LANKLE_FILT[inicio2:final2], label = 'izquierda')
            plt.scatter(tiempofaseapoyo, [minimo1 -( (maximo1 - minimo1) * 0.2 )] * len(fasesapoyo), color = 'red',marker = 's')
            plt.scatter(tiempofasebalanceo, [minimo1 -( (maximo1 - minimo1) * 0.2 )] * len(fasesbalanceo), color = 'green',marker = 's')
            plt.scatter(tiempofaseapoyo2, [minimo1 -( (maximo1 - minimo1) * 0.25 )] * len(fasesapoyo2), color = 'red',marker = 's')
            plt.scatter(tiempofasebalanceo2, [minimo1 -( (maximo1 - minimo1) * 0.25 )] * len(fasesbalanceo2), color = 'green',marker = 's')
            plt.text(df.Time[165], minimo1 - ( (maximo1 - minimo1) * 0.2 ), "F. der")
            plt.text(df.Time[165], minimo1 - ( (maximo1 - minimo1) * 0.25 ), "F. izq")
            
            plt.xlabel('Tiempo [s]')
            plt.ylabel('Grados [º]')
            plt.title('Gráfico Plano Sagital tobillo')
            plt.xlim(df.Time[inicio2], df.Time[final2]) 
            plt.legend()
            plt.savefig('plotTOBILLO.png', dpi=300)  # Set the desired filename and DPI
            
            ############################# generar pdf
            fecha_hora_actual = datetime.datetime.now()
            timestamp_str = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")
            year = fecha_hora_actual.strftime("%Y")
            month = fecha_hora_actual.strftime("%m")
            day = fecha_hora_actual.strftime("%d")
    
            ruta_template = '/media/jose/DataDisk/Ubuntu/OpencvProject/PDF/template.html'
            info = {"NOMBRE_PACIENTE": str(self.nombre_usuario) , "EDAD_PACIENTE": str(self.edad_usuario),
                    "DIAGNOSTICO_PACIENTE": str(self.diagnostico_usuario),
                    "DIA": str(day), "MES": str(month), "YEAR": str(year),
                    "tiempoAPOYOderecho": 0.63, "tiempoAPOYOizquierdo": 0.65,
                    "tiempoBALANCEOderecho": 0.53, "tiempoBALANCEOizquierdo": 0.54,
                    "tiempoDOBLEapoyo": 0.2, "tiempoCICLO": 1.1,
                    "caderaDERECHA": str(round(max(RHIP_FILT))) + '  -  ' + str((round(min(RHIP_FILT)))), "caderaIZQUIERDA": str(round(max(LHIP_FILT))) + '  -  ' + str((round(min(LHIP_FILT)))),
                    "rodillaDERECHA": str(round(max(RKNEE_FILT))) + '  -  ' + str((round(min(RKNEE_FILT)))), "rodillaIZQUIERDA": str(round(max(LKNEE_FILT))) + '  -  ' + str((round(min(LKNEE_FILT)))),
                    "tobilloDERECHO": str(round(max(RANKLE_FILT))) + '  -  ' + str((round(-min(RANKLE_FILT)))), "tobilloIZQUIERDO" : str(round(max(LANKLE_FILT))) + '  -  ' + str((round(-min(LANKLE_FILT))))}
            #print(str(round(max(RANKLE_FILT))) + '  ' + str((round(min(RANKLE_FILT)))))
            timestamp = int(time.time())
            
            # Convierte el timestamp a una cadena (string)
            timestamp_str = str(timestamp)
            #INFORME PLANO SAGITAL
            self.crea_pdf(ruta_template, info, timestamp_str) 
            print('linea post pdf')               
                    
    ##############################################################        
            cap2 = cv2.VideoCapture('videoRESULTADO.avi')
    
            
            fps2 = cap2.get(cv2.CAP_PROP_FPS)
            duracion2 = cap2.get(cv2.CAP_PROP_FRAME_COUNT) / fps2
            largo2 = cap2.get(cv2.CAP_PROP_FRAME_COUNT)
            vectorTiempo2 = np.arange(largo)
            
            frame_width2 = int(cap2.get(3))
            frame_height2 = int(cap2.get(4))
            print('plano')
            print(self.plano)
            
    
            
            while self.hilo_corriendo:
                ret, frame = cap2.read()
                if ret:
                    Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    flip = Image
                    convertir_QT = QImage(flip.data, flip.shape[1], flip.shape[0], QImage.Format_RGB888)
                    pic = convertir_QT.scaled(800, 600, Qt.KeepAspectRatio)
                    self.Imageupd.emit(pic)
                    self.msleep(1000//30)
                    
        else:
            #codigo plano frontal
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
            
            input_video = self.path
            timestamp_video = int(time.time())
            
            # Convierte el timestamp a una cadena (string)
            timestamp_str_video = str(timestamp_video)
            output_video =  + timestamp_str_video + 'FRONTAL.avi'

            self.convert_to_avi(input_video, output_video)

            print(f"Conversion completed: {input_video} -> {output_video}")
            
            #cap = cv2.VideoCapture(self.path)
            cap = cv2.VideoCapture(output_video)
            # Nuevos valores de calidad y fps deseados
            target_quality = 20  # Ajusta según tu preferencia (puedes experimentar con valores entre 0 y 100)
            target_fps = 100      # Ajusta según tu preferencia

            # Establece la calidad y fps deseados para la captura de video
            cap.set(cv2.CAP_PROP_FPS, target_fps)
            cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
#            cap.set(cv2.CAP_PROP_QUALITY, target_quality)

            
            mpDraw = mp.solutions.drawing_utils
            mpPose = mp.solutions.pose
            pose = mpPose.Pose()
            
            fps = cap.get(cv2.CAP_PROP_FPS)
            
#            fps = 20
            duracion = cap.get(cv2.CAP_PROP_FRAME_COUNT) / fps
            largo = cap.get(cv2.CAP_PROP_FRAME_COUNT)
            vectorTiempo = np.arange(largo)
            
            # siguiente linea es para la barra de progreso
            
            
            frame_width = int(cap.get(3))
            frame_height = int(cap.get(4))
            #fps = 30
            
            # Define la calidad y los fps deseados
            # target_quality = 20  # Ajusta según tu preferencia (puedes experimentar con valores entre 0 y 100)
            # target_fps = 15      # Ajusta según tu preferencia

            out = cv2.VideoWriter('videoRESULTADO.avi', cv2.VideoWriter_fourcc('M','J','P','G'), target_fps, (frame_width, frame_height))
            # Obtiene la información actualizada de calidad y fps
            fps = cap.get(cv2.CAP_PROP_FPS)
            quality = out.get(cv2.CAP_PROP_FOURCC)
            com = False
            p = 0
            q = 0
            cut = []
            
            a = 0
            while True:
                a = a + 1
                print (a)
    
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
                        print('inicio')
                        landmarks = results.pose_landmarks.landmark
                        print('landmark')
                
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
                        print('antes de com')        
                        #center_x, center_y, center_z = self.calculate_center_of_mass(self,landmarks)
                        print('despues com')
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
                        RKnee_angle.append(Right_Knee_angle)
                        RAnkle_angle.append(Right_Ankle_angle)
                        LHip_angle.append(180 - Left_Hip_angle)
                        LKnee_angle.append(Left_Knee_angle)
                        LAnkle_angle.append(Left_Ankle_angle)
                        tiempo.append(vectorTiempo[p] / fps)
                        RightHeelTrajectoryX.append(Right_Heel[0])
                        RightHeelTrajectoryY.append(Right_Heel[1])
                        LeftHeelTrajectoryX.append(Left_Heel[0])
                        LeftHeelTrajectoryY.append(Left_Heel[1])
                        RightToeTrajectoryX.append(Right_Toe[0])
                        RightToeTrajectoryY.append(Right_Toe[1])
                        LeftToeTrajectoryX.append(Left_Toe[0])
                        LeftToeTrajectoryY.append(Left_Toe[1])
                        print('apend bueno')
        
        
                        #VCOMx.append(center_x)
                        #VCOMy.append(center_y)
                        
                        
                        RHip_angleB.append(180 - Right_Hip_angle)
                        RKnee_angleB.append(Right_Knee_angle)
                        RAnkle_angleB.append(180 - Right_Ankle_angle)
                        LHip_angleB.append(180 - Left_Hip_angle)
                        LKnee_angleB.append(Left_Knee_angle)
                        LAnkle_angleB.append(180 - Left_Ankle_angle)
                        tiempoB.append(vectorTiempo[q] / fps)
                        RightHeelTrajectoryXB.append(Right_Heel[0])
                        RightHeelTrajectoryYB.append(Right_Heel[1])
                        LeftHeelTrajectoryXB.append(Left_Heel[0])
                        LeftHeelTrajectoryYB.append(Left_Heel[1])
                        RightToeTrajectoryXB.append(Right_Toe[0])
                        RightToeTrajectoryYB.append(Right_Toe[1])
                        LeftToeTrajectoryXB.append(Left_Toe[0])
                        LeftToeTrajectoryYB.append(Left_Toe[1])
        
        
                        #VCOMxB.append(center_x)
                        #VCOMyB.append(center_y)
                        
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
        
        
                        # VCOMx.append(0)
                        # VCOMy.append(0)
                        cut.append(p)
                        
                        
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
            
                
            d = {'Time': tiempo ,'Right_Hip_angle': RHip_angle ,'Right_Knee_angle': RKnee_angle, 'Right_Ankle_angle': RAnkle_angle,'Left_Hip_angle': LHip_angle ,'Left_Knee_angle': LKnee_angle, 'Left_Ankle_angle': LAnkle_angle}
            df = pd.DataFrame(data=d) 
            df.to_csv('MarchaSagital.csv') #GUARDAR EN CSV PARA FACILITAR ANALISIS DE FASES
              
            
            fc1 = 5 # Cut-off frequency of the filter
            #w = fc / (fs / 2) # Normalize the frequency
            #b, a = signal.butter(4, w, 'low')
            b, a = signal.butter(N = 3, Wn = fc1 / (fps / 2), btype='lowpass')
            RHIP_FILT = signal.filtfilt(b, a, df.Right_Hip_angle)
            RKNEE_FILT = signal.filtfilt(b, a, df.Right_Knee_angle)
            RANKLE_FILT = signal.filtfilt(b, a, df.Right_Ankle_angle)
            LHIP_FILT = signal.filtfilt(b, a, df.Left_Hip_angle)
            LKNEE_FILT = signal.filtfilt(b, a, df.Left_Knee_angle)
            LANKLE_FILT = signal.filtfilt(b, a, df.Left_Ankle_angle)
            
            RightHeelTrajectoryX_filt = signal.filtfilt(b, a, RightHeelTrajectoryX)
            RightHeelTrajectoryY_filt = signal.filtfilt(b, a, RightHeelTrajectoryY)
            LeftHeelTrajectoryX_filt = signal.filtfilt(b, a, LeftHeelTrajectoryX)
            LeftHeelTrajectoryY_filt = signal.filtfilt(b, a, LeftHeelTrajectoryY)
            
            RightToeTrajectoryX_filt = signal.filtfilt(b, a, RightToeTrajectoryX)
            RightToeTrajectoryY_filt = signal.filtfilt(b, a, RightToeTrajectoryY)
            LeftToeTrajectoryX_filt = signal.filtfilt(b, a, LeftToeTrajectoryX)
            LeftToeTrajectoryY_filt = signal.filtfilt(b, a, LeftToeTrajectoryY)
            
            d2 = {'Time': tiempo , 'RHEEL_X': RightHeelTrajectoryX_filt, 'RHEEL_Y': RightHeelTrajectoryY_filt, 'LHEEL_X': LeftHeelTrajectoryX_filt, 'LHEEL_Y': LeftHeelTrajectoryY_filt, 'RTOE_X': RightToeTrajectoryX_filt, 'RTOE_Y': RightToeTrajectoryY_filt, 'LTOE_X': LeftToeTrajectoryX_filt, 'LTOE_Y': LeftToeTrajectoryY_filt}
            df2 = pd.DataFrame(data=d2) 
            df2.to_csv('KINEMATIC.csv') #GUARDAR EN CSV PARA FACILITAR ANALISIS DE FASES
    
            ventana = 5
            signal_conv_R = np.convolve(np.diff(RightHeelTrajectoryX_filt), np.ones(ventana) / float(ventana), 'same')
            signal_conv_L = np.convolve(np.diff(LeftHeelTrajectoryX_filt), np.ones(ventana) / float(ventana), 'same')
    
            umbral = 0.02
            apoyo = umbral * np.max(abs(signal_conv_R))
            apoyo2 = umbral * np.max(abs(signal_conv_L))
            tiempofaseapoyo = []
            fasesapoyo = []
            tiempofasebalanceo = []
            fasesbalanceo = []
            signalA = abs(signal_conv_R)
            
            tiempofaseapoyo2 = []
            fasesapoyo2 = []
            tiempofasebalanceo2 = []
            fasesbalanceo2 = []
            signalB = abs(signal_conv_L)
            
            largoSENAL2 = len(RHIP_FILT)
            inicio2 = int(0.5 * largoSENAL2)
            final2 = int(0.9 * largoSENAL2)           
            
            
            for i in range (0,len(signalA)-1):
                if signalA[i] < apoyo:
                    tiempofaseapoyo.append(df.Time[i])
                    fasesapoyo.append(signalA[i])
                else:
                    tiempofasebalanceo.append(df.Time[i])
                    fasesbalanceo.append(signalA[i])
            
            for i in range (0,len(signalB)-1):
                if signalB[i] < apoyo2:
                    tiempofaseapoyo2.append(df.Time[i])
                    fasesapoyo2.append(signalB[i])
                else:
                    tiempofasebalanceo2.append(df.Time[i])
                    fasesbalanceo2.append(signalB[i])       
           
            

            print(cut)
    #        print(minimo1)
    #        print(maximo1)
            minimo1 = min(RHIP_FILT[inicio2:final2])
            maximo1 = max(RHIP_FILT[inicio2:final2])
            minimo2 = min(LHIP_FILT[inicio2:final2])
            maximo2 = max(LHIP_FILT[inicio2:final2])
            

            
            plt.figure(1)
            plt.plot(df.Time[inicio2:final2],RHIP_FILT[inicio2:final2], label = 'derecha')
            plt.plot(df.Time[inicio2:final2],LHIP_FILT[inicio2:final2], label = 'izquierda')
            plt.scatter(tiempofaseapoyo, [minimo1 - ( (maximo1 - minimo1) * 0.2 )] * len(fasesapoyo), color = 'red',marker = 's')
            plt.scatter(tiempofasebalanceo, [minimo1 - ( (maximo1 - minimo1) * 0.2 )] * len(fasesbalanceo), color = 'green',marker = 's')
            plt.scatter(tiempofaseapoyo2, [minimo1 - ( (maximo1 - minimo1) * 0.25 )] * len(fasesapoyo2), color = 'red',marker = 's')
            plt.scatter(tiempofasebalanceo2, [minimo1 - ( (maximo1 - minimo1) * 0.25 )] * len(fasesbalanceo2), color = 'green',marker = 's')
            plt.text(df.Time[165], minimo1 - ( (maximo1 - minimo1) * 0.2 ), "F. der")
            plt.text(df.Time[165], minimo1 - ( (maximo1 - minimo1) * 0.25 ), "F. izq")
            plt.xlabel('Tiempo [s]')
            plt.ylabel('Grados [º]')
            plt.title('Gráfico Plano Frontal cadera')
            plt.xlim(df.Time[inicio2], df.Time[final2]) 
            plt.legend()
            plt.savefig('plot2CADERA.png', dpi=300)  # Set the desired filename and DPI
            
            minimo1 = min(RHIP_FILT[inicio2:final2])
            maximo1 = max(RHIP_FILT[inicio2:final2])
            minimo2 = min(LHIP_FILT[inicio2:final2])
            maximo2 = max(LHIP_FILT[inicio2:final2])
            
            plt.figure(2)
            plt.plot(df.Time[inicio2:final2],RKNEE_FILT[inicio2:final2], label = 'derecha')
            plt.plot(df.Time[inicio2:final2],LKNEE_FILT[inicio2:final2], label = 'izquierda')
            plt.scatter(tiempofaseapoyo, [minimo1 -( (maximo1 - minimo1) * 0.2 )] * len(fasesapoyo), color = 'red',marker = 's')
            plt.scatter(tiempofasebalanceo, [minimo1 -( (maximo1 - minimo1) * 0.2 )] * len(fasesbalanceo), color = 'green',marker = 's')
            plt.scatter(tiempofaseapoyo2, [minimo1 -( (maximo1 - minimo1) * 0.25 )] * len(fasesapoyo2), color = 'red',marker = 's')
            plt.scatter(tiempofasebalanceo2, [minimo1 -( (maximo1 - minimo1) * 0.25 )] * len(fasesbalanceo2), color = 'green',marker = 's')
            plt.text(df.Time[[165]], minimo1 - ( (maximo1 - minimo1) * 0.2 ), "F. der")
            plt.text(df.Time[[165]], minimo1 - ( (maximo1 - minimo1) * 0.25 ), "F. izq")
            
            plt.xlabel('Tiempo [s]')
            plt.ylabel('Grados [º]')
            plt.title('Gráfico Plano Frontal rodilla')
            plt.legend()
            plt.xlim(df.Time[inicio2], df.Time[final2]) 
            plt.savefig('plot2RODILLA.png', dpi=300)  # Set the desired filename and DPI
            
            
            minimo1 = min(RANKLE_FILT[inicio2:final2])
            minimo2 = min(LANKLE_FILT[inicio2:final2])
            maximo1 = max(RANKLE_FILT[inicio2:final2])
            maximo2 = max(LANKLE_FILT[inicio2:final2])
            plt.figure(3)
            plt.plot(df.Time[inicio2:final2],RANKLE_FILT[inicio2:final2], label = 'derecha')
            plt.plot(df.Time[inicio2:final2],LANKLE_FILT[inicio2:final2], label = 'izquierda')
            plt.scatter(tiempofaseapoyo, [minimo1 -( (maximo1 - minimo1) * 0.2 )] * len(fasesapoyo), color = 'red',marker = 's')
            plt.scatter(tiempofasebalanceo, [minimo1 -( (maximo1 - minimo1) * 0.2 )] * len(fasesbalanceo), color = 'green',marker = 's')
            plt.scatter(tiempofaseapoyo2, [minimo1 -( (maximo1 - minimo1) * 0.25 )] * len(fasesapoyo2), color = 'red',marker = 's')
            plt.scatter(tiempofasebalanceo2, [minimo1 -( (maximo1 - minimo1) * 0.25 )] * len(fasesbalanceo2), color = 'green',marker = 's')
            plt.text(df.Time[165], minimo1 - ( (maximo1 - minimo1) * 0.2 ), "F. der")
            plt.text(df.Time[165], minimo1 - ( (maximo1 - minimo1) * 0.25 ), "F. izq")
            
            plt.xlabel('Tiempo [s]')
            plt.ylabel('Grados [º]')
            plt.title('Gráfico Plano Frontal tobillo')
            plt.xlim(df.Time[inicio2], df.Time[final2]) 
            plt.legend()
            plt.savefig('plot2TOBILLO.png', dpi=300)  # Set the desired filename and DPI
            
            ############################# generar pdf
            fecha_hora_actual = datetime.datetime.now()
            timestamp_str = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")
            year = fecha_hora_actual.strftime("%Y")
            month = fecha_hora_actual.strftime("%m")
            day = fecha_hora_actual.strftime("%d")
    
            ruta_template = '/media/jose/DataDisk/Ubuntu/OpencvProject/PDF/template2.html'
            info = {"NOMBRE_PACIENTE": str(self.nombre_usuario) , "EDAD_PACIENTE": str(self.edad_usuario),
                    "DIAGNOSTICO_PACIENTE": str(self.diagnostico_usuario),
                    "DIA": str(day), "MES": str(month), "YEAR": str(year),
                    "tiempoAPOYOderecho": 0.63, "tiempoAPOYOizquierdo": 0.65,
                    "tiempoBALANCEOderecho": 0.53, "tiempoBALANCEOizquierdo": 0.54,
                    "tiempoDOBLEapoyo": 0.2, "tiempoCICLO": 1.1,
                    "caderaDERECHA": str(round(max(RHIP_FILT))) + '  -  ' + str((round(min(RHIP_FILT)))), "caderaIZQUIERDA": str(round(max(LHIP_FILT))) + '  -  ' + str((round(min(LHIP_FILT)))),
                    "rodillaDERECHA": str(round(max(RKNEE_FILT))) + '  -  ' + str((round(min(RKNEE_FILT)))), "rodillaIZQUIERDA": str(round(max(LKNEE_FILT))) + '  -  ' + str((round(min(LKNEE_FILT)))),
                    "tobilloDERECHO": str(round(max(RANKLE_FILT))) + '  -  ' + str((round(-min(RANKLE_FILT)))), "tobilloIZQUIERDO" : str(round(max(LANKLE_FILT))) + '  -  ' + str((round(-min(LANKLE_FILT))))}
            #print(str(round(max(RANKLE_FILT))) + '  ' + str((round(min(RANKLE_FILT)))))
            timestamp = int(time.time())
            
            # Convierte el timestamp a una cadena (string)
            timestamp_str = str(timestamp)
            #INFORME PLANO FRONTAL
            self.crea_pdf(ruta_template, info, timestamp_str) 
            print('linea post pdf')               
                    
    ##############################################################        
            cap2 = cv2.VideoCapture('videoRESULTADO.avi')
    
            
            fps2 = cap2.get(cv2.CAP_PROP_FPS)
            duracion2 = cap2.get(cv2.CAP_PROP_FRAME_COUNT) / fps2
            largo2 = cap2.get(cv2.CAP_PROP_FRAME_COUNT)
            vectorTiempo2 = np.arange(largo)
            
            frame_width2 = int(cap2.get(3))
            frame_height2 = int(cap2.get(4))
            print('plano')
            print(self.plano)
            
    
            
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
