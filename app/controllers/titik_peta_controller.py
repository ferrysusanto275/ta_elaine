from flask import Blueprint,jsonify,request
from app.models.titik_peta import titik_petaModel
model=titik_petaModel()
# def validasiInput():
#     nama = request.json.get('nama')
#     if not nama:
#         return jsonify({'message': 'Nama is required'}), 400
#     return [nama]
titik_peta_bp=Blueprint(model.table_name,__name__)
@titik_peta_bp.route('/api/'+model.table_name)
def get_all():
    return jsonify(model.getAll());
# @grup_instansi_bp.route('/api/'+model.table_name+'/<string:id>')
# def get_by_id(id):
#     grup_instansi = model.getById(id)
#     if grup_instansi:
#         return jsonify(grup_instansi)
#     else:
#         return jsonify({'message': model.table_name.capitalize()+' not found'}), 404
# @grup_instansi_bp.route('/api/'+model.table_name,methods=['POST'])
# def create():
#     data=validasiInput()
#     if not isinstance(data,list):return data
#     if model.create(data[0]):
#         return jsonify({'message': model.table_name.capitalize()+' created'}), 201
#     else:
#         return jsonify({'message': 'Failed to create '+model.table_name}), 500
# @grup_instansi_bp.route('/api/'+model.table_name+'/<string:id>', methods=['PUT'])
# def update(id):
#     data=validasiInput()
#     if not isinstance(data,list):return data
#     grup_instansi = model.getById(id)
#     if grup_instansi:
#         if model.update( data[0],id):
#             return jsonify({'message': model.table_name.capitalize()+' updated'})
#         else:
#             return jsonify({'message': 'Failed to update '+model.table_name}), 500
#     else:
#         return jsonify({'message': model.table_name.capitalize()+' not found'}), 404

# @grup_instansi_bp.route('/api/'+model.table_name+'/<string:id>', methods=['DELETE'])
# def delete_user(id):
#     grup_instansi = model.getById(id)
#     if grup_instansi:
#         if model.delete(id):
#             return jsonify({'message': model.table_name.capitalize()+' deleted'})
#         else:
#             return jsonify({'message': 'Failed to delete '+model.table_name}), 500
#     else:
#         return jsonify({'message': model.table_name.capitalize()+' not found'}), 404
