import numpy as np
import pandas as pd
from app.models.isi import isiModel
from scipy.optimize import minimize

model=isiModel()
df = pd.read_csv('Data CSV/Data_lengkap_part_11.csv')
for index, row in df.iterrows():
    if(row.id!='NaN'):
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
        initial_guess=[]
        bounds=[]
        for i in range(47):
            initial_guess.append(1)
            bounds.append([1,5])
        if(float(row.indeks_2018)>0):
            constraint_2018 = {'type': 'eq', 'fun': lambda params: float(row.indeks_2018)- objective(params)}
            result_2018 = minimize(objective, initial_guess, bounds=bounds, constraints=constraint_2018)
        if(float(row.indeks_2019)>0):
            constraint_2019 = {'type': 'eq', 'fun': lambda params: float(row.indeks_2019)- objective(params)}
            result_2019 = minimize(objective, initial_guess, bounds=bounds, constraints=constraint_2019)
        if(float(row.indeks_2020)>0):
            constraint_2020 = {'type': 'eq', 'fun': lambda params: float(row.indeks_2020)- objective(params)}
            result_2020 = minimize(objective, initial_guess, bounds=bounds, constraints=constraint_2020)
        indikator_2018=[]
        indikator_2019=[]
        indikator_2020=[]
        # Menampilkan hasil
        for i in range(47):
            if(float(row.indeks_2018)>0):
                indikator_2018.append(result_2018.x[i])
            if(float(row.indeks_2019)>0):
                indikator_2019.append(result_2019.x[i])
            if(float(row.indeks_2020)>0):
                indikator_2020.append(result_2020.x[i])
        print(index,float(row.indeks_2018),float(row.indeks_2019),float(row.indeks_2020))
        if(float(row.indeks_2018)>0):
            print("masuk 2018")        
            model.create_bulk(row.id,'2018',indikator_2018)
        if(float(row.indeks_2019)>0):
            print("masuk 2019")   
            model.create_bulk(row.id,'2019',indikator_2019)
        if(float(row.indeks_2020)>0):
            print("masuk 2020")   
            model.create_bulk(row.id,'2020',indikator_2020)

