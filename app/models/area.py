from app.utils.database import Database
from datetime import datetime

class areaModel:
    table_name="area"
    prefix="d"
    def getAll(self):
        db=Database()
        query="SELECT * FROM "+self.table_name;
        cur= db.execute_query(query)
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append({"id":row[0],"nama":row[1]})
        cur.close()
        db.close()
        return data
    def getById(self,id):
        db=Database()
        query="SELECT * FROM "+self.table_name;
        query+=" WHERE id=%s"
        cur= db.execute_query(query,(id,))
        result=cur.fetchone()
        data=result
        if(result):
            data={"id":result[0],"name":result[1]}
        cur.close()
        db.close()

        return data
    def create(self,nama):
        db=Database()
        current_date = datetime.now().date()
        code=self.prefix+current_date.strftime("%Y%m%d")
        query="INSERT INTO "+self.table_name
        query+=" (nama)"
        query+=" VALUES (%s)"
        cur=db.execute_query(query,(nama,))
        db.commit()
        cur.close()
        db.close()
        return True
    def update(self,nama,id):
        db=Database()
        query="UPDATE "+self.table_name
        query+=" SET nama=%s"
        query+=" WHERE id=%s"
        cur=db.execute_query(query,(nama,id))
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