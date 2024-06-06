import numpy as np
import pandas as pd
import decimal
from app.models.isi import isiModel

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
        # cari domain 1
        domain1_2020=float(round(domain1_2021,2))
        domain2_2020=float(round(domain2_2021,2))
        domain3_2020=float(round(domain3_2021,2))
        domain4_2020=float(round(domain4_2021,2))
        print(domain1_2020)
        if(indeks_2020>indeks_2021 and domain1_2021>domain1_2022):
            if(domain1_2020<5):
                domain1_2020=round(domain1_2020+0.01,2)
        if(indeks_2020>indeks_2021 and domain1_2021<domain1_2022):
            if(domain1_2020>1):
                domain1_2020=round(domain1_2020-0.01,2)
        
        # if(domain1_2021!=domain1_2022):
        #     indeks = np.array([data_2021['indeks'].values[0], data_2022['indeks'].values[0]])
        #     indeks = [float(d) for d in indeks]
        #     domain1 = np.array([data_2021['domain1'].values[0], data_2022['domain1'].values[0]])
        #     domain1 = [float(d) for d in domain1]
        #     domain2 = np.array([data_2021['domain2'].values[0], data_2022['domain2'].values[0]])
        #     domain2 = [float(d) for d in domain2]
        #     domain3 = np.array([data_2021['domain3'].values[0], data_2022['domain3'].values[0]])
        #     domain3 = [float(d) for d in domain3]
        #     domain4 = np.array([data_2021['domain4'].values[0], data_2022['domain4'].values[0]])
        #     domain4 = [float(d) for d in domain4]
        #     m1, b1 = np.polyfit(indeks, domain1, 1)  # Use decimal.Decimal for high precision
        #     m2, b2 = np.polyfit(indeks, domain2, 1)  # Use decimal.Decimal for high precision
        #     m3, b3  = np.polyfit(indeks, domain3, 1)  # Use decimal.Decimal for high precision
        #     m4, b4 = np.polyfit(indeks, domain4, 1)  # Use decimal.Decimal for high precision

            # if(indeks_2020>indeks_2021 and domain1_2021>domain1_2022):
            # Extrapolated value for indeks 3.37
            # domain1_2020 = round(m1 * indeks_2020 + b1,2)
            # domain2_2020 = round(m2 * indeks_2020 + b2,2)
            # domain3_2020 = round(m3 * indeks_2020 + b3,2)
            # domain4_2020 = round(m4 * indeks_2020 + b4,2)
        # domain1_2020=round(domain1_2020+0.01,2)
        index_res_2020=round(((domain1_2020*13)+(domain2_2020*25)+(domain3_2020*16.50)+(domain4_2020*45.50))/100,2)
        print(indeks_2020,domain1_2020,domain2_2020,domain3_2020,domain4_2020,index_res_2020)
            # m, b = np.polyfit(indeks, domain1, 1)
            # domain1_2020 = m * indeks_2020 + b
            # print(domain1_2020)
        #     print(row.id)
        #     print('indeks')
        #     print(indeks_2020)
        #     print(data_2021['indeks'].values[0])
        #     print(data_2022['indeks'].values[0])
        #     print("domain1")
        #     print(data_2021['domain1'].values[0])
        #     print(data_2022['domain1'].values[0])
        #     domain1_2020=domain1_2021+0.01


    # else:
        # print(row.instansi)
    # if(indeks_target>data_2021["indeks"].values[0])
    
    # print(indeks_target)
# Data points
# indeks = np.array([2.90, 3.12])
# domain1 = np.array([3.10, 2.70])

# Assuming a linear relationship (might not be accurate)
# m, b = np.polyfit(indeks, domain1, 1)

# Extrapolated value for indeks 3.68
# extrapolated_domain1 = m * 3.68 + b

# Disclaimer