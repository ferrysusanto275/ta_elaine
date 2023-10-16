from flask import Blueprint,jsonify,request
from app.models.domain import domainModel
model=domainModel();
instansi_bp=Blueprint(model.table_name,__name__)
@instansi_bp.route('/'+model.table_name)
def get_all():
    return jsonify(model.getAll());
@instansi_bp.route('/'+model.table_name+'/<string:id>')
def get_by_id(id):
    instansi = model.getById(id)
    if instansi:
        return jsonify(instansi)
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404
@instansi_bp.route('/'+model.table_name,methods=['POST'])
def create():
    nama = request.json.get('nama')
    if not nama:
        return jsonify({'message': 'Nama is required'}), 400
    if model.create(nama):
        return jsonify({'message': model.table_name.capitalize()+' created'}), 201
    else:
        return jsonify({'message': 'Failed to create '+model.table_name}), 500
@instansi_bp.route('/'+model.table_name+'/<string:id>', methods=['PUT'])
def update(id):
    nama = request.json.get('nama')
    if not nama:
        return jsonify({'message': 'Nama is required'}), 400

    instansi = model.getById(id)
    if instansi:
        if model.update( nama,id):
            return jsonify({'message': model.table_name.capitalize()+' updated'})
        else:
            return jsonify({'message': 'Failed to update '+model.table_name}), 500
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404

@instansi_bp.route('/'+model.table_name+'/<string:id>', methods=['DELETE'])
def delete_user(id):
    instansi = model.getById(id)
    if instansi:
        if model.delete(id):
            return jsonify({'message': model.table_name.capitalize()+' deleted'})
        else:
            return jsonify({'message': 'Failed to delete '+model.table_name}), 500
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404
