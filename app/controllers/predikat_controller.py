from flask import Blueprint,jsonify,request
from app.models.predikat import predikat_model
model=predikat_model()
def validasiInput():
    nama = request.json.get('nama')
    if not nama:
        return jsonify({'message': 'Nama is required'}), 400
    batas_bawah = request.json.get('batas_bawah')
    if not batas_bawah:
        return jsonify({'message': 'batas bawah is required'}), 400
        # cek value number atau bukan
    if not isinstance(batas_bawah, (int, float, complex)):
        return jsonify({'message': 'Batas bawah is must number'}), 400
    return [nama, batas_bawah]
predikat_bp=Blueprint(model.table_name,__name__)
@predikat_bp.route('/api/'+model.table_name)
def get_all():
    return jsonify(model.getAll());
@predikat_bp.route('/api/'+model.table_name+'/<string:id>')
def get_by_id(id):
    predikat = model.getById(id)
    if predikat:
        return jsonify(predikat)
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404
@predikat_bp.route('/api/'+model.table_name,methods=['POST'])
def create():
    data=validasiInput()
    if not isinstance(data,list):return data
    if model.create(data[0], data[1]):
        return jsonify({'message': model.table_name.capitalize()+' created'}), 201
    else:
        return jsonify({'message': 'Failed to create '+model.table_name}), 500
@predikat_bp.route('/api/'+model.table_name+'/<string:id>', methods=['PUT'])
def update(id):
    data=validasiInput()
    if not isinstance(data,list):return data
    predikat = model.getById(id)
    if predikat:
        if model.update( data[0],id, data[1]):
            return jsonify({'message': model.table_name.capitalize()+' updated'})
        else:
            return jsonify({'message': 'Failed to update '+model.table_name}), 500
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404

@predikat_bp.route('/api/'+model.table_name+'/<string:id>', methods=['DELETE'])
def delete_user(id):
    predikat = model.getById(id)
    if predikat:
        if model.delete(id):
            return jsonify({'message': model.table_name.capitalize()+' deleted'})
        else:
            return jsonify({'message': 'Failed to delete '+model.table_name}), 500
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404
