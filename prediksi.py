import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import pandas as pd
from app.models.isi import isiModel
from app.models.indikator import indikatorModel

isi_model=isiModel()
indikator_model=indikatorModel()
indikators=indikator_model.getAll()

data = {
    'tahun': [2018, 2019, 2020, 2021, 2022, 2023],
    'value': [isi_model.getById('i2023110600344','in2023110400015',2018)['value'],
         isi_model.getById('i2023110600344','in2023110400015',2019)['value'],
         isi_model.getById('i2023110600344','in2023110400015',2020)['value'],
         isi_model.getById('i2023110600344','in2023110400015',2021)['value'],
         isi_model.getById('i2023110600344','in2023110400015',2022)['value'],
         isi_model.getById('i2023110600344','in2023110400015',2023)['value']]
}
df=pd.DataFrame(data)

y=df['value']
X=df['tahun']
X_train, X_test, y_train, y_test = train_test_split(X.values.reshape(-1, 1), y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
prediksi_2024 = model.predict([[2024]])
rounded_prediction = int(round(float(prediksi_2024)))

    # Pastikan prediksi tetap dalam rentang 1-5
predicted_value = min(max(rounded_prediction, 1), 5)
    # return predicted_value
print(df)
print(prediksi_2024)
print(predicted_value)