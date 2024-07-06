import serial
import time

porta = 'COM7'
baundrate = 9600
valores = []
k = 0

def configurar_porta(porta, baudrate):
    ser = serial.Serial(porta, baudrate)
    time.sleep(2)  # Aguarda 2 segundos para estabilizar a conexão
    return ser

def sonar(ser):
    k = 0
    valores = [0, 0, 0, 0, 0]
    while True:
        if ser.in_waiting > 0:
            k = k+1
            line = ser.readline().decode('utf-8').rstrip()
            valores[k-1] = line    
            if k == 5:
                return valores
                #k = 0
                #valores = [0, 0, 0, 0, 0]

def dados(ser):
    sensor =[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(5):
        for k in range(10):
            valor = sonar(ser)
            sensor[i][k] = valor[i]
            time.sleep(0.101)

    return sensor
        


#ser.close()
