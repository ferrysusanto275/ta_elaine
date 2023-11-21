from flask import Blueprint,jsonify,request,render_template,Response
from app.models.grup_instansi import grup_instansiModel
from app.models.instansi import instansiModel
from app.models.indikator import indikatorModel
from app.models.aspek import aspekModel
from app.models.domain import domainModel
from app.models.isi import isiModel
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import io

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
model=isiModel()
aspek_model=aspekModel()
instansi_model=instansiModel()
indikator_model=indikatorModel()
gi_model=grup_instansiModel()
domain_model=domainModel()
isi_bp=Blueprint(model.table_name,__name__, template_folder='views')
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
    # if not isinstance(year, (int, float, complex)):
    #     return jsonify({'message': 'Year is must number'}), 400
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

@isi_bp.route('/api/'+model.table_name)
def get_all():
    return jsonify(model.getAll());
@isi_bp.route('/api/'+model.table_name+'/<string:instansi>/<string:indikator>/<string:year>')
def get_by_id(instansi,indikator,year):
    isi = model.getById(instansi,indikator,year)
    if isi:
        return jsonify(isi)
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404
@isi_bp.route('/api/'+model.table_name+'/by_aspek/<string:instansi>/<string:domain>/<string:year>')
def get_by_aspek_instansi(instansi,domain,year):
    isi = model.getAllAspekByInstansi(instansi,domain,year)
    if isi:
        return jsonify(isi)
    else:
        return jsonify({'message': model.table_name.capitalize()+' not found'}), 404
@isi_bp.route('/api/'+model.table_name+'/by_domain/<string:instansi>/<string:year>')
def get_by_domain_instansi(instansi,year):
    isi = model.getAllDomainByInstansi(instansi,year)
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
@isi_bp.route('/api/'+model.table_name+'/aspek/<string:instansi>/<string:aspek>/<string:year>')
def getAllbyYearInstansiAspek(year,aspek,instansi):
    return jsonify(model.getAllbyYearInstansiAspek(year,aspek,instansi));
# @isi_bp.route('/api/'+model.table_name+'/<string:indikator1>/<string:indikator2>/grup/<string:gi>')
# def getPerbandingan(indikator1,indikator2,gi):
#     data_gi=gi_model.getById(gi)
#     if('id' not in data_gi):
#         return jsonify({'message': model.table_name.capitalize()+' grup found'}), 404
@isi_bp.route('/api/'+model.table_name+'/<string:indikator1>/<string:indikator2>')
def getPerbandingan(indikator1,indikator2):
    
    dataIndikator1=indikator_model.getById(indikator1)
    if(dataIndikator1 is None):
        return jsonify({'message': model.table_name.capitalize()+' Indikator 1 not found'}), 404
    dataIndikator2=indikator_model.getById(indikator2)
    if(dataIndikator2 is None):
        return jsonify({'message': model.table_name.capitalize()+' Indikator 2 not found'}), 404
    dfIndikator1=model.getAllValue(indikator1)
    dfIndikator2=model.getAllValue(indikator2)
    fig, ax = plt.subplots()
    ax.scatter(dfIndikator1,dfIndikator2,alpha=0.5)
    ax.set_xlabel(dataIndikator1['name'])
    ax.set_ylabel(dataIndikator2['name'])
    ax.set_title(dataIndikator1['name']+" VS "+dataIndikator2['name'])
   # Menggunakan BytesIO untuk menangkap output plot sebagai byte stream
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    # Membuat respons HTTP dengan gambar sebagai byte stream
    return Response(output.getvalue(), mimetype='image/png')
