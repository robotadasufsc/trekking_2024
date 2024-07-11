import RPi.GPIO as gpio
import time
import pigpio

gpio.cleanup()  # Limpa a configuracao de todos os pinos
gpio.setwarnings(False)

# Definir pinos dos motores
PWM_PIN_A = 12  # Pino PWM para o motor A
IN1_PIN_A = 27  # Pino IN1 para o motor A
IN2_PIN_A = 22  # Pino IN2 para o motor A
LED_PIN = 14



# Definir pino do servo motor
SERVO_PIN = 13  # Pino gpio para o servo motor

# Inicializar gpio
gpio.setmode(gpio.BCM)
gpio.setup(PWM_PIN_A, gpio.OUT)
gpio.setup(IN1_PIN_A, gpio.OUT)
gpio.setup(IN2_PIN_A, gpio.OUT)
gpio.setup(SERVO_PIN, gpio.OUT)
gpio.setup(LED_PIN, gpio.OUT)

# Inicializar pigpio para controle de servo
pi = pigpio.pi()
#pi = pigpio.pi('localhost', 8888)
pwm = ''

def direction_servo(direction=0.105):
    pass

def start():
    pass

def stop(): 
    pwm.stop()
    print("pos stop1")
    gpio.cleanup()
    return {'result': 'success'}

def move_forward(): 
    gpio.cleanup()  # Limpa a configuracao de todos os pinos
    print('limpa config')
    gpio.setmode(gpio.BCM)
    gpio.setup(PWM_PIN_A, gpio.OUT)
    gpio.setup(IN1_PIN_A, gpio.OUT)
    gpio.setup(IN2_PIN_A, gpio.OUT)
    gpio.setup(PWM_PIN_A, gpio.OUT)
    print("setup frente ok")
    gpio.output(IN1_PIN_A, gpio.HIGH)
    gpio.output(IN2_PIN_A, gpio.LOW)
    print('portas frente ok')
    pwm = gpio.PWM(PWM_PIN_A, 1)
    pwm.start(100)
    print('setou pwm')
    return {'result': 'success'}
def move_backward(): 
    gpio.cleanup()  # Limpa a configuracao de todos os pinos
    gpio.setmode(gpio.BCM)
    gpio.setup(PWM_PIN_A, gpio.OUT)
    gpio.setup(IN1_PIN_A, gpio.OUT)
    gpio.setup(IN2_PIN_A, gpio.OUT)
    gpio.setup(PWM_PIN_A, gpio.OUT)
    gpio.output(IN1_PIN_A, gpio.LOW)
    gpio.output(IN2_PIN_A, gpio.HIGH)
    pwm = gpio.PWM(PWM_PIN_A, 1)
    pwm.start(100)
    return {'result': 'success'}
def move_left(): 
    pass
    direction_servo('esquerda')
    return {'result': 'success'}
def move_right(): 
    pass
    direction_servo('direita')
    return {'result': 'success'}
