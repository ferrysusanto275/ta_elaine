from flask import Blueprint,jsonify,request,render_template,Response
from app.models.grup_instansi import grup_instansiModel
from app.models.instansi import instansiModel
from app.models.indikator import indikatorModel
from app.models.aspek import aspekModel
from app.models.domain import domainModel
from app.models.isi import isiModel
from scipy.optimize import minimize
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.decomposition import TruncatedSVD
import io
from io import BytesIO
import scipy.cluster.hierarchy as sch 
from decimal import Decimal

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
import seaborn as sns
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
@isi_bp.route('/api/'+model.table_name+"/year")
def get_all_year():
    return jsonify(model.getAllYear());
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
    K = range(2,6)
    inertia = model.kmeans_res()['inertia']
    # return jsonify(inertia['inertia'])
        
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
@isi_bp.route('/api/'+model.table_name+'/kmeans/<string:year>')
def get_kmeans_indexByYear(year):
    K = range(2,6)
    inertia = model.kmeans_resByYear(year)['inertia']
    # return jsonify(inertia['inertia'])
        
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
@isi_bp.route('/api/'+model.table_name+'/kmeans_score')
def get_kmeans_score_index():
    return jsonify(model.kmeans_res()['silhouette_coef'])
@isi_bp.route('/api/'+model.table_name+'/kmeans_score/<string:year>')
def get_kmeans_score_indexByYear(year):
    return jsonify(model.kmeans_resByYear(year)['silhouette_coef'])
@isi_bp.route('/api/'+model.table_name+'/res_kmeans')
def get_res_kmeans_index():
    return model.getDfK().to_html(classes="tabel")
@isi_bp.route('/api/'+model.table_name+'/res_kmeans/<string:year>')
def get_res_kmeans_indexByYear(year):
    df_dict = model.getDfKByYear(year).to_dict(orient='records')
    return jsonify(df_dict)
@isi_bp.route('/api/'+model.table_name+'/plot_kmeans/<string:year>')
def plot_kmeans_indexByYear(year):
    df = model.getDfKByYear(year)
    fig, ax = plt.subplots()
    ax.scatter(df['Indeks'],df['Domain 1'],c=df['Cluster'], cmap='rainbow')
    ax.set_xlabel("Index")
    ax.set_ylabel("Domain 1")
    ax.set_title("Clustering")
   # Menggunakan BytesIO untuk menangkap output plot sebagai byte stream
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    # Membuat respons HTTP dengan gambar sebagai byte stream
    return Response(output.getvalue(), mimetype='image/png')
@isi_bp.route('/api/'+model.table_name+'/plot_dend/<string:year>/<string:linkage>')
def plot_dend_indexByYear(year,linkage):
    df = model.getDfKByYear(year)
    fig = plt.figure(figsize=(10, 6))
    plt.title("Dend2 "+year)
    features = df[['Indeks']]
    dend = sch.dendrogram(sch.linkage(features, method=linkage))
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    # Membuat respons HTTP dengan gambar sebagai byte stream
    return Response(output.getvalue(), mimetype='image/png')

# @isi_bp.route('/api/'+model.table_name+'/res_agglo/<string:year>')
# def get_res_agglo_indexByYear(year):
#     df_dict = model.getDfKByYear(year).to_dict(orient='records')
#     return jsonify(df_dict)

@isi_bp.route('/api/'+model.table_name+'/agglo_score/<string:year>/<string:linkage>')
def get_agglo_score_index(year,linkage):
    
    df=pd.DataFrame(model.getDfByYear(year))
    # features = df[['Indeks', 'Domain 1']]
    # agglo_model = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')  # Adjust parameters as needed
    # labels = agglo_model.fit_predict(features)

    # # Visualize the clusters
    # plt.figure(figsize=(10, 7))
    # plt.scatter(features['Indeks'], features['Domain 1'], c=labels, cmap='rainbow')
    # plt.title("Agglomerative Clustering Results")
    # plt.xlabel("Indeks")
    # plt.ylabel("Domain 1")
    # plt.show()
    return jsonify(model.agglomerative(df,linkage)['silhouette_score'])