# @isi_bp.route('/api/'+model.table_name+'/aspek/<string:aspek1>/<string:aspek2>/grup/<string:gi>')
# def getPerbandinganAspek(aspek1,aspek2,gi):
#     data_gi=gi_model.getById(gi)
#     if(data_gi is None):
#         return jsonify({'message': model.table_name.capitalize()+' group not found'}), 404
@isi_bp.route('/api/'+model.table_name+'/aspek/<string:aspek1>/<string:aspek2>')
def getPerbandinganAspek(aspek1,aspek2):
    dataAspek1=aspek_model.getById(aspek1)
    if(dataAspek1 is None):
        return jsonify({'message': model.table_name.capitalize()+' Aspek 1 not found'}), 404
    dataAspek2=aspek_model.getById(aspek2)
    if(dataAspek2 is None):
        return jsonify({'message': model.table_name.capitalize()+' Aspek 2 not found'}), 404
    dfAspek1=model.getAllAspek(aspek1)
    dfAspek2=model.getAllAspek(aspek2)
    fig, ax = plt.subplots()
    ax.scatter(dfAspek1,dfAspek2,alpha=0.5)
    ax.set_xlabel(dataAspek1['name'])
    ax.set_ylabel(dataAspek2['name'])
    ax.set_title(dataAspek1['name']+" VS "+dataAspek2['name'])
   # Menggunakan BytesIO untuk menangkap output plot sebagai byte stream
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    # Membuat respons HTTP dengan gambar sebagai byte stream
    return Response(output.getvalue(), mimetype='image/png')
# @isi_bp.route('/api/'+model.table_name+'/aspek_indikator/<string:aspek>/<string:indikator>/grup/<string:gi>')
# def getPerbandinganAspekIndikator(aspek,indikator,gi):
#     data_gi=gi_model.getById(gi)
#     if(data_gi is None):
#         return jsonify({'message': model.table_name.capitalize()+' group not found'}), 404
@isi_bp.route('/api/'+model.table_name+'/aspek_indikator/<string:aspek>/<string:indikator>')
def getPerbandinganAspekIndikator(aspek,indikator):
    dataAspek=aspek_model.getById(aspek)
    if(dataAspek is None):
        return jsonify({'message': model.table_name.capitalize()+' Aspek not found'}), 404
    dataIndikator=indikator_model.getById(indikator)
    if(dataIndikator is None):
        return jsonify({'message': model.table_name.capitalize()+' Indikator 1 not found'}), 404
    dfAspek=model.getAllAspek(aspek)
    dfIndikator=model.getAllValue(indikator)
    fig, ax = plt.subplots()
    ax.scatter(dfAspek,dfIndikator,alpha=0.5)
    ax.set_xlabel(dataAspek['name'])
    ax.set_ylabel(dataIndikator['name'])
    ax.set_title(dataAspek['name']+" VS "+dataIndikator['name'])
   # Menggunakan BytesIO untuk menangkap output plot sebagai byte stream
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    # Membuat respons HTTP dengan gambar sebagai byte stream
    return Response(output.getvalue(), mimetype='image/png')
# @isi_bp.route('/api/'+model.table_name+'/domain/<string:domain1>/<string:domain2>/grup/<string:gi>')
# def getPerbandinganDomain(domain1,domain2,gi):
#     data_gi=gi_model.getById(gi)
#     if(data_gi is None):
#         return jsonify({'message': model.table_name.capitalize()+' group not found'}), 404
@isi_bp.route('/api/'+model.table_name+'/domain/<string:domain1>/<string:domain2>')
def getPerbandinganDomain(domain1,domain2):
    dataDomain1=domain_model.getById(domain1)
    if(dataDomain1 is None):
        return jsonify({'message': model.table_name.capitalize()+' Domain 1 not found'}), 404
    dataDomain2=domain_model.getById(domain2)
    if(dataDomain2 is None):
        return jsonify({'message': model.table_name.capitalize()+' Domaian 2 not found'}), 404
    dfDomain1=model.getAllDomain(domain1)
    dfDomain2=model.getAllDomain(domain2)
    fig, ax = plt.subplots()
    ax.scatter(dfDomain1,dfDomain2,alpha=0.5)
    ax.set_xlabel(dataDomain1['name'])
    ax.set_ylabel(dataDomain2['name'])
    ax.set_title(dataDomain1['name']+" VS "+dataDomain2['name'])
   # Menggunakan BytesIO untuk menangkap output plot sebagai byte stream
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    # Membuat respons HTTP dengan gambar sebagai byte stream
    return Response(output.getvalue(), mimetype='image/png')

