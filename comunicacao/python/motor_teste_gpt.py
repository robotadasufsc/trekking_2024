import funcao_sonar3 as funcao_sonar3
import RPi.GPIO as gpio
import time

porta = '/dev/ttyACM0'
freq = 9600
ser = funcao_sonar3.configurar_porta(porta, freq)

PWM_PIN_A = 12  # Pino PWM para o motor A
IN1_PIN_A = 27  # Pino IN1 para o motor A
IN2_PIN_A = 22  # Pino IN2 para o motor A
LED_PIN = 14
SERVO_PIN = 13
VCC = 2  # alimentação para o servo

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(PWM_PIN_A, gpio.OUT)
    gpio.setup(IN1_PIN_A, gpio.OUT)
    gpio.setup(IN2_PIN_A, gpio.OUT)
    gpio.setup(LED_PIN, gpio.OUT)
    gpio.setup(SERVO_PIN, gpio.OUT)
    gpio.setup(VCC, gpio.OUT)
    gpio.output(VCC, gpio.HIGH)

init()
gpio.setwarnings(False)
pwm = gpio.PWM(PWM_PIN_A, 1)
servo = gpio.PWM(SERVO_PIN, 50)
servo.start(0)

def move_forward():
    gpio.output(IN1_PIN_A, gpio.HIGH)
    gpio.output(IN2_PIN_A, gpio.LOW)
    pwm.start(100)

def liga_led():
    gpio.output(LED_PIN, gpio.HIGH)

def desliga_led():
    gpio.output(LED_PIN, gpio.LOW)

def stop_motor():
    pwm.stop()

def move_backward():
    gpio.output(IN1_PIN_A, gpio.LOW)
    gpio.output(IN2_PIN_A, gpio.HIGH)
    pwm.start(100)

def lt():
    servo.ChangeDutyCycle(9)

def rt():
    servo.ChangeDutyCycle(11)

def mid():
    servo.ChangeDutyCycle(10)

try:
    move_forward()
    time.sleep(3)
    stop_motor()
    time.sleep(1)
    rt()

    while True:
        valor = funcao_sonar3.sonar(ser)
        print("frente", valor[1])
        print("lado", valor[0])
        if 3 < valor[1] < 20:
            move_backward()
            liga_led()
            time.sleep(3)
            desliga_led()
            stop_motor()
            print("cabo")
            break

finally:
    gpio.cleanup()
