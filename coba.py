# # -*- coding: utf-8 -*-
# """
# Created on Sat Oct  7 10:06:58 2023

# @author: Elaine
# """
# import pandas as pd 
# import matplotlib.pyplot as plt
# from sklearn import preprocessing
# from sklearn.cluster import KMeans
# import numpy as np 
# from sklearn.metrics import silhouette_score
# from sklearn.cluster import AgglomerativeClustering
# import scipy.cluster.hierarchy as sch

# df =pd.read_csv("Mall_Customers.csv")

# #Langkah-1 
# # plt.figure(figsize=(10,6))
# # plt.scatter(df['Age'],df['Spending Score (1-100)'], alpha=0.5)
# # plt.title("Age vs Spending")
# # plt.xlabel("Age")
# # plt.ylabel("Spending")

# # plt.figure(figsize=(10,6))
# # plt.scatter(df['Age'],df['Annual Income (k$)'], alpha=0.5)
# # plt.title("Age vs Income")
# # plt.xlabel("Age")
# # plt.ylabel("Spending")

# # plt.figure(figsize=(10,6))
# # plt.scatter(df['Spending Score (1-100)'],df['Annual Income (k$)'], alpha=0.5)
# # plt.title("Spending vs Income")
# # plt.xlabel("Spending")
# # plt.ylabel("Income")

# # #Kolom yang memiliki yang korelasi Spending vs Income 

# # label_encoder = preprocessing.LabelEncoder()
# # df['Gender']=label_encoder.fit_transform(df['Gender'])

# # #liat hubungan antara atribut diskret dan numerik 
# # l= df[df['Gender']==1]
# # w= df[df['Gender']==0]
# # plt.boxplot([l['Annual Income (k$)'],w['Annual Income (k$)']])
# # plt.boxplot([l['Spending Score (1-100)'],w['Spending Score (1-100)']])
# # #ngeliat korelasi antara semua atribut 
# # df.corr() 
# # df['Gender'].corr(df['Annual Income (k$)']) #liat korelasi 1-1 
# #pilih fitur 
# # features = df[['Annual Income (k$)', 'Spending Score (1-100)']]
# # print(features)
# # K = range(2,11)
# # inertia = []
# # silhouette_coef = [] 
# # model = [] 

# # for k in K:
# #     kmeans= KMeans(n_clusters=k, random_state=42)
# #     kmeans.fit(features)
# #     model.append(kmeans)
# #     inertia.append(kmeans.inertia_)
# #     score = silhouette_score(features, kmeans.labels_, metric='euclidean')
# #     silhouette_coef.append(score)
# #     print(k,score)
# #plot elbow method 
# # plt.plot(K, inertia, marker='o')
# # plt.xlabel('Jumlah kelompok k')
# # plt.ylabel('Inertia')
# # plt.title('Elbow method')
# # plt.show()

# #nilai k terbaik =5 
# # temp = model[5]
# # klaster_objek = temp.labels_
# # centroids = temp.cluster_centers_
# # jumlah = np.unique(klaster_objek, return_counts=True)
# # dfK= df.copy()
# # dfK['Cluster'] = klaster_objek

# # df1= df[df['Cluster']==5]
# # max1 = df1.max()
# # min1 = df1.min()

# # df2= df[df['Cluster']==4]
# # max2 = df2.max()
# # min2 = df2.min()

# # df3= df[df['Cluster']==3]
# # max3 = df3.max()
# # min3 = df3.min()
# # print(dfK)

# # ## A. Untuk single-linkage

# # # Plot dendrogram dari X
# # plt.figure(figsize=(10, 7))
# # plt.title("Dendrogram Mall Customers - Single Linkage")
# # dend = sch.dendrogram(sch.linkage(features, method='single'))
# # plt.show()
# # # Terlihat bahwa paling baik, dataset Irish dikelompokkan menjadi 5 klaster

# # # Kelompokkan dg algoritma agglomerative, jumlah klaster = 11
# # agglo_model = AgglomerativeClustering(n_clusters=11, affinity='euclidean', linkage='single')
# # agglo_model.fit_predict(features)
# # labels = agglo_model.labels_

# # # Cek koefisien silhoutte 
# # import matplotlib.pyplot as plt
# # from sklearn.metrics import silhouette_score
# # score = silhouette_score(features, agglo_model.labels_,  metric='euclidean')
# # print(score) #0.27

# # ## B. Untuk complete-linkage

