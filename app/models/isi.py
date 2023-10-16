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
            data.append({"instansi":instansi,"indikator":indikator,"value":row[2]})
        cur.close()
        return data
    
    def getById(self,instansi,indikator):
        query="SELECT * FROM "+self.table_name;
        query+=" WHERE instansi=%s AND indikator=%s"
        cur= db.execute_query(query,(instansi,indikator))
        result=cur.fetchone()
        data=result
        if(result):
            instansi=instansi_model.getById(result[0])
            indikator=indikator_model.getById(result[1])
            data.append({"instansi":instansi,"indikator":indikator,"value":result[2]})
        cur.close()
        return data
    
    def create(self,instansi,indikator,value):
        query="INSERT INTO "+self.table_name
        query+=" (instansi,indikator,value)"
        query+=" VALUES (%s,%s,%s)"
        cur=db.execute_query(query,(instansi,indikator,value))
        db.commit()
        cur.close()
        return True
    def update(self,instansi,indikator,value):
        query="UPDATE "+self.table_name
        query+=" SET value=%s "
        query+=" WHERE instansi=%s AND indikator=%s"
        db.execute_query(query,(value,instansi,indikator))
        db.commit()
        return True
    def delete(self,instansi,indikator):
        query="DELETE FROM "+self.table_name
        query+=" WHERE instansi=%s AND indikator=%s"
        db.execute_query(query,(instansi,indikator))
        db.commit()
        return True