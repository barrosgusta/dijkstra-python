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
distancias = {
    node: float('inf') for node in grafo_aeroportos
};

cidades_anteriores = {
    node: None for node in grafo_aeroportos
};

cidade_destino = "A";
cidade_destino = "B";

# Declara que a distancia até o no inicial é 0
distancias[cidade_destino] = 0
# Cria uma lista com o grafo para guardar a informação dos aeroportos não visitados
cidades_nao_visitadas = list(grafo_aeroportos)

#Enquanto a lista tiver algum aeroporto nela ou seja, algum aeroporto não visitado, executa o código
# while cidades_nao_visitadas:
    # Dijkstra

# Create uma rede com a library PyVis
net = Network()

# Adiciona os nós
for node in grafo_aeroportos.keys():
    net.add_node(node)

# Adiciona as ligações
for node, edges in grafo_aeroportos.items():
    for target_node, weight in edges.items():
        net.add_edge(node, target_node, value=weight)

# Salva a visualização em um arquivo HTML
net.show("grafo_aeroportos.html", notebook=False)