import numpy as np
import pandas as pd
from app.models.isi import isiModel
from scipy.optimize import minimize

model=isiModel()
df = pd.read_csv('Data CSV/data 2018-2020 Grup Kementerian.csv')
for index, row in df.iterrows():
    if(row.id!='NaN'):
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
        initial_guess=[]
        bounds=[]
        for i in range(47):
            initial_guess.append(1)
            bounds.append([1,5])
        constraint_2018 = {'type': 'eq', 'fun': lambda params: float(row.indeks_2018)- objective(params)}
        constraint_2019 = {'type': 'eq', 'fun': lambda params: float(row.indeks_2019)- objective(params)}
        constraint_2020 = {'type': 'eq', 'fun': lambda params: float(row.indeks_2020)- objective(params)}
        # Melakukan minimasi
        result_2018 = minimize(objective, initial_guess, bounds=bounds, constraints=constraint_2018)
        result_2019 = minimize(objective, initial_guess, bounds=bounds, constraints=constraint_2019)
        result_2020 = minimize(objective, initial_guess, bounds=bounds, constraints=constraint_2020)
        indikator_2018=[]
        indikator_2019=[]
        indikator_2020=[]
        # Menampilkan hasil
        for i in range(47):
            indikator_2018.append(result_2018.x[i])
            indikator_2019.append(result_2019.x[i])
            indikator_2020.append(result_2020.x[i])
        model.create_bulk(row.id,'2018',indikator_2018)
        model.create_bulk(row.id,'2019',indikator_2019)
        model.create_bulk(row.id,'2020',indikator_2020)
        # print(index,row.id,row.indeks_2018,row.indeks_2019,row.indeks_2020)
# Target nilai x yang ingin dicapai
# x_target = 2.70

# # Fungsi objektif untuk minimasi


# # Batasan nilai a, b, c, d antara 0 dan 4
# bounds = [(1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5),
# (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5),
# (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5),
# (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5),
# (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5), (1, 5)]

# # Kondisi batasan linear
# constraint = {'type': 'eq', 'fun': lambda params: x_target - objective(params)}

# # Nilai awal (initial guess)
# initial_guess = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

# # Melakukan minimasi
# result = minimize(objective, initial_guess, bounds=bounds, constraints=constraint)
# indikator=[]
# # Menampilkan hasil
# for i in range(47):
#     indikator.append(round(result.x[i]))
#     print(i+1,indikator[i])
# print(objective(indikator))
# Menghitung nilai x berdasarkan nilai a, b, c, d terbaru
# x_calculated = (result.x[0] * ba + result.x[1] * bb + result.x[2] * bc + result.x[3] * bd) / (ba + bb + bc + bd)

# # Menampilkan hasil perbandingan dengan pola data sebelumnya
# print("\nPerbandingan dengan pola data sebelumnya:")
# print("Nilai x yang dihitung:", x_calculated)
# print("Nilai x yang diketahui:", x_target)
# print("Selisih antara nilai x dihitung dan x diketahui:", abs(x_calculated - x_target))
