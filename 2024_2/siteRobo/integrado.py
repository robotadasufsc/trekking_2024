import funcao_sonar3 as fs
import motores as mt

import RPi.GPIO as GPIO
import time

sensores = [
	(6, 5),  # Sensor 1
#	(5, 6),    # Sensor 2
#	(20, 21),  # Sensor 3
	# Adicione mais sensores conforme necessário
]

# Definir pinos dos motores
PWM_PIN_A = 12  # Pino PWM para o motor A
IN1_PIN_A = 27  # Pino IN1 para o motor A
IN2_PIN_A = 22  # Pino IN2 para o motor A
LED_PIN = 14



# Configura os sensores
#for trigger_pin, echo_pin in sensores:
	#fs.setup_sensor(trigger_pin, echo_pin)

# configura motores
mt.setup()
a = 0
try:
	while True:
		while a == 0:
			mt.desliga_led()
			mt.motor_forward()
			
			#mt.liga_led()
			distancias = fs.coletar_distancias(sensores)
			print(distancias[0])
			if distancias[0] < 10:
				print("aaaaaaaa")
				mt.liga_led()
				a = 1
			'''	
			if distancias[0] < 10:
				print('entrou condicao')
				a = 1
			else:
				a = 0
			'''
			
		while a == 1:
			print("bbbbbbbbb")
			distancias = fs.coletar_distancias(sensores)
			mt.stop_motor()
			if distancias[0] > 10:
				print("cccccccc")
				a = 0
		
except KeyboardInterrupt:
	print("Medição interrompida pelo usuário")
finally:
	GPIO.cleanup()  # Limpa os pinos GPIO usados
