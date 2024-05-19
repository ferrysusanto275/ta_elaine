from app.utils.database import Database
from datetime import datetime
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
        result=cur.fetchall()
        data=[]
        for row in result: data.append(row[0])
        cur.close()
        db.close()
        return data
    def getAllIndikatorby_Area(self,area):
        db= Database()
        query="SELECT nama from indikator WHERE id in(SELECT indikator.id from analisis_indikator JOIN analisis on analisis_indikator.analisis=analisis.id JOIN analisis_grup on analisis.grup=analisis_grup.id WHERE analisis_grup.grup=%s)"
        cur=db.execute_query(query,(area,))
        result=cur.fetchall()
        data=[]
        for row in result: data.append(row[0])
        cur.close()
        db.close()
        return data
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