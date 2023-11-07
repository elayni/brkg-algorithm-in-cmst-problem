def subroot_assignment(x, G, w, c, Q):
    """
    x: vetor de prioridades
    G: grafico representado como uma lista de adjacencias ou matriz
    w: vetor de demanda ou peso para cada vertice
    c: matriz de custo/distancia entre vertices
    Q: capacidade de cada subarvore
    """

    n = len(w)  # Numero de vertices
    a = [0] * n  # Vetor de subarvores a ser retornado
    s = [0] * n  # Espaço disponível em cada subárvore
    
    # Inicializa os vertices em ordem crescente de x
    vertices = list(range(n))
    vertices.sort(key=lambda i: x[i])
    
    assigned = []  # Lista de vertices ja atribuidos

    # Função auxiliar para encontrar a subárvore com espaço disponível para o vertice i
    def find_subtree_for(i):
        for j in assigned:
            if s[j] >= w[i]:
                return j
        return None

    # Atribui vertices às subárvores ou cria novas subárvores
    for i in vertices:
        subtree = find_subtree_for(i)
        if subtree is not None:
            # Atribui i à subárvore existente
            a[i] = subtree
            s[subtree] -= w[i]
        else:
            # Cria uma nova subárvore com i como raiz
            a[i] = i
            s[i] = Q - w[i]
            assigned.append(i)
    
    return a

# Exemplo de utilização
x = [0.5, 0.2, 0.9]  # Prioridades (geradas por chaves aleatórias no BRKGA)
G = [[0, 1, 2], [1, 0, 2], [2, 0, 1]]  # Grafico (não utilizado neste decoder simples)
w = [10, 20, 15]  # Demandas/pesos
c = [[0, 1, 3], [1, 0, 2], [3, 2, 0]]  # Custos/distancias (não utilizado neste decoder simples)
Q = 35  # Capacidade máxima de cada subárvore

# Executa o decoder de subarvore
assignment = subroot_assignment(x, G, w, c, Q)
print("Assignment:", assignment)
