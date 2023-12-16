import numpy as np
from scipy.optimize import minimize

# Pola data yang diketahui
# data_known = np.array([
#     [1.1, 1.6, 1, 2.79, 1.98],
#     [2.9, 2.8, 2.09, 3.3, 2.7],
#     [0.87, 1.67, 1.10, 3.03, 2.9],
#     [0.78, 1.51, 0.99, 2.74, 1.89],
# ])

# Nilai konstan
ba, bb, bc, bd = 13, 25, 16.5, 45.5

# Target nilai x yang ingin dicapai
x_target = 2.9

# Fungsi objektif untuk minimasi
def objective(params):
    a, b, c, d = params
    return (a * ba + b * bb + c * bc + d * bd) / (ba + bb + bc + bd)

# Batasan nilai a, b, c, d antara 0 dan 4
bounds = [(0, 5), (0, 5), (0, 5), (0, 5)]

# Kondisi batasan linear
constraint = {'type': 'eq', 'fun': lambda params: x_target - objective(params)}

# Nilai awal (initial guess)
initial_guess = [0, 0, 0, 0]

# Melakukan minimasi
result = minimize(objective, initial_guess, bounds=bounds, constraints=constraint)

# Menampilkan hasil
print("Nilai a yang dihitung:", result.x[0])
print("Nilai b yang dihitung:", result.x[1])
print("Nilai c yang dihitung:", result.x[2])
print("Nilai d yang dihitung:", result.x[3])

# Menghitung nilai x berdasarkan nilai a, b, c, d terbaru
x_calculated = (result.x[0] * ba + result.x[1] * bb + result.x[2] * bc + result.x[3] * bd) / (ba + bb + bc + bd)

# Menampilkan hasil perbandingan dengan pola data sebelumnya
print("\nPerbandingan dengan pola data sebelumnya:")
print("Nilai x yang dihitung:", x_calculated)
print("Nilai x yang diketahui:", x_target)
print("Selisih antara nilai x dihitung dan x diketahui:", abs(x_calculated - x_target))
