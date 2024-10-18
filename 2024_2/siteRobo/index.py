from flask import Flask
from flask import render_template
from maquina_estados import *

'''para navegar até a pasta
cd Documents
cd trekking
cd trekking_2024
cd 2024_2
cd siteRobo

'''

app = Flask(__name__)

# pra testar flask --app index run --host=0.0.0.0 sem debug mas site online
# python index.py com debug mas sem acesso online

if __name__ == "__main__":
    app.run(debug=True)    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/controle/')
def controle():
    return render_template('controle.html')
@app.route('/power/')
def power():
    return render_template('power.html')
@app.route('/mapa/')
def mapa():
    return render_template('mapa.html')
@app.route('/start-car') 
def startCar():
    return start()#motor_forward()
@app.route('/stop-car') 
def stopCar(): 
    return stop()#stop_motor()

@app.route('/move-left-car') 
def moveLeftCar():
    pass 
    

@app.route('/move-right-car') 
def moveRightCar():
    pass
    

@app.route('/move-backward-car') 
def moveBackward():
    pass 
    

@app.route('/move-forward-car') 
def moveForward():
    pass
    

