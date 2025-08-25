import sys
import numpy as np
from numpy.random import default_rng
import random
import timeit

np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(linewidth=sys.maxsize)

##Created by Heitor Gabriel Lucena Albuquerque
'''
Este código gera duas matrizes aleatórias (A e B) de tamanho 100 x 100. As matrizes são simétricas e reais em dupla precisão.

   + Executa as seguintes operações matriciais:

    - Soma: C = A + B
    - Multiplicação: C = A x B
    - Transposta: C = A'
    - Calculo do traço da Matriz: y = Tr(A)
    - Encontra o maior e o menor valor da matriz  
    '''


A = np.random.rand(100,100) # Criação de uma matriz A 100x100, formada por números reais entre 0 e 1 de dupla precisão (float de 64 bytes)
A = A + A.T # Para a matriz aleatória ser simétrica, basta somarmos ela com a sua transposta (A+AT)

B = np.random.rand(100,100) # É realizado o mesmo formato de criação para a matriz B
B = B + B.T

sumAB = A+B # Variável que armazena a soma de A+B

temp = """
import numpy as np
A = np.random.rand(100,100)
A = A + A.T
B = np.random.rand(100,100)
B = B + B.T
sumAB = A+B
prodAB = np.matmul(A,B)
Transitiva = A.T
Traco = np.trace(A)
C = A.T
maximo = np.max(A)
minimo = np.min(A)"""

tempCriacao = """
import numpy as np
A = np.random.rand(100,100)
A = A + A.T"""

prodAB = np.matmul(A,B) # Variável que armazena o produto A*B

C = A.T # Variável que armazena a transposta de A (Igual a A, pois ela é simétrica)

Traco = np.trace(A) # Variável que armazena o traço de A
maximo = np.max(A) # Variável que armazena o valor máximo de A
minimo = np.min(A) # Variável que armazena o valor mínimo de A


with open('Resultado.txt', 'w') as f:
    print(f"Matriz A:\n{A}\n", file = f)               #Printa as matrizes resultantes
    print(f"\nMatriz B:\n{B}\n", file = f)
    print(f"Matriz A+B:\n{sumAB}\n", file = f)
    print(f"Matriz A*B:\n{prodAB}\n", file = f)
    print(f"Matriz AT (IGUAL POIS ELA É SIMÉTRICA):\n {C}\n", file = f)
    print(f"Traço da matriz A:\n{Traco}\n", file = f)
    print(f"Valor máximo da matriz A:\n{maximo}\n", file = f)
    print(f"Valor mínimo da matriz A:\n{minimo}\n", file = f)
    print(f"Dimensão das matrizes = {np.ndim(A)} (Bidimensional), sendo no formato: {np.shape(A)}\n", file = f)

    #Calcula o tempo de execução a partir da função timeit, que realiza a mesma operação X vezes e divide o tempo resultante pela quantidade X
    #Para se obter com alta precisão a média de tempo gasta com tal operação.
    print(f"Tempo de criação em média para uma matriz 100x100: {timeit.timeit(stmt=tempCriacao, setup = 'import numpy as np', number= 10000)/10000} segundos.\n", file = f)
    print(f"Tempo da operação de soma de matrizes (100x100) A+B em média: {timeit.timeit(stmt = 'sumAB = A+B', setup= temp, number = 10000)/10000} segundos.\n", file = f)
    print(f"Tempo da operação de produto entre as matrizes (100x100) A e B em média: {timeit.timeit(stmt='prodAB = np.matmul(A,B)', setup=temp, number = 10000)/10000} segundos\n", file = f)
    print(f"Tempo para gerar a matriz transposta (100x100) em média: {timeit.timeit(stmt = 'C = A.T', setup = temp, number = 10000)/10000} segundos.\n", file = f)
    print(f"Tempo para calcular o traço de uma matriz (100x100) em média: {timeit.timeit(stmt= 'Traco = np.trace(A)', setup = temp, number =10000)/10000} segundos.\n", file = f)
    print(f"Tempo para se calcular o máximo de uma matriz (100x100) em média: {timeit.timeit(stmt= 'maximo = np.max(A)', setup=temp, number = 10000)/10000} segundos.\n", file = f)
    print(f"Tempo para se calcular o mínimo de uma matriz (100x100) em média: {timeit.timeit(stmt= 'minimo = np.min(A)', setup=temp, number = 10000)/10000} segundos.\n", file = f)

