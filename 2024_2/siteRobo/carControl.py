import RPi.GPIO as gpio
import time
import pigpio

IN1_PIN_A = 0
IN2_PIN_A = 0
SERVO_PIN = 0
LED_PIN = 0

# Inicializar gpio
def setup_motor(IN1_PINA, IN2_PINA, SERVOPIN, LEDPIN):
    global IN1_PIN_A, IN2_PIN_A, SERVO_PIN, LED_PIN
    IN1_PIN_A = IN1_PINA
    IN2_PIN_A = IN2_PINA
    SERVO_PIN = SERVOPIN
    LED_PIN = LEDPIN

    
def setup():
    #gpio.setup(PWM_PIN_A, gpio.OUT)
    gpio.setup(IN1_PIN_A, gpio.OUT)
    gpio.setup(IN2_PIN_A, gpio.OUT)
    gpio.setup(SERVO_PIN, gpio.OUT)
    gpio.setup(LED_PIN, gpio.OUT)
    


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
    return {'result': 'sucess'}
    

def motor_backward():
    #gpio.cleanup()  # Limpa a configuracao de todos os pinos
    setup()
    gpio.output(IN1_PIN_A, gpio.LOW)
    gpio.output(IN2_PIN_A, gpio.HIGH)
    # FunÃ§Ãµes de controle dos motores
    

def stop_motor():
    setup()
    gpio.output(IN1_PIN_A, gpio.LOW)
    gpio.output(IN2_PIN_A, gpio.LOW)
    #gpio.cleanup()  # Limpa a configuracao de todos os pinos
    return {'result': 'sucess'}

#FunÃ§Ã£o para controlar o servo motor
def set_servo_angle(duty):
    # minimo de 8.5
    #meio de 10.05
    #maximo de 12
    #gpio.cleanup()  # Limpa a configuracao de todos os pinos
    setup()
    

    servo = gpio.PWM(SERVO_PIN,50)
    servo.start(duty)   
    time.sleep(0.7)



def servo_left():
    set_servo_angle(9.3) #8.3
    #time.sleep(0.5)

def servo_right():
    set_servo_angle(10.9) #11.8
    #time.sleep(0.5)
    
def servo_mid():
    set_servo_angle(10.05)
    #time.sleep(0.5)




'''
liga_led()
servo_right()
time.sleep(1)
servo_left()
desliga_led()
time.sleep(1)
'''




