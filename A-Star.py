import copy
import heapq
import sys
import time

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

# ----------------- Estado Objetivo -----------------------

goal = [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 0]]


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

    return int(out_place)

def heuristic_2(state):
    aux = []
    out_place = 0
    for i in range(4):
        for j in range(4):
            aux.append(state[j][i])

    for x in range(16):
        if x == 0 :
            pass
        else:
            if aux[x] != (aux[x-1] + 1):
                if aux[x-1] != 0:
                    out_place += 1
    return out_place


def heuristic_3(state):
    goal_manhattan = {  1 : (0,0) , 2: (1,0), 3: (2, 0), 4: (3, 0),
                    5: (0, 1), 6: (1, 1), 7: (2, 1), 8: (3, 1),
                    9: (0, 2), 10: (1, 2), 11: (2, 2), 12: (3, 2),
                    13: (0, 3), 14: (1, 3), 15: (2, 3), 0: (3, 3) }
    soma = 0
    for i in range(4):
        for j in range(4):
            if(state[i][j]):
              value = state[i][j]
              x, y = goal_manhattan[value]
              soma += abs(i - x)
              soma += abs(j - y)

    return soma    

def heuristic_4(state):
    p1 = 0.3
    p2 = 0.2
    p3 = 0.5

    return (p1 * heuristic_1(state)) + (p2 * heuristic_2(state)) + (p3 * heuristic_3(state))

def heuristic_5(state):
    return max(heuristic_1(state), heuristic_2(state), heuristic_3(state))

# ------------- A-Star --------------------

def removeFromHeap(heap, value):
	index = 0
	for (x, y) in heap:
		if y.state == value:
			heap.pop(index)
		index += 1
	heapq.heapify(heap)


def A_Star (iniTable):
    #Defining the A(Open States) and F(Close States) group as hash tables
    heap = [(iniTable.f(), iniTable)]
    A = {str(iniTable.state) : iniTable}
    F = {}
    while heap:
        X = heapq.heappop(heap)
        if (X[1].state == goal):
            break
        else:
            sucessores = Gerasucessor(X[1])
            for sucessor in sucessores:
                sucessor.hcost = heuristic_1(sucessor.state)
                if not str(sucessor.state) in A:
                    if not str(sucessor.state) in F:
                        heapq.heappush(heap, (sucessor.f(), sucessor))
                        A[str(sucessor.state)] = sucessor
                if str(sucessor.state) in A:
                    if sucessor.gcost < A[str(sucessor.state)].gcost:
                        A.pop(str(sucessor.state))
                        removeFromHeap(heap, sucessor.state)
                if  str(sucessor.state) in F:
                    if sucessor.gcost < F[str(sucessor.state)].gcost:
                        F.pop(str(sucessor.state))
                        A[str(sucessor.state)] = sucessor

            F[str(X[1].state)] = X[1]
    print("Movements:", X[1].gcost)
    print("Memory usage (bytes):", int(sys.getsizeof(A) + sys.getsizeof(F)))

def main():
    inicio = time.time()
    iniState = Node(read_write(), None, 0, 0) #Node(state, parent, gcost, hcost)
    A_Star(iniState)
    fim = time.time()
    print("Execution time:",round(((fim - inicio)*1000)/1000,3),"s")
if __name__ == '__main__':
    main()