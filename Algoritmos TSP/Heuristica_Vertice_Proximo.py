from numpy import loadtxt

def ProcurarCaminho(Matriz, Vertice_Atual, Verificar_Passagem, Tamanho):
    # começa sempre no [0][0]
    contador = 0
    vetor_valor_arestas = []
    vetor_indices_vertices = []

    vetor_indices_vertices.append(0)

    # enquanto eu tiver vértices ainda para passar
    while contador < Tamanho-1:
        if(Verificar_Passagem[Vertice_Atual] == 0):
            menor, index = EncontrarMenor(Matriz, Vertice_Atual, Verificar_Passagem, Tamanho)

            # anoto que já passei por esse vértice
            Verificar_Passagem[Vertice_Atual] = 1
            # pego a posição para esse próximo vertice
            Vertice_Atual = index
                
            vetor_valor_arestas.append(menor)
            vetor_indices_vertices.append(index)

            #print(f'Vetor de verificacao: {Verificar_Passagem}')
            #print(f'Posicao do menor valor: {index} valor: {menor}')
        contador += 1
    
    # faz a última ligação, o último vértice que foi pego com o primeiro que foi passado
    ultimo = Matriz[Vertice_Atual][0]
    vetor_valor_arestas.append(ultimo)

    vetor_indices_vertices.append(0)

    return vetor_valor_arestas, vetor_indices_vertices



def EncontrarMenor(Matriz, Vertice_Atual, Verificar_Passagem, Tamanho):
    
    # pego o maior valor de vetor, para depois poder ir pegando os menores, garantindo diminuir
    menor = max(Matriz[Vertice_Atual])

    for j in range(0, Tamanho):

        # print(f'Atual: {Matriz[Vertice_Atual][j]} Menor: {menor}')
        
                                                # para evitar os ciclos iguais [X][X]
        if(Matriz[Vertice_Atual][j] < menor and Vertice_Atual != j and Verificar_Passagem[j] == 0):
            menor = Matriz[Vertice_Atual][j]

    index = list( Matriz[Vertice_Atual] ).index(menor)

    return menor, index



#Matriz = loadtxt('tsp1_253.txt', dtype=int)
Matriz = loadtxt('tsp2_1248.txt', dtype=int)
#Matriz = loadtxt('tsp3_1194.txt', dtype=int)
#Matriz = loadtxt('tsp4_7013.txt', dtype=int)
#Matriz = loadtxt('tsp5_27603.txt', dtype=int)


Tamanho = len(Matriz[0])

print(f'O tamanho pego é {Tamanho}')
# mas tem que usar -1, pois o Tamanho excede em 1 o indice, ex [0] [1] [2], 
# o Tamanho seria 3, mas o indice só até 2
#print(Matriz[Tamanho-1][Tamanho-1])


# cria um vetor aux p saber por onde já passou
Verificar_Passagem = list(range(Tamanho))

for i in range(0, Tamanho):
    # coloca todos os valores 0
    Verificar_Passagem[i] = 0

vetor_valor_arestas, vetor_indices_vertices = ProcurarCaminho(Matriz, 0, Verificar_Passagem, Tamanho)

Total = 0
for i in vetor_valor_arestas:
    Total += i

print('\n-----Ordem dos Vertices:')
print(*vetor_indices_vertices, sep = ' -> ')
print('-----Ordem das Arestas:')
print(*vetor_valor_arestas, sep = ' -> ')
print(f'Valor total: {Total}')