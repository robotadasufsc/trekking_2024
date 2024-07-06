import serial
import time

porta = 'COM4'
baundrate = 9600

def configurar_porta(porta, baudrate):
    ser = serial.Serial(porta, baudrate)
    time.sleep(2)  # Aguarda 2 segundos para estabilizar a conexão
    return ser

def sonar(ser):
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            
            return line


#ser.close()
