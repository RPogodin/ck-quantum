import pennylane as qml
from pennylane import numpy as np


def U_start():
    qml.PauliX(wires=2)
    for i in range(3):
        qml.Hadamard(wires=i)
        
def U_f():
    qml.Toffoli(wires=[0, 1, 2])
    
def G():
    for i in range(2):
        qml.Hadamard(wires=i)
        qml.PauliX(wires=i)

    qml.Toffoli(wires=[0, 1, 2])
    for i in range(2):
        qml.PauliX(wires=i)
        qml.Hadamard(wires=i)

def U_iteration():
    U_f()
    G()
    
dev = qml.device('default.qubit', shots=1, wires=3)

@qml.qnode(dev)
def circuit(N: int):
    U_start()
    for t in range(N):
        U_iteration()
    return qml.probs(wires=[0, 1])


print(circuit(N=1))
