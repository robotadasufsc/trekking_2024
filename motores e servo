import RPi.GPIO as gpio
import time
import pigpio

# Definir pinos dos motores
PWM_PIN_A = 18  # Pino PWM para o motor A
IN1_PIN_A = 23  # Pino IN1 para o motor A
IN2_PIN_A = 24  # Pino IN2 para o motor A
PWM_PIN_B = 25  # Pino PWM para o motor B
IN1_PIN_B = 8   # Pino IN1 para o motor B
IN2_PIN_B = 7   # Pino IN2 para o motor B

# Definir pino do servo motor
SERVO_PIN = 17  # Pino gpio para o servo motor

# Inicializar gpio
gpio.setmode(gpio.BCM)
gpio.setup(IN1_PIN_A, gpio.OUT)
gpio.setup(IN2_PIN_A, gpio.OUT)
gpio.setup(IN1_PIN_B, gpio.OUT)
gpio.setup(IN2_PIN_B, gpio.OUT)
gpio.setup(SERVO_PIN, gpio.OUT)

# Inicializar pigpio para controle de servo
pi = pigpio.pi()

# Funções de controle dos motores
def motor_forward(pin_pwm, pin_in1, pin_in2):
    gpio.output(pin_in1, gpio.HIGH)
    gpio.output(pin_in2, gpio.LOW)
    pwm = gpio.PWM(pin_pwm, 100)
    pwm.start(50)
    return pwm

def motor_backward(pin_pwm, pin_in1, pin_in2):
    gpio.output(pin_in1, gpio.LOW)
    gpio.output(pin_in2, gpio.HIGH)
    pwm = gpio.PWM(pin_pwm, 100)
    pwm.start(50)
    return pwm

def stop_motor(pwm):
    pwm.stop()

# Função para controlar o servo motor
def set_servo_angle(angle):
    duty = (angle / 18) + 2
    pi.set_servo_pulsewidth(SERVO_PIN, duty)

# Exemplo de movimento do carrinho
try:
    pwm_motor_a = motor_forward(PWM_PIN_A, IN1_PIN_A, IN2_PIN_A)
    pwm_motor_b = motor_forward(PWM_PIN_B, IN1_PIN_B, IN2_PIN_B)
    set_servo_angle(90)  # Posição central do servo

    time.sleep(2)  # Movimento para frente por 2 segundos

    stop_motor(pwm_motor_a)
    stop_motor(pwm_motor_b)

    time.sleep(1)  # Pausa de 1 segundo

    pwm_motor_a = motor_backward(PWM_PIN_A, IN1_PIN_A, IN2_PIN_A)

    time.sleep(2)  # Movimento para trás por 2 segundos

    stop_motor(pwm_motor_a)
    stop_motor(pwm_motor_b)

except KeyboardInterrupt:
    stop_motor(pwm_motor_a)
    stop_motor(pwm_motor_b)
    gpio.cleanup()
    pi.stop()