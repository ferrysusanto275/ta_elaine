import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Membuat data sampel
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5])

# Membuat model regresi linier
model = LinearRegression()
model.fit(X, y)

# Plot data dan regresi linier
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X, model.predict(X), color='red', label='Regresi Linier')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()

# Melakukan ekstrapolasi
X_new = np.array([6, 7, 8]).reshape(-1, 1)
y_pred = model.predict(X_new)

# Menampilkan hasil ekstrapolasi
print("Hasil Ekstrapolasi:")
for x, y_pred_val in zip(X_new.flatten(), y_pred):
    print(f"X = {x}, Prediksi y = {y_pred_val}")