@isi_bp.route('/api/'+model.table_name+'/res_agglo/<string:year>/<string:linkage>')
def get_res_agglo_indexByYear(year, linkage):
    df_dict = model.getDfAByYear(year, linkage).to_dict(orient='records')
    # return jsonify(df_dict)
    return model.getDfAByYear(year, linkage)[['Instansi','Cluster']].to_html()

@isi_bp.route('/api/'+model.table_name+'/insert/<string:instansi>/<string:year>/<string:indeks>')
def insert_by_index(instansi,year,indeks):
    
    data_isi_2021=model.getAllValueByYearInstansi(instansi,2021)
    data_isi_2022=model.getAllValueByYearInstansi(instansi,2022)
    data_known=[[item["val"] for item in data_isi_2021],[item["val"] for item in data_isi_2022]]
    data_known[0].append(hitung_index(data_isi_2021))
    data_known[1].append(hitung_index(data_isi_2022))
    initial_guess=[]
    bounds=[]
    key_change=[]
    all_fill_key=[]
    data_fix=[]
    
    for i,val in enumerate(data_isi_2021):
        initial_guess.append(Decimal(0))
        # bound array 0 nilai max bound ke 1 nilai min
        bounds.append([Decimal(5),Decimal(1)])
        if(data_known[0][-1]!=data_known[1][-1]):
            if(data_known[0][i]==data_known[1][i]):
                data_fix.append(i)
                bounds[i][0]=data_known[0][i]
                initial_guess[i]=data_known[0][i]
            elif((data_known[0][i]>data_known[1][i] and data_known[0][-1]>data_known[1][-1]) or (data_known[0][i]<data_known[1][i] and data_known[0][-1]<data_known[1][-1])):
                max_value = max(Decimal(indeks), data_known[0][-1], data_known[1][-1])
                min_value = min(Decimal(indeks), data_known[0][-1], data_known[1][-1])
                if(max_value==indeks):
                    if(min_value==data_known[0][-1]):
                        bounds[i][1]=data_known[0][i]
                    else:bounds[i][1]=data_known[1][i]
                elif(max_value==data_known[0][-1]):
                    bounds[i][0]=data_known[0][i]
                    if(min_value==data_known[1][-1]):
                        bounds[i][1]=data_known[1][i]
                else:
                    bounds[i][0]=data_known[1][i]
                    if(min_value==data_known[0][-1]):
                        bounds[i][1]=data_known[0][i]
                # cek sebelahan
                initial_guess[i]=bounds[i][1]
                # cari data yang sama 
                key_same=[]
                if((i in all_fill_key)==False):
                    
                    for j,val_other in enumerate(data_known[0]):
                            if(data_known[0][i]==data_known[0][j] and data_known[1][i]==data_known[1][j]):
                                # print(i,j,data_known[0][i],data_known[0][j],data_known[1][i],data_known[1][j])
                                key_same.append(j)
                                all_fill_key.append(j)
                    key_change.append([i,key_same])
                
            else:initial_guess[i]=bounds[i][1]
    # cari data fix yang lebih besar atau harus lebih kecil dari pola
    # print(sorted(data_fix))
    for i in key_change:
        # print(i)
        cd=i[0]
        for j in data_fix:
            # data harus lebih besar
            if(data_known[0][cd]>data_known[0][j] and data_known[1][cd]>data_known[1][j]):
                
                bounds[cd][1]=max(initial_guess[j],bounds[cd][1])
                # print(bounds[cd][1])
                # data harus lebih kecil
            if(data_known[0][cd]<data_known[0][j] and data_known[1][cd]<data_known[1][j]):
                # print(cd,data_known[0][cd],data_known[1][cd],bounds[cd][1])
                bounds[cd][0]=min(initial_guess[j],bounds[cd][1])
                # print(bounds[cd][0])
        
        initial_guess[cd]=bounds[cd][1]
        for j in i[1]:
            initial_guess[j]=initial_guess[cd]
            if(bounds[cd][0]==bounds[cd][1]):data_fix.append(j)
    print(sorted(data_fix))
    n = len(key_change)
    for i in range(n):
        for j in range(0, n-i-1):
            idx1=key_change[j][0]
            idx2=key_change[j+1][0]
            # print(idx1,idx2,data_known[0][idx1],data_known[0][idx1])
            if(data_known[0][idx1]<data_known[0][idx2] and data_known[1][idx1]<data_known[1][idx2]):
                key_change[j],key_change[j+1]=key_change[j+1],key_change[j]
    # print(key_change)
    counter=0
    while(objective(initial_guess)<Decimal(indeks) and counter<len(key_change)):
        i=key_change[counter][0]
        if(bounds[i][0]>initial_guess[i]):
            initial_guess[i]=initial_guess[i]+1
            for j in key_change[counter][1]:
                initial_guess[j]=initial_guess[i]
            if(objective(initial_guess)>Decimal(indeks)):
                initial_guess[i]=initial_guess[i]-1
                for j in key_change[counter][1]:
                    initial_guess[j]=initial_guess[i]
                counter=counter+1
        else:
            counter=counter+1
    
        # cek data yang harus berubah
    initial_guess.append(objective(initial_guess))
 
    
        
    return jsonify({"data_2021":data_known[0],"data_2022":data_known[1],"data_"+year:initial_guess})
