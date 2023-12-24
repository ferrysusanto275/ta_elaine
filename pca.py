import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
# Membuat data dummy
np.random.seed(42)  # Untuk memastikan hasil yang sama setiap kali dijalankan

# Buat data dummy dengan 100 baris dan 17 fitur
num_samples = 100
num_features = 17

data_dummy = np.random.rand(num_samples, num_features)

# Normalisasi data jika diperlukan
# data_dummy = (data_dummy - data_dummy.mean(axis=0)) / data_dummy.std(axis=0)

# Inisialisasi model PCA dengan jumlah komponen yang diinginkan (dalam kasus ini, 2)
pca = PCA(n_components=2)

# Fit-transform data ke ruang PCA
data_pca = pca.fit_transform(data_dummy)

# Komponen Utama
PC1 = pca.components_[0]
PC2 = pca.components_[1]

# Nama fitur
feature_names = [f'I{i}' for i in range(32, 48)] + ['Domain4']

# Tampilkan komponen utama
PC1_values = dict(zip(feature_names, PC1))
PC2_values = dict(zip(feature_names, PC2))

print("Komponen Utama 1 (PC1):")
print(PC1_values)

print("\nKomponen Utama 2 (PC2):")
print(PC2_values)

# Tentukan threshold untuk kelompok pertama
threshold_PC1 = 0.5
threshold_PC2 = -0.5

# Tentukan threshold untuk fitur yang signifikan
threshold_signifikan = 0.2

# Ambil sampel yang memenuhi kriteria kelompok pertama
kelompok_pertama_indices = np.where((data_pca[:, 0] > threshold_PC1) & (data_pca[:, 1] < threshold_PC2))[0]

# Ambil data asli untuk kelompok pertama
kelompok_pertama_data = data_dummy[kelompok_pertama_indices, :]

# Identifikasi fitur yang signifikan dalam membentuk komponen utama
fitur_signifikan_PC1 = [f'I{i+32}' for i in range(len(PC1)) if abs(PC1[i]) > threshold_signifikan]
fitur_signifikan_PC2 = [f'I{i+32}' for i in range(len(PC2)) if abs(PC2[i]) > threshold_signifikan]

# # Visualisasi data dan kelompok pertama
# plt.figure(figsize=(10, 6))
# plt.scatter(data_pca[:, 0], data_pca[:, 1], label='Semua Data', alpha=0.5)
# plt.scatter(data_pca[kelompok_pertama_indices, 0], data_pca[kelompok_pertama_indices, 1], color='red', label='Kelompok Pertama')
# plt.title('Visualisasi Data dengan Kelompok Pertama')
# plt.xlabel('PC1')
# plt.ylabel('PC2')
# plt.legend()
# plt.show()

print("\nFitur Signifikan dalam membentuk PC1:")
print(fitur_signifikan_PC1)

print("\nFitur Signifikan dalam membentuk PC2:")
print(fitur_signifikan_PC2)