# @isi_bp.route('/api/'+model.table_name+'/domain_aspek/<string:domain>/<string:aspek>/grup/<string:gi>')
# def getPerbandinganDomainAspek(domain,aspek,gi):
#     data_gi=gi_model.getById(gi)
#     if(data_gi is None):
#         return jsonify({'message': model.table_name.capitalize()+' group not found'}), 404
@isi_bp.route('/api/'+model.table_name+'/domain_aspek/<string:domain>/<string:aspek>')
def getPerbandinganDomainAspek(domain,aspek):
    dataDomain=domain_model.getById(domain)
    if(dataDomain is None):
        return jsonify({'message': model.table_name.capitalize()+' Domain not found'}), 404
    dataAspek=aspek_model.getById(aspek)
    if(dataAspek is None):
        return jsonify({'message': model.table_name.capitalize()+' Aspek not found'}), 404
    dfDomain=model.getAllDomain(domain)
    dfAspek=model.getAllAspek(aspek)
    fig, ax = plt.subplots()
    ax.scatter(dfDomain,dfAspek,alpha=0.5)
    ax.set_xlabel(dataAspek['name'])
    ax.set_ylabel(dataDomain['name'])
    ax.set_title(dataAspek['name']+" VS "+dataDomain['name'])
   # Menggunakan BytesIO untuk menangkap output plot sebagai byte stream
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    # Membuat respons HTTP dengan gambar sebagai byte stream
    return Response(output.getvalue(), mimetype='image/png')
@isi_bp.route('/api/'+model.table_name+'/domain_indikator/<string:domain>/<string:indikator>')
def getPerbandinganDomainIndikator(domain,indikator):
    dataDomain=domain_model.getById(domain)
    if(dataDomain is None):
        return jsonify({'message': model.table_name.capitalize()+' Domain not found'}), 404
    dataIndikator=indikator_model.getById(indikator)
    if(dataIndikator is None):
        return jsonify({'message': model.table_name.capitalize()+' Indikator not found'}), 404
    dfDomain=model.getAllDomain(domain)
    dfIndikator=model.getAllValue(indikator)
    fig, ax = plt.subplots()
    ax.scatter(dfDomain,dfIndikator,alpha=0.5)
    ax.set_xlabel(dataIndikator['name'])
    ax.set_ylabel(dataDomain['name'])
    ax.set_title(dataIndikator['name']+" VS "+dataDomain['name'])
   # Menggunakan BytesIO untuk menangkap output plot sebagai byte stream
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    # Membuat respons HTTP dengan gambar sebagai byte stream
    return Response(output.getvalue(), mimetype='image/png')
# @isi_bp.route('/api/'+model.table_name+'/index_domain/<string:domain>/grup/<string:gi>')
# def get_perbandingan_index_domain(domain,gi):
#     data_gi=gi_model.getById(gi)
#     if(data_gi is None):
#         return jsonify({'message': model.table_name.capitalize()+' group not found'}), 404
@isi_bp.route('/api/'+model.table_name+'/index_domain/<string:domain>')
def get_perbandingan_index_domain(domain):
    dataDomain=domain_model.getById(domain)
    if(dataDomain is None):
        return jsonify({'message': model.table_name.capitalize()+' Domain not found'}), 404
    dfIndex=model.getAllIndex()
    dfDomain=model.getAllDomain(domain)
    fig, ax = plt.subplots()
    ax.scatter(dfIndex,dfDomain,alpha=0.5)
    ax.set_xlabel("Index")
    ax.set_ylabel(dataDomain['name'])
    ax.set_title("Index VS "+dataDomain['name'])
   # Menggunakan BytesIO untuk menangkap output plot sebagai byte stream
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    # Membuat respons HTTP dengan gambar sebagai byte stream
    return Response(output.getvalue(), mimetype='image/png')
