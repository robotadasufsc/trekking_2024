# Código Python

import serial
import time

# Configura a porta serial (ajuste a porta conforme necessário)
ser = serial.Serial('COM4', 9600)  # Para Windows
# ser = serial.Serial('/dev/ttyUSB0', 9600)  # Para Linux

time.sleep(2)  # Aguarda 2 segundos para estabilizar a conexão

def send_command(command):
    ser.write(command.encode())  # Envia o comando para o Arduino
    print(f'Comando enviado: {command}')

while True:
    command = input('Digite 1 para ligar o LED, 0 para desligar o LED ou q para sair: ')
    
    if command == 'q':
        break
    elif command in ['0', '1']:
        send_command(command)
    else:
        print('Comando inválido. Tente novamente.')

ser.close()  # Fecha a conexão serial
