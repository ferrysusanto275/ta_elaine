import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
from app.models.isi import isiModel
from app.models.indikator import indikatorModel

model=isiModel()
# indikator_model=indikatorModel();
df = pd.read_csv('Data CSV/Data_lengkap.csv')
# df=pd.DataFrame({'id':['i2023110600313'],'indeks_2018':[2.09],'indeks_2019':[1.89],'indeks_2020':[2.57]})
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
def cari_i(index_find,index1,indikators_1,indikators_2):
    data=[]
    pilihan_data=[];
    for i in range(47):
        indikator1=float(indikators_1[i])
        indikator2=float(indikators_2[i])
        indikator_find=[];
        if(index_find>index1):
            if(indikator1>indikator2):
                if(indikator1<5):
                    indikator_find.append(indikator1+1)
                else: indikator_find.append(5)
            elif(indikator1==indikator2):
                indikator_find.append(indikator1)
                if(indikator1<5):
                    indikator_find.append(indikator1+1)
            else:
                if(indikator1>1):
                    indikator_find.append(indikator1-1);
                indikator_find.append(indikator1)
        elif(index_find==index1):
            indikator_find.append(indikator1)
        else:
            if(indikator1<indikator2):
                # indikator naik
                if(indikator1>1):
                    indikator_find.append(indikator1-1);
                else: indikator_find.append(1);
            elif(indikator1==indikator2):
                if(indikator1>1):
                    indikator_find.append(indikator1-1);
                indikator_find.append(indikator1);
            elif(indikator1>indikator2):
                indikator_find.append(indikator1)
                if(indikator1<5):
                    indikator_find.append(indikator1+1);
        data.append(indikator_find[0])
        pilihan_data.append(indikator_find)
    cnt=0
    while(index_find>round(objective(data),2) and cnt<47):
        if(len(pilihan_data[cnt])>1):
            data[cnt]=pilihan_data[cnt][1]
            
            if(index_find<round(objective(data),2)):data[cnt]=pilihan_data[cnt][0]
        cnt+=1
    
    # adjust klo masih kurang
    if(index_find>round(objective(data),2)):
        cnt=0
        while(index_find>round(objective(data),2) and cnt<47):
            if(data[cnt]<5):
                tmp=data[cnt]
                data[cnt]=tmp+1
                if(index_find<round(objective(data),2)):data[cnt]=tmp
            cnt+=1
    else:
        # klo lebih
        while(index_find<round(objective(data),2) and cnt<47):
            if(data[cnt]>1):
                tmp=data[cnt]
                data[cnt]=tmp-1
                if(index_find>round(objective(data),2)):data[cnt]=tmp
            cnt+=1
    return data
for index, row in df.iterrows():
    if(row.id!='NaN'):
#         # esktrapolasi index (regresi)
#         # search index 2021
        data_full={}
        index_2021=model.getIndexbyYearInstansi(instansi=row.id,year=2021);
#         # search index 2022
        index_2022=model.getIndexbyYearInstansi(instansi=row.id,year=2022);
        data_indikator_2021=[float(x['val']) for x in model.getAllValueByYearInstansi(instansi=row.id,year=2021)];
        
        data_indikator_2022=[float(x['val']) for x in model.getAllValueByYearInstansi(instansi=row.id,year=2022)];
        if(index_2021==0):
            index_2021=index_2022
            data_indikator_2021=data_indikator_2022
        if(index_2022==0):
            index_2022=index_2021
            data_indikator_2022=data_indikator_2021
        data_full['2021']=data_indikator_2021
        data_full['2022']=data_indikator_2022
        index_2018=0
        if(float(row.indeks_2018)>0):index_2018=row.indeks_2018
        index_2019=index_2018
        if(float(row.indeks_2019)>0):index_2019=row.indeks_2019
        index_2020=index_2019
        if(float(row.indeks_2020)>0):index_2020=row.indeks_2020
        # print("indeks_real :",index_2018,index_2019,index_2020,index_2021,index_2022)
        if(index_2021>0 and index_2022>0):
            data_2020=cari_i(index_find=index_2020,index1=index_2021,indikators_1=data_indikator_2021,indikators_2=data_indikator_2022)
            indeks_2020=round(objective(data_2020),2)
            data_2019=cari_i(index_find=index_2019,index1=indeks_2020,indikators_1=data_2020,indikators_2=data_indikator_2021)
            indeks_2019=round(objective(data_2019),2)
            data_2018=cari_i(index_find=index_2018,index1=indeks_2019,indikators_1=data_2019,indikators_2=data_2020)
            indeks_2018=round(objective(data_2018),2)
            # print("indeks_obj :",indeks_2018,indeks_2019,indeks_2020,index_2021,index_2022)
            data_full['2020']=data_2020
            data_full['2019']=data_2019
            data_full['2018']=data_2018
            data_full['2018'].append(index_2018)
            data_full['2018'].append(indeks_2018)
            data_full['2019'].append(index_2019)
            data_full['2019'].append(indeks_2019)
            data_full['2020'].append(index_2020)
            data_full['2020'].append(indeks_2020)
            data_full['2021'].append(index_2021)
            data_full['2021'].append(index_2021)
            data_full['2022'].append(index_2022)
            data_full['2022'].append(index_2022)
            print(pd.DataFrame(data_full))           