# @isi_bp.route('/api/'+model.table_name+'/index_aspek/<string:aspek>/grup/<string:gi>')
# def get_perbandingan_index_aspek(aspek,gi):
#     data_gi=gi_model.getById(gi)
#     if(data_gi is None):
#         return jsonify({'message': model.table_name.capitalize()+' group not found'}), 404
@isi_bp.route('/api/'+model.table_name+'/index_aspek/<string:aspek>')
def get_perbandingan_index_aspek(aspek):
    dataAspek=aspek_model.getById(aspek)
    if(dataAspek is None):
        return jsonify({'message': model.table_name.capitalize()+' Aspek not found'}), 404
    dfIndex=model.getAllIndex()
    dfAspek=model.getAllAspek(aspek)
    fig, ax = plt.subplots()
    ax.scatter(dfIndex,dfAspek,alpha=0.5)
    ax.set_xlabel("Index")
    ax.set_ylabel(dataAspek['name'])
    ax.set_title("Index VS "+dataAspek['name'])
   # Menggunakan BytesIO untuk menangkap output plot sebagai byte stream
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    # Membuat respons HTTP dengan gambar sebagai byte stream
    return Response(output.getvalue(), mimetype='image/png')
# @isi_bp.route('/api/'+model.table_name+'/index_indikator/<string:indikator>/grup/<string:gi>')
# def get_perbandingan_index_indikator(indikator,gi):
#     data_gi=gi_model.getById(gi)
#     if(data_gi is None):
#         return jsonify({'message': model.table_name.capitalize()+' group not found'}), 404
@isi_bp.route('/api/'+model.table_name+'/index_indikator/<string:indikator>')
def get_perbandingan_index_indikator(indikator):
    dataIndikator=indikator_model.getById(indikator)
    if(dataIndikator is None):
        return jsonify({'message': model.table_name.capitalize()+' Indikator not found'}), 404
    dfIndex=model.getAllIndex()
    dfIndikator=model.getAllValue(indikator)
    fig, ax = plt.subplots()
    ax.scatter(dfIndex,dfIndikator,alpha=0.5)
    ax.set_xlabel("Index")
    ax.set_ylabel(dataIndikator['name'])
    ax.set_title("Index VS "+dataIndikator['name'])
   # Menggunakan BytesIO untuk menangkap output plot sebagai byte stream
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    # Membuat respons HTTP dengan gambar sebagai byte stream
    return Response(output.getvalue(), mimetype='image/png')

# @isi_bp.route('/api/'+model.table_name+'/kmeans/<string:indikator1>/<string:indikator2>')
# def getKemeans(indikator1,indikator2):
#     data_gi=gi_model.getById()
#     if('id' not in data_gi):
#         return jsonify({'message': model.table_name.capitalize()+' grup found'}), 404
        
#     dataIndikator1=indikator_model.getById(indikator1)
#     if(dataIndikator1 is None):
#         return jsonify({'message': model.table_name.capitalize()+' Indikator 1 not found'}), 404
#     dataIndikator2=indikator_model.getById(indikator2)
#     if(dataIndikator2 is None):
#         return jsonify({'message': model.table_name.capitalize()+' Indikator 2 not found'}), 404
#     dfIndikator1=model.getAllValue(indikator1)
#     dfIndikator2=model.getAllValue(indikator2)
#     data_df=[]
#     for i,indikator in enumerate(dfIndikator1):
#         data_df.append([indikator,dfIndikator2[i]])

#     header_names=[dataIndikator1['name'],dataIndikator2['name']]
#     features = pd.DataFrame(data_df, columns=header_names)
#     K = range(2,11)
#     inertia = []
#     silhouette_coef = [] 
#     model_kmeans = [] 

#     for k in K:
#         kmeans= KMeans(n_clusters=k, random_state=42)
#         kmeans.fit(features)
#         model_kmeans.append(kmeans)
#         inertia.append(kmeans.inertia_)
#         score = silhouette_score(features, kmeans.labels_, metric='euclidean')
#         silhouette_coef.append(score)
        
#     # plot elbow method 
#     fig, ax = plt.subplots()
#     ax.plot(K, inertia, marker='o')
#     ax.set_xlabel('Jumlah kelompok k')
#     ax.set_ylabel('Inertia')
#     ax.set_title("Elbow method "+dataIndikator1['name']+" Vs "+dataIndikator2['name']+" Group "+data_gi['name'])
#    # Menggunakan BytesIO untuk menangkap output plot sebagai byte stream
#     output = io.BytesIO()
#     FigureCanvas(fig).print_png(output)

