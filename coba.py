# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 10:06:58 2023

@author: Elaine
"""
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.cluster import KMeans
import numpy as np 
from sklearn.metrics import silhouette_score
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch

df =pd.read_csv("Mall_Customers.csv")

#Langkah-1 
# plt.figure(figsize=(10,6))
# plt.scatter(df['Age'],df['Spending Score (1-100)'], alpha=0.5)
# plt.title("Age vs Spending")
# plt.xlabel("Age")
# plt.ylabel("Spending")

# plt.figure(figsize=(10,6))
# plt.scatter(df['Age'],df['Annual Income (k$)'], alpha=0.5)
# plt.title("Age vs Income")
# plt.xlabel("Age")
# plt.ylabel("Spending")

# plt.figure(figsize=(10,6))
# plt.scatter(df['Spending Score (1-100)'],df['Annual Income (k$)'], alpha=0.5)
# plt.title("Spending vs Income")
# plt.xlabel("Spending")
# plt.ylabel("Income")

# #Kolom yang memiliki yang korelasi Spending vs Income 

# label_encoder = preprocessing.LabelEncoder()
# df['Gender']=label_encoder.fit_transform(df['Gender'])

# #liat hubungan antara atribut diskret dan numerik 
# l= df[df['Gender']==1]
# w= df[df['Gender']==0]
# plt.boxplot([l['Annual Income (k$)'],w['Annual Income (k$)']])
# plt.boxplot([l['Spending Score (1-100)'],w['Spending Score (1-100)']])
# #ngeliat korelasi antara semua atribut 
# df.corr() 
# df['Gender'].corr(df['Annual Income (k$)']) #liat korelasi 1-1 
#pilih fitur 
features = df[['Annual Income (k$)', 'Spending Score (1-100)']]
print(features)
K = range(2,11)
inertia = []
silhouette_coef = [] 
model = [] 

for k in K:
    kmeans= KMeans(n_clusters=k, random_state=42)
    kmeans.fit(features)
    model.append(kmeans)
    inertia.append(kmeans.inertia_)
    score = silhouette_score(features, kmeans.labels_, metric='euclidean')
    silhouette_coef.append(score)
    print(k,score)
#plot elbow method 
# plt.plot(K, inertia, marker='o')
# plt.xlabel('Jumlah kelompok k')
# plt.ylabel('Inertia')
# plt.title('Elbow method')
# plt.show()

#nilai k terbaik =5 
temp = model[5]
klaster_objek = temp.labels_
centroids = temp.cluster_centers_
jumlah = np.unique(klaster_objek, return_counts=True)
dfK= df.copy()
dfK['Cluster'] = klaster_objek

# df1= df[df['Cluster']==5]
# max1 = df1.max()
# min1 = df1.min()

# df2= df[df['Cluster']==4]
# max2 = df2.max()
# min2 = df2.min()

# df3= df[df['Cluster']==3]
# max3 = df3.max()
# min3 = df3.min()
# print(dfK)

# ## A. Untuk single-linkage

# # Plot dendrogram dari X
# plt.figure(figsize=(10, 7))
# plt.title("Dendrogram Mall Customers - Single Linkage")
# dend = sch.dendrogram(sch.linkage(features, method='single'))
# plt.show()
# # Terlihat bahwa paling baik, dataset Irish dikelompokkan menjadi 5 klaster

# # Kelompokkan dg algoritma agglomerative, jumlah klaster = 11
# agglo_model = AgglomerativeClustering(n_clusters=11, affinity='euclidean', linkage='single')
# agglo_model.fit_predict(features)
# labels = agglo_model.labels_

# # Cek koefisien silhoutte 
# import matplotlib.pyplot as plt
# from sklearn.metrics import silhouette_score
# score = silhouette_score(features, agglo_model.labels_,  metric='euclidean')
# print(score) #0.27

# ## B. Untuk complete-linkage

# plt.figure(figsize=(10, 7))
# plt.title("Dendrogram Mall Customers - Complete Linkage")
# dend = sch.dendrogram(sch.linkage(features, method='complete'))
# plt.show()
# # Terlihat bahwa paling baik, dataset Irish dikelompokkan menjadi 3 klaster

# # Cek koefisien silhoutte 
# agglo_model = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='complete')
# agglo_model.fit_predict(features)
# score = silhouette_score(features, agglo_model.labels_,  metric='euclidean')
# print(score) #0.46


# ## C. Untuk average-linkage

# plt.figure(figsize=(10, 7))
# plt.title("Dendrogram Mall Customers  - Average Linkage")
# dend = sch.dendrogram(sch.linkage(features, method='average'))
# plt.show()
# # Terlihat bahwa paling baik, dataset Irish dikelompokkan menjadi 7 klaster

# # Cek koefisien silhoutte 
# agglo_model = AgglomerativeClustering(n_clusters=7, affinity='euclidean', linkage='average')
# hasil = agglo_model.fit_predict(features)
# score = silhouette_score(features, agglo_model.labels_,  metric='euclidean')
# print(score) #0.54

# #kesimpulan average-linkage yang paling cocok digunakan 
# agglo_model.n_clusters


# dfA= df.copy() #copy data frame
# dfA['Cluster'] = hasil #tambahin kolom cluster, isi dari kolom adalah hasil

# #Hitung pola tiap kelompok
# df_pola = dfA.groupby(['Cluster']).describe()

#Dendrogram
plt.figure(figsize=(10,7))
plt.title("dendrogram")
dend = sch.dendrogram(sch.linkage(features, method='single'))
plt.show 

#kelompok dend
agglo_model = AgglomerativeClustering( n_clusters=11, affinity='euclidean', linkage='single')
hasil1 = agglo_model.fit_predict(features)
labels= agglo_model.labels 

score = silhoette_score (features, agglo_model.labels_, metric ='euclidean')
print(score)


plt.figure(figsize=(10,6))
plt.title("Dend2")
dend = sch.dendrogram(sch.linkage(features, method='complete'))
plt.show 

agglo_model = AgglomerativeClustering(n_clusters=11, affinity='euclidean', linkage='complete')
hasil2 = agglo_model.fit_predict(features)
labels = agglo_model.labels_ 

score =silhouette_score(features, agglo_model.labels_, metric='euclidean')