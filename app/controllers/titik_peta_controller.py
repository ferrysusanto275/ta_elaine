from flask import Blueprint,jsonify,request
from app.models.titik_peta import titik_petaModel
model=titik_petaModel()
titik_peta_bp=Blueprint(model.table_name,__name__)
@titik_peta_bp.route('/api/'+model.table_name+'/<string:tipe>/<string:year>/<string:domain>')
def get_all(tipe,year,domain):
    return jsonify(model.getAll(tipe,year,domain));



