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
def setup():
    gpio.setmode(gpio.BCM)
    gpio.setup(PWM_PIN_A, gpio.OUT)
    gpio.setup(IN1_PIN_A, gpio.OUT)
    gpio.setup(IN2_PIN_A, gpio.OUT)
    gpio.setup(SERVO_PIN, gpio.OUT)
    gpio.setup(LED_PIN, gpio.OUT)
setup()

# Inicializar pigpio para controle de servo
#pi = pigpio.pi()
#pi = pigpio.pi('localhost', 8888)
pwm = gpio.PWM(PWM_PIN_A, 1)

def liga_led():
    setup()
    gpio.output(LED_PIN, gpio.HIGH)
    
def desliga_led():
    setup()
    gpio.output(LED_PIN, gpio.LOW)

# FunÃ§Ãµes de controle dos motores
def motor_forward(pin_pwm, pin_in1, pin_in2):
    gpio.cleanup()  # Limpa a configuracao de todos os pinos
    setup()
    gpio.output(IN1_PIN_A, gpio.HIGH)
    gpio.output(IN2_PIN_A, gpio.LOW)
    pwm = gpio.PWM(PWM_PIN_A, 1)
    pwm.start(100)
    return pwm

def motor_backward(pin_pwm, pin_in1, pin_in2):
    gpio.cleanup()  # Limpa a configuracao de todos os pinos
    setup()
    gpio.output(IN1_PIN_A, gpio.LOW)
    gpio.output(IN2_PIN_A, gpio.HIGH)
    pwm = gpio.PWM(PWM_PIN_A, 1)
    pwm.start(100)
    return pwm

def stop_motor(pwm):
    pwm.stop()
    gpio.cleanup()  # Limpa a configuracao de todos os pinos

#FunÃ§Ã£o para controlar o servo motor
def set_servo_angle(duty):
    gpio.cleanup()  # Limpa a configuracao de todos os pinos
    gpio.setmode(gpio.BCM)
    gpio.setup(SERVO_PIN, gpio.OUT)

    servo = gpio.PWM(13,50)
    servo.start(0)   
    servo.ChangeDutyCycle(duty)  



except KeyboardInterrupt:
    stop_motor(pwm)
    gpio.cleanup()
    pi.stop()
