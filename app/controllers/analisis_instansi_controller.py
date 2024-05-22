from flask import Blueprint,jsonify,request
from app.models.analisis_instansi import analisis_instansiModel
model=analisis_instansiModel()
grup_analisis_instansibp=Blueprint(model.table_name,__name__)
def validasiInput():
    analisis = request.json.get('analisis')
    if not analisis:
        return jsonify({'message': 'analisis is required'}), 400
    instansi = request.json.get('instansi')
    if not instansi:
        return jsonify({'message': 'instansi is required'}), 400
    return [analisis,instansi]
@grup_analisis_instansibp.route('/api/'+model.table_name)
def get_all():
    return jsonify(model.getAll());
@grup_analisis_instansibp.route('/api/'+model.table_name+'/<string:analisis>')
def get_all_instansi_analisis(analisis):
    return jsonify(model.getAllByAnalisis(analisis));
@grup_analisis_instansibp.route('/api/'+model.table_name,methods=['POST'])
def create():
    data=validasiInput()
    instansi = model.getById(data[0], data[1])
    if(instansi):
        return jsonify({'message': 'Data sudah pernah dimasukkan'})
    if not isinstance(data,list):return data
    if model.create(data[0],data[1]):
        return jsonify({'message': model.table_name.capitalize()+' created'}), 201
    else:
        return jsonify({'message': 'Failed to create '+model.table_name}), 500
# @grup_analisis_instansibp.route('/api/'+model.table_name+'/<string:id>', methods=['PUT'])
# def update(id):
#     data=validasiInput()
#     if not isinstance(data,list)py:return data
#     instansi = model.getById(id)
#     if instansi:
#         if model.update( data[0],id):
#             return jsonify({'message': model.table_name.capitalize()+' updated'})
#         else:
#             return jsonify({'message': 'Failed to update '+model.table_name}), 500
#     else:
#         return jsonify({'message': model.table_name.capitalize()+' not found'}), 404

@grup_analisis_instansibp.route('/api/'+model.table_name+'/<string:analisis>/<string:instansi>', methods=['DELETE'])
def delete_user(analisis, instansi):
    cek = model.getById(analisis, instansi)
    if cek:
        if model.delete(analisis, instansi):
            return jsonify({'message': model.table_name.capitalize()+' deleted'})
        else:
            return jsonify({'message': 'Failed to delete '+model.table_name}), 500
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404
