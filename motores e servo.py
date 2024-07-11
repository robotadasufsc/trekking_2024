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
def motor_forward(pin_pwm, pin_in1, pin_in2):
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
    return pwm

def motor_backward(pin_pwm, pin_in1, pin_in2):
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

    return pwm

def stop_motor(pwm):
    pwm.stop()
    print("pos stop1")
    gpio.cleanup()  # Limpa a configuracao de todos os pinos
    print("pos stop2")

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

# Exemplo de movimento do carrinho
try:
    while True:
        pwm_motor_a = motor_backward(PWM_PIN_A, IN1_PIN_A, IN2_PIN_A)
        #pulso = angle_to_pulsewidth(90)
        #set_servo_angle(3)  # PosiÃ§Ã£o central do servo
        liga_led()
        time.sleep(2)  # Movimento para frente por 2 segundos
        desliga_led()
        #stop_motor(pwm_motor_a)

        

        time.sleep(1)  # Pausa de 1 segundo

        #pwm_motor_a = motor_forward(PWM_PIN_A, IN1_PIN_A, IN2_PIN_A)

        time.sleep(2)  # Movimento para trÃ¡s por 2 segundos

        #stop_motor(pwm_motor_a)
        

except KeyboardInterrupt:
    stop_motor(pwm_motor_a)
    stop_motor(pwm_motor_b)
    gpio.cleanup()
    pi.stop()