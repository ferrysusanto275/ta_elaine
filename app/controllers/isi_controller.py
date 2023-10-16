from flask import Blueprint,jsonify,request
from app.models.instansi import instansiModel
from app.models.indikator import indikatorModel
from app.models.isi import isiModel
model=isiModel()
instansi_model=instansiModel()
indikator_model=indikatorModel()
isi_bp=Blueprint(model.table_name,__name__)
def validasiId(instansi,indikator):
    if not instansi:
        return jsonify({'message': 'Instansi is required'}), 400
    cekInstansi=instansi_model.getById(instansi)
    if not cekInstansi:
        return jsonify({'message': 'Instansi not found'}), 400
    if not indikator:
        return jsonify({'message': 'Indikator is required'}), 400
    cekIndikator=indikator_model.getById(indikator)
    if not cekIndikator:
        return jsonify({'message': 'Indikator not found'}), 400
    return[instansi,indikator]
def validasiInput():
    instansi = request.json.get('instansi')
    indikator = request.json.get('indikator')
    id=validasiId(instansi,indikator)
    if not isinstance(id,list): return id
    value = validasiValue();
    if not isinstance(value,list): return value
    return [instansi,indikator,value[0]]
def validasiValue():
    value = request.json.get('value')
    if not value:
        return jsonify({'message': 'Value is required'}), 400
    # cek value number atau bukan
    if not isinstance(value, (int, float, complex)):
        return jsonify({'message': 'Value is must number'}), 400
    return [value]

@isi_bp.route('/'+model.table_name)
def get_all():
    return jsonify(model.getAll());
@isi_bp.route('/'+model.table_name+'/<string:instansi>/<string:indikator>')
def get_by_id(instansi,indikator):
    isi = model.getById(instansi,indikator)
    if isi:
        return jsonify(isi)
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404
@isi_bp.route('/'+model.table_name,methods=['POST'])
def create():
    data=validasiInput()
    if not isinstance(data,list):return data
    if model.create(instansi=data[0],indikator=data[1],value=data[2]):
        return jsonify({'message': model.table_name.capitalize()+' created'}), 201
    else:
        return jsonify({'message': 'Failed to create '+model.table_name}), 500
@isi_bp.route('/'+model.table_name+'/<string:instansi>'+'/<string:indikator>', methods=['PUT'])
def update(instansi,indikator):
    id=validasiId(instansi,indikator)
    if not isinstance(id,list):return id
    data=validasiValue()
    if not isinstance(data,list):return data
    instansi = model.getById(id)
    if instansi:
        if model.update( instansi=id[0],indikator=id[1],value=data[0]):
            return jsonify({'message': model.table_name.capitalize()+' updated'})
        else:
            return jsonify({'message': 'Failed to update '+model.table_name}), 500
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404

@isi_bp.route('/'+model.table_name+'/<string:instansi>/<string:indikator>', methods=['DELETE'])
def delete_user(instansi,indikator):
    instansi = model.getById(instansi,indikator)
    if instansi:
        if model.delete(id):
            return jsonify({'message': model.table_name.capitalize()+' deleted'})
        else:
            return jsonify({'message': 'Failed to delete '+model.table_name}), 500
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404
