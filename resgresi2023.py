import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
from app.models.isi import isiModel
from app.models.indikator import indikatorModel

isi_model=isiModel()
indikator_model=indikatorModel()
indikators=indikator_model.getAll()
# indikator_model=indikatorModel();
# df = pd.read_csv('Data CSV/Data_lengkap_part_13.csv')
# df=pd.DataFrame({'id':['i2023110600313'],'indeks_2018':[2.09],'indeks_2019':[1.89],'indeks_2020':[2.57]})
# list_indikator=indikator_model.getAll()
def domain(id,data_cari,data_domain,data_index):

    df=pd.DataFrame(isi_model.getDf23())
    df = df[df['Instansi']==id]
    data_drop=['Instansi','Year', 'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10',
    'I11', 'I12', 'I13', 'I14', 'I15', 'I16', 'I17', 'I18', 'I19', 'I20',
    'I21', 'I22', 'I23', 'I24', 'I25', 'I26', 'I27', 'I28', 'I29', 'I30',
    'I31', 'I32', 'I33', 'I34', 'I35', 'I36', 'I37', 'I38', 'I39', 'I40',
    'I41', 'I42', 'I43', 'I44', 'I45', 'I46', 'I47']
    if(data_cari<=10):
        data_drop.append('Domain 2')
        data_drop.append('Domain 3')
        data_drop.append('Domain 4')
    elif(data_cari<=20):
        data_drop.append('Domain 1')
        data_drop.append('Domain 3')
        data_drop.append('Domain 4')
    elif(data_cari<=31):
        data_drop.append('Domain 1')
        data_drop.append('Domain 2')
        data_drop.append('Domain 4')
    else:
        data_drop.append('Domain 1')
        data_drop.append('Domain 2')
        data_drop.append('Domain 3')
    # print(data_drop)
    y_train=df['I'+str(data_cari)].to_numpy()
    # X_train=df['Domain 1,Index'].to_numpy()
    X_train=df.drop(data_drop, axis = 1).to_numpy()
    
    model = LinearRegression()
    model.fit(X_train, y_train)

    # # Contoh data baru untuk diprediksi
    X_new = np.array([[data_domain, data_index]])    # Prediksi untuk tahun 2022 dengan index 4

    # # Lakukan prediksi
    prediction = model.predict(X_new)
    # Bulatkan prediksi ke integer terdekat
    rounded_prediction = int(round(prediction[0]))

    # Pastikan prediksi tetap dalam rentang 1-5
    predicted_value = min(max(rounded_prediction, 1), 5)
    return predicted_value
# print(round(prediction[0]))
def predict_indikator(instansi,domain1,domain2,domain3,domain4,index):
    data=[]
    for i in range(47):
        if(i<10):data.append(domain(instansi,(i+1),domain1,index))
        elif(i<20):data.append(domain(instansi,(i+1),domain2,index))
        elif(i<31):data.append(domain(instansi,(i+1),domain3,index))
        else:data.append(domain(instansi,(i+1),domain4,index))
    data.append(objective(data))
    return data 
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
    return (domain1*(13/100))+(domain2*(25/100))+(domain3*(16.5/100))+(domain4*(45.5/100))
print(predict_indikator('i2023110600004',4.1,3.4,2.27,4.13,3.64))
# print(predict_indikator('i2023110600005',2.0,3.9,1.18,4.02,3.26))