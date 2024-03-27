import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
from app.models.isi import isiModel
from app.models.indikator import indikatorModel
from app.models.domain import domainModel
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
def domain1(params):
    i1,i2,i3,i4,i5,i6,i7,i8,i9,i10=params
    return (i1+i2+i3+i4+i5+i6+i7+i8+i9+i10)*(1.3/13)
def domain2(params):
    i11,i12,i13,i14,i15,i16,i17,i18,i19,i20=params
    aspek2=(i11+i12+i13+i14)*(2.5/10)  
    aspek3=(i15+i16+i17+i18)*(2.5/10)
    aspek4=(i19+i20)*(2.5/5)
    return (aspek2*(10/25))+(aspek3*(10/25))+(aspek4*(5/25))
def domain3(params):
    i21,i22,i23,i24,i25,i26,i27,i28,i29,i30,i31=params
    aspek5=(i21+i22+i23+i24+i25+i26+i27+i28)*(1.5/12)
    aspek6=(i29+i30+i31)*(1.5/4.5)
    return (aspek5*(12/16.5))+(aspek6*(4.5/16.5));
def domain4(params):
    i32,i33,i34,i35,i36,i37,i38,i39,i40,i41,i42,i43,i44,i45,i46,i47=params
    aspek7=(i32+i33+i34+i35+i36+i37+i38+i39+i40+i41)*(2.75/27.5)
    aspek8=(i42+i43+i44+i45+i46+i47)*(3/18)
    return (aspek7*(27.5/45.5))+(aspek8*(18/45.5));

def regresi(indikator1,indikator2,domain1,domain2):
        res=0
        if(domain1>domain2):
            if(indikator1>indikator2):
                if(indikator1<5):
                    res=indikator1+1
                else:
                    res=5
            elif(indikator1==indikator2):
                if(indikator1<5):
                    res =indikator1+1
                else:
                    res=5   
            else:
                if(indikator1>1):
                    res =indikator1-1
                else:
                    res=indikator1
        elif(domain1==domain2):
            res=indikator1
        else:
            if(indikator1<indikator2):
                if(indikator1>1):
                    res=indikator1-1
                else:
                    res=(indikator1)
            elif(indikator1==indikator2):
                if(indikator1>1):
                    res=(indikator1-1)
                else:
                    res=(indikator1)   
            else:
                if(indikator1<5):
                    res=(indikator1+1)
                else:
                    res=(5)
        return res
