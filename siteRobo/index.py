from flask import Flask
from flask import render_template
from carControl import stop

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/controle/')
def controle():
    return render_template('controle.html')
@app.route('/power/')
def power():
    return render_template('power.html')

@app.route('/move-forward') 
def stopCar(): 
    return stop()