# Fungsi objektif untuk minimasi
def objective(params):
    i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,i21,i22,i23,i24,i25,i26,i27,i28,i29,i30,i31,i32,i33,i34,i35,i36,i37,i38,i39,i40,i41,i42,i43,i44,i45,i46,i47=params
    domain1=(i1+i2+i3+i4+i5+i6+i7+i8+i9+i10)*Decimal(1.3/13)
    
    aspek2=(i11+i12+i13+i14)*Decimal(2.5/10)
    aspek3=(i15+i16+i17+i18)*Decimal(2.5/10)
    aspek4=(i19+i20)*Decimal(2.5/5)
    aspek5=(i21+i22+i23+i24+i25+i26+i27+i28)*Decimal(1.5/12)
    aspek6=(i29+i30+i31)*Decimal(1.5/4.5)
    aspek7=(i32+i33+i34+i35+i36+i37+i38+i39+i40+i41)*Decimal(2.75/27.5)
    aspek8=(i42+i43+i44+i45+i46+i47)*Decimal(3/18)
    domain2=(aspek2*Decimal(10/25))+(aspek3*Decimal(10/25))+(aspek4*Decimal(5/25))
    domain3=(aspek5*Decimal(12/16.5))+(aspek6*Decimal(4.5/16.5))
    domain4=(aspek7*Decimal(27.5/45.5))+(aspek8*Decimal(18/45.5))
    # print(domain1,domain2,domain3,domain4)
    return (domain1*Decimal(13/100))+(domain2*Decimal(25/100))+(domain3*Decimal(16.5/100))+(domain4*Decimal(45.5/100))
def hitung_index(params):
    x=0
    data_aspek={};
    
    for val in params:
        if val['id_aspek'] not in data_aspek:
            data_aspek[val['id_aspek']] = {"bobot":val['bobot_aspek'],"id_domain":val['id_domain'],"bobot_domain":val['bobot_domain'],"val":val['val']*val['bobot_indikator']/val['bobot_aspek']}
        else:
            data_aspek[val['id_aspek']]['val']+=val['val']*val['bobot_indikator']/val['bobot_aspek']
    
    data_domain={}
    jml_bobot=0
    for key, val in data_aspek.items():
        if val['id_domain'] not in data_domain:
            data_domain[val['id_domain']] = {"bobot":val['bobot_domain'],"val":val['val']*val['bobot']/val['bobot_domain']}
            jml_bobot+=val['bobot_domain']
        else: data_domain[val['id_domain']]['val'] += val['val']*val['bobot']/val['bobot_domain']
    index=0;
    for key, val in data_domain.items():
        index+=val['val']*val['bobot']/jml_bobot
    
    return index
