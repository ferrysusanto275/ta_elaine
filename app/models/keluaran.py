from app.utils.database import Database
from datetime import datetime
db=Database()
class keluaranModel:
    table_name="analisis"
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
            data.append({"id":row[0],"nama":row[1], "penanggung_jawab":row[2], "grup":row[3]})
        # db.close()
        return data