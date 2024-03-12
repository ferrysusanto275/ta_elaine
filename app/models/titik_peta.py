from app.utils.database import Database
from datetime import datetime
from app.models.isi import isiModel
db=Database()
isi_model=isiModel()
class titik_petaModel:
    table_name="titik_peta"
    prefix="tp"
    def getAll(self,tipe,year,domain_filter):
        db=Database()
        query="SELECT m.id,m.nama,m.x,m.y,i.id FROM "+self.table_name+" m";
        query+=" JOIN grup_instansi gi ON gi.titik_peta=m.id";
        query+=" JOIN instansi i ON gi.id=i.group_instansi";
        query+=" Where gi.tipe="+tipe;
        # print(query)
        cur= db.execute_query(query)
        result=cur.fetchall()
        cur.close()
        db.close()
        data=[]
        print(int(domain_filter)==0)
        for row in result:
            if(int(domain_filter) == 0):
                idx=isi_model.getIndexbyYearInstansi(year,row[4])
                print("Index "+str(idx))
            else:
                idx=isi_model.getAllDomainEmpat(row[4],year)
                print("domain "+str(idx))
           
            flag=True
            for item in data:
                if(row[0]==item['id']):
                    item['total_titik']+=1
                    item['total_index']+=idx
                    flag=False
            if(flag):
             data.append({"id":row[0],"nama":row[1],"x":row[2],"y":row[3],"total_index":idx,"total_titik":1})
        

        return data
    