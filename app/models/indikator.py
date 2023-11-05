from app.utils.database import db
from datetime import datetime
from app.models.aspek import aspekModel
from app.models.instansi import instansiModel
aspek_model=aspekModel();
instansi_model=instansiModel();
class indikatorModel:
    table_name="indikator"
    prefix="in"
    def getAll(self):
        query="SELECT * FROM "+self.table_name;
        cur= db.execute_query(query)
        result=cur.fetchall()
        data=[]
        for row in result:
            aspek=aspek_model.getById(row[1])
            data.append({"id":row[0],"aspek":aspek,"nama":row[2],"bobot":row[3]})
        cur.close()
        return data
    
    def getAll_byIndex(self,aspek,instansi,year):
        query="SELECT *,(SELECT `value` FROM isi WHERE indikator=id AND instansi=%s AND year=%s) as ni FROM "+self.table_name;
        query+=" WHERE aspek=%s"
        cur= db.execute_query(query,(instansi,year,aspek))
        result=cur.fetchall()
        aspek=aspek_model.getById(aspek)
        instansi=instansi_model.getById(instansi)
        data=[{"aspek":aspek,"instansi":instansi,"year":year,'jml_indikator':len(result)}]
        jml_res=0
        for row in result:
            result=row[3]*row[4]
            jml_res+=result
            data.append({"id":row[0],"nama":row[2],"bobot":row[3],"NI":row[4],"hasil":result})
        data.append({"Jumlah (NI X BI)":jml_res})
        data.append({"Index":1/aspek['bobot']*jml_res})
        cur.close()
        return data
    
    def getById(self,id):
        query="SELECT * FROM "+self.table_name;
        query+=" WHERE id=%s"
        cur= db.execute_query(query,(id,))
        result=cur.fetchone()
        data=result
        if(result):
            aspek=aspek_model.getById(result[1])
            data={"id":result[0],"aspek":aspek,"name":result[2],"bobot":result[3]}
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
    def create(self,nama,bobot,aspek):
        current_date = datetime.now().date()
        code=self.prefix+current_date.strftime("%Y%m%d")
        query="INSERT INTO "+self.table_name
        query+=" (id, nama,bobot,aspek)"
        query+=" VALUES (%s, %s,%s,%s)"
        cur=db.execute_query(query,(self.getLastId(code),nama,bobot,aspek))
        db.commit()
        cur.close()
        return True
    def update(self,nama,bobot,aspek,id):
        query="UPDATE "+self.table_name
        query+=" SET nama=%s, bobot=%s, aspek=%s "
        query+=" WHERE id=%s"
        db.execute_query(query,(nama,bobot,aspek,id))
        db.commit()
        return True
    def delete(self,id):
        query="DELETE FROM "+self.table_name
        query+=" WHERE id=%s"
        db.execute_query(query,(id,))
        db.commit()
        return True
    def getAllByAspek(self,aspek):
        query="SELECT * FROM "+self.table_name;
        query+=" WHERE aspek=%s"
        cur= db.execute_query(query,(aspek,))
        result=cur.fetchall()
        data=[]
        for row in result:
            # aspek=Grup_instansi.getById(row[2])
            data.append({"id":row[0],"nama":row[2], "bobot":row[3]})
        cur.close()
        return data
    def getAllDomain(self):
        query="SELECT DISTINCT(d.id),d.nama FROM `indikator` m JOIN aspek a ON m.aspek=a.id JOIN domain d on a.domain=d.id"
        cur= db.execute_query(query)
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append({"id":row[0],"nama":row[1]})
        cur.close()
        return data
    def getAllAspek(self,domain):
        
        query="SELECT DISTINCT(a.id),a.nama FROM `indikator` m JOIN aspek a ON m.aspek=a.id "
        query+=" WHERE a.domain=%s"        
        # print(query)
        cur= db.execute_query(query,(domain,))
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append({"id":row[0],"nama":row[1]})
        cur.close()
        return data
   