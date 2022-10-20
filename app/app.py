""" Aplicación Principal para el Sistema de Vigilancia """
from flask import Flask, render_template, url_for, redirect # Clases Importadas

app = Flask(__name__) #Se inicializa una aplicación

""" RUTAS de la APP """
@app.route('/')
def index():
    """ Función para renderizar la pagina principal (VideoStreaming) """
    return render_template('index.html')

@app.route('/ondemand')
def ondemand():
    """ Función para renderizar la pagina (VideoOnDemand) """
    return render_template('ondemand.html')

def pagina_no_encontrada(error):
    """ Función para renderizar la pagina principal por algun error 404 """
    return redirect(url_for('index'))

if __name__ == '__main__': #Si estamos en el archivo main (inicial), se ejecuta la aplicación
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)
