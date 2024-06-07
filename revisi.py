import numpy as np
import pandas as pd
import decimal
from app.models.isi import isiModel
def hitungIndex(domain1,domain2,domain3,domain4):
    return round((domain1*(13/100))+(domain2*(25/100))+(domain3*(16.5/100))+(domain4*(45.5/100)),2)
def hitungDomain1(aspek1):
    return round(aspek1*13/13,2)
def hitungDomain2(aspek2,aspek3,aspek4):
    return round(aspek2*10/25+aspek3*10/25+aspek4*5/25,2)
def hitungDomain3(aspek5,aspek6):
    return round((aspek5*(12/16.5))+(aspek6*(4.5/16.5)),2)
def hitungDomain4(aspek7,aspek8):
    return round((aspek7*(27.5/45.5))+(aspek8*(18/45.5)),2)

def hitungAspek1(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10):
    return round((i1+i2+i3+i4+i5+i6+i7+i8+i9+i10)*(1.3/13),2)

def hitungAspek2(i11,i12,i13,i14):
    return round((i11+i12+i13+i14)*(2.5/10),2)
def hitungAspek3(i15,i16,i17,i18):
    return round((i15+i16+i17+i18)*(2.5/10),2)
def hitungAspek4(i19,i20):
    return round((i19+i20)*(2.5/5),2)

def hitungAspek5(i21,i22,i23,i24,i25,i26,i27,i28):
    return round((i21+i22+i23+i24+i25+i26+i27+i28)*(1.5/12),2)
def hitungAspek6(i29,i30,i31):
    return round((i29+i30+i31)*(1.5/4.5),2)

def hitungAspek7(i32,i33,i34,i35,i36,i37,i38,i39,i40,i41):
    return round((i32+i33+i34+i35+i36+i37+i38+i39+i40+i41)*(2.75/27.5),2)
def hitungAspek8(i42,i43,i44,i45,i46,i47):
    return round((i42+i43+i44+i45+i46+i47)*(3/18),2)
# hitung bobot minimal ketika salah satu indikator berubah di setiap aspek atau doamain tertentu
minD1=hitungIndex(hitungDomain1(hitungAspek1(1,0,0,0,0,0,0,0,0,0)),0,0,0)
minAspek2=hitungIndex(0,hitungDomain2(hitungAspek2(1,0,0,0),0,0),0,0)
minAspek3=hitungIndex(0,hitungDomain2(0,hitungAspek3(1,0,0,0),0),0,0)
minAspek4=hitungIndex(0,hitungDomain2(0,0,hitungAspek4(1,0)),0,0)
minD2=min(minAspek2,minAspek3,minAspek4)


minAspek5=hitungIndex(0,0,hitungDomain3(hitungAspek5(1,0,0,0,0,0,0,0),0),0)
minAspek6=hitungIndex(0,0,hitungDomain3(0,hitungAspek6(1,0,0)),0)
minD3=min(minAspek5,minAspek6)

minAspek7=hitungIndex(0,0,0,hitungDomain4(hitungAspek7(1,0,0,0,0,0,0,0,0,0),0))
minAspek8=hitungIndex(0,0,0,hitungDomain4(0,hitungAspek8(1,0,0,0,0,0)))
minD4=min(minAspek7,minAspek8)
minIndeks=min(minD1,minD2,minD3,minD4)
print(minD1)
print(minD2,minAspek2,minAspek3,minAspek4)
print(minD3,minAspek5,minAspek6)
print(minD4,minAspek7,minAspek8)
print(minIndeks)
# ts tahun_selanjutnya
# ts2 2 tahun_selanjutnya
def cariDomain(indeks_target,data_ts,data_ts2):
    # inisisalisasi domain yang boleh diubah
    flagDomain1=True
    flagDomain2=True
    flagDomain3=True
    flagDomain4=True
    # inisialisasi domain find disamakan dengan domain ts
    domain_find={"domain1":float(data_ts.domain1),"domain2":float(data_ts.domain2),"domain3":float(data_ts.domain3),"domain4":float(data_ts.domain4)}
    index_res=hitungIndex(domain_find['domain1'],domain_find['domain2'],domain_find['domain3'],domain_find['domain4'])
    # ajust naik
    while(index_res<indeks_target):
        if(domain_find['domain1']<indeks_target and flagDomain1): 
            domain_find['domain1']=round(domain_find['domain1']+minD1,2)
            flagDomain1=False
        elif(domain_find['domain2']<indeks_target and flagDomain2):
            domain_find['domain2']=round(domain_find['domain2']+minD2,2)
            flagDomain2=False
        elif(domain_find['domain3']<indeks_target  and flagDomain3):
            domain_find['domain3']=round(domain_find['domain3']+minD3,2)
            flagDomain3=False
        elif(domain_find['domain4']<indeks_target and flagDomain4):
            domain_find['domain4']=round(domain_find['domain4']+minD4,2)
            flagDomain4=False
        else:
            flagDomain1=True
            flagDomain2=True
            flagDomain3=True
            flagDomain4=True
        # print(domain_find,index_res,indeks_target)
        index_res=hitungIndex(domain_find['domain1'],domain_find['domain2'],domain_find['domain3'],domain_find['domain4'])
    while(index_res>indeks_target):
        if(domain_find['domain1']>1 and flagDomain1): 
            domain_find['domain1']=round(domain_find['domain1']-minD1,2)
            flagDomain1=False
        elif(domain_find['domain2']>1 and flagDomain2):
            domain_find['domain2']=round(domain_find['domain2']-minD2,2)
            flagDomain2=False
        elif(domain_find['domain3']>1  and flagDomain3):
            domain_find['domain3']=round(domain_find['domain3']-minD3,2)
            flagDomain3=False
        elif(domain_find['domain4']>1 and flagDomain4):
            domain_find['domain4']=round(domain_find['domain4']-minD4,2)
            flagDomain4=False
        else:
            flagDomain1=True
            flagDomain2=True
            flagDomain3=True
            flagDomain4=True
        # print(domain_find,index_res,indeks_target)
        index_res=hitungIndex(domain_find['domain1'],domain_find['domain2'],domain_find['domain3'],domain_find['domain4'])
        # ajust turun
    
    # membatasi perubahan max value dengan indeks yang dicari

    return domain_find
