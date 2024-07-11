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
#pi = pigpio.pi()
#pi = pigpio.pi('localhost', 8888)
pwm = gpio.PWM(PWM_PIN_A, 1)

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
    gpio.cleanup()  # Limpa a configuracao de todos os pinos


#FunÃ§Ã£o para controlar o servo motor
def set_servo_angle(duty):
    gpio.cleanup()  # Limpa a configuracao de todos os pinos
    #duty = (angle / 18) + 2
    #pi.set_servo_pulsewidth(SERVO_PIN, duty)
    gpio.setmode(gpio.BCM)
    gpio.setup(SERVO_PIN, gpio.OUT)

    servo = gpio.PWM(13,50)
    servo.start(0)   
    servo.ChangeDutyCycle(duty)  


# Exemplo de movimento do carrinho
try:
    while True:
        
        #pwm_motor_a = motor_backward(PWM_PIN_A, IN1_PIN_A, IN2_PIN_A)
        #pulso = angle_to_pulsewidth(90)
        stop_motor(pwm)









        break
        set_servo_angle(9)  # PosiÃ§Ã£o central do servo
        time.sleep(1)
        set_servo_angle(11)
        time.sleep(1)
        #liga_led()
        #time.sleep(2)  # Movimento para frente por 2 segundos
        #desliga_led()
        #stop_motor(pwm)

        

        #time.sleep(1)  # Pausa de 1 segundo

        #pwm_motor_a = motor_forward(PWM_PIN_A, IN1_PIN_A, IN2_PIN_A)

        #time.sleep(2)  # Movimento para trÃ¡s por 2 segundos

        #stop_motor(pwm_motor_a)
        

except KeyboardInterrupt:
    stop_motor(pwm)
    gpio.cleanup()
    pi.stop()