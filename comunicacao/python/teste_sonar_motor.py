import funcao_sonar3 as funcao_sonar3
import RPi.GPIO as gpio
import time
import pigpio

porta = '/dev/ttyACM0'
freq = 9600
ser = funcao_sonar3.configurar_porta(porta, freq)


PWM_PIN_A = 12  # Pino PWM para o motor A
IN1_PIN_A = 27  # Pino IN1 para o motor A
IN2_PIN_A = 22  # Pino IN2 para o motor A
LED_PIN = 14

gpio.setmode(gpio.BCM)
gpio.setup(PWM_PIN_A, gpio.OUT)
gpio.setup(IN1_PIN_A, gpio.OUT)
gpio.setup(IN2_PIN_A, gpio.OUT)

gpio.setup(LED_PIN, gpio.OUT)

pwm = gpio.PWM(PWM_PIN_A, 1)

gpio.cleanup()  # Limpa a configuracao de todos os pinos
gpio.setwarnings(False)


def move_forward(): 
    gpio.cleanup()  # Limpa a configuracao de todos os pinos
    gpio.setmode(gpio.BCM)
    gpio.setup(PWM_PIN_A, gpio.OUT)
    gpio.setup(IN1_PIN_A, gpio.OUT)
    gpio.setup(IN2_PIN_A, gpio.OUT)
    gpio.setup(PWM_PIN_A, gpio.OUT)
    gpio.output(IN1_PIN_A, gpio.HIGH)
    gpio.output(IN2_PIN_A, gpio.LOW)
    pwm.start(100)

def liga_led():  #arrumar------------
    gpio.setmode(gpio.BCM)
    gpio.setup(LED_PIN, gpio.OUT)
    gpio.output(LED_PIN, gpio.HIGH)
    
def desliga_led():
    gpio.setmode(gpio.BCM)
    gpio.setup(LED_PIN, gpio.OUT)
    gpio.output(LED_PIN, gpio.LOW)

def stop_motor():
    pwm.stop()



move_forward()

while True:
    valor = funcao_sonar3.sonar(ser)
    print("frente",valor[1])
    print("lado",valor[0])
    if valor[1] < 20:
        liga_led()
        stop_motor()
        time.sleep(3)
        desliga_led()
        break