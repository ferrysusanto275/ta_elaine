import numpy as np
import pandas as pd
import decimal
from app.models.isi import isiModel
def hitungIndex(domain1,domain2,domain3,domain4):
    return round((domain1*(13/100))+(domain2*(25/100))+(domain3*(16.5/100))+(domain4*(45.5/100)),2)
def hitungDomain1(aspek1):
    return aspek1*13/13
def hitungAspek1(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10):
    return (i1+i2+i3+i4+i5+i6+i7+i8+i9+i10)*(1.3/13)
isi=isiModel()
df_allValue=isi.getAllValue()
df = pd.read_csv('Data CSV/Data_lengkap_part_01.csv')
for index, row in df.iterrows():
    dfInstansi=df_allValue[df_allValue['id']==row.id]
    data_2021=dfInstansi[dfInstansi["year"]==2021]
    data_2022=dfInstansi[dfInstansi["year"]==2022]
    # cari domain 2020
    indeks_2020=row.indeks_2020
    if(data_2021['indeks'].values.size>0 and data_2022['indeks'].values.size>0):
        indeks_2021=data_2021['indeks'].values[0]
        domain1_2021=data_2021['domain1'].values[0]
        domain1_2022=data_2022['domain1'].values[0]
        domain2_2021=data_2021['domain2'].values[0]
        domain2_2022=data_2022['domain2'].values[0]
        domain3_2021=data_2021['domain3'].values[0]
        domain3_2022=data_2022['domain3'].values[0]
        domain4_2021=data_2021['domain4'].values[0]
        domain4_2022=data_2022['domain4'].values[0]
        # cari domain
        domain1_2020=float(round(domain1_2021,2))
        domain2_2020=float(round(domain2_2021,2))
        domain3_2020=float(round(domain3_2021,2))
        domain4_2020=float(round(domain4_2021,2))
        index_res_2020=hitungIndex(domain1_2020,domain2_2020,domain3_2020,domain4_2020)
        flagDomain1=True
        flagDomain2=True
        flagDomain3=True
        flagDomain4=True
        while(index_res_2020<indeks_2020-0.013):

            if(domain1_2020<indeks_2020 and flagDomain1):
                # print("masuk domain1")
                # bobot terkecil domain 1 = 
                domain1_2020=round(domain1_2020+0.1,2)
                flagDomain1=False
            elif(domain2_2020<indeks_2020 and flagDomain2):
                # print("masuk domain2")
                domain2_2020=round(domain2_2020+0.2,2)
                flagDomain2=False
            elif(domain3_2020<indeks_2020  and flagDomain3):
                # print("masuk domain3")
                domain3_2020=round(domain3_2020+0.27,2)
                flagDomain3=False
            elif(domain4_2020<indeks_2020 and flagDomain4):
                # print("masuk domain4")
                domain4_2020=round(domain4_2020+0.39,2)
                flagDomain4=False
            else:
                # print("reset")
                flagDomain1=True
                flagDomain2=True
                flagDomain3=True
                flagDomain4=True
            index_res_2020=hitungIndex(domain1_2020,domain2_2020,domain3_2020,domain4_2020)
        while(index_res_2020>indeks_2020+0.013):

            if(domain1_2020>1 and flagDomain1):
                # print("masuk domain1")
                # bobot terkecil domain 1 = 
                domain1_2020=round(domain1_2020-0.1,2)
                flagDomain1=False
            elif(domain2_2020>1 and flagDomain2):
                # print("masuk domain2")
                domain2_2020=round(domain2_2020-0.2,2)
                flagDomain2=False
            elif(domain3_2020>1  and flagDomain3):
                # print("masuk domain3")
                domain3_2020=round(domain3_2020-0.27,2)
                flagDomain3=False
            elif(domain4_2020+1 and flagDomain4):
                # print("masuk domain4")
                domain4_2020=round(domain4_2020-0.39,2)
                flagDomain4=False
            else:
                # print("reset")
                flagDomain1=True
                flagDomain2=True
                flagDomain3=True
                flagDomain4=True
            index_res_2020=hitungIndex(domain1_2020,domain2_2020,domain3_2020,domain4_2020)
        print(indeks_2020,domain1_2020,domain2_2020,domain3_2020,domain4_2020,index_res_2020)
        # break
        