@isi_bp.route('/api/'+model.table_name+'/pca/<string:year>')
def pcaByYear(year):
    df = model.getDfKByYear(year)
    # print(df)
    # df = df[df['Group'] == 'Kementerian Pusat']

    # print(filtered_df)
    # numerical_columns = df.columns[df.columns.str.startswith('I')]

    # Selecting only the numerical columns for PCA
    X = df[['I1','I2','I3','I4','I5','I6','I7','I8','I9','I10',
    'I11','I12','I13','I14','I15','I16','I17','I18','I19','I20',
    'I21','I22','I23','I24','I25','I26','I27','I28','I29','I30',
     'I31','I32','I33','I34','I35','I36','I37','I38','I39','I40',
      'I41','I42','I43','I44','I45','I46','I47','Indeks']]
    # X=df[['I1','Indeks']]
    # X_standardized = StandardScaler().fit_transform(X)

    # Apply PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(X)
    # principal_components = principal_components+(7.5)
    # if pca.components_[0, 0] < 0:
    #     principal_components[:, 0] = -1 * principal_components[:, 0]
    # if pca.components_[1, 0] < 0:
    #     principal_components[:, 1] = -1 * principal_components[:, 1]

    # Create a DataFrame with the first two principal components and additional information
    pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
    pca_df['Cluster'] = df['Cluster']

    # Scatter plot
    # fig, ax = plt.subplots()

    fig, ax = plt.subplots(figsize=(15, 6))
    sns.scatterplot(x='PC1', y='PC2', data=pca_df, hue='Cluster',s=100, palette='Set1')
    plt.title('PCA Plot of Institutions')
    plt.xlabel('Principal Component 1 (PC1)')
    plt.ylabel('Principal Component 2 (PC2)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Adjust legend position
    # plt.show()
    # Using BytesIO to capture the plot as a byte stream
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    # plt.savefig(output, format='png')  # Save the plot to BytesIO in PNG format
    # plt.close(fig)  # Close the plot to release resources

    # Creating an HTTP response with the plot as a byte stream
    return Response(output.getvalue(), mimetype='image/png')

@isi_bp.route('/api/'+model.table_name+'/svd/<string:year>')
def svdByYear(year):
    df = model.getDfKByYear(year)
    # print(df)
    # df = df[df['Group'] == 'Kementerian Pusat']

    # print(filtered_df)
    # numerical_columns = df.columns[df.columns.str.startswith('I')]

    # Selecting only the numerical columns for PCA
    X = df[['I1','I2','I3','I4','I5','I6','I7','I8','I9','I10',
    'I11','I12','I13','I14','I15','I16','I17','I18','I19','I20',
    'I21','I22','I23','I24','I25','I26','I27','I28','I29','I30',
     'I31','I32','I33','I34','I35','I36','I37','I38','I39','I40',
      'I41','I42','I43','I44','I45','I46','I47','Indeks']]
    # print(X)
    # X=df[['Indeks']]
    
    target=df['Cluster'].values
    X['target']=target
    svd = TruncatedSVD(n_components=2)
    df_svd = svd.fit_transform(X)
    fig, ax = plt.subplots()
    print(df_svd[:, 1])
    scatter = ax.scatter(df_svd[:, 0], df_svd[:, 1], c=df['Cluster'], cmap='viridis', edgecolors='k', alpha=0.7)
    ax.set_title('SVD-based Clustering')
    ax.set_xlabel('SVD Component 1')
    ax.set_ylabel('SVD Component 2')
    legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
    ax.add_artist(legend1)
    # return jsonify("")

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    # plt.savefig(output, format='png')  # Save the plot to BytesIO in PNG format
    # plt.close(fig)  # Close the plot to release resources

    # Creating an HTTP response with the plot as a byte stream
    return Response(output.getvalue(), mimetype='image/png')
@isi_bp.route('/api/'+model.table_name+'/pca_agglo/<string:year>/<string:linkage>')
def pcaAggloByYear(year,linkage):
    df = model.getDfAByYear(year,linkage)
    # print(df)
    # df = df[df['Group'] == 'Kementerian Pusat']

    # print(filtered_df)
    # numerical_columns = df.columns[df.columns.str.startswith('I')]

    # Selecting only the numerical columns for PCA
    X = df[['I1','I2','I3','I4','I5','I6','I7','I8','I9','I10',
    'I11','I12','I13','I14','I15','I16','I17','I18','I19','I20',
    'I21','I22','I23','I24','I25','I26','I27','I28','I29','I30',
     'I31','I32','I33','I34','I35','I36','I37','I38','I39','I40',
      'I41','I42','I43','I44','I45','I46','I47','Indeks']]
    # X=df[['I1','Indeks']]
    # X_standardized = StandardScaler().fit_transform(X)

    # Apply PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(X)
    # principal_components = principal_components+(7.5)
    # if pca.components_[0, 0] < 0:
    #     principal_components[:, 0] = -1 * principal_components[:, 0]
    # if pca.components_[1, 0] < 0:
    #     principal_components[:, 1] = -1 * principal_components[:, 1]

    # Create a DataFrame with the first two principal components and additional information
    pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
    pca_df['Cluster'] = df['Cluster']

    # Scatter plot
    # fig, ax = plt.subplots()

    fig, ax = plt.subplots(figsize=(15, 6))
    sns.scatterplot(x='PC1', y='PC2', data=pca_df, hue='Cluster',s=100, palette='Set1')
    plt.title('PCA Agglomerative')
    plt.xlabel('Principal Component 1 (PC1)')
    plt.ylabel('Principal Component 2 (PC2)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Adjust legend position
    # plt.show()
    # Using BytesIO to capture the plot as a byte stream
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    # plt.savefig(output, format='png')  # Save the plot to BytesIO in PNG format
    # plt.close(fig)  # Close the plot to release resources

    # Creating an HTTP response with the plot as a byte stream
    return Response(output.getvalue(), mimetype='image/png')

@isi_bp.route('/api/'+model.table_name+'/svd_agglo/<string:year>/<string:linkage>')
def svdAggloByYear(year,linkage):
    df = model.getDfAByYear(year,linkage)
    # print(df)
    # df = df[df['Group'] == 'Kementerian Pusat']

    # print(filtered_df)
    # numerical_columns = df.columns[df.columns.str.startswith('I')]

    # Selecting only the numerical columns for PCA
    X = df[['I1','I2','I3','I4','I5','I6','I7','I8','I9','I10',
    'I11','I12','I13','I14','I15','I16','I17','I18','I19','I20',
    'I21','I22','I23','I24','I25','I26','I27','I28','I29','I30',
     'I31','I32','I33','I34','I35','I36','I37','I38','I39','I40',
      'I41','I42','I43','I44','I45','I46','I47','Indeks']]
    # print(X)
    # X=df[['Indeks']]
    
    target=df['Cluster'].values
    X['target']=target
    svd = TruncatedSVD(n_components=2)
    df_svd = svd.fit_transform(X)
    fig, ax = plt.subplots()
    print(df_svd[:, 1])
    scatter = ax.scatter(df_svd[:, 0], df_svd[:, 1], c=df['Cluster'], cmap='viridis', edgecolors='k', alpha=0.7)
    ax.set_title('SVD Agglomerative')
    ax.set_xlabel('SVD Component 1')
    ax.set_ylabel('SVD Component 2')
    legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
    ax.add_artist(legend1)
    # return jsonify("")

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    # plt.savefig(output, format='png')  # Save the plot to BytesIO in PNG format
    # plt.close(fig)  # Close the plot to release resources

    # Creating an HTTP response with the plot as a byte stream
    return Response(output.getvalue(), mimetype='image/png')