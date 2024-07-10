import bluerobotics_navigator as navigator
#import RPi.GPIO as gpio
import time
#import pigpio
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


def stop(): 
    navigator.set_pwm_enable(False)
    navigator.set_pwm_channel_duty_cycle(IN1_PIN_M, 0)
    navigator.set_pwm_channel_duty_cycle(IN2_PIN_M, 0)
    navigator.set_pwm_channel_duty_cycle(PWM_PIN_M, 0)
    direction_servo('reto')
    return {'result': 'success'}
def move_forward(): 
    navigator.set_pwm_channel_duty_cycle(IN1_PIN_M, 0)
    navigator.set_pwm_channel_duty_cycle(IN2_PIN_M, 1)
    navigator.set_pwm_channel_duty_cycle(PWM_PIN_M, 1)
    navigator.set_pwm_enable(True)
    return {'result': 'success'}
def move_backward(): 
    navigator.set_pwm_channel_duty_cycle(IN1_PIN_M, 1)
    navigator.set_pwm_channel_duty_cycle(IN2_PIN_M, 0)
    navigator.set_pwm_channel_duty_cycle(PWM_PIN_M, 1)
    navigator.set_pwm_enable(True)
    return {'result': 'success'}
def move_left(): 
    direction_servo('esquerda')
    return {'result': 'success'}
def move_right(): 
    direction_servo('direita')
    return {'result': 'success'}