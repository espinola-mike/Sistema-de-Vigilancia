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

# @app.route('/ondemand')
# def ondemand():
#     """ Función para renderizar la pagina (VideoOnDemand) """
#     return render_template('ondemand.html')

#Rutas para las respuestas de las cámaras
@app.route('/camara1')
def camara1():
    #2Do-Parametro; tipo de contenido donde multipart... es usado
    #para obtener una secuencia en la que cada parte replace a la anterior
    return Response(generate(c1), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/camara2')
def camara2():
    return Response(generate(c2), mimetype='multipart/x-mixed-replace; boundary=frame')
    
# Rutas para el video ondemand

def es_bisiesto(anio: int) -> bool:
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)


def obtener_dias_del_mes(mes: int, anio: int) -> int:
    # Abril, junio, septiembre y noviembre tienen 30
    if mes in [4, 6, 9, 11]:
        return 30
    # Febrero depende de si es o no bisiesto
    if mes == 2:
        if es_bisiesto(anio):
            return 29
        else:
            return 28
    else:
        # En caso contrario, tiene 31 días
        return 31


print(obtener_dias_del_mes(2,2022))


@app.route('/ondemand')
def ondemand():
    """ Función para renderizar la pagina (VideoOnDemand) """
    data = {
        'video1': 'video/vid.mp4',
        'video2': 'video/vid.mp4',
        'video3': 'video/vid.mp4',
        'video4': 'video/vid.mp4',
        'video5': 'video/vid.mp4',
        'video6': 'video/vid.mp4',
        'video7': 'video/vid.mp4',
        'video8': 'video/vid.mp4'
    }
    video = '#'

    return render_template('ondemand.html', video=video, data=data)


@app.route('/ondemand/<video>')
def ondemand_video(video):
    """ Función para renderizar la pagina (VideoOnDemand) """
    data = {
        'video1': 'video/vid.mp4',
        'video2': 'video/vid.mp4',
        'video3': 'video/vid.mp4',
        'video4': 'video/vid.mp4',
        'video5': 'video/vid.mp4',
        'video6': 'video/vid.mp4',
        'video7': 'video/vid.mp4',
        'video8': 'video/vid.mp4'
    }
    if len(video) == 0:
        video = '#'

    return render_template('ondemand.html', video=video, data=data)





def pagina_no_encontrada(error):
    """ Función para renderizar la pagina principal por algun error 404 """
    return redirect(url_for('index'))

if __name__ == '__main__': #Si estamos en el archivo main (inicial), se ejecuta la aplicación
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)
