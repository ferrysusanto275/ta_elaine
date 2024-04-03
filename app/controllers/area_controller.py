from flask import Blueprint,jsonify,request
from app.models.area import areaModel
model=areaModel();
area_bp=Blueprint(model.table_name,__name__)
def validasiInput():
    nama = request.json.get('nama')
    if not nama:
        return jsonify({'message': 'Nama is required'}), 400
    return [nama]
@area_bp.route('/api/'+model.table_name)
def get_all():
    return jsonify(model.getAll());
@area_bp.route('/api/'+model.table_name+'/<string:id>')
def get_by_id(id):
    area = model.getById(id)
    if area:
        return jsonify(area)
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404
@area_bp.route('/api/'+model.table_name,methods=['POST'])
def create():
    data=validasiInput()
    if not isinstance(data,list):return data
    if model.create(data[0]):
        return jsonify({'message': model.table_name.capitalize()+' created'}), 201
    else:
        return jsonify({'message': 'Failed to create '+model.table_name}), 500
@area_bp.route('/api/'+model.table_name+'/<string:id>', methods=['PUT'])
def update(id):
    data=validasiInput()
    if not isinstance(data,list):return data
    instansi = model.getById(id)
    if instansi:
        if model.update( data[0],id):
            return jsonify({'message': model.table_name.capitalize()+' updated'})
        else:
            return jsonify({'message': 'Failed to update '+model.table_name}), 500
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404

@area_bp.route('/api/'+model.table_name+'/<string:id>', methods=['DELETE'])
def delete_user(id):
    instansi = model.getById(id)
    if instansi:
        if model.delete(id):
            return jsonify({'message': model.table_name.capitalize()+' deleted'})
        else:
            return jsonify({'message': 'Failed to delete '+model.table_name}), 500
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404
