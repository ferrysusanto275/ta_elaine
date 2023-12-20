import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
from app.models.isi import isiModel
from app.models.indikator import indikatorModel

model=isiModel()
# indikator_model=indikatorModel();
df = pd.read_csv('Data CSV/Data_lengkap_part_01.csv')
# list_indikator=indikator_model.getAll()
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
for index, row in df.iterrows():
    if(row.id!='NaN'):
        data_full = {"2018": [], "2019": [], "2020": [], "2021": [], "2022": []}
        # esktrapolasi index (regresi)
        # search index 2021
        index_2021=model.getIndexbyYearInstansi(instansi=row.id,year=2021);
        # search index 2022
        index_2022=model.getIndexbyYearInstansi(instansi=row.id,year=2022);
        # jika data 2021 dan 2022 di temukan
        if(index_2021>0 and index_2022 >0):
            X_train = np.array([index_2021,index_2022]).reshape(-1, 1)
        elif(index_2021>0):
            X_train = np.array([index_2021,index_2021]).reshape(-1, 1)
        elif(index_2022>0):
            X_train = np.array([index_2022,index_2022]).reshape(-1, 1)
        else: X_train=None
        if(X_train is not None):
            data_indikator_2021=pd.DataFrame(model.getAllValueByYearInstansi(instansi=row.id,year=2021));
            data_indikator_2022=pd.DataFrame(model.getAllValueByYearInstansi(instansi=row.id,year=2022));
            for index_in, row_in in data_indikator_2021.iterrows():
                indikator_2021=row_in.val
                row_2022=data_indikator_2022.loc[index_in];
                indikator_2022=row_2022.val
                if(indikator_2021==0):indikator_2021=indikator_2022
                if(indikator_2022==0):indikator_2022=indikator_2021
                data_full['2021'].append(indikator_2021)
                data_full['2022'].append(indikator_2022)
                y_train = np.array([indikator_2021,indikator_2022])
                        # Melatih model regresi linier
                model_regresi = LinearRegression()
                model_regresi.fit(X_train, y_train)
                # # Membuat prediksi untuk data di luar rentang pelatihan
                X_extrapolate = np.array([row.indeks_2018,row.indeks_2019,row.indeks_2020]).reshape(-1, 1)
                y_pred_extrapolate = model_regresi.predict(X_extrapolate)
                # Modifikasi hasil prediksi menjadi bilangan bulat dalam rentang 0-5
                y_pred_extrapolate_int = np.clip(np.round(y_pred_extrapolate), 0, 5)
                data_full['2018'].append(y_pred_extrapolate_int[0])
                data_full['2019'].append(y_pred_extrapolate_int[1])
                data_full['2020'].append(y_pred_extrapolate_int[2])
            print(len(data_full["2018"]))
                # regresi menurut indikator
            for i in range(len(data_full["2018"])):
                # indikator ke i sebagai penentu
                for j in range(len(data_full["2018"])):
                    
                        if(j==0):
                            # inisialisasi
                            data_full['2018_'+str(i)]=[]
                            data_full['2019_'+str(i)]=[]
                            data_full['2020_'+str(i)]=[]
                        X_train=np.array([data_full["2021"][i],data_full["2022"][i]]).reshape(-1,1)
                        y_train=np.array([data_full["2021"][j],data_full["2022"][j]])
                        model_regresi = LinearRegression()
                        model_regresi.fit(X_train, y_train)
                        X_extrapolate = np.array([data_full["2018"][i],data_full["2019"][i],data_full["2020"][i]]).reshape(-1,1)
                        y_pred_extrapolate = model_regresi.predict(X_extrapolate)
                        data_full['2018_'+str(i)].append(y_pred_extrapolate_int[0])
                        data_full['2019_'+str(i)].append(y_pred_extrapolate_int[1])
                        data_full['2020_'+str(i)].append(y_pred_extrapolate_int[2])
            
                # temp_2021= data_full["2021"][:i] + data_full["2021"][i + 1:]
                # temp_2022= data_full["2022"][:i] + data_full["2022"][i + 1:]
                # temp_2018= data_full["2018"][:i] + data_full["2018"][i + 1:]
                # temp_2019= data_full["2019"][:i] + data_full["2019"][i + 1:]
                # temp_2020= data_full["2020"][:i] + data_full["2020"][i + 1:]
                # X_train=np.array([temp_2021,temp_2022])
                # y_train=np.array([data_full["2021"][i],data_full["2022"][i]])
                # model_regresi = LinearRegression()
                # model_regresi.fit(X_train, y_train)
                # X_extrapolate = np.array([temp_2018,temp_2019,temp_2020])
                # y_pred_extrapolate = model_regresi.predict(X_extrapolate)
                # # inisialisasi
                # if(i==0):
                #     data_full['2018_']=[]
                #     data_full['2019_']=[]
                #     data_full['2020_']=[]
                # print(data_full)    
                # data_full['2018_'].append(y_pred_extrapolate_int[0])
                # data_full['2019_'].append(y_pred_extrapolate_int[1])
                # data_full['2020_'].append(y_pred_extrapolate_int[2])
                # initial_guess_2018.append(y_pred_extrapolate_int[0])
                # initial_guess_2019.append(y_pred_extrapolate_int[1])
                # initial_guess_2020.append(y_pred_extrapolate_int[2])
            print(pd.DataFrame(data_full))
            if(float(row.indeks_2018)>0):
                print("masuk 2018")        
                model.create_bulk(row.id,'2018',data_full["2018"])
            if(float(row.indeks_2019)>0):
                print("masuk 2019")   
                model.create_bulk(row.id,'2019',data_full["2019"])
            if(float(row.indeks_2020)>0):
                print("masuk 2020")   
                model.create_bulk(row.id,'2020',data_full["2020"])
            # initial_guess_2018_tahap2=[]
            # initial_guess_2019_tahap2=[]
            # initial_guess_2020_tahap2=[]
            # dianggap dr prediksi sebelumnya indikator 1 benar
            # for index_in, row_in in data_indikator_2021.iterrows():

            # print(row.indeks_2019,round(objective(initial_guess_2018),2))


        #     for indikator in list_indikator:
        #         indikator_2021=0
        #         indikator_2022=0
        #         if(index_2021>0):
        #             indikator_2021=model.getById(instansi=row.id,indikator=indikator['id'],year=2021)['value']
        #         if(index_2022>0):
        #             indikator_2022=model.getById(instansi=row.id,indikator=indikator['id'],year=2021)['value']
        #         if(indikator_2021==0):indikator_2021=indikator_2022
        #         if(indikator_2022==0):indikator_2022=indikator_2021
        #         data_indikator_2021.append(indikator_2021)
        #         data_indikator_2022.append(indikator_2022)
        #         y_train = np.array([indikator_2021,indikator_2022])
        #         # Melatih model regresi linier
        #         model_regresi = LinearRegression()
        #         model_regresi.fit(X_train, y_train)
        #         # # Membuat prediksi untuk data di luar rentang pelatihan
        #         X_extrapolate = np.array([row.indeks_2018,row.indeks_2019,row.indeks_2020]).reshape(-1, 1)
        #         y_pred_extrapolate = model_regresi.predict(X_extrapolate)
        #         # Modifikasi hasil prediksi menjadi bilangan bulat dalam rentang 0-5
        #         y_pred_extrapolate_int = np.clip(np.round(y_pred_extrapolate), 0, 5)
        #         initial_guess.append(y_pred_extrapolate_int)

        # print(y_pred_extrapolate_int)
         
