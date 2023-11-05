from flask import Blueprint,jsonify,request
from app.models.aspek import aspekModel
from app.models.domain import domainModel
from app.models.instansi import instansiModel
model=aspekModel()
domain_model=domainModel()
instansi_model=instansiModel()
aspek_bp=Blueprint(model.table_name,__name__)
def validasiInput():
    nama = request.json.get('nama')
    if not nama:
        return jsonify({'message': 'Nama is required'}), 400
    bobot = request.json.get('bobot')
    if not bobot:
        return jsonify({'message': 'Bobot is required'}), 400
    # cek bobot number atau bukan
    if not isinstance(bobot, (int, float, complex)):
        return jsonify({'message': 'Bobot is must number'}), 400
    domain = request.json.get('domain')
    if not domain:
        return jsonify({'message': 'Domain is required'}), 400
    cekDomain=domain_model.getById(domain)
    if not cekDomain:
        return jsonify({'message': 'Domain not found'}), 400
    return [nama,bobot,domain]
# @aspek_bp.route('/api/index_'+model.table_name+'/<string:instansi>/<string:year>/<string:domain>')
# def get_by_index(domain,instansi,year):
#     if not domain:
#         return jsonify({'message': 'domain is required'}), 400
#     cekDomain=domain_model.getById(domain)
#     if not cekDomain:
#         return jsonify({'message': 'Domain not found'}), 400
#     if not instansi:
#         return jsonify({'message': 'Domain is required'}), 400
#     cekInstansi=instansi_model.getById(instansi)
#     if not cekInstansi:
#         return jsonify({'message': 'Instansi not found'}), 400
#     if not year:
#         return jsonify({'message': 'Year is required'}), 400
#     if not isinstance(year, (int, float, complex)):
#         return jsonify({'message': 'Year is must number'}), 400
#     aspek = model.getAll_byIndex(domain=domain,instansi=instansi,year=year)
#     if aspek:
#         return jsonify(aspek)
#     else:
#         return jsonify({'message': model.table_name.capitalize()+' not found'}), 404
@aspek_bp.route('/api/'+model.table_name)
def get_all():
    return jsonify(model.getAll());
@aspek_bp.route('/api/'+model.table_name+'/<string:id>')
def get_by_id(id):
    instansi = model.getById(id)
    if instansi:
        return jsonify(instansi)
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404
@aspek_bp.route('/api/'+model.table_name,methods=['POST'])
def create():
    data=validasiInput()
    if not isinstance(data,list):return data
    if model.create(data[0],data[1],data[2]):
        return jsonify({'message': model.table_name.capitalize()+' created'}), 201
    else:
        return jsonify({'message': 'Failed to create '+model.table_name}), 500
@aspek_bp.route('/api/'+model.table_name+'/<string:id>', methods=['PUT'])
def update(id):
    data=validasiInput()
    if not isinstance(data,list):return data
    instansi = model.getById(id)
    if instansi:
        if model.update( data[0],data[1],data[2],id):
            return jsonify({'message': model.table_name.capitalize()+' updated'})
        else:
            return jsonify({'message': 'Failed to update '+model.table_name}), 500
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404

@aspek_bp.route('/api/'+model.table_name+'/<string:id>', methods=['DELETE'])
def delete_user(id):
    instansi = model.getById(id)
    if instansi:
        if model.delete(id):
            return jsonify({'message': model.table_name.capitalize()+' deleted'})
        else:
            return jsonify({'message': 'Failed to delete '+model.table_name}), 500
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404
@aspek_bp.route('/api/'+model.table_name+'/domain/<string:domain>')
def get_all_by_domain(domain):
    return jsonify(model.getAllByDomain(domain));
