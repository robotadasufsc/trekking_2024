import RPi.GPIO as gpio
import time
import pigpio
import numpy as np
import cv2


imagem = cv2.VideoCapture(0)

modo = 0

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
pwm = ''

def direction_servo(direction=0.105):
    pass

def stop():
    if pwm != '':
        pwm.stop()
    print("pos stop1")
    gpio.cleanup()
    return {'result': 'success'}

def move_forward(): 
    gpio.cleanup()  # Limpa a configuracao de todos os pinos
    print('limpa config')
    gpio.setmode(gpio.BCM)
    gpio.setup(PWM_PIN_A, gpio.OUT)
    gpio.setup(IN1_PIN_A, gpio.OUT)
    gpio.setup(IN2_PIN_A, gpio.OUT)
    gpio.setup(PWM_PIN_A, gpio.OUT)
    print("setup frente ok")
    gpio.output(IN1_PIN_A, gpio.HIGH)
    gpio.output(IN2_PIN_A, gpio.LOW)
    print('portas frente ok')
    pwm = gpio.PWM(PWM_PIN_A, 1)
    pwm.start(100)
    print('setou pwm')
    return {'result': 'success'}
def move_backward(): 
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
    return {'result': 'success'}
def move_left(): 
    pass
    direction_servo('esquerda')
    return {'result': 'success'}
def move_right(): 
    pass
    direction_servo('direita')
    return {'result': 'success'}

def distancia(imageFrame):
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    if not m:
        m = True
        altura, largura, _ = imageFrame.shape

    # Definindo a faixa de cor vermelha
    red_lower = np.array([0, 120, 70], np.uint8)
    red_upper = np.array([10, 255, 255], np.uint8)
    red_mask1 = cv2.inRange(hsvFrame, red_lower, red_upper)

    red_lower = np.array([170, 120, 70], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red_mask2 = cv2.inRange(hsvFrame, red_lower, red_upper)

    red_mask = red_mask1 + red_mask2

    # Aplicando operações morfológicas
    kernel = np.ones((5, 5), "uint8")
    red_mask = cv2.dilate(red_mask, kernel)

    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:
            x, y, w, h = cv2.boundingRect(contour)
            altura_objeto = h
            distancia = ((2.2 * 14) / h)
            print(f"Altura do objeto: {altura_objeto}, Distância: {distancia}")


while True:

    _, imageFrame = imagem.read()

    d = distancia(imageFrame)

    if modo == 0:

        if sf <= 5 and d <= 9: 'n sei se isso funciona'

            stop_motor(pwm_motor_a)
            liga_led()
             
        else:

            motor_forward()

            
    

    #pwm_motor_a = motor_backward(PWM_PIN_A, IN1_PIN_A, IN2_PIN_A)
    #pulso = angle_to_pulsewidth(90)
    #set_servo_angle(3)  # PosiÃ§Ã£o central do servo
    # liga_led()
    # time.sleep(2)  # Movimento para frente por 2 segundos
    # desliga_led()
    #stop_motor(pwm_motor_a)

    

    # time.sleep(1)  # Pausa de 1 segundo

    #pwm_motor_a = motor_forward(PWM_PIN_A, IN1_PIN_A, IN2_PIN_A)

    # time.sleep(2)  # Movimento para trÃ¡s por 2 segundos

    #stop_motor(pwm_motor_a)
