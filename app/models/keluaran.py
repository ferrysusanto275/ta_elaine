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
