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
            data.append({"id":row[0],"nama":row[1], "grup":row[2]})
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
            data.append({"id":row[0],"nama":row[1], "penanggung_jawab":row[2], "grup":row[3]})
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
            data={"id":result[0],"name":result[1],"grup":result[1]}
        cur.close()
        db.close()
        return data
    def create(self,nama, grup):
        db=Database()
        query="INSERT INTO "+self.table_name
        query+=" (nama,grup)"
        query+=" VALUES (%s)"
        cur=db.execute_query(query,(nama, grup))
        db.commit()
        cur.close()
        db.close()
        return True
    def update(self,nama,grup,id):
        db=Database()
        query="UPDATE "+self.table_name
        query+=" SET nama=%s, grup=%s"
        query+=" WHERE id=%s"
        cur=db.execute_query(query,(nama,grup,id))
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
