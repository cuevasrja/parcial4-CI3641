from abc import ABC, abstractmethod
from typing import List
from secuencia import Pila, Cola, Secuencia

class Busqueda(ABC):
    """
    ### Description
    Abstract class that represents a search algorithm.

    ### Attributes
    - Grafo: List[List[int]] -> Graph represented as an adjacency list.

    ### Methods
    - crear_secuencia() -> Secuencia: Abstract method that creates a sequence.
    - buscar(D: int, H: int) -> int: Searches for the shortest path between two nodes.
    """
    def __init__(self, grafo: List[List[int]]):
        self.Grafo: List[List[int]] = grafo

    @abstractmethod
    def crear_secuencia(self) -> Secuencia:
        pass

    def buscar(self, D: int, H: int) -> int:
        visitados: List[bool] = [False] * len(self.Grafo)
        secuencia: Secuencia = self.crear_secuencia()
        secuencia.agregar(D)
        visitados[D] = True
        while not secuencia.vacio():
            nodo: int = secuencia.remover()
            if nodo == H:
                return sum(visitados)
            for vecino in self.Grafo[nodo]:
                if not visitados[vecino]:
                    secuencia.agregar(vecino)
                    visitados[vecino] = True
        return -1

class DFS(Busqueda):
    """
    ### Description
    Class that represents a depth-first search algorithm.

    ### Attributes
    - Grafo: List[List[int]] -> Graph represented as an adjacency list.

    ### Methods
    - crear_secuencia() -> Pila: Creates a stack.
    """
    def __init__(self, grafo: List[List[int]]):
        super().__init__(grafo)

    def crear_secuencia(self) -> Pila:
        return Pila()

class BFS(Busqueda):
    """
    ### Description
    Class that represents a breadth-first search algorithm.

    ### Attributes
    - Grafo: List[List[int]] -> Graph represented as an adjacency list.

    ### Methods
    - crear_secuencia() -> Cola: Creates a queue.
    """
    def __init__(self, grafo: List[List[int]]):
        super().__init__(grafo)

    def crear_secuencia(self) -> Cola:
        return Cola()
    
# Test the classes

# Graph represented as an adjacency list
grafo: List[List[int]] = [
    [1, 2],     # 0
    [0, 3, 4],  # 1
    [0, 5, 6],  # 2
    [1],        # 3
    [1],        # 4
    [2],        # 5
    [2]         # 6
]

# Create a DFS object
dfs: DFS = DFS(grafo)
# Create a BFS object
bfs: BFS = BFS(grafo)

# Test the DFS algorithm
print(dfs.buscar(0, 6))
print(dfs.buscar(0, 3))
print(dfs.buscar(0, 5))
print(dfs.buscar(0, 4))
print(dfs.buscar(0, 1))
print(dfs.buscar(0, 2))

# Test the BFS algorithm
print(bfs.buscar(0, 6))
print(bfs.buscar(0, 3))
print(bfs.buscar(0, 5))
print(bfs.buscar(0, 4))
print(bfs.buscar(0, 1))