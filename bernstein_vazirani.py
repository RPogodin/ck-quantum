import pennylane as qml
from pennylane import numpy as np

# Bernstein-Vazirani

ALWAYS_ONE_WIRE = 0
ALWAYS_ZERO_WIRE = 1
ALWAYS_MINUS_WIRE = 2
CONSTANT_WIRES_COUNT = 3




x0 = 1
x1 = 1
x2 = 1


def get_wire(i):
    return i + CONSTANT_WIRES_COUNT


def xor_oracle(x, y):
    xs_coef = [x0, x1, x2]
    for i in range(3):
        if xs_coef[i] == 1:
            qml.Toffoli(wires=[ALWAYS_ONE_WIRE, x[i], y])
        else:
            qml.Toffoli(wires=[ALWAYS_ZERO_WIRE, x[i], y])


def phase_oracle(x):
    xor_oracle(x, ALWAYS_MINUS_WIRE)


def bernstein_vazirani_algorithm():
    qml.PauliX(wires=ALWAYS_ONE_WIRE)
    qml.Hadamard(wires=ALWAYS_MINUS_WIRE)
    qml.PauliZ(wires=ALWAYS_MINUS_WIRE)

    qml.Hadamard(wires=get_wire(0))
    qml.Hadamard(wires=get_wire(1))
    qml.Hadamard(wires=get_wire(2))

    phase_oracle([get_wire(0), get_wire(1), get_wire(2)])

    qml.Hadamard(wires=get_wire(0))
    qml.Hadamard(wires=get_wire(1))
    qml.Hadamard(wires=get_wire(2))

    return qml.probs(wires=[get_wire(0), get_wire(1), get_wire(2)])

qml.drawer.use_style("default")

dev = qml.device("default.qubit", shots=1000, wires=4 + CONSTANT_WIRES_COUNT)

circuit = qml.QNode(bernstein_vazirani_algorithm, dev)
probs = circuit()
binary_str = "{0:b}".format(np.argmax(probs))
binary_str = "0" * (3 - len(binary_str)) + binary_str
for i in range(3):
    print(f"x{i} = {int(binary_str[i])}")
