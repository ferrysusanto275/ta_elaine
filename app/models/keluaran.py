from app.utils.database import Database
from datetime import datetime
from app.models.isi import isiModel
import pandas as pd 
from decimal import Decimal
from sklearn.cluster import KMeans, AgglomerativeClustering
import scipy.cluster.hierarchy as sch 
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt 
from sklearn import preprocessing
from sklearn.decomposition import PCA
import numpy as np
isi=isiModel()
class keluaranModel:
    table_name="analisis"
    def getAll(self):
        db=Database()
        query="SELECT * FROM "+self.table_name;
        cur= db.execute_query(query)
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append({"id":row[0],"nama":row[1], "penanggung_jawab":row[2], "target_tahun":row[3], "grup":row[4]})
        cur.close()
        db.close()
        return data
    def getAllByGrup(self,grup):
        db=Database()
        query="SELECT * FROM "+self.table_name;
        query+=" WHERE grup=%s"
        cur= db.execute_query(query,(grup,))
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append({"id":row[0],"nama":row[1], "penanggung_jawab":row[2], "target_tahun":row[3], "grup":row[4]})
        cur.close()
        db.close()
        return data
    def getById(self, id):
        db=Database()
        query="SELECT * FROM "+self.table_name 
        query+=" WHERE id=%s"
        cur= db.execute_query(query,(id,))
        result=cur.fetchone()
        data=result
        if(result):
            data={"id":result[0],"name":result[1], "target_tahun":result[3], "grup":result[4]}
        cur.close()
        db.close()
        return data
    def create(self,nama, penanggung_jawab, target_tahun, grup):
        db=Database()
        query="INSERT INTO "+self.table_name
        query+=" (nama, penanggung_jawab, target_tahun, grup)"
        query+=" VALUES (%s,%s,%s,%s)"
        cur=db.execute_query(query,(nama, penanggung_jawab, target_tahun, grup))
        db.commit()
        cur.close()
        db.close()
        return True
    def update(self,nama, penanggung_jawab, target_tahun, grup, id):
        db=Database()
        query="UPDATE "+self.table_name
        query+=" SET nama=%s, penanggung_jawab=%s, target_tahun=%s, grup=%s"
        query+=" WHERE id=%s"
        cur=db.execute_query(query,(nama, penanggung_jawab, target_tahun, grup,id))
        db.commit()
        cur.close()
        db.close()
        return True
    def delete(self,id):
        db=Database()
        query="DELETE FROM "+self.table_name
        query+=" WHERE id=%s"
        cur=db.execute_query(query,(id,))
        db.commit()
        cur.close()
        db.close()
        return True
    def getAllInstansiby_Area(self,area):
        db= Database()
        query="SELECT id from instansi WHERE id in(SELECT analisis_instansi.instansi from analisis_instansi JOIN analisis on analisis_instansi.analisis=analisis.id JOIN analisis_grup on analisis.grup=analisis_grup.id WHERE analisis_grup.grup=%s)"
        cur=db.execute_query(query,(area,))
        result = [row[0] for row in cur.fetchall()]
        cur.close()
        db.close()
        return result
    def getAllIndikatorby_Area(self,area):
        db= Database()
        query="SELECT nama from indikator WHERE id in(SELECT analisis_indikator.indikator from analisis_indikator JOIN analisis on analisis_indikator.analisis=analisis.id JOIN analisis_grup on analisis.grup=analisis_grup.id WHERE analisis_grup.grup=%s) ORDER BY id"
        cur=db.execute_query(query,(area,))
        result = [row[0].lower() for row in cur.fetchall()]
        cur.close()
        db.close()
        return result
    def kmeans_res(self,area,year):
        df=isi.getDfAllIndikatorWOBobot()
        if(area!="0"):
            data_area=self.getAllInstansiby_Area(area)
            df=df[df['id'].astype('str').isin(data_area)]
            data_indikator=self.getAllIndikatorby_Area(area)

        df=df[df['year']== int(year)]
       
        if(area!="0"):
            features = df[data_indikator]
        else: features = df[['indeks']]
            
        K = range(2,6)
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
            best_num_clusters = model[np.argmax(silhouette_coef)]
        if(area!="0"):
            df=df[data_indikator+['nama']]
        centroids = kmeans.cluster_centers_
        return {"inertia":inertia,"silhouette_coef":silhouette_coef,'best_model':best_num_clusters,'df':df,'centroids':centroids,'features':features}
    
    def kmeans_res_bobot(self,area,year):
        df=isi.getDfAllIndikatorBobot()
        if(area!="0"):
            data_area=self.getAllInstansiby_Area(area)
            df=df[df['id'].astype('str').isin(data_area)]
            data_indikator=self.getAllIndikatorby_Area(area)
        df=df[df['year']== int(year)]
        if(area!="0"):
            features = df[data_indikator]
            # features = preprocessing.scale(df[data_indikator])
        else: features = df[['indeks']]
        K = range(2,6)
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
            best_num_clusters = model[np.argmax(silhouette_coef)]
        if(area!="0"):
            df=df[data_indikator+['nama']]
        centroids = kmeans.cluster_centers_
        return {"inertia":inertia,"silhouette_coef":silhouette_coef,'best_model':best_num_clusters,'df':df,'centroids':centroids}
    def getDfK_bobot(self,area,year):
        kmeans_obj=self.kmeans_res_bobot(area,year)
        klaster_objek = kmeans_obj['best_model'].labels_
        dfK= kmeans_obj['df'].copy()
        dfK['Cluster'] = klaster_objek
        
        return dfK
    def getDfK(self,area,year):
        kmeans_obj=self.kmeans_res(area,year)
        klaster_objek = kmeans_obj['best_model'].labels_
        dfK= kmeans_obj['df'].copy()
        dfK['Cluster'] = klaster_objek
        dfK['Centroid']=kmeans_obj['centroids']
        return dfK
    def get_res_pca_bobot(self,year,area):
        df=self.getDfK_bobot(area,year)
        data_indikator=self.getAllIndikatorby_Area(area)
        df_indikator=df[data_indikator]
        print(df_indikator)
        # df_indikator = preprocessing.scale(df_indikator)
        print(df_indikator)
        pca = PCA()
        pca.fit(df_indikator) # melakukan perhitungan PCA
        per_var = np.round(pca.explained_variance_ratio_* 100, decimals=1)
        labels = ['PC' + str(x) for x in range(1, len(per_var)+1)] #labelin diagram
        pca_data = pca.transform(df_indikator)
        pca_df = pd.DataFrame(pca_data, index=df_indikator.T.columns, columns=labels)
        loading_scores = pd.Series(pca.components_[0], index=data_indikator)
        sorted_loading_scores = loading_scores.abs().sort_values(ascending=False)

        # # mengambil data 10 biji
        top_10_genes = sorted_loading_scores[0:10].index.values
        # print(top_10_genes)
        
        return {"df":df,"pca":pca,'per_var':per_var,'pca_df':pca_df,'labels':labels,'top_10':loading_scores[top_10_genes]}
    def get_res_pca(self,year,area):
        df=self.getDfK(area,year)
        data_indikator=self.getAllIndikatorby_Area(area)
        df_indikator=df[data_indikator]
        # scaled_data = preprocessing.scale(df_indikator)
        pca = PCA()
        pca.fit(df_indikator) # melakukan perhitungan PCA
        per_var = np.round(pca.explained_variance_ratio_* 100, decimals=1)
        labels = ['PC' + str(x) for x in range(1, len(per_var)+1)] #labelin diagram
        pca_data = pca.transform(df_indikator)
        pca_df = pd.DataFrame(pca_data, index=df_indikator.T.columns, columns=labels)
        loading_scores = pd.Series(pca.components_[0], index=data_indikator)
        sorted_loading_scores = loading_scores.abs().sort_values(ascending=False)

        # # mengambil data 10 biji
        top_10_genes = sorted_loading_scores[0:10].index.values
        # print(top_10_genes)
        
        return {"df":df,"pca":pca,'per_var':per_var,'pca_df':pca_df,'labels':labels,'top_10':loading_scores[top_10_genes]}
    def agglo_res(self,area,year,linkage):
        df=isi.getDfAllIndikatorWOBobot()
        if(area!="0"):
            data_area=self.getAllInstansiby_Area(area)
            data_indikator=self.getAllIndikatorby_Area(area)
            df=df[df['id'].astype('str').isin(data_area)]
        else: data_indikator=['indeks']  
        if(area!="0"):
            df=df[df['id'].astype('str').isin(data_area)]
        df=df[df['year']== int(year)]
       
        features = df[data_indikator]
        K = range(2,6)
        silhouette_coef = []
        model = []
        for k in K:
            agglo_model = AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage=linkage)
            agglo_model.fit_predict(features)
            
            model.append(agglo_model)
            # print(agglo_model)
            score = silhouette_score(features, agglo_model.labels_, metric='euclidean')
            silhouette_coef.append(score)
        best_num_clusters = model[np.argmax(silhouette_coef)]
        df=df[data_indikator+['nama']]
        return {"silhouette_score":silhouette_coef,"best_num_clusters":best_num_clusters,'df':df,'data_indikator':data_indikator}
    def agglo_res_bobot(self,area,year,linkage):
        df=isi.getDfAllIndikatorBobot()
        if(area!="0"):
            data_area=self.getAllInstansiby_Area(area)
            data_indikator=self.getAllIndikatorby_Area(area)
            df=df[df['id'].astype('str').isin(data_area)]
        else: data_indikator=['indeks']  
        if(area!="0"):
            df=df[df['id'].astype('str').isin(data_area)]
        df=df[df['year']== int(year)]
       
        features = df[data_indikator]
        K = range(2,6)
        silhouette_coef = []
        model = []
        for k in K:
            agglo_model = AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage=linkage)
            agglo_model.fit_predict(features)
            
            model.append(agglo_model)
            # print(agglo_model)
            score = silhouette_score(features, agglo_model.labels_, metric='euclidean')
            silhouette_coef.append(score)
        best_num_clusters = model[np.argmax(silhouette_coef)]
        df=df[data_indikator+['nama']]
        return {"silhouette_score":silhouette_coef,"best_num_clusters":best_num_clusters,'df':df,'data_indikator':data_indikator}
    def getDfAByareaYear(self,area,year,linkage):
        agglo_obj=self.agglo_res(area,year,linkage)
        klaster_objek = agglo_obj['best_num_clusters']
        labels = klaster_objek.fit_predict(agglo_obj['df'][agglo_obj['data_indikator']])
        dfK = agglo_obj['df'].copy()
        dfK['Cluster'] = labels
        return dfK
    def getDfAByareaYear_bobot(self,area,year,linkage):
        agglo_obj=self.agglo_res_bobot(area,year,linkage)
        klaster_objek = agglo_obj['best_num_clusters']
        labels = klaster_objek.fit_predict(agglo_obj['df'][agglo_obj['data_indikator']])
        dfK = agglo_obj['df'].copy()
        dfK['Cluster'] = labels
        return dfK
  