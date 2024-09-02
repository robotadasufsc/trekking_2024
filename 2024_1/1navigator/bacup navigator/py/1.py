import numpy as np

# Criando duas matrizes aleatórias
A = np.random.rand(3, 3)
B = np.random.rand(3, 3)

# Imprimindo as matrizes
print("Matriz A:")
print(A)
print("\nMatriz B:")
print(B)

# Adicionando as matrizes
soma = A + B
print("\nSoma das matrizes A e B:")
print(soma)

# Multiplicando as matrizes
produto = np.dot(A, B)
print("\nProduto das matrizes A e B:")
print(produto)

# Calculando a transposta de uma matriz
transposta_A = np.transpose(A)
print("\nTransposta da matriz A:")
print(transposta_A)

# Calculando a inversa de uma matriz
try:
    inversa_A = np.linalg.inv(A)
    print("\nInversa da matriz A:")
    print(inversa_A)
except np.linalg.LinAlgError:
    print("\nA matriz A é singular e não possui inversa.")

# Calculando o determinante de uma matriz
determinante_A = np.linalg.det(A)
print("\nDeterminante da matriz A:", determinante_A)
