import pennylane as qml
from pennylane import numpy as np

ALWAYS_ONE_WIRE = 0
ALWAYS_ONE_WIRE_TWO = 1
CONSTANT_WIRES_COUNT = 2


def get_wire(i):
    return i + CONSTANT_WIRES_COUNT


N = 3
M = N - 1


def int_to_binary(x, N=0):
    res = [1 if x == "1" else 0 for x in "{0:b}".format(x)]
    if res:
        while len(res) < N:
            res.append(0)
    return res


def xor_oracle(x, y):
    qml.Toffoli(wires=[ALWAYS_ONE_WIRE, x[0], y[0]])
    qml.Toffoli(wires=[ALWAYS_ONE_WIRE, x[2], y[0]])

    qml.Toffoli(wires=[ALWAYS_ONE_WIRE, x[1], y[1]])
    qml.Toffoli(wires=[ALWAYS_ONE_WIRE, ALWAYS_ONE_WIRE_TWO, y[1]])


qml.drawer.use_style("default")
dev = qml.device("default.qubit", shots=2, wires= N + M + CONSTANT_WIRES_COUNT)


def saimon_algorithm():
    qml.PauliX(wires=ALWAYS_ONE_WIRE)
    qml.PauliX(wires=ALWAYS_ONE_WIRE_TWO)

    for i in range(N):
        qml.Hadamard(wires=get_wire(i))

    xor_oracle([get_wire(i) for i in range(N)], [get_wire(N + i) for i in range(M)])

    for i in range(N):
        qml.Hadamard(wires=get_wire(i))

    for i in range(M):
        qml.measure(wires=[get_wire(N + i)])

    return qml.sample(wires=[get_wire(x) for x in range(N)])


circuit = qml.QNode(saimon_algorithm, dev)
print(circuit())
