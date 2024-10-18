import RPi.GPIO as GPIO
import time

val_anteriores = [0,0,0]

def setup_sensor(trigger_pin, echo_pin):
    GPIO.setup(trigger_pin, GPIO.OUT)
    GPIO.setup(echo_pin, GPIO.IN)

def medir_distancia(trigger_pin, echo_pin):
    pulso_inicial = 0
    pulso_final = 0
    
    #print("oi")
    GPIO.output(trigger_pin, GPIO.LOW)
    time.sleep(0.01)

    # Envia um pulso de 10µs no pino Trigger
    #pulso_inicial = time.time()
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, GPIO.LOW)
    
   
    #b = 0
    '''
    while b == 0:
        print("estado ", GPIO.input(echo_pin))
        if GPIO.input(echo_pin) == GPIO.HIGH:
            print("oi2")
            pulso_final = time.time()
            b = 1
            
    '''
    # Espera pelo início do pulso de retorno no Echo
    while GPIO.input(echo_pin) == GPIO.LOW:
        #print("oi1")
        pulso_inicial = time.time()
        #print(pulso_inicial)
        #b += 1
        #if b == 2000:
          #  break


    # Captura o final do pulso de retorno no Echo
    while GPIO.input(echo_pin) == GPIO.HIGH:
        #print("oi2")
        pulso_final = time.time()
        #b += 1
        #if b == 2000:
           # break

   # if pulso_final == 0 or pulso_inicial == 0:
    #    return -10

    # Calcula a duração do pulso
    duracao_pulso = pulso_final - pulso_inicial

    # Calcula a distância em centímetros (velocidade do som: 34300 cm/s)
    distancia = duracao_pulso * 34300 / 2
    
    #print("distancia ", distancia)


    return distancia
    


def coletar_distancias(sensores):
    global val_anteriores
    valores = []
    for trigger_pin, echo_pin in sensores:
        dist = medir_distancia(trigger_pin, echo_pin)
        valores.append(dist)
     
    
    if val_anteriores[0] != 0: 
        for i in range(3):
            if valores[i] > 150:
                valores[i] = val_anteriores[i]
    else:
        val_anteriores = valores
        
    for i in range(3):
        if val_anteriores[i] > 150:
            val_anteriores[i] = 150
    
   
    return valores
    