# Membuat data untuk pelatihan
# X_train = np.array([1.98,2.92]).reshape(-1, 1)
# y_train = np.array([1,3])

# # Melatih model regresi linier
# model = LinearRegression()
# model.fit(X_train, y_train)

# # Membuat prediksi untuk data di luar rentang pelatihan
# X_extrapolate = np.array([2.09,1.89,2.57]).reshape(-1, 1)
# y_pred_extrapolate = model.predict(X_extrapolate)

# # Modifikasi hasil prediksi menjadi bilangan bulat dalam rentang 0-5
# y_pred_extrapolate_int = np.clip(np.round(y_pred_extrapolate), 0, 5)

# # Menampilkan hasil prediksi
# for x, y_pred in zip(X_extrapolate, y_pred_extrapolate_int):
#     print(f'Input: {x[0]}, Prediksi (bulat): {int(y_pred)}')

# Plot hasil
# plt.scatter(X_train, y_train, label='Data Pelatihan')
# plt.plot(X_train, model.predict(X_train), color='blue', label='Model Regresi Linier')
# plt.scatter(X_extrapolate, y_pred_extrapolate_int, color='red', label='Prediksi Ekstrapolasi (bulat)')
# plt.xlabel('Variabel Independen (X)')
# plt.ylabel('Variabel Dependen (Y)')
# plt.legend()
#  plt.show()
