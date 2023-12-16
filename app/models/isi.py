from app.utils.database import Database
from datetime import datetime
from app.models.instansi import instansiModel
from app.models.indikator import indikatorModel
from app.models.aspek import aspekModel
from app.models.domain import domainModel
import numpy as np
import pandas as pd 
from sklearn.cluster import KMeans, AgglomerativeClustering
import scipy.cluster.hierarchy as sch 
import matplotlib.pyplot as plt 
from sklearn.metrics import silhouette_score

indikator_model=indikatorModel();
instansi_model=instansiModel();
aspek_model=aspekModel();
domain_model=domainModel()
class isiModel:
    table_name="isi"
    def getAll(self):
        db=Database()
        query="SELECT * FROM "+self.table_name;
        cur= db.execute_query(query)
        result=cur.fetchall()
        data=[]
        for row in result:
            instansi=instansi_model.getById(row[0])
            indikator=indikator_model.getById(row[1])
            data.append({"instansi":instansi,"indikator":indikator,"year":row[2],"value":row[3]})
        cur.close()
        db.close()
        return data
    
    def getById(self,instansi,indikator,year):
        db=Database()
        query="SELECT * FROM "+self.table_name;
        query+=" WHERE instansi=%s AND indikator=%s AND year=%s"
        cur= db.execute_query(query,(instansi,indikator,year))
        result=cur.fetchone()
        data=result
        if(result):
            instansi=instansi_model.getById(result[0])
            indikator=indikator_model.getById(result[1])
            data={"instansi":instansi,"indikator":indikator,"year":result[2],"value":result[3]}
            # data.append({"instansi":instansi,"indikator":indikator,"tahun":result[2],"value":result[3]})
        cur.close()
        db.close()
        return data
    
    def create(self,instansi,indikator,year,value):
        db=Database()
        query="INSERT INTO "+self.table_name
        query+=" (instansi,indikator,year,value)"
        query+=" VALUES (%s,%s,%s,%s)"
        cur=db.execute_query(query,(instansi,indikator,year,value))
        db.commit()
        cur.close()
        db.close()
        return True
    def update(self,instansi,indikator,year,value):
        db=Database()
        query="UPDATE "+self.table_name
        query+=" SET value=%s "
        query+=" WHERE instansi=%s AND indikator=%s AND year=%s"
        cur=db.execute_query(query,(value,instansi,indikator,year))
        db.commit()
        cur.close()
        db.close()
        return True
    def delete(self,instansi,indikator,year):
        db=Database()
        query="DELETE FROM "+self.table_name
        query+=" WHERE instansi=%s AND indikator=%s AND year=%s"
        cur=db.execute_query(query,(instansi,indikator,year))
        db.commit()
        cur.close()
        db.close()
        return True
     # dapetin semua tahun yang ada di tabel isi
    def getAllYear(self):
        db=Database()
        query="SELECT DISTINCT(year) FROM "+self.table_name;
        cur= db.execute_query(query)
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append(row[0])
        cur.close()
        db.close()
        return data
    def getAllbyYearInstansiAspek(self,year,aspek,instansi):
        db=Database()
        query="SELECT * FROM "+self.table_name+" m JOIN indikator i ON m.indikator=i.id";
        query+=" WHERE m.year=%s AND m.instansi=%s AND i.aspek=%s"
        cur= db.execute_query(query,(year,instansi,aspek))
        result=cur.fetchall()
        data=[]
        for row in result:
            instansi=instansi_model.getById(row[0])
            indikator=indikator_model.getById(row[1])
            data.append({"instansi":instansi,"indikator":indikator,"year":row[3],"value":row[2]})
        cur.close()
        db.close()
        return data
    def getAllValue(self,indikator):
        db=Database()
        query="SELECT m.value FROM "+self.table_name+" m JOIN instansi i ON m.instansi=i.id";
        query+=" WHERE m.indikator=%s"
        query+=" ORDER BY i.id,m.year"
        # query+=" WHERE  m.indikator=%s"
        cur= db.execute_query(query,(indikator,))
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append(row[0])
        cur.close()
        db.close()
        return data
    def getAllValueByYear(self,indikator,year):
        db=Database()
        query="SELECT m.value FROM "+self.table_name+" m JOIN instansi i ON m.instansi=i.id";
        query+=" WHERE m.indikator=%s AND m.year=%s"
        query+=" ORDER BY i.id,m.year"
        # query+=" WHERE  m.indikator=%s"
        cur= db.execute_query(query,(indikator,year))
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append(row[0])
        cur.close()
        db.close()
        return data
    def getAllAspekByInstansi(self,instansi,domain,year):
        db=Database()
        query="SELECT a.id,a.nama,a.bobot,ROUND(SUM(m.value*indikator.bobot)/a.bobot,2) FROM "+self.table_name+" m";
        query+=" JOIN indikator ON m.indikator=indikator.id"
        query+=" JOIN aspek a on indikator.aspek=a.id"
        query+=" JOIN domain d on a.domain=d.id"
        query+=" WHERE m.instansi=%s and a.domain=%sand m.year=%s"
        query+=" GROUP BY a.id"
        print(query)
        cur= db.execute_query(query,(instansi,domain,year))
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append({"id":row[0],"nama":row[1],"bobot":row[2],"na":row[3]})
        cur.close()
        db.close()
        return data
    def getAllDomainByInstansi(self,instansi,year):
        data_domains=domain_model.getAll()
        data=[]
        for domain in data_domains:
            nd=0;
            data_aspek=self.getAllAspekByInstansi(instansi,domain['id'],year)
            for aspek in data_aspek:
                nd+=round(float(aspek['na'])*float(aspek['bobot'])/float(domain['bobot']),2)
            data.append({"id":domain['id'],"nama":domain['nama'],"bobot":domain['bobot'],"nd":round(nd,2)})
        
        return data
    def getAllAspek(self,aspek):
        db=Database()
        query="SELECT ROUND(SUM(m.value*indikator.bobot)/a.bobot,2) FROM "+self.table_name+" m";
        query+=" JOIN instansi i ON m.instansi=i.id"
        query+=" JOIN indikator ON m.indikator=indikator.id"
        query+=" JOIN aspek a on indikator.aspek=a.id"
        query+=" WHERE indikator.aspek=%s"
        query+=" GROUP BY i.id,m.year"
        query+=" ORDER BY i.id,m.year"
        cur= db.execute_query(query,(aspek,))
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append(row[0])
        cur.close()
        db.close()
        return data
    def getAllAspekByYear(self,aspek,year):
        db=Database()
        query="SELECT ROUND(SUM(m.value*indikator.bobot)/a.bobot,2) FROM "+self.table_name+" m";
        query+=" JOIN instansi i ON m.instansi=i.id"
        query+=" JOIN indikator ON m.indikator=indikator.id"
        query+=" JOIN aspek a on indikator.aspek=a.id"
        query+=" WHERE indikator.aspek=%s AND m.year=%s"
        query+=" GROUP BY i.id,m.year"
        query+=" ORDER BY i.id,m.year"
        cur= db.execute_query(query,(aspek,year))
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append(row[0])
        cur.close()
        db.close()
        return data
    def getAllDomain(self,domain):
        data_domain=domain_model.getById(domain)
        data_aspek=aspek_model.getAllByDomain(domain)
        value_aspek=[];
        for aspek in data_aspek:
            value_aspek.append(self.getAllAspek(aspek['id']))
        data=[]
        for i,nilai in enumerate(value_aspek[0]):
            jml=0
            for index,aspek in enumerate(data_aspek):
                jml+=value_aspek[index][i]*aspek['bobot']
            data.append(round(jml/data_domain['bobot'],2))
        return data
    def getAllDomainByYear(self,domain,year):
        data_domain=domain_model.getById(domain)
        data_aspek=aspek_model.getAllByDomain(domain)
        value_aspek=[];
        for aspek in data_aspek:
            value_aspek.append(self.getAllAspekByYear(aspek['id'],year))
        data=[]
        for i,nilai in enumerate(value_aspek[0]):
            jml=0
            for index,aspek in enumerate(data_aspek):
                jml+=value_aspek[index][i]*aspek['bobot']
            data.append(round(jml/data_domain['bobot'],2))
        return data
    def getAllIndex(self):
        data_domains=domain_model.getAll()
        data=[]
        jml_domain=0;
        value_domain=[];
        for domain in data_domains:
            value_domain.append(self.getAllDomain(domain['id']))
            jml_domain+=domain['bobot']
        for i,nilai in enumerate(value_domain[0]):
            jml=0
            for index,domain in enumerate(data_domains):
                jml+=value_domain[index][i]*domain['bobot']
            data.append(round(jml/jml_domain,2))
        return data
    def getAllIndexbyYear(self,year):
        data_domains=domain_model.getAll()
        data=[]
        jml_domain=0;
        value_domain=[];
        for domain in data_domains:
            value_domain.append(self.getAllDomainByYear(domain['id'],year))
            jml_domain+=domain['bobot']
        for i,nilai in enumerate(value_domain[0]):
            jml=0
            for index,domain in enumerate(data_domains):
                jml+=value_domain[index][i]*domain['bobot']
            data.append(round(jml/jml_domain,2))
        return data
    def getDf(self):
        db=Database()
        query="SELECT i.nama,gi.nama,m.year,m.value FROM "+self.table_name+" m";
        query+=" JOIN instansi i ON m.instansi=i.id"
        query+=" JOIN grup_instansi gi ON i.group_instansi=gi.id"
        query+=" WHERE m.indikator=%s"
        query+=" ORDER BY i.id,m.year"
        # query+=" WHERE  m.indikator=%s"
        data={"No":[],"Instansi":[],"Group":[],"Year":[]}
        list_indikator=indikator_model.getAll()
        for indikator in list_indikator:
           data[indikator['nama']]=self.getAllValue(indikator['id'])
        list_aspek=aspek_model.getAll()
        for aspek in list_aspek:
           data[aspek['nama']]=self.getAllAspek(aspek['id'])
        list_domain=domain_model.getAll()
        for domain in list_domain:
           data[domain['nama']]=self.getAllDomain(domain['id'])
        data["Indeks"]=self.getAllIndex()

        cur= db.execute_query(query,(list_indikator[0]['id'],))
        result=cur.fetchall()
        
        for i,row in enumerate(result):
           data['No'].append(i+1)
           data['Instansi'].append(row[0])
           data['Group'].append(row[1])
           data['Year'].append(row[2])
            
            
        cur.close()
        db.close()
        return data
    def getDfByYear(self,year):
        db=Database()
        query="SELECT i.nama,gi.nama,m.value FROM "+self.table_name+" m";
        query+=" JOIN instansi i ON m.instansi=i.id"
        query+=" JOIN grup_instansi gi ON i.group_instansi=gi.id"
        query+=" WHERE m.indikator=%s AND m.year=%s"
        query+=" ORDER BY i.id,m.year"
        # query+=" WHERE  m.indikator=%s"
        data={"No":[],"Instansi":[],"Group":[]}
        list_indikator=indikator_model.getAll()
        for indikator in list_indikator:
           data[indikator['nama']]=self.getAllValueByYear(indikator['id'],year)
        list_aspek=aspek_model.getAll()
        for aspek in list_aspek:
           data[aspek['nama']]=self.getAllAspekByYear(aspek['id'],year)
        list_domain=domain_model.getAll()
        for domain in list_domain:
           data[domain['nama']]=self.getAllDomainByYear(domain['id'], year)
        data["Indeks"]=self.getAllIndexbyYear(year)

        cur= db.execute_query(query,(list_indikator[0]['id'],year))
        result=cur.fetchall()
        
        for i,row in enumerate(result):
           data['No'].append(i+1)
           data['Instansi'].append(row[0])
           data['Group'].append(row[1])
        #    data['Year'].append(row[2])
            
            
        cur.close()
        db.close()
        return data
    def res_kmeans(self,df):
        features = df[['Indeks']]
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
        return {"inertia":inertia,"silhouette_coef":silhouette_coef,'best_model':best_num_clusters,'df':df}
    def kmeans_res(self):
        df=pd.DataFrame(self.getDf())
        return self.res_kmeans(df)
    def kmeans_resByYear(self,year):
        df=pd.DataFrame(self.getDfByYear(year))
        return self.res_kmeans(df)
    def getDfK(self):
        kmeans_obj=self.kmeans_res()
        klaster_objek = kmeans_obj['best_model'].labels_
        dfK= kmeans_obj['df'].copy()
        dfK['Cluster'] = klaster_objek
        return dfK
    def getDfKByYear(self,year):
        kmeans_obj=self.kmeans_resByYear(year)
        klaster_objek = kmeans_obj['best_model'].labels_
        dfK= kmeans_obj['df'].copy()
        dfK['Cluster'] = klaster_objek
        return dfK
    def getAllValueByYearInstansi(self,instansi,year):
        db=Database()
        query="SELECT m.value,ind.id,ind.bobot,a.id,a.bobot,d.id,d.bobot FROM "+self.table_name+" m"
        query+=" JOIN instansi i ON m.instansi=i.id"
        query+=" JOIN indikator ind ON m.indikator=ind.id"
        query+=" JOIN aspek a ON ind.aspek=a.id"
        query+=" JOIN domain d ON a.domain=d.id"
        query+=" WHERE m.instansi=%s AND m.year=%s"
        query+=" ORDER BY ind.id"
        # query+=" WHERE  m.indikator=%s"
        cur= db.execute_query(query,(instansi,year))
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append({"val":row[0],"id_indikator":row[1],"bobot_indikator":row[2],"id_aspek":row[3],"bobot_aspek":row[4],"id_domain":row[5],"bobot_domain":row[6]})
        cur.close()
        db.close()
        return data
    
    def getDfAByYear(self,year,linkage):
        df=pd.DataFrame(self.getDfByYear(year))
        agglo_obj=self.agglomerative(df,linkage)
        klaster_objek = agglo_obj['best_num_clusters']
        labels = klaster_objek.fit_predict(df[['Indeks']])
        dfK = df.copy()
        dfK['Cluster'] = labels
        return dfK
    # def agglomerative(self, df,linkage, silhouette_threshold=0.5):
    #     features = df[['Indeks']]
    #     num_samples = len(features)
    #     max_clusters = min(10, num_samples) 
    #     clusters_range = range(2, max_clusters + 1)

    #     silhouette_coef = []
    #     models = []

    #     for k in clusters_range:
    #         agglo_model = AgglomerativeClustering(n_clusters=k, affinity='euclidean', linkage=linkage)
    #         models.append(agglo_model)
    #         labels = agglo_model.fit_predict(features)
    #         score = silhouette_score(features, labels, metric='euclidean')
    #         silhouette_coef.append(score)

    #     # Filter models based on silhouette_threshold
    #     # above_threshold_models = [model for model, score in zip(models, silhouette_coef) if score > silhouette_threshold]

    #     if above_threshold_models:
    #         best_model = above_threshold_models[np.argmax(silhouette_coef)]
    #         best_num_clusters = best_model.n_clusters
    #     else:
    #         best_model = models[np.argmax(silhouette_coef)]
    #         best_num_clusters = best_model.n_clusters

    #     return {"silhouette_score": silhouette_coef, "best_num_clusters": best_num_clusters}
    def agglomerative(self, df, linkage):
        features= df[['Indeks']]
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
        return {"silhouette_score":silhouette_coef,"best_num_clusters":best_num_clusters}