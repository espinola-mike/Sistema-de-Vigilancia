""" Aplicación Principal para el Sistema de Vigilancia """
from flask import Flask, render_template, url_for, redirect, Response # Clases Importadas
from modulos.modA import *
import cv2

app = Flask(__name__) #Se inicializa una aplicación

#Camaras:
c1 = cv2.VideoCapture(0)
""" c2 = cv2.VideoCapture('http://192.168.1.3:4747/video') """

#Configuraciones de las Cámaras
exp_val = -6
codec = 0x47504A4D # MJPG

#Camara 1

#Camara 2
""" c2.set(cv2.CAP_PROP_FPS, 30.0)
c2.set(cv2.CAP_PROP_FOURCC, codec)
c2.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
c2.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
c2.set(cv2.CAP_PROP_EXPOSURE, exp_val) """

#Camara 3

#Camara 4

#Función para generar el streaming en el navegador
def generate(camara):
    return captura(camara)

""" RUTAS de la APP """
@app.route('/')
def index():
    """ Función para renderizar la pagina principal (VideoStreaming) """
    return render_template('index.html')

@app.route('/ondemand')
def ondemand():
    """ Función para renderizar la pagina (VideoOnDemand) """
    return render_template('ondemand.html')

#Rutas para las respuestas de las cámaras
@app.route('/camara1')
def camara1():
    #2Do-Parametro; tipo de contenido donde multipart... es usado
    #para obtener una secuencia en la que cada parte replace a la anterior
    return Response(generate(c1), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/camara2')
def camara2():
    return Response(generate(c2), mimetype='multipart/x-mixed-replace; boundary=frame')
    
def pagina_no_encontrada(error):
    """ Función para renderizar la pagina principal por algun error 404 """
    return redirect(url_for('index'))

if __name__ == '__main__': #Si estamos en el archivo main (inicial), se ejecuta la aplicación
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=False, port=5000)
