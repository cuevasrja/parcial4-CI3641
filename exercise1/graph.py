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
    