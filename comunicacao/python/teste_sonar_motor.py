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
VCC = 2 #alimentaço pro servo

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(PWM_PIN_A, gpio.OUT)
    gpio.setup(IN1_PIN_A, gpio.OUT)
    gpio.setup(IN2_PIN_A, gpio.OUT)
    gpio.setup(SERVO_PIN, gpio.OUT)
    gpio.setup(VCC, gpio.OUT)


init()
gpio.setwarnings(False)
pwm = gpio.PWM(PWM_PIN_A, 1)
gpio.output(VCC, gpio.HIGH)
gpio.cleanup()  # Limpa a configuracao de todos os pinos


def move_forward(): 
    init()
    gpio.output(IN1_PIN_A, gpio.HIGH)
    gpio.output(IN2_PIN_A, gpio.LOW)
    pwm.start(100)
    #gpio.cleanup()  # Limpa a configuracao de todos os pinos

def liga_led():
    gpio.setmode(gpio.BCM)
    gpio.setup(LED_PIN, gpio.OUT)
    gpio.output(LED_PIN, gpio.HIGH)
    #gpio.cleanup()  # Limpa a configuracao de todos os pinos

    
def desliga_led():
    gpio.setmode(gpio.BCM)
    gpio.setup(LED_PIN, gpio.OUT)
    gpio.output(LED_PIN, gpio.LOW)
    #gpio.cleanup()  # Limpa a configuracao de todos os pinos

def stop_motor():
    pwm.stop()
    gpio.cleanup()  # Limpa a configuracao de todos os pinos

def move_backward(): 
    init()
    gpio.output(IN1_PIN_A, gpio.LOW)
    gpio.output(IN2_PIN_A, gpio.HIGH)
    pwm.start(100)
    #gpio.cleanup()  # Limpa a configuracao de todos os pinos

def lt(): # Gira para esquerda
    init()
    servo = gpio.PWM(SERVO_PIN,50)
    servo.start(0)   
    servo.ChangeDutyCycle(9)  
    #gpio.cleanup()  # Limpa a configuracao de todos os pinos

def rt(): # Gira para direita
    init()
    servo = gpio.PWM(SERVO_PIN,50)
    servo.start(0)   
    servo.ChangeDutyCycle(11)  
    #gpio.cleanup()  # Limpa a configuracao de todos os pinos

def mid(): # Gira servo para o meio
    init()
    servo = gpio.PWM(SERVO_PIN,50)
    servo.start(0)   
    servo.ChangeDutyCycle(10)  
    #gpio.cleanup()  # Limpa a configuracao de todos os pinos



move_backward()
time.sleep(1)
liga_led()
time.sleep(1)
mid()
stop_motor()
time.sleep(1)
rt()


'''while True:

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
    '''
    