def cariAspek(data_find,data_ts):
    aspek_find=data_find
    aspek_find['aspek1']=data_find['domain1']
    # perhitungan domain 2
    # inisialisasi dengan data dari tahun selanjutnya
    aspek_find['aspek2']=float(data_ts.aspek2)
    aspek_find['aspek3']=float(data_ts.aspek3)
    aspek_find['aspek4']=float(data_ts.aspek4)
    domain2_res=hitungDomain2(aspek_find['aspek2'],aspek_find['aspek3'],aspek_find['aspek4'])
    aspek2_flag=True
    aspek3_flag=True
    aspek4_flag=True
    while(domain2_res<data_find['domain2']):
        if(aspek_find['aspek2']<data_find['domain2'] and aspek2_flag):
           
            aspek_find['aspek2']=round(aspek_find['aspek2']+minAspek2,2)
            aspek2_flag=False
        elif(aspek_find['aspek3']<data_find['domain2'] and aspek3_flag):
            aspek_find['aspek3']=round(aspek_find['aspek3']+minAspek3,2)
            aspek3_flag=False
        elif(aspek_find['aspek4']<data_find['domain2']  and aspek4_flag):
            aspek_find['aspek4']=round(aspek_find['aspek4']+minAspek4,2)
            aspek4_flag=False
        else:
            aspek4_flag=True
            aspek2_flag=True
            aspek3_flag=True
        domain2_res=hitungDomain2(aspek_find['aspek2'],aspek_find['aspek3'],aspek_find['aspek4'])
    while(domain2_res>data_find['domain2']):
        if(aspek_find['aspek2']>1 and aspek2_flag):
           
            aspek_find['aspek2']=round(aspek_find['aspek2']-minAspek2,2)
            aspek2_flag=False
        elif(aspek_find['aspek3']>1 and aspek3_flag):
            aspek_find['aspek3']=round(aspek_find['aspek3']-minAspek3,2)
            aspek3_flag=False
        elif(aspek_find['aspek4']>1  and aspek4_flag):
            aspek_find['aspek4']=round(aspek_find['aspek4']-minAspek4,2)
            aspek4_flag=False
        else:
            aspek4_flag=True
            aspek2_flag=True
            aspek3_flag=True
        domain2_res=hitungDomain2(aspek_find['aspek2'],aspek_find['aspek3'],aspek_find['aspek4'])


    return aspek_find
isi=isiModel()
df_allValue=isi.getAllValue()
df = pd.read_csv('Data CSV/Data_lengkap_part_01.csv')
for index, row in df.iterrows():
    # mendapatkan dari database semua value indikator ditahun 2021 dan 2022
    dfInstansi=df_allValue[df_allValue['id']==row.id]
    # jika instansi di temukan dalam database 2021 dan 2022
    if(dfInstansi.size>0):
        # hanya data yang ada pada tahun 2021 dan 2022 yang di kerjakan
        # inisialisasi indeks sesuai data yang ad pada csv jika tidak di temukan mengambil data tahun sebelumnya
        indeks_2018=0
        if(float(row.indeks_2018)>0):indeks_2018=row.indeks_2018
        indeks_2019=indeks_2018
        if(float(row.indeks_2019)>0):indeks_2019=row.indeks_2019
        indeks_2020=indeks_2019
        if(float(row.indeks_2020)>0):indeks_2020=row.indeks_2020
        # memisahkan data ke tiap tahun
        # untuk mempermudah perhitngan data yang diambil hanya data value disetiap tahunnya
        data_angka=['i1','i2','i3','i4','i5','i6','i7','i8','i9','i10','i11','i12','i13','i14','i15','i16','i17','i18','i19','i20','i21','i22','i23','i24','i25','i26','i27','i28','i29','i30','i31','i32','i33','i34','i35','i36','i37','i38','i39','i40','i41','i42','i43','i44','i45','i46','i47','aspek1','aspek2','aspek3','aspek4','aspek5','aspek6','aspek7','aspek8','domain1','domain2','domain3','domain4']
        data_2021=dfInstansi[dfInstansi["year"]==2021][data_angka].iloc[0]
        data_2022=dfInstansi[dfInstansi["year"]==2022][data_angka].iloc[0]
        
        # cari domain 2020
        data_2020=cariDomain(indeks_2020,data_2021,data_2022)
        data_2020=cariAspek(data_2020,data_2021)
        print(data_2020,hitungIndex(data_2020['domain1'],data_2020['domain2'],data_2020['domain3'],data_2020['domain4']),indeks_2020)
    