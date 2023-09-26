from pyvis.network import Network

grafo_aeroportos = {
    'A': {'B': 2, 'F': 8, 'H': 17, 'E': 7, 'D': 4, 'C': 8, 'L': 27, 'G': 21},
    'B': {'F': 6, 'C': 5, 'A': 2},
    'C': {'A': 8, 'B': 5, 'D': 2, 'E': 7, 'I': 11, 'G': 10},
    'D': {'A': 4, 'C': 2, 'E': 4},
    'E': {'A': 7, 'C': 7, 'D': 4, 'F': 3, 'G': 9, 'H': 7},
    'F': {'A': 8, 'B': 6, 'E': 3, 'I': 6},
    'G': {'A': 21, 'C': 10, 'E': 9, 'J': 3, 'K': 6, 'L': 5, 'P': 10},
    'H': {'A': 17, 'E': 7, 'I': 1, 'M': 15, 'R': 15},
    'I': {'C': 11, 'F': 6, 'H': 1, 'J': 3, 'K': 2},
    'J': {'G': 3, 'I': 3, 'N': 2},
    'K': {'G': 6, 'I': 2, 'T': 9},
    'L': {'A': 27, 'G': 5, 'M': 3, 'N': 8, 'O': 1},
    'M': {'H': 15, 'L': 3, 'N': 6},
    'N': {'J': 2, 'L': 8, 'M': 6, 'P': 12, 'R': 12},
    'O': {'L': 1, 'R': 9},
    'P': {'G': 10, 'N': 12, 'Q': 3, 'R': 6},
    'Q': {'P': 3, 'R': 7},
    'R': {'H': 15, 'N': 12, 'O': 9, 'P': 6, 'Q': 7},
    'S': {'F': 13, 'T': 4, 'U': 11},
    'T': {'K': 9, 'S': 4, 'U': 6},
    'U': {'S': 11, 'T': 6, 'V': 2, 'W': 12},
    'V': {'U': 2, 'X': 6},
    'W': {'U': 12, 'X': 13},
    'X': {'V': 6, 'W': 13, 'AG': 9, 'AH': 11},
    'Y': {'Z': 5},
    'Z': {'Y': 5, 'AA': 8, 'AG': 5},
    'AA': {'Z': 8, 'AB': 7},
    'AB': {'AA': 7, 'AC': 6, 'AD': 3, 'AE': 4, 'AG': 7},
    'AC': {'AB': 6},
    'AD': {'AB': 3},
    'AE': {'AB': 4, 'AF': 3},
    'AF': {'AE': 3, 'AI': 22, 'AN': 50, 'AP': 7},
    'AG': {'X': 9, 'Z': 5, 'AB': 7, 'AH': 8},
    'AH': {'X': 11, 'AG': 8},
    'AI': {'AF': 22, 'AJ': 7, 'AM': 26},
    'AJ': {'AI': 7, 'AK': 12, 'AL': 15},
    'AK': {'AJ': 12, 'AL': 5},
    'AL': {'AJ': 15, 'AK': 5, 'AM': 6},
    'AM': {'AI': 26, 'AL': 6, 'AN': 4},
    'AN': {'AF': 50, 'AM': 4},
    'AO': {'AP': 7},
    'AP': {'AF': 7, 'AO': 7}
}

# Declara que todas as distancias são infinitas, já que nenhuma foi visitada
# Cria um dicionario com a cidade como chave e a distancia como valor
distancias = {
    node: float('inf') for node in grafo_aeroportos
};

# Declara que todas as cidades anteriores são nulas, já que nenhuma foi visitada
# Cria um dicionario com a cidade como chave e a cidade anterior como valor
cidades_anteriores = {
    node: None for node in grafo_aeroportos
};

def CidadeValida(cidade):
    return cidade in grafo_aeroportos

print("Cidades válidas: ")
print(grafo_aeroportos.keys())
print("Digite a cidade inicial: ")
cidade_inicial = input()
while not CidadeValida(cidade_inicial):
    print("Cidade inválida, digite novamente: ")
    cidade_inicial = input()

print("Digite a cidade destino: ")
cidade_destino = input()
while not CidadeValida(cidade_destino):
    print("Cidade inválida, digite novamente: ")
    cidade_destino = input()


# Declara que a distancia até o no inicial é 0
distancias[cidade_inicial] = 0
# Cria uma lista com o grafo para guardar a informação dos aeroportos não visitados
cidades_nao_visitadas = list(grafo_aeroportos)

#Enquanto a lista tiver algum aeroporto nela ou seja, algum aeroporto não visitado, executa o código
while cidades_nao_visitadas:
    #Seleciona a cidade com a menor distancia das cidades não visitadas usando funcoes lambda
    cidade_atual = min(cidades_nao_visitadas, key=lambda node: distancias[node])

    #Seleciona a cidade com a menor distancia das cidades não visitadas usando for
    # distancia_atual = float('inf')
    # for cidade, distancia in distancias.items():
    #     if cidade in cidades_nao_visitadas:
    #         if distancia < distancia_atual:
    #             distancia_atual = distancia
    #             cidade_atual = cidade

    #Compara a distancia da cidade atual com todas as cidades vizinhas, atualizando a distancia e a cidade anterior
    #Para cada cidade vizinha da cidade atual
    for cidade_vizinha, peso in grafo_aeroportos[cidade_atual].items():
        #Se a distancia da cidade atual + o peso da aresta for menor que a distancia da cidade vizinha
        if distancias[cidade_atual] + peso < distancias[cidade_vizinha]:
            #Atualiza a distancia da cidade vizinha
            distancias[cidade_vizinha] = distancias[cidade_atual] + peso
            #Atualiza a cidade anterior da cidade vizinha
            cidades_anteriores[cidade_vizinha] = cidade_atual

    #Remove a cidade atual da lista de cidades não visitadas
    cidades_nao_visitadas.remove(cidade_atual)

#Cria uma lista com o caminho percorrido
caminho = []

#Adiciona a cidade destino na lista
caminho.append(cidade_destino)

#Cria o caminho a partir das cidades anterioes de cada cidade
while cidades_anteriores[cidade_destino] != cidade_inicial:
    #Adiciona a cidade anterior da cidade destino na lista
    caminho.append(cidades_anteriores[cidade_destino])
    #Atualiza a cidade destino para a cidade anterior da cidade destino
    cidade_destino = cidades_anteriores[cidade_destino]

#Adiciona a cidade inicial na lista
caminho.append(cidade_inicial)

#Inverte a lista para mostrar o caminho correto
caminho.reverse()

#Imprime o caminho
print(caminho)

# Create uma rede com a library PyVis
net = Network()

# Adiciona os nós
for vertice in grafo_aeroportos.keys():
    net.add_node(vertice)

# Adiciona as ligações
for vertice, arestas in grafo_aeroportos.items():
    for vertice_alvo, peso in arestas.items():
        net.add_edge(vertice, vertice_alvo, value = peso)

# Salva a visualização em um arquivo HTML
net.show("grafo_aeroportos.html", notebook=False)