from app.utils.database import Database
from app.models.isi import isiModel
db=Database()
isi_model=isiModel()
class titik_petaModel:
    table_name="titik_peta"
    prefix="tp"
    def getAll(self,tipe,year,domain_filter):
        df=isi_model.getAllIndeks_isi()
        df= df[df['year'] == int(year)]
        df=df[df['tipe'] == int(tipe)]
        df['nama_titik']=df['tp_nama']

        grouped_df = df.groupby(['x', 'y','nama_titik'])[domain_filter].mean().reset_index()
        data=grouped_df.to_dict()
        return data
    