import funcao_sonar3 as funcao_sonar3
import RPi.GPIO as gpio
import time

porta = '/dev/ttyACM0'
freq = 9600
def connect():
    ser = funcao_sonar3.configurar_porta(porta, freq)
    return ser

lado = "meio"

PWM_PIN_A = 12  # Pino PWM para o motor A
IN1_PIN_A = 27  # Pino IN1 para o motor A
IN2_PIN_A = 22  # Pino IN2 para o motor A
LED_PIN = 14
SERVO_PIN = 13
adf

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(PWM_PIN_A, gpio.OUT)
    gpio.setup(IN1_PIN_A, gpio.OUT)
    gpio.setup(IN2_PIN_A, gpio.OUT)
    gpio.setup(SERVO_PIN, gpio.OUT)

init()
gpio.setwarnings(False)
pwm = gpio.PWM(PWM_PIN_A, 1)
gpio.cleanup()  # Limpa a configuracao de todos os pinos

def move_forward(): 
    init()
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
    init()
    gpio.output(IN1_PIN_A, gpio.LOW)
    gpio.output(IN2_PIN_A, gpio.LOW)

def move_backward(): 
    init()
    gpio.output(IN1_PIN_A, gpio.LOW)
    gpio.output(IN2_PIN_A, gpio.HIGH)
    pwm.start(100)
 

def lt(): # Gira para esquerda
    global lado
    init()
    lado = "esquerda"
    servo = gpio.PWM(SERVO_PIN,50)
    servo.start(0)   
    servo.ChangeDutyCycle(8)  
    time.sleep(0.5)

def rt(): # Gira para direita
    global lado
    init()
    lado = "direita"
    servo = gpio.PWM(SERVO_PIN,50)
    servo.start(0)   
    servo.ChangeDutyCycle(12)
    time.sleep(0.5)

def mid(): # Gira servo para o meio
    global lado
    init()
    lado = "meio"
    servo = gpio.PWM(SERVO_PIN,50)
    servo.start(0)   
    servo.ChangeDutyCycle(10.1)  
    time.sleep(0.5)

move_forward()
mid()
def start():
    ser = connect()
    while True:
        valor = funcao_sonar3.sonar(ser)
        print("frente",valor[1])
        print("lado",valor[0])
        if 3 < valor[1] < 20:    
            move_backward()
            liga_led()  #precisa estar no meio
            stop_motor()      
            time.sleep(3)
            desliga_led()
            print("cabo")
            break

        if 200 < valor[0] < 1000 and lado != "direita": 
            rt()
        elif valor[0] < 20 and lado != "esquerda":
            lt()
        elif lado != "meio":
            mid()
start()