# # plt.figure(figsize=(10, 7))
# # plt.title("Dendrogram Mall Customers - Complete Linkage")
# # dend = sch.dendrogram(sch.linkage(features, method='complete'))
# # plt.show()
# # # Terlihat bahwa paling baik, dataset Irish dikelompokkan menjadi 3 klaster

# # # Cek koefisien silhoutte 
# # agglo_model = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='complete')
# # agglo_model.fit_predict(features)
# # score = silhouette_score(features, agglo_model.labels_,  metric='euclidean')
# # print(score) #0.46


# # ## C. Untuk average-linkage

# # plt.figure(figsize=(10, 7))
# # plt.title("Dendrogram Mall Customers  - Average Linkage")
# # dend = sch.dendrogram(sch.linkage(features, method='average'))
# # plt.show()
# # # Terlihat bahwa paling baik, dataset Irish dikelompokkan menjadi 7 klaster

# # # Cek koefisien silhoutte 
# # agglo_model = AgglomerativeClustering(n_clusters=7, affinity='euclidean', linkage='average')
# # hasil = agglo_model.fit_predict(features)
# # score = silhouette_score(features, agglo_model.labels_,  metric='euclidean')
# # print(score) #0.54

# # #kesimpulan average-linkage yang paling cocok digunakan 
# # agglo_model.n_clusters


# # dfA= df.copy() #copy data frame
# # dfA['Cluster'] = hasil #tambahin kolom cluster, isi dari kolom adalah hasil

# # #Hitung pola tiap kelompok
# # df_pola = dfA.groupby(['Cluster']).describe()

# #Dendrogram
# # plt.figure(figsize=(10,7))
# # plt.title("dendrogram")
# # dend = sch.dendrogram(sch.linkage(features, method='single'))
# # plt.show 

# # #kelompok dend
# # agglo_model = AgglomerativeClustering( n_clusters=11, affinity='euclidean', linkage='single')
# # hasil1 = agglo_model.fit_predict(features)
# # labels= agglo_model.labels 

# # score = silhoette_score (features, agglo_model.labels_, metric ='euclidean')
# # print(score)


# # plt.figure(figsize=(10,6))
# # plt.title("Dend2")
# # dend = sch.dendrogram(sch.linkage(features, method='complete'))
# # plt.show 

# # agglo_model = AgglomerativeClustering(n_clusters=11, affinity='euclidean', linkage='complete')
# # hasil2 = agglo_model.fit_predict(features)
# # labels = agglo_model.labels_ 

# # score =silhouette_score(features, agglo_model.labels_, metric='euclidean')

# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.decomposition import PCA
# from sklearn.preprocessing import StandardScaler
# import seaborn as sns 


# # Assuming you have your data in a DataFrame named 'df'
# # Extract numerical columns for PCA
# df = pd.read_csv('Data CSV/Data Evaluasi SPBE Tahun 2021-2022.xlsx')
# numerical_columns = df.columns[df.columns.str.startswith('I')]

# # Selecting only the numerical columns for PCA
# X = df[numerical_columns]

# # Standardize the data (important for PCA)
# X_standardized = StandardScaler().fit_transform(X)

# # Apply PCA
# pca = PCA(n_components=2)
# principal_components = pca.fit_transform(X_standardized)

# # Create a DataFrame with the first two principal components and additional information
# pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
# pca_df['Nama Instansi'] = df['Nama Instansi']

