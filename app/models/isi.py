from app.utils.database import Database
from datetime import datetime
from app.models.instansi import instansiModel
from app.models.indikator import indikatorModel

indikator_model=indikatorModel();
instansi_model=instansiModel();
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
    def getAllValue(self,indikator,gi):
        db=Database()
        query="SELECT m.value FROM "+self.table_name+" m JOIN instansi i ON m.instansi=i.id";
        query+=" WHERE i.group_instansi=%s and m.indikator=%s"
        query+=" ORDER BY i.id,m.year"
        # query+=" WHERE  m.indikator=%s"
        cur= db.execute_query(query,(gi,indikator))
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append(row[0])
        cur.close()
        db.close()
        return data
    def getAllAspek(self,aspek,gi):
        db=Database()
        query="SELECT ROUND(SUM(m.value*indikator.bobot)/a.bobot,2) FROM "+self.table_name+" m";
        query+=" JOIN instansi i ON m.instansi=i.id"
        query+=" JOIN indikator ON m.indikator=indikator.id"
        query+=" JOIN aspek a on indikator.aspek=a.id"
        query+=" WHERE i.group_instansi=%s and indikator.aspek=%s"
        query+=" GROUP BY i.id,m.year"
        query+=" ORDER BY i.id,m.year"
        cur= db.execute_query(query,(gi,aspek))
        result=cur.fetchall()
        cur.close()
        db.close()
        return result