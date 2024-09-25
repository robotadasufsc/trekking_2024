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
trigger_pin = 19
echo_pin = 26

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
    gpio.setup(trigger_pin, gpio.OUT)
    gpio.setup(echo_pin, gpio.IN)
setup()



def liga_led():
    setup()
    gpio.output(LED_PIN, gpio.HIGH)
    
def desliga_led():
    setup()
    gpio.output(LED_PIN, gpio.LOW)

# FunÃ§Ãµes de controle dos motores
def motor_forward():
    #gpio.cleanup()  # Limpa a configuracao de todos os pinos
    setup()
    gpio.output(IN1_PIN_A, gpio.HIGH)
    gpio.output(IN2_PIN_A, gpio.LOW)
    

def motor_backward():
    #gpio.cleanup()  # Limpa a configuracao de todos os pinos
    setup()
    gpio.output(IN1_PIN_A, gpio.LOW)
    gpio.output(IN2_PIN_A, gpio.HIGH)
    

def stop_motor():
    setup()
    gpio.output(IN1_PIN_A, gpio.LOW)
    gpio.output(IN2_PIN_A, gpio.LOW)
    #gpio.cleanup()  # Limpa a configuracao de todos os pinos

#FunÃ§Ã£o para controlar o servo motor
def set_servo_angle(duty):
    #gpio.cleanup()  # Limpa a configuracao de todos os pinos
    setup()

    servo = gpio.PWM(SERVO_PIN,50)
    servo.start(duty)   
    time.sleep(1)

set_servo_angle(8)
stop_motor()
