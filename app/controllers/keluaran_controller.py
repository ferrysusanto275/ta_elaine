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
    penanggung_jawab = request.json.get('penanggung_jawab')
    if not penanggung_jawab:
        return jsonify({'message': 'penanggung_jawab is required'}), 400
    target_tahun = request.json.get('target_tahun')
    if not target_tahun:
        return jsonify({'message': 'target_tahun is required'}), 400
    return [nama,penanggung_jawab, target_tahun, grup]
@keluaranbp.route('/api/'+model.table_name)
def get_all():
    return jsonify(model.getAll());
@keluaranbp.route('/api/'+model.table_name+"/indikator/<string:area>")
def get_all_indikator(area):
    return jsonify(model.getAllIndikatorby_Area(area=area));
@keluaranbp.route('/api/'+model.table_name+"/res_kmeans/<string:area>/<string:year>")
def get_res_kmeans_areaByYear(area,year):
    df_dict = model.getDfK(area,year).to_dict(orient='records')
    return jsonify(df_dict)
@keluaranbp.route('/api/'+model.table_name+"/res_kmeans_bobot/<string:area>/<string:year>")
def get_res_kmeans_areaByYear_bobot(area,year):
    df_dict = model.getDfK_bobot(area,year).to_dict(orient='records')
    return jsonify(df_dict)
@keluaranbp.route('/api/'+model.table_name+"/res_agglo/<string:area>/<string:year>/<string:linkage>")
def get_res_agglo_areaByYear(area,year,linkage):
    df_dict = model.getDfAByareaYear(area,year,linkage).to_dict(orient='records')
    return jsonify(df_dict)

    # return jsonify(data_indikator);  
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
    if model.create(data[0], data[1], data[2], data[3]):
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
        if model.update( data[0], data[1], data[2], data[3],id):
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
