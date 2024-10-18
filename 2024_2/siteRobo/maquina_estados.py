import funcao_sonar3 as fs
import carControl as mt
import numpy as np

import RPi.GPIO as gpio
import time


#gpio.cleanup()  # Limpa a configuracao de todos os pinos
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)


sensores = [
	(6, 5),  # Sensor 1
 	(23, 24),# Sensor 2
	(2, 3),  # Sensor 3
	# Adicione mais sensores conforme necessário
]

# Definir pinos dos motores

IN1_PIN_A = 27  # Pino IN1 para o motor A
IN2_PIN_A = 22  # Pino IN2 para o motor A
LED_PIN = 14
SERVO_PIN = 19  # Pino gpio para o servo motor

mt.setup_motor(IN1_PIN_A, IN2_PIN_A, SERVO_PIN, LED_PIN)


# Configura os sensores
for trigger_pin, echo_pin in sensores:
	fs.setup_sensor(trigger_pin, echo_pin)
	


'''
mt.servo_left()
print("left")
time.sleep(1)
mt.servo_mid()
mt.liga_led()
print("mid")
time.sleep(1)
mt.servo_right()
mt.desliga_led()
print("right")
time.sleep(1)
'''


mt.stop_motor()
A = 1



def mapear(mini, maxi, entrada):
	dif = maxi- mini
	proporcao = dif/10
	resultado = mini + entrada*proporcao
	return resultado
	
	
'''
n=0

while True:
	distancias = fs.coletar_distancias(sensores)
	distancias[0] = int(distancias[0])
	distancias[1] = int(distancias[1])
	distancias[2] = int(distancias[2])
	print("dis ", distancias)
	print(" ")

	#if distancias[1] < 150:
#		mt.set_servo_angle(11)
#	else:
#		mt.set_servo_angle(9)




	for i in np.arange(1, 11, 1):
		print("i ",i)
		mt.set_servo_angle(mapear(8.5, 12, i))
'''


def start():
	global A
	A = 1
	Ant_A = 0
	print("start",A)
	gpio.setwarnings(False)
	gpio.setmode(gpio.BCM)
	mt.setup_motor(IN1_PIN_A, IN2_PIN_A, SERVO_PIN, LED_PIN)


	# Configura os sensores
	for trigger_pin, echo_pin in sensores:
		fs.setup_sensor(trigger_pin, echo_pin)
	
	while A < 4:
		if A == 0: # para no cone
			print("0",A)
			mt.liga_led()
			mt.motor_backward()
			time.sleep(0.5)
			mt.stop_motor()
			
			time.sleep(5)
			A = 5
			
				
		if A == 1: #frente mantendo distancia parede
			print("1",A)
			mt.set_servo_angle(mapear(8.5, 12, 6))
			mt.motor_forward()
			mt.desliga_led()
			n = int(time.time())
			m = int(time.time())

			while A == 1: 
				n = int(time.time())
				mt.set_servo_angle(mapear(8.5, 12, 5))
				
				distancias = fs.coletar_distancias(sensores)
				distancias[0] = int(distancias[0])
				distancias[1] = int(distancias[1])
				distancias[2] = int(distancias[2])
				print("dis ", distancias)
				
				if distancias[0] < 100:
					A = 0
					
					
					
				'''
				if n-m > 1:
					m = int(time.time())
					if distancias[1] < 40:
						mt.set_servo_angle(mapear(8.5, 12, 7))
					if distancias[1] < 60:
						mt.set_servo_angle(mapear(8.5, 12, 4))
					if distancias[2] < 10:
						mt.set_servo_angle(mapear(8.5, 12, 10))
						time.sleep(1)
						mt.set_servo_angle(mapear(8.5, 12, 6))
						time.sleep(3)
					
				
				if distancias[1] < 100:
					mt.set_servo_angle(mapear(8.5, 12, 7))
				else:
					mt.set_servo_angle(mapear(8.5, 12, 5))
				if distancias[2] < 100:
					mt.set_servo_angle(mapear(8.5, 12, 10))
					time.sleep(1)
					mt.set_servo_angle(mapear(8.5, 12, 6))
					time.sleep(3)
					
				'''	
					
				'''
				mt.servo_left()
				time.sleep(0.2)
				
				if distancias[0] < 100:
					A = 0
					
				mt.servo_right()
				time.sleep(0.08)
				
				if distancias[0] < 100:
					A = 0
				'''
		
		if A == 2: #curva direita
			print("2",A)
			mt.servo_left()
			mt.motor_backward()
			mt.desliga_led()
			time.sleep(1) #verificar quanto tempo precisa pra fazer retorno 3 pontos
			mt.servo_right()
			mt.motor_forward()
			time.sleep(1)
			mt.servo_mid()
			A = 1 # vai para o codigo de ir pra frente
			while A == 2:
				distancias = fs.coletar_distancias(sensores)
				#print(distancias)
				if distancias[0] < 10:
					A = 0
			
		
	
				
	return {'result': 'sucess'}
					
def stop():
	gpio.cleanup()
	global A
	print("stop",A)
	A = 5
	print(A)
	print("stop2",A)
	
	return {'result': 'sucess'}

#start()
'''
try:
	while A < 5:
		if A == 0:
			mt.stop_motor()
			#mt.liga_led()
			time.sleep(5)
			
		if A == 1:
			#mt.servo_mid()
			mt.motor_forward()
			#mt.desliga_led()

			while A == 1:
				distancias = fs.coletar_distancias(sensores)
				print(distancias)
				if distancias[0] < 10:
					A = 0

		
except KeyboardInterrupt:
	print("Medição interrompida pelo usuário")
finally:
	gpio.cleanup()  # Limpa os pinos GPIO usados
'''
