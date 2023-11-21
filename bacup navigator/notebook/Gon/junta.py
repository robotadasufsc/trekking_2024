import RPi.GPIO as gpio
import time
import pigpio
import numpy as np
import cv2
import funcao_sonar3

imagem = cv2.VideoCapture(0)

cones = 0

meio = 0

m = False

d = 99

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


def liga_led():  #arrumar------------
    gpio.output(LED_PIN, gpio.HIGH)
    
def desliga_led():
    gpio.output(LED_PIN, gpio.LOW)


def motor_forward():
    gpio.cleanup() 
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
    gpio.cleanup() 
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
    gpio.cleanup() 

def set_servo_angle(angle):
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
    
    cm = min(me)    #ponto medio do cone
    return min(dist)  #distancia do objeto para a camera - calibrar

def baliza():
    set_servo_angle(11)
    motor_backward()
    time.sleep(1)
    set_servo_angle(9)
    motor_forward()
    time.sleep(1)
    set_servo_angle(10)
    motor_forward()

def curva90():
    if s[1] < s[0]:
        set_servo_angle(11)
        time.sleep(3)
    
    else:
        set_servo_angle(9)
        time.sleep(3)

while True:
    s = funcao_sonar3.sonar()

    _, imageFrame = imagem.read()

    d = distancia(imageFrame,m)

    if s[0] <= 5 and d <= 9: 
        stop_motor()
        liga_led()    
        time.sleep(2)
        desliga_led()
        baliza()
        d = 99

    else:
        motor_forward()
        if (meio-cm) > 20:
            set_servo_angle(11)
        elif (meio-cm) < 20:
            set_servo_angle(9)
        else:
            set_servo_angle(10)

        if s[0] <= 50 and d == 99: 
            curva90(s)


    if ((s[1] - s[2])**2)**(1/2) < 2:
        set_servo_angle(10)
        motor_forward()

    elif s[1] <= 5:
        set_servo_angle(11)
    
    elif s[1] >= 20 or s[2] <= 5:
        set_servo_angle(9)

    else:
        set_servo_angle(10)

