from app.utils.database import Database
from datetime import datetime
db=Database()
class analisis_indikatorModel:
    table_name="analisis_indikator"
    def getAll(self):
        query="SELECT m.analisis, i.id, i.nama FROM "+self.table_name;
        query+=" m JOIN indikator i ON m.indikator=i.id";
        cur= db.execute_query(query)
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append({"analisis":row[0],"indikator":row[1], "nama_indikator": row[2]})
        # db.close()
        return data
    def getAllByAnalisis(self,analisis):
        query="SELECT m.analisis, i.id, i.nama FROM "+self.table_name;
        query+=" m JOIN indikator i ON m.indikator=i.id";
        query+=" WHERE m.analisis=%s"
        cur= db.execute_query(query,(analisis,))
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append({"analisis":row[0],"indikator":row[1], "nama_indikator": row[2]})
        # db.close()
        return data