import funcao_sonar3 as funcao_sonar3  #pedir ajudo para o iuri
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
servo_pi= 2
SERVO_PIN = 13

gpio.setwarnings(False)

gpio.setmode(gpio.BCM)
gpio.setup(PWM_PIN_A, gpio.OUT)
gpio.setup(IN1_PIN_A, gpio.OUT)
gpio.setup(IN2_PIN_A, gpio.OUT)
gpio.setup(SERVO_PIN, gpio.OUT)
gpio.setup(servo_pi, gpio.OUT)
gpio.output(servo_pi, gpio.HIGH)

gpio.setup(LED_PIN, gpio.OUT)

pi = pigpio.pi()

pwm = gpio.PWM(SERVO_PIN, 50)  # Frequ�ncia de 50 Hz (20ms per�odo)
pwm.start(0)

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

def liga_led():
    gpio.setmode(gpio.BCM)
    gpio.setup(LED_PIN, gpio.OUT)
    gpio.output(LED_PIN, gpio.HIGH)

    
def desliga_led():
    gpio.setmode(gpio.BCM)
    gpio.setup(LED_PIN, gpio.OUT)
    gpio.output(LED_PIN, gpio.LOW)

def stop_motor():
    pwm.stop()

def move_backward(): 
    gpio.cleanup()  # Limpa a configuracao de todos os pinos
    gpio.setmode(gpio.BCM)
    gpio.setup(PWM_PIN_A, gpio.OUT)
    gpio.setup(IN1_PIN_A, gpio.OUT)
    gpio.setup(IN2_PIN_A, gpio.OUT)
    gpio.setup(PWM_PIN_A, gpio.OUT)
    gpio.output(IN1_PIN_A, gpio.LOW)
    gpio.output(IN2_PIN_A, gpio.HIGH)
    pwm.start(100)

def set_servo_angle(angle):
    duty = 2 + (angle / 18)  # Calcula a largura do pulso para o �ngulo
    gpio.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    gpio.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)



def baliza():
    set_servo_angle(11)
    move_backward()
    time.sleep(1)
    set_servo_angle(9)
    move_forward()
    time.sleep(1)
    set_servo_angle(10)
    move_forward()

set_servo_angle(11)