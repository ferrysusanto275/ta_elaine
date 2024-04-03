from flask import Blueprint,jsonify,request
from app.models.keluaran import keluaranModel
model=keluaranModel()
keluaranbp=Blueprint(model.table_name,__name__)
def validasiInput():
    nama = request.json.get('nama')
    if not nama:
        return jsonify({'message': 'Nama is required'}), 400
    grup = request.json.get('grup')
    if not grup:
        return jsonify({'message': 'grup is required'}), 400
    return [nama,grup]
@keluaranbp.route('/api/'+model.table_name)
def get_all():
    return jsonify(model.getAll());
@keluaranbp.route('/api/'+model.table_name+'/inisiatif/<string:grup>')
def get_all_analisis_grup(grup):
    return jsonify(model.getAllByGrup(grup));
@keluaranbp.route('/api/'+model.table_name+'/<string:id>')
def get_by_id(id):
    grup_analisis = model.getById(id)
    if grup_analisis:
        return jsonify(grup_analisis)
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404
@keluaranbp.route('/api/'+model.table_name,methods=['POST'])
def create():
    data=validasiInput()
    if not isinstance(data,list):return data
    if model.create(data[0], data[1]):
        return jsonify({'message': model.table_name.capitalize()+' created'}), 201
    else:
        return jsonify({'message': 'Failed to create '+model.table_name}), 500
@keluaranbp.route('/api/'+model.table_name+'/<string:id>', methods=['PUT'])
def update(id):
    data=validasiInput()
    print(data)
    if not isinstance(data,list):return data
    instansi = model.getById(id)
    if instansi:
        if model.update( data[0],data[1],id):
            return jsonify({'message': model.table_name.capitalize()+' updated'})
        else:
            return jsonify({'message': 'Failed to update '+model.table_name}), 500
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404

@keluaranbp.route('/api/'+model.table_name+'/<string:id>', methods=['DELETE'])
def delete_user(id):
    instansi = model.getById(id)
    if instansi:
        if model.delete(id):
            return jsonify({'message': model.table_name.capitalize()+' deleted'})
        else:
            return jsonify({'message': 'Failed to delete '+model.table_name}), 500
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404
