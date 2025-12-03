# Tính toán
inputs = ["00", "01", "10", "11"]

for inp in inputs:
    qc = QuantumCircuit(2)

    # 1. Khởi tạo trạng thái đầu vào
    # Nếu bit là '1', ta dùng cổng X để lật |0> thành |1>
    if inp[0] == "1":
        qc.x(1)
    if inp[1] == "1":
        qc.x(0)

    # 2. Áp dụng mạch H + CNOT
    qc.h(1)  # H lên qubit 1
    qc.cx(1, 0)  # CNOT (control=1, target=0)

    # 3. Xem kết quả
    state = Statevector(qc)
    pretty_output = format_state(state)
    print(f"|{inp}>      | {pretty_output}")
