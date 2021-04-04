# Fase 3 - Teste - Tabuleiro

import copy
import heapq

# ----------------- Estado Objetivo -----------------------

goal = [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 0]]


# ----------------- Nó -----------------------

class Node:
    def __init__(self, state, parent, gcost = 0, hcost = 0):
        self.state = state
        self.gcost = gcost
        self.parent = parent
        self.hcost = hcost

    def f(self):
        return self.gcost + self.hcost

    def __lt__(self, other):
        return self.state < other.state

# ----------------- Leitura da entrada -----------------------
def read_write():
    matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    entrada = input().split(' ')
    entrada = [x for x in entrada if x]
    index = 0

    for i in range(4):
        for j in range(4):
            matriz[i][j] = int(entrada[index])
            index += 1
    return matriz

# ----------------- Encontrando espaço em branco -----------------------

def find_blank(Node):
    for i, linha in enumerate(Node.state):
        if 0 in linha:
            coluna = linha.index(0)
            return (i, coluna)


# ----------------- Gera sucessores -----------------------

def Gerasucessor(parent_node):

    Sucessores = []
    (i, j) = find_blank(parent_node)

    if i > 0:
        new_table = copy.deepcopy(parent_node.state)
        sucessor = Node(new_table, parent_node, 1 + parent_node.gcost, 0)
        board = sucessor.state
        board[i][j] = board[i - 1][j]  # up
        board[i - 1][j] = 0
        Sucessores.append(sucessor)

    if i < 3:
        new_table = copy.deepcopy(parent_node.state)
        sucessor = Node(new_table, parent_node, 1 + parent_node.gcost, 0)
        board = sucessor.state
        board[i][j] = board[i + 1][j]  # down
        board[i + 1][j] = 0
        Sucessores.append(sucessor)

    if j > 0:
        new_table = copy.deepcopy(parent_node.state)
        sucessor = Node(new_table, parent_node, 1 + parent_node.gcost, 0)
        board = sucessor.state
        board[i][j] = board[i][j - 1]  # left
        board[i][j - 1] = 0
        Sucessores.append(sucessor)

    if j < 3:
        new_table = copy.deepcopy(parent_node.state)
        sucessor = Node(new_table, parent_node, 1 + parent_node.gcost, 0)
        board = sucessor.state
        board[i][j] = board[i][j + 1]  # right
        board[i][j + 1] = 0
        Sucessores.append(sucessor)

    return Sucessores

# ------------- Heuristicas --------------------

def heuristic_1(Node):
    out_place = 0
    for i in range(4):
        for j in range(4):
            if Node[i][j] != goal[i][j]:
                out_place += 1

    return out_place



# ------------- A-Star --------------------


def check(State, A):
    index = 0
    for (x, y) in A:
        if str(y.state) == str(State):
            return index
        index += 1
    return None


def A_Star (iniTable):
    #Defining the A(Open States) and F(Close States) group as hash tables
    heap = [(iniTable.f(), iniTable)]
    A = {str(iniTable.state) : iniTable}
    F = {}
    #count = 0
    while heap:
        X = heapq.heappop(heap)
        if (X[1].state == goal):
            break
        else:
            sucessores = Gerasucessor(X[1])
            for sucessor in sucessores:
                sucessor.hcost = heuristic_1(sucessor.state)
                #index_A = check(sucessor.state, A)
                #index_F = check(sucessor.state, F)
                if not str(sucessor.state) in A:
                    if not str(sucessor.state) in F:
                        heapq.heappush(heap, (sucessor.f(), sucessor))
                        A[str(sucessor.state)] = sucessor
                if str(sucessor.state) in A:
                    if sucessor.gcost < A[str(sucessor.state)].gcost:
                        A.pop(str(sucessor.state))
                        index = check(sucessor.state, heap)
                        heap.pop(index)
                if  str(sucessor.state) in F:
                    if sucessor.gcost < F[str(sucessor.state)].gcost:
                        F.pop(str(sucessor.state))
                        A[str(sucessor.state)] = sucessor

            F[str(X[1].state)] = X[1]
            #count += 1

            #heap = sorted(heap, key=lambda tup: (tup[0], tup[1]))
            #print(len(A), "\n")
    print(X[1].gcost)

def main():
    iniState = Node(read_write(), None, 0, 0) #Node(state, parent, gcost, hcost)
    A_Star(iniState)

if __name__ == '__main__':
    main()

