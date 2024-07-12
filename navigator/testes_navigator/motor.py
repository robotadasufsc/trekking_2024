import bluerobotics_navigator as navigator
#import RPi.GPIO as gpio
import time
#import pigpio

navigator.init()


# Definir pinos dos motores
PWM_PIN_M = navigator.PwmChannel.Ch4 # Pino PWM para o motor 
IN1_PIN_M = navigator.PwmChannel.Ch3  # Pino IN1 para o motor s
IN2_PIN_M = navigator.PwmChannel.Ch2  # Pino IN2 para o motor 

# Definir pino do servo motor
SERVO_PIN = navigator.PwmChannel.Ch1 # Pino para o servo motor

# Definir estado dos PWMs
navigator.set_pwm_freq_hz(60)
navigator.set_pwm_enable(True)

# Inicializar o Navigator
navigator.init() 




# Funções de controle dos motores
def motor_forward(pin_pwm, pin_in1, pin_in2):
    navigator.set_pwm_channel_duty_cycle(pin_in1, 0)
    navigator.set_pwm_channel_duty_cycle(pin_in2, 1)
    navigator.set_pwm_channel_duty_cycle(pin_pwm, 1)
    navigator.set_pwm_enable(True)

def stop_motor(pin_pwm, pin_in1, pin_in2):
    navigator.set_pwm_enable(False)
    navigator.set_pwm_channel_duty_cycle(pin_in1, 0)
    navigator.set_pwm_channel_duty_cycle(pin_in2, 0)
    navigator.set_pwm_channel_duty_cycle(pin_pwm, 0)



# Exemplo de movimento do carrinho
try:
    print("ligando")
    time.sleep(5)  # Pausa de 1 segundo
    print("acelera")
    print(navigator.get_pwm_enable())

    motor_forward(PWM_PIN_M, IN1_PIN_M, IN2_PIN_M)
    print(navigator.get_pwm_enable())
 

    time.sleep(5)  # Pausa de 1 segundo
    print("parou")

    stop_motor(PWM_PIN_M, IN1_PIN_M, IN2_PIN_M)
    print(navigator.get_pwm_enable())


    
    print("espera")

except KeyboardInterrupt:
    #stop_motor(pwm_motor)
    #gpio.cleanup()
    #pi.stop()
    navigator.set_pwm_enable(False)