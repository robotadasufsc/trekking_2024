import RPi.GPIO as GPIO
import time

def setup_sensor(trigger_pin, echo_pin):
    GPIO.setup(trigger_pin, GPIO.OUT)
    GPIO.setup(echo_pin, GPIO.IN)

def medir_distancia(trigger_pin, echo_pin):
    GPIO.output(trigger_pin, GPIO.LOW)
    time.sleep(0.01)

    # Envia um pulso de 10µs no pino Trigger
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, GPIO.LOW)

    # Espera pelo início do pulso de retorno no Echo
    while GPIO.input(echo_pin) == GPIO.LOW:
        pulso_inicial = time.time()

    # Captura o final do pulso de retorno no Echo
    while GPIO.input(echo_pin) == GPIO.HIGH:
        pulso_final = time.time()

    # Calcula a duração do pulso
    duracao_pulso = pulso_final - pulso_inicial

    # Calcula a distância em centímetros (velocidade do som: 34300 cm/s)
    distancia = duracao_pulso * 34300 / 2

    return distancia

def coletar_distancias(sensores):
    valores = []
    for trigger_pin, echo_pin in sensores:
        dist = medir_distancia(trigger_pin, echo_pin)
        valores.append(dist)
    return valores
