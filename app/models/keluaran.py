from app.utils.database import Database
from datetime import datetime
from app.models.isi import isiModel
import pandas as pd 
from decimal import Decimal
from sklearn.cluster import KMeans, AgglomerativeClustering
import scipy.cluster.hierarchy as sch 
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt 
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
        query="SELECT id from instansi WHERE id in(SELECT instansi.id from analisis_instansi JOIN analisis on analisis_instansi.analisis=analisis.id JOIN analisis_grup on analisis.grup=analisis_grup.id WHERE analisis_grup.grup=%s)"
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
        if(area!="0"):
            data_area=self.getAllInstansiby_Area(area)
            data_indikator=self.getAllIndikatorby_Area(area)
        df=isi.getDfAllIndikator()
        if(area!="0"):
            df=df[df['id'].astype('str').isin(data_area)]
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
        return {"inertia":inertia,"silhouette_coef":silhouette_coef,'best_model':best_num_clusters,'df':df}
    def getDfK(self,area,year):
        kmeans_obj=self.kmeans_res(area,year)
        klaster_objek = kmeans_obj['best_model'].labels_
        dfK= kmeans_obj['df'].copy()
        dfK['Cluster'] = klaster_objek
        return dfK
    def agglo_res(self,area,year,linkage):
        if(area!="0"):
            data_area=self.getAllInstansiby_Area(area)
            data_indikator=self.getAllIndikatorby_Area(area)
        else: data_indikator=['indeks']    
        df=isi.getDfAllIndikator()
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
        return {"silhouette_score":silhouette_coef,"best_num_clusters":best_num_clusters,'df':df,'data_indikator':data_indikator}
    def getDfAByareaYear(self,area,year,linkage):
        agglo_obj=self.agglo_res(area,year,linkage)
        klaster_objek = agglo_obj['best_num_clusters']
        labels = klaster_objek.fit_predict(agglo_obj['df'][agglo_obj['data_indikator']])
        dfK = agglo_obj['df'].copy()
        dfK['Cluster'] = labels
        return dfK
    # def getAllDf(self):
    #     db= Database()
    #     query="SELECT a.id,a.nama,a.penanggung_jawab,a.target_tahun,a.grup,ag.nama 'nama_grup',ind.nama 'nama_indikator',ind.id 'id_indikator',ins.id 'id_instansi',ins.nama 'nama_instansi',isi.year,isi.value, area.id 'id_area', area.nama 'area_nama'"
    #     query+=" FROM analisis a"
    #     query+=" JOIN analisis_grup ag ON a.grup=ag.id"
    #     query+=" JOIN analisis_indikator ai ON a.id=ai.analisis"
    #     query+=" JOIN indikator ind on ai.indikator=ind.id"
    #     query+=" JOIN analisis_instansi ain on a.id=ain.analisis"
    #     query+=" JOIN instansi ins on ain.instansi=ins.id"
    #     query+=" JOIN isi on isi.instansi=ins.id and isi.indikator=ind.id"
    #     query+=" JOIN area on ag.grup=area.id"
    #     # print(query)
    #     cur= db.execute_query(query)
    #     result=cur.fetchall()
    #     data=[]
    #     data_tambah={}
    #     for row in result:
    #         # , "nama_indikator":row[6],"id_indikator":row[7],"value":row[11]
    #         newdata= {"id_instansi":row[8],"nama_instansi":row[9], "year":row[10], "id_area":row[12],"area_nama":row[13]}
    #         if(newdata not in data):
    #             data.append(newdata)
    #             data_tambah[str(newdata['id_area'])+"-"+str(newdata['year'])+"-"+str(newdata['id_instansi'])]={row[6]:row[11]}
    #         else:data_tambah[str(newdata['id_area'])+"-"+str(newdata['year'])+"-"+str(newdata['id_instansi'])][row[6]]=row[11]
    #     for i, row in enumerate(data):
    #         data[i]['val_indikator']=data_tambah[str(row['id_area'])+"-"+str(row['year'])+"-"+str(row['id_instansi'])]
            
        
    #     cur.close()
    #     db.close()
    #     return data