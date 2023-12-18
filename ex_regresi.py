import numpy as np
from sklearn.linear_model import LinearRegression

# Fungsi tujuan
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
    # ... (sebagaimana telah didefinisikan dalam pertanyaan)

# Fungsi untuk ekstrapolasi regresi
def extrapolate_regression(params):
    # Data untuk ekstrapolasi
    X_extrapolate = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)

    # Membentuk model regresi linear
    model = LinearRegression()

    # Membentuk matriks X untuk regresi linear
    X_train = np.array([objective(params) for _ in range(len(X_extrapolate))]).reshape(-1, 1)

    # Nilai y yang akan diekstrapolasi
    y_extrapolate = model.fit(X_train, X_extrapolate).predict(X_extrapolate)

    return y_extrapolate

# Memanggil fungsi ekstrapolasi
params = np.ones(47)  # Ganti ini dengan nilai yang sesuai
extrapolated_values = extrapolate_regression(params)

# Menampilkan hasil ekstrapolasi
print("Hasil Ekstrapolasi:")
print(extrapolated_values)
