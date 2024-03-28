from app.utils.database import Database
from datetime import datetime
db=Database()
class grup_analisis_instansiModel:
    table_name="analisis_grup"
    grup_nama=['Tata Kelola SPBE', 'Layanan SPBE', 'Teknologi Informasi dan Komunikasi', 'Sumber Daya Manusia SPBE']
    def getAll(self):
        query="SELECT * FROM "+self.table_name;
        cur= db.execute_query(query)
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append({"id":row[0],"nama":row[1], "grup":row[2]})
        # db.close()
        return data
    def getAllByGrup(self,grup):
        query="SELECT * FROM "+self.table_name;
        query+=" WHERE grup=%s"
        cur= db.execute_query(query,(grup,))
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append({"id":row[0],"nama":row[1], "grup":row[2]})
        # db.close()
        return data