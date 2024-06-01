from app.utils.database import Database
class analisis_indikatorModel:
    table_name="analisis_indikator"
    def getAll(self):
        db=Database()
        query="SELECT m.analisis, i.id, i.nama FROM "+self.table_name;
        query+=" m JOIN indikator i ON m.indikator=i.id";
        cur= db.execute_query(query)
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append({"analisis":row[0],"indikator":row[1], "nama_indikator": row[2]})
        cur.close()
        db.close()
        return data
    def getAllByAnalisis(self,analisis):
        db=Database()
        query="SELECT m.analisis, i.id, i.nama_lengkap FROM "+self.table_name;
        query+=" m JOIN indikator i ON m.indikator=i.id";
        query+=" WHERE m.analisis=%s"
        cur= db.execute_query(query,(analisis,))
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append({"analisis":row[0],"indikator":row[1], "nama_indikator": row[2]})
        cur.close()
        db.close()
        return data
    
    def create(self,analisis, indikator):
        db=Database()
        query="INSERT INTO "+self.table_name
        query+=" (analisis, indikator)"
        query+=" VALUES (%s,%s)"
        cur=db.execute_query(query,(analisis, indikator))
        db.commit()
        cur.close()
        db.close()
        return True
    def delete(self,analisis, indikator):
        db=Database()
        query="DELETE FROM "+self.table_name
        query+=" WHERE analisis=%s AND indikator=%s"
        cur=db.execute_query(query,(analisis, indikator))
        db.commit()
        cur.close()
        db.close()
        return True
        
    def getById(self,analisis, indikator):
        db=Database()
        query="SELECT * FROM "+self.table_name;
        query+=" WHERE analisis=%s AND indikator=%s"
        cur= db.execute_query(query,(analisis, indikator))
        result=cur.fetchone()
        data=result
        if(result):
            data={"analisis":result[0],"indikator":result[1]}
        cur.close()
        db.close()

        return data