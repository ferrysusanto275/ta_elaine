from app.utils.database import Database
from datetime import datetime
class analisis_instansiModel:
    table_name="analisis_instansi"
    def getAll(self):
        db=Database()
        query="SELECT m.analisis, i.id, i.nama FROM "+self.table_name;
        query+=" m JOIN instansi i ON m.instansi=i.id";
        cur= db.execute_query(query)
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append({"analisis":row[0],"instansi":row[1], "nama_instansi": row[2]})
        cur.close()
        db.close()
        return data
    def getAllByAnalisis(self,analisis):
        db=Database()
        query="SELECT m.analisis, i.id, i.nama FROM "+self.table_name;
        query+=" m JOIN instansi i ON m.instansi=i.id";
        query+=" WHERE m.analisis=%s"
        cur= db.execute_query(query,(analisis,))
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append({"analisis":row[0],"instansi":row[1], "nama_instansi": row[2]})
        cur.close()
        db.close()
        return data
    
    def create(self,analisis, instansi):
        db=Database()
        query="INSERT INTO "+self.table_name
        query+=" (analisis, instansi)"
        query+=" VALUES (%s,%s)"
        cur=db.execute_query(query,(analisis, instansi))
        db.commit()
        cur.close()
        db.close()
        return True
    def delete(self,analisis, instansi):
        db=Database()
        query="DELETE FROM "+self.table_name
        query+=" WHERE analisis=%s AND instansi=%s"
        cur=db.execute_query(query,(analisis, instansi))
        db.commit()
        cur.close()
        db.close()
        return True
        
    def getById(self,analisis, instansi):
        db=Database()
        query="SELECT * FROM "+self.table_name;
        query+=" WHERE analisis=%s AND instansi=%s"
        cur= db.execute_query(query,(analisis, instansi))
        result=cur.fetchone()
        data=result
        if(result):
            data={"analisis":result[0],"instansi":result[1]}
        cur.close()
        db.close()

        return data