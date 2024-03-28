from flask import Blueprint,jsonify,request
from app.models.keluaran import keluaranModel
model=keluaranModel()
keluaranbp=Blueprint(model.table_name,__name__)
@keluaranbp.route('/api/'+model.table_name)
def get_all():
    return jsonify(model.getAll());
@keluaranbp.route('/api/'+model.table_name+'/<string:grup>')
def get_all_analisis_grup(grup):
    return jsonify(model.getAllByGrup(grup));