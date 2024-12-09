# !/bin/bash

# This script is used to run the main program

function menu() {
    echo -e "\033[92m1.\033[0m $1 exe1-b <n>"
    echo -e "\033[92m2.\033[0m $1 exe1-c"
    echo -e "\033[92m5.\033[0m $1 exe3"
    echo -e "\033[92m6.\033[0m $1 exe3-test"
    echo -e "\033[92m6.\033[0m $1 exe4"
    echo -e "\033[92m6.\033[0m $1 exe5 <n>"
    echo -e "\033[92m6.\033[0m $1 help"
}

# If the input is lower than 1, the program will exit
if [ $# -lt 1 ]; then
    echo -e "\033[91;1mError:\033[0m The program needs at least 1 argument"
    echo -e "For more information, type: \033[1;92m$0 help\033[0m"
    exit 1
fi

if [ $1 == "help" ]; then
    echo -e "\033[92;1mUsage:\033[0m $0 <command> <args>"
    echo -e "\033[92;1mCommands:\033[0m"
    menu $0
    exit 0
fi

ACTUAL_PATH=$(pwd)
SRC_PATH=$(dirname $0)

cd $SRC_PATH

if [ $1 == "exe1-b" ]; then
    cd exercise1
    python secuencia.py
    cd ..
elif [ $1 == "exe1-c" ]; then
    cd exercise1
    python graph.py
    cd ..
elif [ $1 == "exe3" ]; then
    cd exercise3
    python main.py
    cd ..
elif [ $1 == "exe3-test" ]; then
    cd exercise3
    coverage run -m unittest discover
    coverage report -m
    coverage html
    cd ..
else
    echo -e "\033[91;1mError:\033[0m The command is not valid"
    echo -e "For more information, type: \033[1;92m$0 help\033[0m"
    cd $ACTUAL_PATH
    exit 1
fi

cd $ACTUAL_PATH