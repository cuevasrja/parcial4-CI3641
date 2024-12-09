from simulator import Simulator

# Execute the simulator
simulator = Simulator()

# While the user does not enter "SALIR", the simulator will continue to run
while True:
    # Get the user's action
    command = input("> \033[94;1m")
    print("\033[0m", end="")

    # If the action is "SALIR", exit the loop
    if command.upper() == "SALIR":
        break
    # If the action starts with "CLASS ", try to add a class
    elif command.upper().startswith("CLASS "):
        # Divide the action into parts
        _, class_name, *methods = command.split()
        # If the methods list is not empty and the first element is ":", add a class with a superclass
        if len(methods) > 0 and methods[0] == ":":
            # Divide the methods list into superclass name and methods
            _, superclass_name, *methods = methods
            # If ":" is in the methods, print an error and continue with the next loop
            if ":" in methods:
                print("\033[91;1mError: El nombre \":\" no es válido para un método...\033[0m")
                continue
            # Add the class with a superclass name
            simulator.add_class(class_name, methods, superclass_name)
        else:
            # If ":" is in the methods, print an error and continue with the next loop
            if ":" in methods:
                print("\033[91;1mError: El nombre \":\" no es válido para un método.\033[0m")
                continue
            # Add the class without a superclass name
            simulator.add_class(class_name, methods)
    # If the action starts with "DESCRIBIR ", try to describe the class
    elif command.upper().startswith("DESCRIBIR "):
        # If the action is divided into two parts, describe the class
        if len(command.split()) == 2:
            _, class_name = command.split()
            print(simulator.describe_class(class_name))
        else:
            # If the action is not divided into two parts, print an error
            print("\033[91;1mError: Comando inválido.\033[0m")
            print("\033[92;1mUSO:\033[0m")
            print("\033[93m\tUSO: DESCRIBIR <nombre>\033[0m")
    else:
        # If the action is not valid, print an error
        print("\033[91;1mError: Comando inválido.\033[0m")
        print("\033[92;1mUSO:\033[0m")
        print("\033[93m\tCLASS <tipo> [<nombre>]\033[0m")
        print("\033[93m\tDESCRIBIR <nombre>\033[0m")
        print("\033[93m\tSALIR\033[0m")