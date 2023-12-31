from app.utils.database import Database
from datetime import datetime
from app.models.domain import domainModel
from app.models.instansi import instansiModel

class aspekModel:
    def __init__(self):
        self.db=Database()
        self.table_name="aspek"
        self.prefix="a"
    def getAll(self):
        db= Database()
        domain_model=domainModel()
        query="SELECT * FROM "+self.table_name;
        cur= db.execute_query(query)
        result=cur.fetchall()
        data=[]
        for row in result:
            domain=domain_model.getById(row[1])
            data.append({"id":row[0],"domain":domain,"nama":row[2],"bobot":row[3]})
        cur.close()
        db.close()
        return data

    # def getAll_byIndex(self,domain,instansi,year):
    #     db= Database()
    #     domain_model=domainModel()
    #     instansi_model=instansiModel()
    #     query="SELECT *,(SELECT SUM(i.value*m.bobot) FROM `indikator` m JOIN isi i ON m.id=i.indikator WHERE m.aspek=aspek.id AND i.instansi=%s AND i.year=%s)*1/bobot na FROM "+self.table_name
    #     query+=" WHERE domain=%s"
    #     cur= db.execute_query(query,(instansi,year,domain))
    #     result=cur.fetchall()
    #     domain=domain_model.getById(domain)
    #     instansi=instansi_model.getById(instansi)
    #     data=[{"domain":domain,"instansi":instansi,"year":year,"jml_aspek":len(result)}]
    #     jml_res=0
    #     for row in result:
    #         result=row[4]*row[3]
    #         jml_res+=result
    #         data.append({"id":row[0],"nama":row[2],"bobot":row[3],"NA":row[4],"hasil":result})
    #     data.append({"Jumlah (NA X BA)":jml_res})
    #     data.append({"Index":1/domain['bobot']*jml_res})
    #     db.close()
    #     return data

    def getAllByDomain(self,domain):
        db= Database()
        query="SELECT * FROM "+self.table_name;
        query+=" WHERE domain=%s"
        cur= db.execute_query(query,(domain,))
        result=cur.fetchall()
        data=[]
        for row in result:
            data.append({"id":row[0],"nama":row[2], "bobot":row[3]})
        cur.close()
        db.close()
        return data
    def getById(self,id):
        db= Database()
        domain_model=domainModel()
        query="SELECT * FROM "+self.table_name;
        query+=" WHERE id=%s"
        cur= db.execute_query(query,(id,))
        result=cur.fetchone()
        data=result
        if(result):
            domain=domain_model.getById(result[1])
            data={"id":result[0],"domain":domain,"name":result[2],"bobot":result[3]}
        cur.close()
        db.close()
        return data
    def getLastId(self,code):
        db= Database()
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
    def create(self,nama,bobot,domain):
        db= Database()
        current_date = datetime.now().date()
        code=self.prefix+current_date.strftime("%Y%m%d")
        query="INSERT INTO "+self.table_name
        query+=" (id, nama,bobot,domain)"
        query+=" VALUES (%s, %s,%s,%s)"
        cur=db.execute_query(query,(self.getLastId(code),nama,bobot,domain))
        cur.close()
        db.commit()
        db.close()
        return True
    def update(self,nama,bobot,domain,id):
        db= Database()
        query="UPDATE "+self.table_name
        query+=" SET nama=%s, bobot=%s, domain=%s "
        query+=" WHERE id=%s"
        cur=db.execute_query(query,(nama,bobot,domain,id))
        db.commit()
        cur.close()
        db.close()
        return True
    def delete(self,id):
        db= Database()
        query="DELETE FROM "+self.table_name
        query+=" WHERE id=%s"
        cur=db.execute_query(query,(id,))
        db.commit()
        cur.close()
        db.close()
        return True