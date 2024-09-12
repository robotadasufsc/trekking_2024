import RPi.GPIO as GPIO
import time

# Definindo o modo de numeração dos pinos
GPIO.setmode(GPIO.BCM)

# Definindo os pinos do Trigger e Echo
TRIG = 19  # GPIO 23
ECHO = 26  # GPIO 24

# Configurando os pinos de Trigger e Echo
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def medir_distancia():
    # Certificando que o Trigger está baixo
    GPIO.output(TRIG, LOW)
    time.sleep(0.5)  # Aguarda X segundos antes de começar a medição
    
    # Envia um pulso de 10µs no pino Trigger
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)  # Pulso de 10 microsegundos
    GPIO.output(TRIG, GPIO.LOW)
    
    # Espera pelo início do pulso de retorno no Echo
    while GPIO.input(ECHO) == GPIO.LOW:
        pulso_inicial = time.time()
    
    # Captura o final do pulso de retorno no Echo
    while GPIO.input(ECHO) == GPIO.HIGH:
        pulso_final = time.time()
    
    # Calcula o tempo de duração do pulso
    duracao_pulso = pulso_final - pulso_inicial
    
    # Calcula a distância em centímetros (velocidade do som: 34300 cm/s)
    distancia = duracao_pulso * 34300 / 2
    
    return distancia

try:
    while True:
        dist = medir_distancia()
        print(f"Distância: {dist:.2f} cm")
        time.sleep(1)

except KeyboardInterrupt:
    print("Medição interrompida pelo usuário")
    GPIO.cleanup()  # Limpa os pinos GPIO usados
