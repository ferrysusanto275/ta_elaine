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
    df=isi_model.getDfAllIndikatorClear()
    df=df[df['id']==instansi]
    data_indikator=indikator_model.getById(indikator)
    df=df[['year',data_indikator['name'].lower()]]
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

def getDfLinear2024(instansi, indikator):
    data = {
    'tahun': [2018, 2019, 2020, 2021, 2022, 2023],
    'value': [isi_model.getById(instansi,indikator,2018)['value'],
         isi_model.getById(instansi,indikator,2019)['value'],
         isi_model.getById(instansi,indikator,2020)['value'],
         isi_model.getById(instansi,indikator,2021)['value'],
         isi_model.getById(instansi,indikator,2022)['value'],
         isi_model.getById(instansi,indikator,2023)['value']]
        }
    df=pd.DataFrame(data)
    prediksi_2024=data['value'][5]
    if(data['value'][4]<data['value'][5]) & (prediksi_2024<5):
        prediksi_2024+=1

    elif (data['value'][4]>data['value'][5]) & (prediksi_2024>1):
        prediksi_2024-=1
    
    rounded_prediction = int(round(float(prediksi_2024)))

        # Pastikan prediksi tetap dalam rentang 1-5
    predicted_value = min(max(rounded_prediction, 1), 5)
        # return predicted_value
    # print(prediksi_2024)
    # print(predicted_value)
    df=df._append({"tahun":2024,"value":predicted_value}, ignore_index=True)
    return df
@prediksi_bp.route('/api/'+ an+'/df_linear_reg24/<string:instansi>/<string:indikator>')
def prediksiLinear24(instansi, indikator):
    
    return getDfLinear2024(instansi,indikator).to_html(classes="tabel")
@prediksi_bp.route('/api/'+ an+'/png_linear_reg24/<string:instansi>/<string:indikator>')
def pngprediksiLinear24(instansi, indikator):
    df=getDfLinear2024(instansi,indikator)
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