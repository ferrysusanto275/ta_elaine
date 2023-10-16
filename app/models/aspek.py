from app.utils.database import db
from datetime import datetime
from app.models.domain import domainModel
domain_model=domainModel();
class aspekModel:
    table_name="aspek"
    prefix="a"
    def getAll(self):
        query="SELECT * FROM "+self.table_name;
        cur= db.execute_query(query)
        result=cur.fetchall()
        data=[]
        for row in result:
            domain=domain_model.getById(row[1])
            data.append({"id":row[0],"domain":domain,"nama":row[2],"bobot":row[3]})
        cur.close()
        return data
    
    def getById(self,id):
        query="SELECT * FROM "+self.table_name;
        query+=" WHERE id=%s"
        cur= db.execute_query(query,(id,))
        result=cur.fetchone()
        data=result
        if(result):
            domain=domain_model.getById(result[1])
            data={"id":result[0],"domain":domain,"name":result[2],"bobot":result[3]}
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
    def create(self,nama,bobot,domain):
        current_date = datetime.now().date()
        code=self.prefix+current_date.strftime("%Y%m%d")
        query="INSERT INTO "+self.table_name
        query+=" (id, nama,bobot,domain)"
        query+=" VALUES (%s, %s,%s,%s)"
        cur=db.execute_query(query,(self.getLastId(code),nama,bobot,domain))
        db.commit()
        cur.close()
        return True
    def update(self,nama,bobot,domain,id):
        query="UPDATE "+self.table_name
        query+=" SET nama=%s, bobot=%s, domain=%s "
        query+=" WHERE id=%s"
        db.execute_query(query,(nama,bobot,domain,id))
        db.commit()
        return True
    def delete(self,id):
        query="DELETE FROM "+self.table_name
        query+=" WHERE id=%s"
        db.execute_query(query,(id,))
        db.commit()
        return True