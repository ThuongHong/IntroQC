# 1. Khởi tạo mạch 2 qubit
qc = QuantumCircuit(2)

# 2. Tạo trạng thái đầu vào |+>|+>
qc.h([0, 1])

# 3. Áp dụng Oracle pha Z_f cho hàm XOR
# Lý thuyết: (-1)^(x XOR y) = (-1)^x * (-1)^y => Cổng Z trên cả 2 qubit
qc.z(0)
qc.z(1)

# 4. Hiển thị kết quả
state = Statevector(qc)
pretty_output = format_state(state)
print(f"Trạng thái cuối cùng sau Oracle pha Z_f: | {pretty_output}")
