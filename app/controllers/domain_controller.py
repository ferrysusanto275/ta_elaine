from flask import Blueprint,jsonify,request
from app.models.domain import domainModel
from app.models.aspek import aspekModel
model=domainModel();
aspek_model=aspekModel();
domain_bp=Blueprint(model.table_name,__name__)
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
    return [nama,bobot]
@domain_bp.route('/'+model.table_name)
def get_all():
    return jsonify(model.getAll());
@domain_bp.route('/index_'+model.table_name+'/<string:instansi>')
def get_all():
    return jsonify(model.getAll());
@domain_bp.route('/'+model.table_name+'/<string:id>')
def get_by_id(id):
    instansi = model.getById(id)
    if instansi:
        return jsonify(instansi)
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404
@domain_bp.route('/'+model.table_name,methods=['POST'])
def create():
    data=validasiInput()
    if not isinstance(data,list):return data
    if model.create(data[0],data[1]):
        return jsonify({'message': model.table_name.capitalize()+' created'}), 201
    else:
        return jsonify({'message': 'Failed to create '+model.table_name}), 500
@domain_bp.route('/'+model.table_name+'/<string:id>', methods=['PUT'])
def update(id):
    data=validasiInput()
    if not isinstance(data,list):return data
    instansi = model.getById(id)
    if instansi:
        if model.update( data[0],data[1],id):
            return jsonify({'message': model.table_name.capitalize()+' updated'})
        else:
            return jsonify({'message': 'Failed to update '+model.table_name}), 500
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404

@domain_bp.route('/'+model.table_name+'/<string:id>', methods=['DELETE'])
def delete_user(id):
    instansi = model.getById(id)
    if instansi:
        if model.delete(id):
            return jsonify({'message': model.table_name.capitalize()+' deleted'})
        else:
            return jsonify({'message': 'Failed to delete '+model.table_name}), 500
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404
