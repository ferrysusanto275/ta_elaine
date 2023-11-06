from app.utils.database import Database
from datetime import datetime
class predikat_model:
    table_name="predikat"
    prefix="p"
    def getAll(self):
        db=Database()
        query="SELECT * FROM "+self.table_name;
        cur= db.execute_query(query)
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append({"id":row[0],"nama":row[1],"batas_bawah":row[2]})
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
            data={"id":result[0],"name":result[1],"batas_bawah":result[2]}
        cur.close()
        db.close()
        return data
    def getLastId(self,code):
        db=Database()
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
        cur.close()
        db.close()
        return code+strIdx
    def create(self,nama, batas_bawah):
        db=Database()
        current_date = datetime.now().date()
        code=self.prefix+current_date.strftime("%Y%m%d")
        query="INSERT INTO "+self.table_name
        query+=" (id, nama, batas_bawah)"
        query+=" VALUES (%s, %s, %s)"
        cur=db.execute_query(query,(self.getLastId(code),nama, batas_bawah))
        db.commit()
        cur.close()
        db.close()
        return True
    def update(self,nama,id, batas_bawah):
        db=Database()
        query="UPDATE "+self.table_name
        query+=" SET nama=%s,batas_bawah=%s"
        query+=" WHERE id=%s"
        cur=db.execute_query(query,(nama, batas_bawah, id))
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
    def getAllNilai(self,nilai):
        db=Database()
        query="SELECT * FROM "+self.table_name
        query+=" WHERE batas_bawah <= %s"
        query+=" ORDER BY batas_bawah DESC LIMIT 1"
        cur= db.execute_query(query,(nilai,))
        result=cur.fetchone()
        data=result
        if(result):
            data={"id":result[0],"name":result[1],"batas_bawah":result[2]}
        cur.close()
        db.close()
        return data