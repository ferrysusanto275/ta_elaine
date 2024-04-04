from flask import Blueprint,jsonify,request
from app.models.aspek import aspekModel
from app.models.indikator import indikatorModel
from app.models.instansi import instansiModel
model=indikatorModel()
aspek_model=aspekModel()
indikator_bp=Blueprint(model.table_name,__name__)
instansi_model=instansiModel();
def validasiInput():
    nama = request.json.get('nama')
    if not nama:
        return jsonify({'message': 'Nama is required'}), 400
    nama_lengkap = request.json.get('nama_lengkap')
    if not nama_lengkap:
        return jsonify({'message': 'Nama Lengkap is required'}), 400
    bobot = request.json.get('bobot')
    if not bobot:
        return jsonify({'message': 'Bobot is required'}), 400
    # cek bobot number atau bukan
    if not isinstance(bobot, (int, float, complex)):
        return jsonify({'message': 'Bobot is must number'}), 400
    aspek = request.json.get('aspek')
    if not aspek:
        return jsonify({'message': 'Aspek is required'}), 400
    cekAspek=aspek_model.getById(aspek)
    if not cekAspek:
        return jsonify({'message': 'Aspek not found'}), 400
    return [nama,bobot,aspek,nama_lengkap]
@indikator_bp.route('/api/'+model.table_name)
def get_all():
    return jsonify(model.getAll());

@indikator_bp.route('/api/'+model.table_name+'/<string:id>')
def get_by_id(id):
    instansi = model.getById(id)
    if instansi:
        return jsonify(instansi)
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404

# @indikator_bp.route('/api/index_'+model.table_name+'/<string:instansi>/<string:year>/<string:aspek>')
# def get_by_aspek_instansi(aspek,instansi,year):
#     if not aspek:
#         return jsonify({'message': 'Aspek is required'}), 400
#     cekAspek=aspek_model.getById(aspek)
#     if not cekAspek:
#         return jsonify({'message': 'Aspek not found'}), 400
#     if not instansi:
#         return jsonify({'message': 'Instansi is required'}), 400
#     cekInstansi=instansi_model.getById(instansi)
#     if not cekInstansi:
#         return jsonify({'message': 'Instansi not found'}), 400
#     if not year:
#         return jsonify({'message': 'Year is required'}), 400
#     if not isinstance(year, (int, float, complex)):
#         return jsonify({'message': 'Year is must number'}), 400
    
#     indikator = model.getAll_byIndex(aspek,instansi,year)
#     if indikator:
#         return jsonify(indikator)
#     else:
#         return jsonify({'message': model.table_name.capitalize()+' not found'}), 404

@indikator_bp.route('/api/'+model.table_name,methods=['POST'])
def create():
    data=validasiInput()
    if not isinstance(data,list):return data
    if model.create(data[0],data[1],data[2],data[3]):
        return jsonify({'message': model.table_name.capitalize()+' created'}), 201
    else:
        return jsonify({'message': 'Failed to create '+model.table_name}), 500
@indikator_bp.route('/api/'+model.table_name+'/<string:id>', methods=['PUT'])
def update(id):
    data=validasiInput()
    if not isinstance(data,list):return data
    instansi = model.getById(id)
    if instansi:
        if model.update( data[0],data[1],data[2],data[3],id):
            return jsonify({'message': model.table_name.capitalize()+' updated'})
        else:
            return jsonify({'message': 'Failed to update '+model.table_name}), 500
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404

@indikator_bp.route('/api/'+model.table_name+'/<string:id>', methods=['DELETE'])
def delete_user(id):
    instansi = model.getById(id)
    if instansi:
        if model.delete(id):
            return jsonify({'message': model.table_name.capitalize()+' deleted'})
        else:
            return jsonify({'message': 'Failed to delete '+model.table_name}), 500
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404
@indikator_bp.route('/api/'+model.table_name+'/aspek/<string:aspek>')
def get_all_by_aspek(aspek):
    return jsonify(model.getAllByAspek(aspek));
@indikator_bp.route('/api/'+model.table_name+'/domain')
def get_all_domain():
    return jsonify(model.getAllDomain());
@indikator_bp.route('/api/'+model.table_name+'/domain/<string:domain>')
def get_all_aspek(domain):
    return jsonify(model.getAllAspek(domain));