from flask import Blueprint,jsonify,request
from app.models.analisis_indikator import analisis_indikatorModel
model=analisis_indikatorModel()
grup_analisis_indikatorbp=Blueprint(model.table_name,__name__)
@grup_analisis_indikatorbp.route('/api/'+model.table_name)
def get_all():
    return jsonify(model.getAll());
@grup_analisis_indikatorbp.route('/api/'+model.table_name+'/<string:analisis>')
def get_all_indikator_analisis(analisis):
    return jsonify(model.getAllByAnalisis(analisis));