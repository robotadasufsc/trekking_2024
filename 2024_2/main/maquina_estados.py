import funcao_sonar_rasp as fs
import motores as mt

import RPi.GPIO as GPIO
import time

sensores = [
(6, 5),  # Sensor 1
# (5, 6),    # Sensor 2
# (20, 21),  # Sensor 3
# Adicione mais sensores conforme necessário
]

# Definir pinos dos motores

IN1_PIN_A = 27  # Pino IN1 para o motor A
IN2_PIN_A = 22  # Pino IN2 para o motor A
LED_PIN = 14
SERVO_PIN = 13  # Pino gpio para o servo motor

# Configura os sensores
#for trigger_pin, echo_pin in sensores:
#fs.setup_sensor(trigger_pin, echo_pin)

# configura motores
mt.setup()
A = 1
try:
if A == 0:
mt.stop_motor()
mt.liga_led()

if A == 1:
mt.motor_forward()
mt.desliga_led()
while A == 1:
distancias = fs.coletar_distancias(sensores)
print(distancias)
if distancias[0] < 10:
A = 0


except KeyboardInterrupt:
print("Medição interrompida pelo usuário")
finally:
GPIO.cleanup()  # Limpa os pinos GPIO usados