#     # Membuat respons HTTP dengan gambar sebagai byte stream
#     return Response(output.getvalue(), mimetype='image/png')
# @isi_bp.route('/api/'+model.table_name+'/kmeans_aspek/<string:aspek1>/<string:aspek2>/grup/<string:gi>')
# def getKemeansAspek(aspek1,aspek2,gi):
#     data_gi=gi_model.getById(gi)
#     if('id' not in data_gi):
#         return jsonify({'message': model.table_name.capitalize()+' grup found'}), 404
        
#     dataAspek1=aspek_model.getById(aspek1)
#     if(dataAspek1 is None):
#         return jsonify({'message': model.table_name.capitalize()+' Aspek 1 not found'}), 404
#     dataAspek2=aspek_model.getById(aspek2)
#     if(dataAspek2 is None):
#         return jsonify({'message': model.table_name.capitalize()+' Aspek 2 not found'}), 404
#     dfAspek1=model.getAllAspek(aspek1,gi)
#     dfAspek2=model.getAllAspek(aspek2,gi)
    
#     data_df=[]
#     for i,val_aspek in enumerate(dfAspek1):
#         data_df.append([val_aspek,dfAspek2[i]])
#     header_names=[dataAspek1['name'],dataAspek2['name']]
#     features = pd.DataFrame(data_df, columns=header_names)
#     K = range(2,11)
#     inertia = []
#     silhouette_coef = [] 
#     model_kmeans = [] 

#     for k in K:
#         kmeans= KMeans(n_clusters=k, random_state=42)
#         kmeans.fit(features)
#         model_kmeans.append(kmeans)
#         inertia.append(kmeans.inertia_)
#         score = silhouette_score(features, kmeans.labels_, metric='euclidean')
#         silhouette_coef.append(score)
        
#     # plot elbow method 
#     fig, ax = plt.subplots()
#     ax.plot(K, inertia, marker='o')
#     ax.set_xlabel('Jumlah kelompok k')
#     ax.set_ylabel('Inertia')
#     ax.set_title("Elbow method "+dataAspek1['name']+" Vs "+dataAspek2['name']+" Group "+data_gi['name'])
#    # Menggunakan BytesIO untuk menangkap output plot sebagai byte stream
#     output = io.BytesIO()
#     FigureCanvas(fig).print_png(output)

#     # Membuat respons HTTP dengan gambar sebagai byte stream
#     return Response(output.getvalue(), mimetype='image/png')
# @isi_bp.route('/api/'+model.table_name+'/kmeans_aspek_indikator/<string:aspek>/<string:indikator>/grup/<string:gi>')
# def getKemeansAspek_indikator(aspek,indikator,gi):
#     data_gi=gi_model.getById(gi)
#     if('id' not in data_gi):
#         return jsonify({'message': model.table_name.capitalize()+' grup found'}), 404
        
#     dataAspek=aspek_model.getById(aspek)
#     if(dataAspek is None):
#         return jsonify({'message': model.table_name.capitalize()+' Aspek not found'}), 404
#     dataIndikator=indikator_model.getById(indikator)
#     if(dataIndikator is None):
#         return jsonify({'message': model.table_name.capitalize()+' Indikator 1 not found'}), 404
#     dfAspek=model.getAllAspek(aspek,gi)
#     dfIndikator=model.getAllValue(indikator,gi)
    
#     data_df=[]
#     for i,val_aspek in enumerate(dfAspek):
#         data_df.append([val_aspek,dfIndikator[i]])
#     header_names=[dataAspek['name'],dataIndikator['name']]
#     features = pd.DataFrame(data_df, columns=header_names)
#     K = range(2,11)
#     inertia = []
#     silhouette_coef = [] 
#     model_kmeans = [] 

#     for k in K:
#         kmeans= KMeans(n_clusters=k, random_state=42)
#         kmeans.fit(features)
#         model_kmeans.append(kmeans)
#         inertia.append(kmeans.inertia_)
#         score = silhouette_score(features, kmeans.labels_, metric='euclidean')
#         silhouette_coef.append(score)
        
