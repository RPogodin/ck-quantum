import pennylane as qml
from pennylane import numpy as np

ALWAYS_ONE_WIRE = 0
ALWAYS_ZERO_WIRE = 1
ALWAYS_MINUS_WIRE = 2
CONSTANT_WIRES_COUNT = 3

def get_wire(i):
    return i + CONSTANT_WIRES_COUNT

# constant
def xor_oracle_f1(x, y):
    pass

# constant
def xor_oracle_f2(x, y):
    qml.CNOT(wires=[ALWAYS_ONE_WIRE, y])

# balanced
def xor_oracle_f3(x, y):
    qml.Toffoli(wires=[ALWAYS_ONE_WIRE, x[0], y])
    qml.Toffoli(wires=[ALWAYS_ONE_WIRE, x[1], y])

#balanced
def xor_oracle_f4(x, y):
    qml.CNOT(wires=[x[1], y])


black_boxes_dict = {"f1": xor_oracle_f1, "f2": xor_oracle_f2, "f3": xor_oracle_f3, "f4": xor_oracle_f4}

def get_random_black_box(black_boxes_dict):
    black_boxes_dict_list_keys = list(black_boxes_dict.keys())
    n = np.random.randint(0, len(black_boxes_dict_list_keys))
    print(f"{black_boxes_dict_list_keys[n]} black box was chosen")
    return black_boxes_dict_list_keys[n]

xor_oracle = black_boxes_dict[get_random_black_box(black_boxes_dict)]

def phase_oracle(x):
    xor_oracle(x, ALWAYS_MINUS_WIRE)




def doce_algorithm():
    qml.PauliX(wires=ALWAYS_ONE_WIRE)
    qml.Hadamard(wires=ALWAYS_MINUS_WIRE)
    qml.PauliZ(wires=ALWAYS_MINUS_WIRE)

    qml.Hadamard(wires=get_wire(0))
    qml.Hadamard(wires=get_wire(1))

    phase_oracle([get_wire(0), get_wire(1)])

    qml.Hadamard(wires=get_wire(0))
    qml.Hadamard(wires=get_wire(1))

    return qml.probs(wires=[get_wire(0), get_wire(1)])

dev = qml.device("default.qubit", shots=1000, wires= 5 + CONSTANT_WIRES_COUNT)


circuit = qml.QNode(doce_algorithm, dev)
prob_of_all_zeros = circuit()[0]

if prob_of_all_zeros > 0.99:
    print("Function is constant")
else:
    print("Function is balanced")

