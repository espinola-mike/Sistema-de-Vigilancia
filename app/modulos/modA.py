""" Creación del módulo 1 para captar video en vivo """
import cv2

def captura(camara):
    while True:
        camara.grab()
        ret, frame = camara.retrieve(0)
        if not ret:
            break
        #Comprime la imagen y la almacena en el buffer de memoria
        #Se codificará en JPG para reducir la carga en la red
        (flag, buffer) = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        #Se verifica si la imagen ha sido codificada
        if not flag:
            continue
        #Funcion para generar cada frame codificado en jpg
        #Como una matriz de bytes para que sea consumido por
        #el navegador
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
              bytearray(frame) + b'\r\n')