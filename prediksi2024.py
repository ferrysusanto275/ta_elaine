import numpy as np
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

import pandas as pd
from app.models.isi import isiModel
from app.models.indikator import indikatorModel

isi_model=isiModel()
indikator_model=indikatorModel()
indikators=indikator_model.getAll()

df=isi_model.getDfAllIndikatorClear();
df=df[df['id']=='i2023110600081']
df=df[['year','i15','indeks']]
print(df)
# Menggunakan regresi linier
# Model untuk Prediksi i15
model_i15 = LinearRegression()
X_i15 = df[['year']]
y_i15 = df['i15']
model_i15.fit(X_i15, y_i15)

# Prediksi nilai i15 untuk tahun 2024
i15_prediksi = int(round(model_i15.predict([[2024]])[0]))

# Model untuk Prediksi Indeks
model_indeks = LinearRegression()
X_indeks = df[['year', 'i15']]
y_indeks = df['indeks']
model_indeks.fit(X_indeks, y_indeks)

# Prediksi indeks untuk tahun 2024
indeks_prediksi = model_indeks.predict([[2024, i15_prediksi]])

# Nilai aktual untuk tahun 2023
nilai_aktual_indeks = df.loc[df['year'] == 2023, 'indeks'].values[0]

# Menghitung MAE untuk indeks
mae_indeks = mean_absolute_error([nilai_aktual_indeks], indeks_prediksi)

print("Prediksi i15 untuk tahun 2024:", i15_prediksi)
print("Prediksi indeks untuk tahun 2024:", indeks_prediksi[0])
print("MAE untuk prediksi indeks:", mae_indeks)
# data2022=isi_model.getById('i2023110600081','in2023110400015',2022)['value']
# data2023=isi_model.getById('i2023110600081','in2023110400015',2023)['value']
# data2024=data2023
# if(data2022<data2023) & (data2024<5):
#     data2024+=1

# elif (data2022>data2023) & (data2024>1):
#     data2024-=1
# print(data2024)
# data = {
#     'tahun': [2018, 2019, 2020, 2021, 2022, 2023],
#     'value': [isi_model.getById('i2023110600081','in2023110400015',2018)['value'],
#          isi_model.getById('i2023110600081','in2023110400015',2019)['value'],
#          isi_model.getById('i2023110600081','in2023110400015',2020)['value'],
#          isi_model.getById('i2023110600081','in2023110400015',2021)['value'],
#          isi_model.getById('i2023110600081','in2023110400015',2022)['value'],
#          isi_model.getById('i2023110600081','in2023110400015',2023)['value']]
# }
# df=pd.DataFrame(data)

# y=df['value']
# X=df['tahun']
# X_train, X_test, y_train, y_test = train_test_split(X.values.reshape(-1, 1), y, test_size=0.2, random_state=42)

# model = LinearRegression()
# model.fit(X_train, y_train)
# prediksi_2024 = model.predict([[2024]])
# rounded_prediction = int(round(float(prediksi_2024)))

#     # Pastikan prediksi tetap dalam rentang 1-5
# predicted_value = min(max(rounded_prediction, 1), 5)
#     # return predicted_value
# # print(prediksi_2024)
# # print(predicted_value)
# df=df._append({"tahun":2024,"value":predicted_value}, ignore_index=True)
# print(df)
# # # X.append(predicted_value)
# # # y.append(2024)
# # # Buat grafik garis
# plt.plot(df['tahun'], df['value'], label='Data')
# # # plt.plot(X, model.predict(X.values.reshape(-1, 1)), label='Linear Regression')
# # # plt.plot(X.max(), prediksi_2024, marker='o', color='red', label='Prediksi Tahun 2024')

# plt.xlabel('Tahun')
# plt.ylabel('Value')
# plt.title('Grafik Garis Linear Regresi')
# plt.legend()
# plt.show()