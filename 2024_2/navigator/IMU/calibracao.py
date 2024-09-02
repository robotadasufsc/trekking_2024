import bluerobotics_navigator as navigator
from IPython.display import clear_output
import time
import numpy as np

# faz as inicializacoes necessarias
navigator.init()
valor1 = []
valor2 = [] 
valor3 =[]

# funcao de media movel para uma lista de valores
# values sao a lista de valores total
# window_size é o número dos ultimos valores recebidos na qual fará essa média
def moving_average(values, window_size):
    if len(values) < window_size:
        return sum(values) / len(values)
    else:
        return sum(values[-window_size:]) / window_size
    
# adiciona um valor a lista de valores total
# values sao a lista total
# window_size é o número de valores que será efetuado essa média móvel
# threshold é o limite que é considerado para esse valor ser usado na média ou descartado
# max_size é o tamanho maximo permitido pra lista total armazenar 
def add_value(values, new_value, window_size, threshold, max_size=1000):
    if len(values) < window_size:
        moving_avg = sum(values) / len(values) if values else new_value
    else:
        moving_avg = sum(values[-window_size:]) / window_size

    # Check for discrepancy
    if abs(new_value - moving_avg) <= threshold:
        values.append(new_value)
        
        # Ensure the values list does not exceed max_size
        if len(values) > max_size:
            values.pop(0)  # Remove the oldest value

    else:
        #print(f"Value {new_value} is a discrepancy and will be ignored.")
        pass
    return moving_average(values, window_size)


# calibra eixo y
def calibra_y(amostras):
    for i in range(amostras):  
        acceleration = navigator.read_accel()
        acy = acceleration.y
        valor1.append(acy)
    
    calibration_data = valor1
    calibration_data = np.array(calibration_data)
    media = np.mean(calibration_data, axis=0)
    return media

# calibra eixo x
def calibra_x(amostras):
    for i in range(amostras):
        acceleration = navigator.read_accel()
        acx = acceleration.x
        valor2.append(acx)
    
    calibration_data = valor2
    calibration_data = np.array(calibration_data)
    media = np.mean(calibration_data, axis=0)
    return media

# calibra eixo z
def calibra_z(amostras):
    for i in range(amostras):
        acceleration = navigator.read_accel()
        acz = acceleration.z
        valor3.append(acz)
    
    calibration_data = valor3
    calibration_data = np.array(calibration_data)
    media = np.mean(calibration_data, axis=0)
    return media
