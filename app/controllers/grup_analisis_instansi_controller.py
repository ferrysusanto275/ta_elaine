from flask import Blueprint,jsonify,request
from app.models.grup_analisis_instansi import grup_analisis_instansiModel
model=grup_analisis_instansiModel()
grup_analisisbp=Blueprint(model.table_name,__name__)
@grup_analisisbp.route('/api/'+model.table_name)
def get_all():
    return jsonify(model.getAll());
@grup_analisisbp.route('/api/'+model.table_name+'/bagian')
def get_bagian():
    return jsonify(model.grup_nama);
@grup_analisisbp.route('/api/'+model.table_name+'/<string:grup>')
def get_all_analisis_grup(grup):
    return jsonify(model.getAllByGrup(grup));