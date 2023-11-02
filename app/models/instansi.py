from app.utils.database import db
from app.models.grup_instansi import grup_instansiModel
from datetime import datetime

Grup_instansi= grup_instansiModel();

class instansiModel:
    table_name="instansi"
    prefix="i"
    def getAll(self):
        query="SELECT * FROM "+self.table_name;
        cur= db.execute_query(query)
        result=cur.fetchall()
        data=[]
        for row in result:
            grup=Grup_instansi.getById(row[2])
            data.append({"id":row[0],"nama":row[1],"grup":grup})
        cur.close()
        return data
    def getAllByGrup(self,grup):
        query="SELECT * FROM "+self.table_name;
        query+=" WHERE group_instansi=%s"
        cur= db.execute_query(query,(grup,))
        result=cur.fetchall()
        data=[]
        for row in result:
            # grup=Grup_instansi.getById(row[2])
            data.append({"id":row[0],"nama":row[1]})
        cur.close()
        return data
    def getById(self,id):
        query="SELECT * FROM "+self.table_name;
        query+=" WHERE id=%s"
        cur= db.execute_query(query,(id,))
        result=cur.fetchone()
        data=result
        if(result):
            grup=Grup_instansi.getById(result[2])
            data={"id":result[0],"name":result[1],"grup":grup}
        cur.close()
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
        cur.close()
        return code+strIdx
    def create(self,nama,grup):
        current_date = datetime.now().date()
        code=self.prefix+current_date.strftime("%Y%m%d")
        query="INSERT INTO "+self.table_name
        query+=" (id, nama,group_instansi)"
        query+=" VALUES (%s, %s,%s)"
        cur=db.execute_query(query,(self.getLastId(code),nama,grup))
        db.commit()
        cur.close()
        return True
    def update(self,nama,id,grup):
        query="UPDATE "+self.table_name
        query+=" SET nama=%s , group_instansi=%s"
        query+=" WHERE id=%s"
        db.execute_query(query,(nama,grup,id))
        db.commit()
        return True
    def delete(self,id):
        query="DELETE FROM "+self.table_name
        query+=" WHERE id=%s"
        db.execute_query(query,(id,))
        db.commit()
        return True