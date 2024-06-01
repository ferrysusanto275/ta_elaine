from app.utils.database import Database
from datetime import datetime
from app.models.aspek import aspekModel
class indikatorModel:
    table_name="indikator"
    prefix="in"
    def getAll(self):
        db=Database()
        aspek_model=aspekModel();
        query="SELECT * FROM "+self.table_name;
        cur= db.execute_query(query)
        result=cur.fetchall()
        data=[]
        for row in result:
            aspek=aspek_model.getById(row[1])
            data.append({"id":row[0],"aspek":aspek,"nama":row[2],"nama_lengkap":row[3],"bobot":row[4]})
        cur.close()
        db.close()
        return data
    
    def getById(self,id):
        db=Database()
        aspek_model=aspekModel();
        query="SELECT * FROM "+self.table_name;
        query+=" WHERE id=%s"
        cur= db.execute_query(query,(id,))
        result=cur.fetchone()
        data=result
        if(result):
            aspek=aspek_model.getById(result[1])
            data={"id":result[0],"aspek":aspek,"name":result[2],"nama_lengkap":result[3],"bobot":result[4]}
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
    def create(self,nama,bobot,aspek,nama_lengkap):
        db=Database()
        current_date = datetime.now().date()
        code=self.prefix+current_date.strftime("%Y%m%d")
        query="INSERT INTO "+self.table_name
        query+=" (id, nama,bobot,aspek,nama_lengkap)"
        query+=" VALUES (%s, %s,%s,%s,%s)"
        cur=db.execute_query(query,(self.getLastId(code),nama,bobot,aspek,nama_lengkap))
        db.commit()
        cur.close()
        db.close()
        return True
    def update(self,nama,bobot,aspek,nama_lengkap,id):
        db=Database()
        query="UPDATE "+self.table_name
        query+=" SET nama=%s, bobot=%s, aspek=%s, nama_lengkap=%s "
        query+=" WHERE id=%s"
        cur=db.execute_query(query,(nama,bobot,aspek,nama_lengkap,id))
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
    def getAllByAspek(self,aspek):
        db=Database()
        query="SELECT * FROM "+self.table_name;
        query+=" WHERE aspek=%s"
        cur= db.execute_query(query,(aspek,))
        result=cur.fetchall()
        data=[]
        for row in result:
            # aspek=Grup_instansi.getById(row[2])
            data.append({"id":row[0],"nama":row[2],"nama_lengkap":row[3], "bobot":row[4]})
        cur.close()
        db.close()
        return data
    def getAllDomain(self):
        db=Database()
        query="SELECT DISTINCT(d.id),d.nama,d.bobot FROM `indikator` m JOIN aspek a ON m.aspek=a.id JOIN domain d on a.domain=d.id"
        cur= db.execute_query(query)
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append({"id":row[0],"nama":row[1],"bobot":row[2]})
        cur.close()
        db.close()
        return data
    def getAllAspek(self,domain):
        db=Database()
        query="SELECT DISTINCT(a.id),a.nama,a.bobot FROM `indikator` m JOIN aspek a ON m.aspek=a.id "
        query+=" WHERE a.domain=%s" 
        cur= db.execute_query(query,(domain,))
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append({"id":row[0],"nama":row[1],"bobot":row[2]})
        cur.close()
        db.close()
        return data
   