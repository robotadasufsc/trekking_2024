import serial
import time


# funcao para fazer comunicacao serial entre arduino e raspberry
def configurar_porta(porta, baudrate):
    ser = serial.Serial(porta, baudrate)
    time.sleep(2)  # Aguarda 2 segundos para estabilizar a conexao
    return ser

# funcao que recebe os valores dos 5 sensores arduino
def sonar(ser):
    k = 0
    valores = [0, 0, 0, 0, 0]
    while True:
        if ser.in_waiting > 0:
            k = k+1
            line = ser.readline().decode('utf-8', errors='ignore').rstrip()
            if line[0] in '0123456789':
                line = int(line)
            valores[k-1] = line    
            if k == 5:
                return valores
                
# funcao que organiza os dados de uma forma mais legivel na tela
def dados(ser):
    sensor = [[0 for _ in range(10)] for _ in range(5)] # inicializa com zeros
    for i in range(5):
        for k in range(10):
            valor = sonar(ser)
            sensor[i][k] = valor[i]
    print('---------------')
            

    return sensor
        

# funcao que retira dados indesejados         
def filtro(ser):
    x = 0
    valor = [[[0 for _ in range(10)] for _ in range(5)]]
    valor4 = [[[0 for _ in range(10)] for _ in range(5)]]
    while True:
        valor2 = valor[x]
        valor.append(dados(ser))
        x = x+1
        
        valor3 = valor[x]
        for i in range(5):
            for k in range(10):
                if valor3[i][k] == valor2[i][k]:
                    valor4[i][k] = 'bateu'
                    

                elif valor3[i][k] != valor2[i][k]:
                        valor4[i][k] = valor3[i][k]
        return valor4
                
        
        
          

#ser.close()
