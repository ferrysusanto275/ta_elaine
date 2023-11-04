from app.utils.database import db
from datetime import datetime
from app.models.instansi import instansiModel
from app.models.indikator import indikatorModel
indikator_model=indikatorModel();
instansi_model=instansiModel();
class isiModel:
    table_name="isi"
    def getAll(self):
        query="SELECT * FROM "+self.table_name;
        cur= db.execute_query(query)
        result=cur.fetchall()
        data=[]
        for row in result:
            instansi=instansi_model.getById(row[0])
            indikator=indikator_model.getById(row[1])
            data.append({"instansi":instansi,"indikator":indikator,"year":row[2],"value":row[3]})
        cur.close()
        return data
    
    def getById(self,instansi,indikator,year):
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
        return data
    
    def create(self,instansi,indikator,year,value):
        query="INSERT INTO "+self.table_name
        query+=" (instansi,indikator,year,value)"
        query+=" VALUES (%s,%s,%s,%s)"
        cur=db.execute_query(query,(instansi,indikator,year,value))
        db.commit()
        cur.close()
        return True
    def update(self,instansi,indikator,year,value):
        query="UPDATE "+self.table_name
        query+=" SET value=%s "
        query+=" WHERE instansi=%s AND indikator=%s AND year=%s"
        db.execute_query(query,(value,instansi,indikator,year))
        db.commit()
        return True
    def delete(self,instansi,indikator,year):
        query="DELETE FROM "+self.table_name
        query+=" WHERE instansi=%s AND indikator=%s AND year=%s"
        db.execute_query(query,(instansi,indikator,year))
        db.commit()
        return True
     # dapetin semua tahun yang ada di tabel isi
    def getAllYear(self):
        query="SELECT DISTINCT(year) FROM "+self.table_name;
        cur= db.execute_query(query)
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append(row[0])
        cur.close()
        return data
    def getAllbyYearInstansiAspek(self,year,aspek,instansi):
        query="SELECT * FROM "+self.table_name+" m JOIN indikator i ON m.indikator=i.id";
        query+=" WHERE m.year=%s AND m.instansi=%s AND i.aspek=%s"
        cur= db.execute_query(query,(year,instansi,aspek))
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append(row[0])
        cur.close()
        return data