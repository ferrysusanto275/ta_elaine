from flask import Blueprint,jsonify,request
from app.models.keluaran import keluaranModel
from app.models.isi import isiModel
model=keluaranModel()
isi=isiModel()
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
@keluaranbp.route('/api/'+model.table_name+"/df_all/<string:area>")
def get_all_df(area):
    data_area=model.getAllInstansiby_Area(area);
    data_indikator=model.getAllIndikatorby_Area(area)
    df=isi.getDfAllIndikator()
    df=df[df['id'].astype('str').isin(data_area)]
    # features = df[data_indikator]
    # K = range(2,6)
    # inertia = []
    # silhouette_coef = [] 
    # model = [] 
    # for k in K:
    #     kmeans= KMeans(n_clusters=k, random_state=42)
    #     kmeans.fit(features)
    #     model.append(kmeans)
    #     inertia.append(kmeans.inertia_)
    #     score = silhouette_score(features, kmeans.labels_, metric='euclidean')
    #     silhouette_coef.append(score)
    # best_num_clusters = model[np.argmax(silhouette_coef)]
    print(df)
    # return {"inertia":inertia,"silhouette_coef":silhouette_coef,'best_model':best_num_clusters,'df':df}
    return jsonify(data_indikator);  