#     # plot elbow method 
#     fig, ax = plt.subplots()
#     ax.plot(K, inertia, marker='o')
#     ax.set_xlabel('Jumlah kelompok k')
#     ax.set_ylabel('Inertia')
#     ax.set_title("Elbow method "+dataAspek['name']+" Vs "+dataIndikator['name']+" Group "+data_gi['name'])
#    # Menggunakan BytesIO untuk menangkap output plot sebagai byte stream
#     output = io.BytesIO()
#     FigureCanvas(fig).print_png(output)

#     # Membuat respons HTTP dengan gambar sebagai byte stream
#     return Response(output.getvalue(), mimetype='image/png')
# @isi_bp.route('/api/'+model.table_name+'/kmeans_domain/<string:domain1>/<string:domain2>/grup/<string:gi>')
# def getKemeansDomain(domain1,domain2,gi):
#     data_gi=gi_model.getById(gi)
#     if(data_gi is None):
#         return jsonify({'message': model.table_name.capitalize()+' group not found'}), 404
#     dataDomain1=domain_model.getById(domain1)
#     if(dataDomain1 is None):
#         return jsonify({'message': model.table_name.capitalize()+' Domain 1 not found'}), 404
#     dataDomain2=domain_model.getById(domain2)
#     if(dataDomain2 is None):
#         return jsonify({'message': model.table_name.capitalize()+' Domaian 2 not found'}), 404
#     dfDomain1=model.getAllDomain(domain1,gi)
#     dfDomain2=model.getAllDomain(domain2,gi)
    
#     data_df=[]
#     for i,val_domain in enumerate(dfDomain1):
#         data_df.append([val_domain,dfDomain2[i]])
#     header_names=[dataDomain1['name'],dataDomain2['name']]
#     features = pd.DataFrame(data_df, columns=header_names)
#     K = range(2,11)
#     inertia = []
#     silhouette_coef = [] 
#     model_kmeans = [] 

#     for k in K:
#         kmeans= KMeans(n_clusters=k, random_state=42)
#         kmeans.fit(features)
#         model_kmeans.append(kmeans)
#         inertia.append(kmeans.inertia_)
#         score = silhouette_score(features, kmeans.labels_, metric='euclidean')
#         silhouette_coef.append(score)
        
#     # plot elbow method 
#     fig, ax = plt.subplots()
#     ax.plot(K, inertia, marker='o')
#     ax.set_xlabel('Jumlah kelompok k')
#     ax.set_ylabel('Inertia')
#     ax.set_title("Elbow method "+dataDomain1['name']+" Vs "+dataDomain2['name']+" Group "+data_gi['name'])
#    # Menggunakan BytesIO untuk menangkap output plot sebagai byte stream
#     output = io.BytesIO()
#     FigureCanvas(fig).print_png(output)

#     # Membuat respons HTTP dengan gambar sebagai byte stream
#     return Response(output.getvalue(), mimetype='image/png')
@isi_bp.route('/api/'+model.table_name+'/kmeans')
def get_kmeans_index():
    dfIndex=model.getAllIndex()
    features = pd.DataFrame(dfIndex, columns=['indeks'])
    K = range(2,11)
    inertia = []
    silhouette_coef = [] 
    model_kmeans = [] 

    for k in K:
        kmeans= KMeans(n_clusters=k, random_state=42)
        kmeans.fit(features)
        model_kmeans.append(kmeans)
        inertia.append(kmeans.inertia_)
        score = silhouette_score(features, kmeans.labels_, metric='euclidean')
        silhouette_coef.append(score)
        
    # plot elbow method 
    fig, ax = plt.subplots()
    ax.plot(K, inertia, marker='o')
    ax.set_xlabel('Jumlah kelompok k')
    ax.set_ylabel('Inertia')
    ax.set_title("Elbow method Indeks ")
   # Menggunakan BytesIO untuk menangkap output plot sebagai byte stream
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    # Membuat respons HTTP dengan gambar sebagai byte stream
    return Response(output.getvalue(), mimetype='image/png')
@isi_bp.route('/api/'+model.table_name+'/res_kmeans')
def get_res_kmeans_index():
            # data[counter-1].append("I1")
    
    return jsonify(model.getDf())