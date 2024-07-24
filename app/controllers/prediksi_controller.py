from flask import Blueprint,jsonify,request,render_template,Response
from app.models.isi import isiModel
from app.models.indikator import indikatorModel
import io
from io import BytesIO
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from app.models.indikator import indikatorModel
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
isi_model=isiModel()
indikator_model=indikatorModel()
an="prediksi"
prediksi_bp=Blueprint(an,__name__, template_folder='views')
def getDfLinear(instansi, indikator):
    df=isi_model.getAllIndeks_isi()
    df=df[df['id']==instansi]
    df=df[['year',indikator.lower()]]
    df.columns=['tahun','value']
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
    # print(prediksi_2024)
    # print(predicted_value)
    df=df._append({"tahun":2024,"value":predicted_value}, ignore_index=True)
    
    # Calculate the MSE and MAE
    mse = 1 - model.score(X_train, y_train)
    print("mse :",mse)
    # Add the MSE as a new column to the DataFrame
    # df['mse'] = mse
    return df
@prediksi_bp.route('/api/'+ an+'/df_linear_reg/<string:instansi>/<string:indikator>')
def prediksiLinear(instansi, indikator):
    df_dict=getDfLinear(instansi,indikator).to_dict(orient='records')
    return jsonify(df_dict)

@prediksi_bp.route('/api/'+ an+'/png_linear_reg/<string:instansi>/<string:indikator>')
def pngprediksiLinear(instansi, indikator):
    df=getDfLinear(instansi,indikator)
    fig, ax = plt.subplots()
    ax.plot(df['tahun'], df['value'], marker='o')
    ax.set_xlabel('Tahun')
    ax.set_ylabel('Value')
    ax.set_title("Grafik Garis Linear Regresi")
   # Menggunakan BytesIO untuk menangkap output plot sebagai byte stream
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    # Membuat respons HTTP dengan gambar sebagai byte stream
    return Response(output.getvalue(), mimetype='image/png')
