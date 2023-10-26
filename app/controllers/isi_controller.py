from flask import Blueprint,jsonify,request
from app.models.instansi import instansiModel
from app.models.indikator import indikatorModel
from app.models.isi import isiModel
model=isiModel()
instansi_model=instansiModel()
indikator_model=indikatorModel()
isi_bp=Blueprint(model.table_name,__name__)
def validasiId(instansi,indikator,year):
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
    if not year:
        return jsonify({'message': 'Year is required'}), 400
    # cek value number atau bukan
    if not isinstance(year, (int, float, complex)):
        return jsonify({'message': 'Year is must number'}), 400
    return[instansi,indikator,year]
def validasiInput():
    instansi = request.json.get('instansi')
    indikator = request.json.get('indikator')
    year = request.json.get('year')
    id=validasiId(instansi,indikator,year)
    if not isinstance(id,list): return id
    value = validasiValue();
    if not isinstance(value,list): return value
    return [instansi,indikator,value[0],year]
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
@isi_bp.route('/api/'+model.table_name+'/<string:instansi>/<string:indikator>/<string:year>')
def get_by_id(instansi,indikator,year):
    isi = model.getById(instansi,indikator,year)
    if isi:
        return jsonify(isi)
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404
@isi_bp.route('/api/'+model.table_name,methods=['POST'])
def create():
    data=validasiInput()
    if not isinstance(data,list):return data
    cekisi = model.getById(instansi=data[0],indikator=data[1],year=data[3])
    # print(data)
    # return jsonify(cekisi)
    if not cekisi:
        if model.create(instansi=data[0],indikator=data[1],value=data[2],year=data[3]):
            return jsonify({'message': model.table_name.capitalize()+' created'}), 201
        else:
            return jsonify({'message': 'Failed to create '+model.table_name}), 500
    else:
        return jsonify({'message': model.table_name.capitalize()+' is already available'}), 500
@isi_bp.route('/api/'+model.table_name+'/<string:instansi>/<string:indikator>/<string:year>', methods=['PUT'])
def update(instansi,indikator,year):
    id=validasiId(instansi,indikator,year)
    if not isinstance(id,list):return id
    data=validasiValue()
    if not isinstance(data,list):return data
    isi = model.getById(instansi,indikator,year)
    if isi:
        if model.update( instansi,indikator,year ,data[0]):
            return jsonify({'message': model.table_name.capitalize()+' updated'})
        else:
            return jsonify({'message': 'Failed to update '+model.table_name}), 500
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404

@isi_bp.route('/api/'+model.table_name+'/<string:instansi>/<string:indikator>/<string:year>', methods=['DELETE'])
def delete_user(instansi,indikator,year):
    isi = model.getById(instansi,indikator,year)
    if isi:
        if model.delete(id):
            return jsonify({'message': model.table_name.capitalize()+' deleted'})
        else:
            return jsonify({'message': 'Failed to delete '+model.table_name}), 500
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404
@isi_bp.route('/api/year')
def get_allYear():
    return jsonify(model.getAllYear());