from flask import Blueprint,jsonify,request
from app.models.instansi import instansiModel
model=instansiModel();
instansi_bp=Blueprint('instansi',__name__)
@instansi_bp.route('/instansi')
def get_all():
    return jsonify(model.getAll());
@instansi_bp.route('/instansi/<string:id>')
def get_by_id(id):
    instansi = model.getById(id)
    if instansi:
        return jsonify(instansi)
    else:
        return jsonify({'message': 'Instansi not found'}), 404
@instansi_bp.route('/instansi',methods=['POST'])
def create():
    nama = request.json.get('nama')
    if not nama:
        return jsonify({'message': 'Nama is required'}), 400
    if model.create(nama):
        return jsonify({'message': 'Instansi created'}), 201
    else:
        return jsonify({'message': 'Failed to create user'}), 500
@instansi_bp.route('/instansi/<string:id>', methods=['PUT'])
def update(id):
    nama = request.json.get('nama')
    if not nama:
        return jsonify({'message': 'Nama is required'}), 400

    instansi = model.getById(id)
    if instansi:
        if model.update( nama,id):
            return jsonify({'message': 'Instansi updated'})
        else:
            return jsonify({'message': 'Failed to update instansi'}), 500
    else:
        return jsonify({'message': 'Instansi not found'}), 404

@instansi_bp.route('/instansi/<string:id>', methods=['DELETE'])
def delete_user(id):
    instansi = model.getById(id)
    if instansi:
        if model.delete(id):
            return jsonify({'message': 'Instansi deleted'})
        else:
            return jsonify({'message': 'Failed to delete instansi'}), 500
    else:
        return jsonify({'message': 'Instansi not found'}), 404
