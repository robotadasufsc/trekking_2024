import comunicacao.python.funcao_sonar3 as funcao_sonar3

porta = 'COM7'
freq = 9600

ser = funcao_sonar3.configurar_porta(porta, freq)


while True:
   array = funcao_sonar3.dados(ser)
   #valor  = funcao_sonar3.sonar(ser)
   print(array)
   print('')



    
# colocar variaveis globais no codigo principal pra usar nas funcoes
# filtrar valores iguais pra tirar o time.sleep da funcao dados
# funcao generica no arudino que recebe somentes as portas digitais do sensor
