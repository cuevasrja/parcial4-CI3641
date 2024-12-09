from abc import ABC, abstractmethod
from typing import List, Any

class Secuencia(ABC):
    """
    ### Description
    Abstract class that represents a sequence of elements.

    ### Attributes
    - Lista: List[Any] -> List of elements.

    ### Methods
    - agregar(elemento: Any) -> None: Abstract method that adds an element to the sequence.
    - remover() -> Any: Abstract method that removes an element from the sequence.
    - vacio() -> bool: Returns True if the sequence is empty, False otherwise.
    """
    def __init__(self):
        self.Lista: List[Any] = []

    @abstractmethod
    def agregar(self, elemento: Any):
        pass

    @abstractmethod
    def remover(self) -> Any:
        pass

    def vacio(self) -> bool:
        return len(self.Lista) == 0
    
class Pila(Secuencia):
    """
    ### Description
    Class that represents a stack of elements.

    ### Attributes
    - Lista: List[Any] -> List of elements.

    ### Methods
    - agregar(elemento: Any) -> None: Adds an element to the stack.
    - remover() -> Any: Removes an element from the stack.
    - vacio() -> bool: Returns True if the stack is empty, False otherwise.
    """
    def __init__(self):
        super().__init__()

    def agregar(self, elemento: Any) -> None:
        self.Lista.append(elemento)

    def remover(self) -> Any:
        if self.vacio():
            raise ValueError("La pila está vacía")
        return self.Lista.pop()
    
class Cola(Secuencia):
    """
    ### Description
    Class that represents a queue of elements.

    ### Attributes
    - Lista: List[Any] -> List of elements.

    ### Methods
    - agregar(elemento: Any) -> None: Adds an element to the queue.
    - remover() -> Any: Removes an element from the queue.
    - vacio() -> bool: Returns True if the queue is empty, False otherwise.
    """
    def __init__(self):
        super().__init__()

    def agregar(self, elemento: Any) -> None:
        self.Lista.append(elemento)

    def remover(self) -> Any:
        if self.vacio():
            raise ValueError("La cola está vacía")
        return self.Lista.pop(0)
    
# Test the classes

# Create a stack
pila = Pila()
assert pila.vacio()
pila.agregar(1)
assert not pila.vacio()
pila.agregar(2)
assert not pila.vacio()
pila.agregar(3)
assert not pila.vacio()
assert pila.remover() == 3
assert not pila.vacio()
assert pila.remover() == 2
assert not pila.vacio()
assert pila.remover() == 1
assert pila.vacio()

# Create a queue
cola = Cola()
assert cola.vacio()
cola.agregar(1)
assert not cola.vacio()
cola.agregar(2)
assert not cola.vacio()
cola.agregar(3)
assert not cola.vacio()
assert cola.remover() == 1
assert not cola.vacio()
assert cola.remover() == 2
assert not cola.vacio()
assert cola.remover() == 3
assert cola.vacio()

print("All tests passed!")