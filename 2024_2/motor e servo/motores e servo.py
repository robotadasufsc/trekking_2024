import RPi.GPIO as gpio
import time
import pigpio

#gpio.cleanup()  # Limpa a configuracao de todos os pinos
gpio.setwarnings(False)

# Definir pinos dos motores
PWM_PIN_A = 12  # Pino PWM para o motor A
IN1_PIN_A = 27  # Pino IN1 para o motor A
IN2_PIN_A = 22  # Pino IN2 para o motor A
LED_PIN = 14

# Definir pino do servo motor
SERVO_PIN = 13  # Pino gpio para o servo motor

# Inicializar gpio
def setup():
    gpio.setmode(gpio.BCM)
    gpio.setup(PWM_PIN_A, gpio.OUT)
    gpio.setup(IN1_PIN_A, gpio.OUT)
    gpio.setup(IN2_PIN_A, gpio.OUT)
    gpio.setup(SERVO_PIN, gpio.OUT)
    gpio.setup(LED_PIN, gpio.OUT)
setup()



def liga_led():
    setup()
    gpio.output(LED_PIN, gpio.HIGH)
    time.sleep(3)
   
def desliga_led():
    setup()
    gpio.output(LED_PIN, gpio.LOW)
    time.sleep(3)

# FunÃ§Ãµes de controle dos motores
def motor_forward(t): #inserir tempo
    gpio.cleanup()  # Limpa a configuracao de todos os pinos
    setup()
   
    gpio.output(IN1_PIN_A, gpio.HIGH)
    gpio.output(IN2_PIN_A, gpio.LOW)
    pwm = gpio.PWM(PWM_PIN_A, 1)
    pwm.start(100)
    time.sleep(t)
    return pwm

def motor_backward(t): #inserir tempo
    gpio.cleanup()  # Limpa a configuracao de todos os pinos
    setup()
   
    gpio.output(IN1_PIN_A, gpio.LOW)
    gpio.output(IN2_PIN_A, gpio.HIGH)
    pwm = gpio.PWM(PWM_PIN_A, 1)
    pwm.start(100)
    time.sleep(t)
    return pwm

def stop_motor(pwm):
    pwm.stop()
    gpio.cleanup()  # Limpa a configuracao de todos os pinos

#FunÃ§Ã£o para controlar o servo motor
def set_servo_angle(duty): #duty deve ser definido entre os valores de 8 a 12
    #gpio.cleanup()  # Limpa a configuracao de todos os pinos
    setup()

    servo = gpio.PWM(SERVO_PIN,50) #Frequência do PWM no pino, 50hz
    servo.start(duty)
    time.sleep(1)
    #servo.ChangeDutyCycle(duty)
   
liga_led()
motor_forward(1)


# liga_led()
# set_servo_angle(10)
# time.sleep(5)
# print('servo')
# desliga_led()


# except KeyboardInterrupt:
#     stop_motor(pwm)
#     gpio.cleanup()
#     pi.stop()
