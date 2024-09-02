
#FUNCIONA

import numpy as np
import bluerobotics_navigator as navigator
import time
import datetime
import matplotlib.pyplot as plt
import import_ipynb
import calibracao
from bluerobotics_navigator import PwmChannel
from scipy.integrate import simpson


# Definir pinos dos motores
PWM_PIN_M = navigator.PwmChannel.Ch4 # Pino PWM para o motor 
IN1_PIN_M = navigator.PwmChannel.Ch3  # Pino IN1 para o motor s
IN2_PIN_M = navigator.PwmChannel.Ch2  # Pino IN2 para o motor 

# Definir pino do servo motor
SERVO_PIN = navigator.PwmChannel.Ch1 # Pino para o servo motor

# Definir estado dos PWMs
navigator.set_pwm_freq_hz(60)
navigator.set_pwm_enable(True)

# Inicializar o Navigator
navigator.init() 



# Funções de controle dos motores
def motor_forward():
    navigator.set_pwm_channel_duty_cycle(IN1_PIN_M, 0)
    navigator.set_pwm_channel_duty_cycle(IN2_PIN_M, 1)
    navigator.set_pwm_channel_duty_cycle(PWM_PIN_M, 1)
    navigator.set_pwm_enable(True)

def motor_backward():
    navigator.set_pwm_channel_duty_cycle(IN1_PIN_M, 1)
    navigator.set_pwm_channel_duty_cycle(IN2_PIN_M, 0)
    navigator.set_pwm_channel_duty_cycle(PWM_PIN_M, 1)
    navigator.set_pwm_enable(True)

def stop_motor():
    navigator.set_pwm_enable(False)
    navigator.set_pwm_channel_duty_cycle(IN1_PIN_M, 0)
    navigator.set_pwm_channel_duty_cycle(IN2_PIN_M, 0)
    navigator.set_pwm_channel_duty_cycle(PWM_PIN_M, 0)

def direction_servo(direction=0.105):
    navigator.set_pwm_enable(True)
    if direction == 'direita':
        x = 0.15
    elif direction == 'esquerda':
        x = 0.105
    elif direction == 'reto':
        x = 0.13
        
    else:
        x = direction
    navigator.set_pwm_channel_duty_cycle(SERVO_PIN, x)




# Defina a duração do loop em segundos

frente = 2 # tempo que vai pra frente
re = 2 # tempo que vai pra trás
duracao = 7  # por exemplo, 5 segundos
Ts = 0.001 # tempo da amostragem

# declaracao de variaveis 
tempo_inicial = time.time()
value_accel_x = []
value_accel_y = []
value_accel_z = []

value_giro_x = []
value_giro_y = []
value_giro_z = []
valor_filtro = []

velocita = [0]
posita = [0]
tempo = [0]

# leitura dados dos sensores
acceleration = navigator.read_accel()
accel_x = acceleration.x
accel_y = acceleration.y
accel_z = acceleration.z

angular_velocity = navigator.read_gyro()
giro_x = angular_velocity.x
giro_y = angular_velocity.y
giro_z = angular_velocity.z

acceleration = navigator.read_accel()
acy = acceleration.y
offsety = calibracao.calibra_y(1000) # offset obtido através da calibração
x = 0.105

# loop que faz o carrinho andar pelo tempo determinado
while time.time() - tempo_inicial < duracao:
    tempo.append(tempo[-1] + Ts)
    tempo_atual = time.time() - tempo_inicial
    if tempo_atual < duracao:
        direction_servo('reto')
        motor_forward() #-------------------------------------------------------

    #elif tempo_atual > frente and tempo_atual < duracao:
        #motor_backward()
    acceleration = navigator.read_accel()
    accel_x = acceleration.x
    accel_y = calibracao.add_value(valor_filtro, acceleration.y, 400, 1, 20000) - offsety
    accel_z = acceleration.z
    value_accel_y.append(accel_y)

    # Integração para obter a velocidade usando a regra de Simpson
    if len(value_accel_y) > 1:
        new_velocita = simpson(value_accel_y, dx=Ts)
    else:
        new_velocita = 0
    velocita.append(new_velocita)
    
    # Integração para obter a posição usando a regra de Simpson
    if len(velocita) > 1:
        new_posita = simpson(velocita, dx=Ts)
    else:
        new_posita = 0
    posita.append(new_posita)
    
    time.sleep(Ts)  # Adicione um atraso para simular uma operação dentro do loop, esse vai ser o tempo de amostragem dos dados
stop_motor()
#print(value_accel_y)
print(f"O loop foi executado por {duracao} segundos taxa de amostragem {Ts}.")

plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)  # (linhas, colunas, índice do subplot)
plt.plot(range(len(value_accel_y)), value_accel_y, label='m/s^2')
plt.xlabel('Time')
plt.ylabel('Values')
plt.title('aceleracao Y')
plt.legend()
plt.grid(True)



#---------------------------

plt.show()