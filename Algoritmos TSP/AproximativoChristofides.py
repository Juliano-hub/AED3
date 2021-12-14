from networkx.algorithms.approximation.traveling_salesman import christofides
from networkx.convert_matrix import from_numpy_matrix
from numpy import loadtxt 
from time import perf_counter

def Menu():
    print('\n------------Menu:')
    print('1) tsp1_253.txt')
    print('2) tsp2_1248.txt')
    print('3) tsp3_1194.txt')
    print('4) tsp4_7013.txt')
    print('5) tsp5_27603.txt')
    op = int(input('Digite uma opção de arquivo para executar:'))

    return op

def Retornar_Arquivo(Escolher_Arquivo):
    if(Escolher_Arquivo == 1):
        Matriz = loadtxt('tsp1_253.txt', dtype=int)
    elif(Escolher_Arquivo == 2):
        Matriz = loadtxt('tsp2_1248.txt', dtype=int)
    elif(Escolher_Arquivo == 3):
        Matriz = loadtxt('tsp3_1194.txt', dtype=int)
    elif(Escolher_Arquivo == 4):
        Matriz = loadtxt('tsp4_7013.txt', dtype=int)
    elif(Escolher_Arquivo == 5):
        Matriz = loadtxt('tsp5_27603.txt', dtype=int)

    return Matriz

Escolher_Arquivo = Menu()

global inicio 
inicio = perf_counter()

Matriz = Retornar_Arquivo(Escolher_Arquivo)

Matriz_christofides = from_numpy_matrix(Matriz)

Matriz_christofides = christofides(Matriz_christofides)

Matriz_christofides = list(Matriz_christofides)

#print(Matriz_christofides)

Valores = []
#tps2_1248: [0, 2, 3, 4, 5, 1, 0]
#tsp2_1248: 378 -> 170 -> 223 -> 273 -> 164 -> 64

#tps1_253: [0, 7, 4, 3, 5, 9, 6, 1, 10, 2, 8, 0]
#tps1_253: 12 -> 9 -> 4 -> 12 -> 3 -> 99 -> 72 -> 12 -> 13 -> 23 -> 4

for i in range(len(Matriz_christofides)-1):
    Valores.append(Matriz[Matriz_christofides[i]][Matriz_christofides[i+1]])


#print(Valores)

print(f'Custo do caminho: {sum(Valores)}')

fim = perf_counter()

print(f'Tempo de execução segundo calculo da biblioteca TIME: {fim - inicio} segundos')