def cari_indikator(domain_2023,domain_2022,indikator_2021,indikator_2022):
    data=[]
    # print(domain_2023,domain_2022)
    indikator_find = []
    for i in range(10):
        indikator2 = float(data_indikator_2022[i])
        indikator1 = float(data_indikator_2021[i])
        indikator_find.append(regresi(indikator1=indikator1,indikator2=indikator2,domain1=domain_2023[0],domain2=domain_2022[0]))    
    cnt=0
    domain_target=domain_2023[0]
    jarak=10
    # indikator kurang
    if(domain_target>round(domain1(indikator_find),2)):
        while(domain_target>round(domain1(indikator_find),2)and cnt<jarak):
            # cnt+=1
            if(indikator_find[cnt]<5):
                indikator_find[cnt]+=1
                if(domain_target<round(domain1(indikator_find),2)):
                    indikator_find[cnt]-=1
            cnt+=1
            if(domain_target>round(domain1(indikator_find),2) and cnt>=jarak): cnt=0
    else:
        # indikator lebih
        while(domain_target<round(domain1(indikator_find),2)and cnt<jarak):
            # cnt+=1
            if(indikator_find[cnt]>1):
                indikator_find[cnt]-=1
                if(domain_target>round(domain1(indikator_find),2)):
                    indikator_find[cnt]+=1
            cnt+=1
            if(domain_target<round(domain1(indikator_find),2) and cnt>=jarak): cnt=0
    for i in indikator_find:
        data.append(i)
    print("Domain 1",domain_2023[0],domain1(indikator_find))
    indikator_find=[]

    for i in range(10,20):
        # print(i)
        indikator2 = float(data_indikator_2022[i])
        indikator1 = float(data_indikator_2021[i])
        indikator_find.append(regresi(indikator1=indikator1,indikator2=indikator2,domain1=domain_2023[1],domain2=domain_2022[1]))  
    # print(indikator_find)  
    cnt=0
    domain_target=domain_2023[1]
    jarak=10
    # indikator kurang
    if(domain_target>round(domain2(indikator_find),2)):
        while(domain_target>round(domain2(indikator_find),2)and cnt<jarak):
            # cnt+=1
            if(indikator_find[cnt]<5):
                indikator_find[cnt]+=1
                if(domain_target<round(domain2(indikator_find),2)):
                    indikator_find[cnt]-=1
            cnt+=1
            if(domain_target>round(domain2(indikator_find),2) and cnt>=jarak): cnt=0
    else:
        # indikator lebih
        while(domain_target<round(domain2(indikator_find),2)and cnt<jarak):
            # cnt+=1
            if(indikator_find[cnt]>1):
                indikator_find[cnt]-=1
                if(domain_target>round(domain2(indikator_find),2)):
                    indikator_find[cnt]+=1
            cnt+=1
            if(domain_target<round(domain2(indikator_find),2) and cnt>=jarak): cnt=0
    for i in indikator_find:
        data.append(i)
    print("Domain 2",domain_2023[1],domain2(indikator_find))
    indikator_find=[]
    for i in range(20,31):
        # print(i)
        indikator2 = float(data_indikator_2022[i])
        indikator1 = float(data_indikator_2021[i])
        indikator_find.append(regresi(indikator1=indikator1,indikator2=indikator2,domain1=domain_2023[2],domain2=domain_2022[2]))  
    # print(indikator_find)  
    cnt=0
    domain_target=domain_2023[2]
    jarak=11
    # indikator kurang
    if(domain_target>round(domain3(indikator_find),2)):
        while(domain_target>round(domain3(indikator_find),2)and cnt<jarak):
            # cnt+=1
            if(indikator_find[cnt]<5):
                indikator_find[cnt]+=1
                if(domain_target<round(domain3(indikator_find),2)):
                    indikator_find[cnt]-=1
            cnt+=1
            if(domain_target>round(domain3(indikator_find),2) and cnt>=jarak): cnt=0
    else:
        # indikator lebih
        while(domain_target<round(domain3(indikator_find),2)and cnt<jarak):
            # cnt+=1
            if(indikator_find[cnt]>1):
                indikator_find[cnt]-=1
                if(domain_target>round(domain3(indikator_find),2)):
                    indikator_find[cnt]+=1
            cnt+=1
            if(domain_target<round(domain3(indikator_find),2) and cnt>=jarak): cnt=0
    for i in indikator_find:
        data.append(i)
    print("Domain 3",domain_2023[2],domain3(indikator_find))

    indikator_find=[]
    for i in range(31,47):
        # print(i)
        indikator2 = float(data_indikator_2022[i])
        indikator1 = float(data_indikator_2021[i])
        indikator_find.append(regresi(indikator1=indikator1,indikator2=indikator2,domain1=domain_2023[3],domain2=domain_2022[3]))  
    # print(indikator_find)  
    cnt=0
    domain_target=domain_2023[3]
    jarak=16
    # indikator kurang
    if(domain_target>round(domain4(indikator_find),2)):
        while(domain_target>round(domain4(indikator_find),2)and cnt<jarak):
            # cnt+=1
            if(indikator_find[cnt]<5):
                indikator_find[cnt]+=1
                if(domain_target<round(domain4(indikator_find),2)):
                    indikator_find[cnt]-=1
            cnt+=1
            # if(domain_target>round(domain4(indikator_find),2) and cnt>=jarak): cnt=0
    else:
        # indikator lebih
        while(domain_target<round(domain4(indikator_find),2)and cnt<jarak):
            # cnt+=1
            if(indikator_find[cnt]>1):
                indikator_find[cnt]-=1
                if(domain_target>round(domain4(indikator_find),2)):
                    indikator_find[cnt]+=1
            cnt+=1
            # if(domain_target<round(domain4(indikator_find),2) and cnt>=jarak): cnt=0
    for i in indikator_find:
        data.append(i)

    print("Domain 4",domain_2023[3],domain4(indikator_find))
    # print(data)
    
    return data
    # if(domain_2023>domain_2022):
    #     indikator_2021>indikator_2022
model=isiModel()
indikator_model=indikatorModel()
indikators=indikator_model.getAll()
domain_model=domainModel()
domains=domain_model.getAll()

df = pd.read_csv('Data CSV/Data_lengkap Tahun 2023.csv')

data_insert=[]
for index, row in df.iterrows():
    if(row.id!='NaN'):
        index_2021=model.getIndexbyYearInstansi(instansi=row.id,year=2021)
        index_2022=model.getIndexbyYearInstansi(instansi=row.id,year=2022)
        data_indikator_2021=[float(x['val']) for x in model.getAllValueByYearInstansi(instansi=row.id,year=2021)]
        data_indikator_2022=[float(x['val']) for x in model.getAllValueByYearInstansi(instansi=row.id,year=2022)]
        domain_2021=[]
        domain_2022=[]
        domain_2023=[]
        for i,domain in enumerate(domains):
            domain_2023.append(float(row['domain'+str(i+1)]))
            domain_2021.append(model.getDomainByYearInstansi(domain=domain['id'],year=2021,instansi=row.id))
            domain_2022.append(model.getDomainByYearInstansi(domain=domain['id'],year=2021,instansi=row.id))
        if(index_2021==0):
            index_2021=index_2022
            data_indikator_2021=data_indikator_2022
            domain_2021=domain_2022
        if(index_2022==0):
            index_2022=index_2021
            data_indikator_2022=data_indikator_2021
            domain_2022=domain_2021
        # print(domain_2023,domain_2022,domain_2021)
        index_2023=0
        if(float(row.index_2023)>0):index_2023=row.index_2023
        if(index_2021>0 and index_2022>0):
            data_2023=cari_indikator(domain_2023=domain_2023,domain_2022=domain_2022,indikator_2021=data_indikator_2021, indikator_2022=data_indikator_2022)
        print(objective(data_2023),row.index_2023)
for i,indikator in enumerate(indikators):
    data_insert.append((row.id,indikator['id'],2018,data_2023[i]))
model.create_bulk(row.id,'2023',data_2023)