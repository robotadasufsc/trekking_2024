import RPi.GPIO as gpio
import time
import pigpio
import numpy as np
import cv2


imagem = cv2.VideoCapture(0)

modo = 0

meio = 0

m = False

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


def liga_led():
    gpio.output(LED_PIN, gpio.HIGH)
    
def desliga_led():
    gpio.output(LED_PIN, gpio.LOW)

# FunÃ§Ãµes de controle dos motores
def motor_forward():
    gpio.cleanup()  # Limpa a configuracao de todos os pinos
    gpio.setmode(gpio.BCM)
    gpio.setup(PWM_PIN_A, gpio.OUT)
    gpio.setup(IN1_PIN_A, gpio.OUT)
    gpio.setup(IN2_PIN_A, gpio.OUT)
    gpio.setup(PWM_PIN_A, gpio.OUT)
    gpio.output(IN1_PIN_A, gpio.HIGH)
    gpio.output(IN2_PIN_A, gpio.LOW)
    pwm = gpio.PWM(PWM_PIN_A, 1)
    pwm.start(100)


def motor_backward():
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


def stop_motor():
    pwm = gpio.PWM(PWM_PIN_A, 1)
    pwm.stop()
    gpio.cleanup()  # Limpa a configuracao de todos os pinos

#FunÃ§Ã£o para controlar o servo motor
def set_servo_angle(angle):
    #duty = (angle / 18) + 2
    #pi.set_servo_pulsewidth(SERVO_PIN, duty)
    gpio.setup(13, gpio.OUT)
    servo = gpio.PWM(13, 100)
    servo.start(0)
    servo.ChangeDutyCycle(angle)
    
    
def angle_to_pulsewidth(angle):
    PULSE_WIDTH_MIN = 500
    PULSE_WIDTH_MAX = 2500
    if angle < 0:
        angle = 0
    elif angle > 180:
        angle = 180
    pulsewidth = PULSE_WIDTH_MIN + (PULSE_WIDTH_MAX - PULSE_WIDTH_MIN) * (angle / 180.0)
    print(pulsewidth)
    return pulsewidth

import cv2
import numpy as np

def distancia(imageFrame,m):
    global meio
    global cm
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
    dist = []
    me = []

    if not m:
        m = True
        altura, largura, _ = imageFrame.shape
        meio = (int(largura/2), int(altura/2))

    # Definindo a faixa de cor laranja
    orange_lower = np.array([5, 100, 100], np.uint8)
    orange_upper = np.array([15, 255, 255], np.uint8)
    orange_mask = cv2.inRange(hsvFrame, orange_lower, orange_upper)

    # Aplicando operações morfológicas
    kernel = np.ones((5, 5), "uint8")
    orange_mask = cv2.dilate(orange_mask, kernel)

    contours, _ = cv2.findContours(orange_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:
            x, y, w, h = cv2.boundingRect(contour)
            distancia = ((2.2 * 14) / h)
            dist.append(distancia)
            me.append(x)
    
    cm = min(me)
    return min(dist)

def baliza():
    set_servo_angle(11)
    motor_backward()
    time.sleep(1)
    set_servo_angle(9)
    motor_forward()
    time.sleep(1)
    set_servo_angle(10)
    motor_forward()
        


# Exemplo de movimento do carrinho
while True:
    _, imageFrame = imagem.read()

    d = distancia(imageFrame,m)

    if 'sf' <= 5 and d <= 9: 
        stop_motor()
        liga_led()    
        time.sleep(2)
        desliga_led()
        baliza()

    else:
        motor_forward()
        if (meio-cm) > 20:
            set_servo_angle(11)
        elif (meio-cm) < 20:
            set_servo_angle(9)
        else:
            set_servo_angle(10)

    if "sl" <= 5:
        set_servo_angle(11)
    
    elif "sl" >= 20:
        set_servo_angle(9)
    
    else:
        set_servo_angle(10)