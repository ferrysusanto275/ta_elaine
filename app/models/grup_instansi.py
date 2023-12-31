from app.utils.database import Database
from datetime import datetime
db=Database()
class grup_instansiModel:
    table_name="grup_instansi"
    prefix="gi"
    def getAll(self):
        query="SELECT * FROM "+self.table_name;
        cur= db.execute_query(query)
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append({"id":row[0],"nama":row[1]})
        # db.close()
        return data
    def getById(self,id):
        query="SELECT * FROM "+self.table_name;
        query+=" WHERE id=%s"
        cur= db.execute_query(query,(id,))
        result=cur.fetchone()
        data=result
        if(result):
            data={"id":result[0],"name":result[1]}
        # db.close()
        return data
    def getLastId(self,code):
        code_q=code+"%"
        query="SELECT MAX(id) FROM "+self.table_name
        query+=" WHERE id LIKE %s"
        cur= db.execute_query(query,(code_q,))
        result=cur.fetchone()
        idx=0
        if(result[0] is not None):
            idx=int(result[0][-5:])
        idx+=1;
        strIdx="00000"+str(idx)
        strIdx=strIdx[-5:]
        # db.close()
        return code+strIdx
    def create(self,nama):
        current_date = datetime.now().date()
        code=self.prefix+current_date.strftime("%Y%m%d")
        query="INSERT INTO "+self.table_name
        query+=" (id, nama)"
        query+=" VALUES (%s, %s)"
        cur=db.execute_query(query,(self.getLastId(code),nama))
        db.commit()
        # db.close()
        return True
    def update(self,nama,id):
        query="UPDATE "+self.table_name
        query+=" SET nama=%s"
        query+=" WHERE id=%s"
        db.execute_query(query,(nama,id))
        db.commit()
        return True
    def delete(self,id):
        query="DELETE FROM "+self.table_name
        query+=" WHERE id=%s"
        db.execute_query(query,(id,))
        db.commit()
        return True