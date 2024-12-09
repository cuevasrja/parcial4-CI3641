from typing import Dict, List, Set


class ClassType:
    """
    ### Description
    Class that represents a class with its methods.

    ### Attributes
    - name: str -> Name of the class.
    - superclass: str|None -> Name of the superclass.
    - methods: Dict[str, str] -> Dictionary of methods.

    ### Methods
    - add_method(method: str) -> None: Adds a method to the class.
    - get_method(method: str) -> str|None: Returns the method if it exists in the class or its superclass.
    """

    def __init__(self, class_name: str, superclass: str|None = None):
        """
        ### Description
        Initializes the ClassType object.

        ### Parameters
        - class_name: str -> Name of the class.
        - superclass: str|None -> Name of the superclass.
        """
        self.name: str = class_name
        self.superclass: str|None = superclass
        self.methods: Dict[str, str] = {}

    def add_method(self, method: str) -> None:
        """
        ### Description
        Adds a method to the class.

        ### Parameters
        - method: str -> Name of the method.

        ### Returns
        - None
        """
        self.methods[method] = f'{self.name} :: {method}'

    def get_method(self, method: str) -> str|None:
        """
        ### Description
        Returns the method if it exists in the class or its superclass.

        ### Parameters
        - method: str -> Name of the method.

        ### Returns
        - str|None: Method if it exists, None otherwise.
        """
        if method in self.methods:
            return self.methods[method]
        elif self.superclass:
            return self.superclass.get_method(method)
        else:
            return None


class Simulator:
    """
    ### Description
    Class that represents a simulator of classes.
    
    ### Attributes
    - classes: Dict[str, ClassType] -> Dictionary of classes.

    ### Methods
    - add_class(class_name: str, methods: List[str], superclass_name: str|None = None) -> None: Adds a new class to the simulator.
    - describe_class(name: str) -> str: Describes an existing class in the simulator.
    """
    def __init__(self):
        """
        ### Description
        Initializes the Simulator object.
        """
        self.classes: Dict[str, ClassType] = {}

    def add_class(self, class_name: str, methods: List[str], superclass_name: str|None = None) -> None:
        """
        ### Description
        Adds a new class to the simulator.

        ### Parameters
        - class_name: str -> Name of the class.
        - methods: List[str] -> List of methods.
        - superclass_name: str|None -> Name of the superclass. Default is None.

        ### Returns
        - None
        """
        # Verify if the class name already exists in the simulator
        if class_name in self.classes:
            print(f'\033[91;1mError: La clase {class_name} ya existe.\n\033[0m')
            return
        # Verify if the superclass name exists
        if superclass_name and superclass_name not in self.classes:
            print(f'\033[91;1mError: La super clase {superclass_name} no existe.\n\033[0m')
            return
        # Verify if the methods have duplicates
        if len(set(methods)) < len(methods):
            print('\033[91;1mError: Nombres de métodos duplicados.\n\033[0m')
            return
        # Obtain the superclass from the classes dictionary
        superclass: ClassType = self.classes.get(superclass_name)
        # Verify if the class inherits from itself
        while superclass:
            if superclass.name == class_name:
                print(f'\033[91;1mError: La clase {class_name} no puede heredar de ella misma.\n\033[0m')
                return
            superclass = superclass.superclass
        # Obtain the superclass from the classes dictionary
        superclass = self.classes.get(superclass_name)
        # Create a new class that inherits from the superclass
        new_class: ClassType = ClassType(class_name, superclass)
        # Add the methods to the new class
        for method in methods:
            new_class.add_method(method)
        # Add the new class to the classes dictionary
        self.classes[class_name] = new_class

    def describe_class(self, name: str) -> str:
        """
        ### Description
        Describes an existing class in the simulator.

        ### Parameters
        - name: str -> Name of the class.

        ### Returns
        - str: Description of the class
        """
        # Verify if the class name exists in the simulator
        if name not in self.classes:
            print(f'\033[91;1mError: La clase {name} no existe.\n\033[0m')
            return
        # Obtain the class from the classes dictionary
        class_type: ClassType|str = self.classes[name]
        # Create a set to store the printed methods
        printed_methods: Set[str] = set()

        # Initialize the string of methods
        string_methods: str = ""
        # Iterate over classes until there is no superclass
        while class_type:
            # Iterate over the methods of the class
            for method in class_type.methods:
                # Check if the method has not been printed
                if method not in printed_methods:
                    # Include the method in the string and add it to the printed methods
                    if not string_methods:
                        string_methods = f'{method} -> {class_type.get_method(method)}'
                    else:
                        string_methods += f'\n{method} -> {class_type.get_method(method)}'
                    printed_methods.add(method)
            # Obtain the superclass from the classes dictionary
            class_type = class_type.superclass
        # Verify if there are no methods
        if not printed_methods:
            string_methods = f'La clase {name} no tiene métodos.'
        return string_methods