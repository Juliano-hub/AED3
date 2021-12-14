from numpy import loadtxt, arange
from time import perf_counter
from itertools import permutations

def CompararTempo():
    # 1h
    # caso passar muito tempo, força a execução a parar 
    if(perf_counter() >= 3600):
        return True
    return False


def AlgoritmoForcaBruta(Matriz):
    Tamanho = len(Matriz[0])
    Todos_Simbolos = list(arange(Tamanho))

    x=0
    Contador=0
    SomaAnterior=0

    permutacao = permutations(list(Todos_Simbolos))   
    for PermutacaoAtual in permutacao:
        sair = CompararTempo()
        if(sair==True):
            return SomaAnterior, sair

        SomaPermutacaoAtual = 0
        if(PermutacaoAtual[0] != 0):
            # caso não começar com 0, quer dizer que a permutação não irá se iniciar em [0][0], então todas as permutação de [0][0]
            # foram feitas, então pode sair da execução
            break

        # troca os indices dos vertices pelos seus pesos e soma tudo
        for x in range(len(PermutacaoAtual)-1):
            SomaPermutacaoAtual += Matriz[PermutacaoAtual[x]][PermutacaoAtual[x+1]]
        
        # força o vertice final a se ligar com o inicio [0][0] para formar o ciclo
        SomaPermutacaoAtual += Matriz[PermutacaoAtual[x+1]][0]

        if(Contador < 1):
            Contador +=1
            SomaAnterior = SomaPermutacaoAtual
        # caso Contador >= 1, significa que já tem 1 combinação guardada, tanto sendo a primeira, ou alguma combinação que já foi comparada
        # e está sendo guardada por ser a menor de todas até o momento
        else:
            SomaAnterior = min(SomaAnterior, SomaPermutacaoAtual)

    return SomaAnterior, sair

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
print('Executando...')

MenorValorCaminho, SairPeloIf = AlgoritmoForcaBruta(Matriz)
print(f'Saiu pela delimitação de tempo:{SairPeloIf}')
print(f'O menor caminho eh: {MenorValorCaminho}')
fim = perf_counter()

print(f'Tempo de execução segundo calculo da biblioteca TIME: {fim - inicio} segundos')