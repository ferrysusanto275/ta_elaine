from app.utils.database import Database
from datetime import datetime
db=Database()
class titik_petaModel:
    table_name="titik_peta"
    prefix="tp"
    def getAll(self):
        query="SELECT * FROM "+self.table_name;
        cur= db.execute_query(query)
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append({"id":row[0],"nama":row[1],"x":row[2],"y":row[3]})
        # db.close()
        return data
    