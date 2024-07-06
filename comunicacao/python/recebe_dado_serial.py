# Código Python

import serial
import time

porta = 'COM4'
def sonar(porta):
    # Configura a porta serial (ajuste a porta conforme necessário)
    ser = serial.Serial(porta, 9600)  # Para Windows
    # ser = serial.Serial('/dev/ttyUSB0', 9600)  # Para Linux

    time.sleep(2)  # Aguarda 2 segundos para estabilizar a conexão

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            return line
            #print(f'Dado recebido do Arduino: {line}')

    

    # decode converte bytes pra string
    # rstrip retira espaços do final da string