# # Scatter plot
# plt.figure(figsize=(10, 6))
# sns.scatterplot(x='PC1', y='PC2', data=pca_df, hue='Nama Instansi', palette='Set2', s=100)
# plt.title('PCA Plot of Institutions')
# plt.xlabel('Principal Component 1 (PC1)')
# plt.ylabel('Principal Component 2 (PC2)')
# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Adjust legend position
# plt.show()
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import r2_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
df = pd.read_csv('house_price_data.csv')
#mencari kolerasi tiap atribut dengan target
print(df.corr())
#dari korelasi diambil 3 atribut prediktor untuk di tes
#sqft_living, sqft_above, dan grade
price = df[['price']].values
dataPred = df.drop(['id','date','price','bedrooms','bathrooms',
'sqft_lot','floors','waterfront',

'view','condition','sqft_basement','yr_built','yr_renovated','zipcode',
'lat','long','sqft_living15','sqft_lot15'], axis = 1)
#Simple Predictor
for i in dataPred.columns:
#Split dataset utk training dan test
    X_train, X_test, y_train, y_test = train_test_split(dataPred[[i]],
    price, test_size=0.2, random_state=3)
    #Buat dan latih (fit) model regresi linear
    model_regres = LinearRegression()
    model_regres.fit(X_train, y_train)
    #Retrieve the slope (koefisien pd atribut prediktor):
    print(model_regres.coef_)
    #Retrieve the intercept:
    print(model_regres.intercept_)
    #Lakukan prediksi dari X_test, simpan hasilnya di y_pred
    y_pred = model_regres.predict(X_test)
    # Hitung dan tampilkan MAE, MSE dan RMSE
    print('Mean Absolute Error (MAE):', metrics.mean_absolute_error(y_test,
    y_pred))
    print('Mean Squared Error (MSE):', metrics.mean_squared_error(y_test,
    y_pred))
    print('Root Mean Squared Error (RMSE):',
    np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
# Hitung dan tampilkan R2
r_2 = r2_score(y_test, y_pred)
print(r_2)
# Evaluasi Model Regresi dengan K-Fold
crossvalidation = KFold(n_splits=10, random_state=1, shuffle=True)
#Scoring
scores = cross_val_score(model_regres,X_train, y_train,
scoring="neg_mean_absolute_error", cv=crossvalidation, n_jobs=1)
print(scores)
print("Avg MAE: " + str(np.mean(scores)))
scores = cross_val_score(model_regres, X_train, y_train,
scoring="neg_mean_squared_error", cv=crossvalidation, n_jobs=1)
print(scores)
print("Avg MSE: " + str(np.mean(scores)))
scores = cross_val_score(model_regres, X_train, y_train,
scoring="neg_root_mean_squared_error", cv=crossvalidation, n_jobs=1)
print(scores)
print("Avg RMSE: " + str(np.mean(scores)))
scores = cross_val_score(model_regres, X_train, y_train, scoring="r2",
cv=crossvalidation, n_jobs=1)
print(scores)
print("Avg R2: " + str(np.mean(scores)))
#Mulitiple Predictor
#Predictor: sqft_living, grade, sqft_above
X1 = df[['grade','sqft_living','sqft_above']].values
X1.shape
Y1 = df[['price']].values
Y1.shape
#Split dataset training dan test

X1_train, X1_test, Y1_train, Y1_test = train_test_split(X1, Y1,
test_size=0.2, random_state=3)
#Train
model_regres = LinearRegression()
model_regres.fit(X1_train, Y1_train) #training the algorithm
#To retrieve the intercept:
print(model_regres.intercept_)
#For retrieving the slope:
print(model_regres.coef_)
#EVALAUASI DAN PENYIMPANAN MODEL
#Dengan data uji/test
Y1_pred = model_regres.predict(X1_test)
#Hitung dan tampilkan MAE, MSE dan RMSE
print('Mean Absolute Error:', metrics.mean_absolute_error(Y1_test,
Y1_pred))
print('Mean Squared Error:', metrics.mean_squared_error(Y1_test, Y1_pred))
print('Root Mean Squared Error:',
np.sqrt(metrics.mean_squared_error(Y1_test,
Y1_pred)))
# Hitung dan tampilkan R2
r_2 = r2_score(Y1_test, Y1_pred)
print('R2: ', r_2)
# Evaluasi Model Regresi dengan K-Fold
crossvalidation = KFold(n_splits=10, random_state=1, shuffle=True)
#Scoring
scores = cross_val_score(model_regres,X1_train,Y1_train,
scoring="neg_mean_absolute_error", cv=crossvalidation, n_jobs=1)
print(scores)
print("Avg MAE: " + str(np.mean(scores)))
scores = cross_val_score(model_regres, X1_train, Y1_train,
scoring="neg_mean_squared_error", cv=crossvalidation, n_jobs=1)
print(scores)
print("Avg MSE: " + str(np.mean(scores)))
scores = cross_val_score(model_regres, X1_train, Y1_train,
scoring="neg_root_mean_squared_error", cv=crossvalidation, n_jobs=1)
print(scores)
print("Avg RMSE: " + str(np.mean(scores)))
scores = cross_val_score(model_regres, X1_train, Y1_train, scoring="r2",
cv=crossvalidation, n_jobs=1)
print(scores)
print("Avg R2: " + str(np.mean(scores)))
#Predictor: sqft_living, grade
X1 = df[['grade','sqft_living']].values
X1.shape
Y1 = df[['price']].values
Y1.shape
#Split dataset training dan test
X1_train, X1_test, Y1_train, Y1_test = train_test_split(X1, Y1,
test_size=0.2, random_state=3)
#Train
model_regres = LinearRegression()
model_regres.fit(X1_train, Y1_train) #training the algorithm
#To retrieve the intercept:
print(model_regres.intercept_)

#For retrieving the slope:
print(model_regres.coef_)
#EVALAUASI DAN PENYIMPANAN MODEL
#Dengan data uji/test
Y1_pred = model_regres.predict(X1_test)
#Hitung dan tampilkan MAE, MSE dan RMSE
print('Mean Absolute Error:', metrics.mean_absolute_error(Y1_test,
Y1_pred))
print('Mean Squared Error:', metrics.mean_squared_error(Y1_test, Y1_pred))
print('Root Mean Squared Error:',
np.sqrt(metrics.mean_squared_error(Y1_test,
Y1_pred)))
# Hitung dan tampilkan R2
r_2 = r2_score(Y1_test, Y1_pred)
print('R2: ', r_2)
# Evaluasi Model Regresi dengan K-Fold
crossvalidation = KFold(n_splits=10, random_state=1, shuffle=True)
#Scoring
scores = cross_val_score(model_regres,X1_train,Y1_train,
scoring="neg_mean_absolute_error", cv=crossvalidation, n_jobs=1)
print(scores)
print("Avg MAE: " + str(np.mean(scores)))
scores = cross_val_score(model_regres, X1_train, Y1_train,
scoring="neg_mean_squared_error", cv=crossvalidation, n_jobs=1)
print(scores)
print("Avg MSE: " + str(np.mean(scores)))
scores = cross_val_score(model_regres, X1_train, Y1_train,
scoring="neg_root_mean_squared_error", cv=crossvalidation, n_jobs=1)
print(scores)
print("Avg RMSE: " + str(np.mean(scores)))
scores = cross_val_score(model_regres, X1_train, Y1_train, scoring="r2",
cv=crossvalidation, n_jobs=1)
print(scores)
print("Avg R2: " + str(np.mean(scores)))
#Predictor: sqft_living, sqft_above
X1 = df[['sqft_living','sqft_above']].values
X1.shape
Y1 = df[['price']].values
Y1.shape
#Split dataset training dan test
X1_train, X1_test, Y1_train, Y1_test = train_test_split(X1, Y1,
test_size=0.2, random_state=3)
#Train
model_regres = LinearRegression()
model_regres.fit(X1_train, Y1_train) #training the algorithm
#To retrieve the intercept:
print(model_regres.intercept_)
#For retrieving the slope:
print(model_regres.coef_)
#EVALAUASI DAN PENYIMPANAN MODEL
#Dengan data uji/test
Y1_pred = model_regres.predict(X1_test)
#Hitung dan tampilkan MAE, MSE dan RMSE
print('Mean Absolute Error:', metrics.mean_absolute_error(Y1_test,
Y1_pred))

print('Mean Squared Error:', metrics.mean_squared_error(Y1_test, Y1_pred))
print('Root Mean Squared Error:',
np.sqrt(metrics.mean_squared_error(Y1_test,
Y1_pred)))
# Hitung dan tampilkan R2
r_2 = r2_score(Y1_test, Y1_pred)
print('R2: ', r_2)
# Evaluasi Model Regresi dengan K-Fold
crossvalidation = KFold(n_splits=10, random_state=1, shuffle=True)
#Scoring
scores = cross_val_score(model_regres,X1_train,Y1_train,
scoring="neg_mean_absolute_error", cv=crossvalidation, n_jobs=1)
print(scores)
print("Avg MAE: " + str(np.mean(scores)))
scores = cross_val_score(model_regres, X1_train, Y1_train,
scoring="neg_mean_squared_error", cv=crossvalidation, n_jobs=1)
print(scores)
print("Avg MSE: " + str(np.mean(scores)))
scores = cross_val_score(model_regres, X1_train, Y1_train,
scoring="neg_root_mean_squared_error", cv=crossvalidation, n_jobs=1)
print(scores)
print("Avg RMSE: " + str(np.mean(scores)))
scores = cross_val_score(model_regres, X1_train, Y1_train, scoring="r2",
cv=crossvalidation, n_jobs=1)
print(scores)
print("Avg R2: " + str(np.mean(scores)))
#Predictor: grade, sqft_above
X1 = df[['grade','sqft_above']].values
X1.shape
Y1 = df[['price']].values
Y1.shape
#Split dataset training dan test
X1_train, X1_test, Y1_train, Y1_test = train_test_split(X1, Y1,
test_size=0.2, random_state=3)
#Train
model_regres = LinearRegression()
model_regres.fit(X1_train, Y1_train) #training the algorithm
#To retrieve the intercept:
print(model_regres.intercept_)
#For retrieving the slope:
print(model_regres.coef_)
#EVALAUASI DAN PENYIMPANAN MODEL
#Dengan data uji/test
Y1_pred = model_regres.predict(X1_test)
#Hitung dan tampilkan MAE, MSE dan RMSE
print('Mean Absolute Error:', metrics.mean_absolute_error(Y1_test,
Y1_pred))
print('Mean Squared Error:', metrics.mean_squared_error(Y1_test, Y1_pred))
print('Root Mean Squared Error:',
np.sqrt(metrics.mean_squared_error(Y1_test,
Y1_pred)))
# Hitung dan tampilkan R2
r_2 = r2_score(Y1_test, Y1_pred)

print('R2: ', r_2)
# Evaluasi Model Regresi dengan K-Fold
crossvalidation = KFold(n_splits=10, random_state=1, shuffle=True)
#Scoring
scores = cross_val_score(model_regres,X1_train,Y1_train,
scoring="neg_mean_absolute_error", cv=crossvalidation, n_jobs=1)
print(scores)
print("Avg MAE: " + str(np.mean(scores)))
scores = cross_val_score(model_regres, X1_train, Y1_train,
scoring="neg_mean_squared_error", cv=crossvalidation, n_jobs=1)
print(scores)
print("Avg MSE: " + str(np.mean(scores)))
scores = cross_val_score(model_regres, X1_train, Y1_train,
scoring="neg_root_mean_squared_error", cv=crossvalidation, n_jobs=1)
print(scores)
print("Avg RMSE: " + str(np.mean(scores)))
scores = cross_val_score(model_regres, X1_train, Y1_train, scoring="r2",
cv=crossvalidation, n_jobs=1)
print(scores)
print("Avg R2: " + str(np.mean(scores)))
# #REGRESI NON-LINEAR
# model_RFR = RandomForestRegressor()
# #Data train & test
# #1. Atribut X1: 'sqft_living','sqft_above','grade'
# #2. Atribut X1: 'sqft_living','grade'
# #3. Atribut X1: 'sqft_living','sqft_above'
# #4. Atribut X1: 'grade','sqft_above'
# X1 = df[['sqft_living','sqft_above','grade']]
# Y1 = df[['price']]
# X_train, X_test, y_train, y_test = train_test_split(X1, Y1, test_size=0.2,
# random_state=3)
# # Buat array dari dataframe
# X_train_RFR = np.array(X_train.values)
# X_test_RFR = np.array(X_test.values)
# y_train_RFR = np.array(y_train.values)
# # Ubah format y_train ke array
# y_train_RFR_2 = y_train_RFR.ravel()
# # train the model
# model_RFR.fit(X_train_RFR, y_train_RFR_2)
# # predict on test data
# y_predRFR = model_RFR.predict(X_test_RFR)
# # Hitung dan tampilkan MAE, MSE dan RMSE model non-linear
# print('')
# print('Model regresi non-liner:')
# print('MAE model non-linear:', metrics.mean_absolute_error(y_test,
# y_predRFR))
# print('MSE model non-linear:', metrics.mean_squared_error(y_test, y_predRFR))
# print('RMSE model non-linear::', np.sqrt(metrics.mean_squared_error(y_test,
# y_predRFR)))
# # Hitung dan tampilkan R2 model non-linear
# r_2 = r2_score(y_test, y_predRFR)
# print('R^2 model non-linear: ', r_2)
# crossvalidation = KFold(n_splits=10, random_state=1, shuffle=True)
# #Scoring

# scores = cross_val_score(model_RFR,X_train,y_train_RFR_2,
# scoring="neg_mean_absolute_error", cv=crossvalidation, n_jobs=1)
# print(scores)
# print("Avg MAE: " + str(np.mean(scores)))
# scores = cross_val_score(model_RFR, X_train_RFR, y_train_RFR_2,
# scoring="neg_mean_squared_error", cv=crossvalidation, n_jobs=1)
# print(scores)
# print("Avg MSE: " + str(np.mean(scores)))
# scores = cross_val_score(model_RFR, X_train_RFR, y_train_RFR_2,
# scoring="neg_root_mean_squared_error", cv=crossvalidation, n_jobs=1)
# print(scores)
# print("Avg RMSE: " + str(np.mean(scores)))
# scores = cross_val_score(model_RFR, X_train_RFR, y_train_RFR_2, scoring="r2",
# cv=crossvalidation, n_jobs=1)
# print(scores)
# print("Avg R2: " + str(np.mean(scores)))