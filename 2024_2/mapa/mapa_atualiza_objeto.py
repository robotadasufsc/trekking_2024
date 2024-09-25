# Valor que identifica objetos
valor_objetos = 1


# Criando classe de objetos
class Objeto:
   
   lista_obj = []


   def __init__(self, posicao, valor):
       self.posicao = posicao
       self.valor = valor
       Objeto.lista_obj.append(self)  # Armazenando em uma lista os objetos
       

def atualizar_objetos(): #função de atualização

    objeto3 = Objeto((5,5), valor_objetos)

    return objeto3

#juntando com o ultrassonico
porta = '/dev/ttyACM0'
freq = 9600

ser = funcao_sonar.configurar_porta(porta, freq)

while True:
    
    valor_sensor = int(funcao_sonar.sonar(ser))
    print(valor_sensor)
    
    if valor_sensor >= 30:

        break

atualizar_objetos() 
print("recebido")

# Criando os objetos que serão adicionados
objeto1 = Objeto((9, 0), valor_objetos)
objeto2 = Objeto((9,9), valor_objetos)

# Criando a matriz
matriz = np.zeros((10,10))


# Adicionando os objetos na matriz
for objeto in Objeto.lista_obj:
   matriz[objeto.posicao] = objeto.valor


# Criando uma matriz binária com o objeto de interesse destacado
matriz_objeto_destacado = np.zeros_like(matriz)
# adicionando um "false" em cada posição que há um objeto
for objeto in Objeto.lista_obj:
   matriz_objeto_destacado[objeto.posicao] = 1
print(matriz)
# Ponto de referência
referencia = (0, 0)
matriz[referencia] = 5


distancias_objeto = distance_transform_edt(matriz_objeto_destacado == 0)


print(matriz)


fig, ax = plt.subplots()


img = ax.imshow(distancias_objeto, cmap='YlOrRd', interpolation='none')


# Círculo de referência
circulo = Circle(referencia, 0.5, color='blue', alpha=0.5)
ax.add_patch(circulo)


# Mostrar a distância atual
distancia_text = ax.text(0.05, 0.95, '', transform=ax.transAxes, fontsize=12, verticalalignment='top')


# Atualizar distância
def atualizar_distancia():


   distancia_ref_obj = distancias_objeto[referencia[1], referencia[0]]
   distancia_text.set_text(f'Distância: {distancia_ref_obj:.2f}')
   plt.draw()

'''
# Mover a posição de referência
def mudar_posicao(event):


   global referencia


   step = 1
   nova_referencia = list(referencia)


   if event.key == 'up':
       nova_referencia[1] -= step
   elif event.key == 'down':
       nova_referencia[1] += step
   elif event.key == 'left':
       nova_referencia[0] -= step
   elif event.key == 'right':
       nova_referencia[0] += step


   nova_referencia = tuple(nova_referencia)


   if 0 <= nova_referencia[0] < matriz.shape[0] and 0 <= nova_referencia[1] < matriz.shape[1]:
       # Atualizando a matriz
       matriz[referencia] = 0  # removendo a referência antiga
       referencia = nova_referencia
       matriz[referencia] = 1  # adicionando a nova referência


       # Atualizando a imagem
       img.set_data(distance_transform_edt(matriz_objeto_destacado == 0))


       # Atualizando a posição do círculo
       circulo.center = referencia


       # Atualizando a distância
       atualizar_distancia()


# Conectando a função de atualização de posição ao evento de pressionar uma tecla
fig.canvas.mpl_connect('key_press_event', mudar_posicao)


# Inicializar a distância
atualizar_distancia()
'''

plt.title('Mapa')
plt.colorbar(img)
plt.show()