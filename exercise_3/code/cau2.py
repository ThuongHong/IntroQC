# 3 qubit đầu vào (0, 1, 2) và 3 qubit đầu ra (3, 4, 5)
qc = QuantumCircuit(6)

# 1. Tính F = AB XOR C trên qubit 5
qc.ccx(0, 1, 5)  # Toffoli(A, B, F) -> F = AB
qc.cx(2, 5)  # CNOT(C, F) -> F = AB XOR C

# 2. Tính E = (NOT A)B + A(NOT C) trên qubit 4
# Phần 1: (NOT A)B
qc.x(0)  # NOT A
qc.ccx(0, 1, 4)  # Toffoli(NOT A, B, E) -> E = (NOT A)B
qc.x(0)  # Quay lại A ban đầu

# Phần 2: A(NOT C)
qc.x(2)  # NOT C
qc.ccx(0, 2, 4)  # Toffoli(A, NOT C, E) -> E = (NOT A)B + A(NOT C)
qc.x(2)  # Quay lại C ban đầu

# 3. Tính D = NOT A trên qubit 3
qc.x(0)  # NOT A
qc.cx(0, 3)  # CNOT(A, D) -> D = NOT A
qc.x(0)  # Quay lại A ban đầu
