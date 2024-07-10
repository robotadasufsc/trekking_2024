from flask import Flask
from flask import render_template
from carControl import stop
from carControl import move_forward
from carControl import move_backward
from carControl import move_left
from carControl import move_right
app = Flask(__name__)
# pra testar flask --app index run --debug --host=0.0.0.0    
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

@app.route('/stop-car') 
def stopCar(): 
    return stop()

@app.route('/move-left-car') 
def moveLeftCar(): 
    return move_left()

@app.route('/move-right-car') 
def moveRightCart():
    return move_right()

@app.route('/move-backward-car') 
def moveBackward(): 
    return move_backward()

@app.route('/move-forward-car') 
def moveForward(): 
    return move_forward()

