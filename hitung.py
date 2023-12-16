import numpy as np
# from decimal import Decimal
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
x_target = 2.70

# Fungsi objektif untuk minimasi
def objective(params):
    i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,i21,i22,i23,i24,i25,i26,i27,i28,i29,i30,i31,i32,i33,i34,i35,i36,i37,i38,i39,i40,i41,i42,i43,i44,i45,i46,i47=params
    domain1=(i1+i2+i3+i4+i5+i6+i7+i8+i9+i10)*(1.3/13)
    
    aspek2=(i11+i12+i13+i14)*(2.5/10)
    aspek3=(i15+i16+i17+i18)*(2.5/10)
    aspek4=(i19+i20)*(2.5/5)
    aspek5=(i21+i22+i23+i24+i25+i26+i27+i28)*(1.5/12)
    aspek6=(i29+i30+i31)*(1.5/4.5)
    aspek7=(i32+i33+i34+i35+i36+i37+i38+i39+i40+i41)*(2.75/27.5)
    aspek8=(i42+i43+i44+i45+i46+i47)*(3/18)
    domain2=(aspek2*(10/25))+(aspek3*(10/25))+(aspek4*(5/25))
    domain3=(aspek5*(12/16.5))+(aspek6*(4.5/16.5))
    domain4=(aspek7*(27.5/45.5))+(aspek8*(18/45.5))
    # print(domain1,domain2,domain3,domain4)
    return (domain1*(13/100))+(domain2*(25/100))+(domain3*(16.5/100))+(domain4*(45.5/100))

# Batasan nilai a, b, c, d antara 0 dan 4
bounds = [(1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5),
(1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5),
(1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5),
(1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5),
(1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5)]

# Kondisi batasan linear
constraint = {'type': 'eq', 'fun': lambda params: x_target - objective(params)}

# Nilai awal (initial guess)
initial_guess = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

# Melakukan minimasi
result = minimize(objective, initial_guess, bounds=bounds, constraints=constraint)
indikator=[]
# Menampilkan hasil
for i in range(47):
    indikator.append(round(result.x[i]))
    print(i+1,indikator[i])
print(objective(indikator))
# Menghitung nilai x berdasarkan nilai a, b, c, d terbaru
# x_calculated = (result.x[0] * ba + result.x[1] * bb + result.x[2] * bc + result.x[3] * bd) / (ba + bb + bc + bd)

# # Menampilkan hasil perbandingan dengan pola data sebelumnya
# print("\nPerbandingan dengan pola data sebelumnya:")
# print("Nilai x yang dihitung:", x_calculated)
# print("Nilai x yang diketahui:", x_target)
# print("Selisih antara nilai x dihitung dan x diketahui:", abs(x_calculated - x_target))
