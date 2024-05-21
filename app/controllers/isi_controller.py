from flask import Blueprint,jsonify,request,render_template,Response
from app.models.grup_instansi import grup_instansiModel
from app.models.instansi import instansiModel
from app.models.indikator import indikatorModel
from app.models.aspek import aspekModel
from app.models.domain import domainModel
from app.models.isi import isiModel
from app.models.area import areaModel
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
from app.models.keluaran import keluaranModel

model=isiModel()
aspek_model=aspekModel()
instansi_model=instansiModel()
indikator_model=indikatorModel()
area_model=areaModel()
gi_model=grup_instansiModel()
domain_model=domainModel()
keluaran=keluaranModel()
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

@isi_bp.route('/api/'+model.table_name+'/kmeans')
def get_kmeans_index():
    K = range(2,6)
    inertia = model.kmeans_res()['inertia']
   
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
@isi_bp.route('/api/'+model.table_name+'/kmeans/<string:year>/<string:area>')
def get_kmeans_areaByYear(year,area):
    K = range(2,6)
    inertia = keluaran.kmeans_res(area,year)['inertia']
        
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
@isi_bp.route('/api/'+model.table_name+'/kmeans_score/<string:year>/<string:area>')
def get_kmeans_score_areaByYear(year,area):
    return jsonify(keluaran.kmeans_res(area,year)['silhouette_coef'])
@isi_bp.route('/api/'+model.table_name+'/res_kmeans')
def get_res_kmeans_index():
    return model.getDfK().to_html(classes="tabel")
@isi_bp.route('/api/'+model.table_name+'/get_df23/<string:year>/<string:analisis>/<string:indikator>/<string:baik>')
def get_df23(year,analisis,indikator,baik):
    indikator_layanan=np.array(["in2023110400014","in2023110400015","in2023110400028","in2023110400030","in2023110400033","in2023110400032","in2023110400034","in2023110400035","in2023110400036","in2023110400037","in2023110400038","in2023110400039","in2023110400040","in2023110400041","in2023110400042","in2023110400043","in2023110400044","in2023110400045","in2023110400046","in2023110400047"])
    index = np.where(indikator_layanan == indikator)[0]
    
    df=model.getDf23(analisis=analisis,year=year,indikator=indikator)
    nilai_layanan=3
    if(np.any(index)):nilai_layanan=4
    if(baik=="0"):
        # tampil data terbaik
       
        print(nilai_layanan)
        df=df[df['Value']>=nilai_layanan]
        df.sort_values(by='Value', ascending=False)
    else:
        df=df[df['Value']<nilai_layanan]
        df.sort_values(by='Value')
    df=df.to_dict(orient='records')
    return jsonify(df)
@isi_bp.route('/api/'+model.table_name+'/res_kmeans/<string:year>')
def get_res_kmeans_indexByYear(year):
    df_dict = model.getDfKByYear(year).to_dict(orient='records')
    return jsonify(df_dict)
@isi_bp.route('/api/'+model.table_name+'/plot_kmeans/<string:year>/<string:area>')
def plot_kmeans_indexByYear(year,area):
    if(area!="0"):
        data_indikator=keluaran.getAllIndikatorby_Area(area)

    df = keluaran.getDfK(area,year)
    fig, ax = plt.subplots()
    if(area!="0"):
        X = df[data_indikator]
        pca = PCA(n_components=2)
        principal_components = pca.fit_transform(X)
        pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])

        ax.scatter(pca_df['PC1'], pca_df['PC2'],c=df['Cluster'], cmap='rainbow')
        ax.set_xlabel('Component 1')
        ax.set_ylabel('Component 2')
        ax.set_title("Clustering")
    else: 
        ax.scatter(df['domain1'], df['indeks'],c=df['Cluster'], cmap='rainbow')
        ax.set_xlabel('Domain 1')
        ax.set_ylabel('Indeks')
        ax.set_title("Clustering")
    
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    # Membuat respons HTTP dengan gambar sebagai byte stream
    return Response(output.getvalue(), mimetype='image/png')
@isi_bp.route('/api/'+model.table_name+'/plot_dend/<string:year>/<string:linkage>/<string:area>')
def plot_dend_indexByYear(year,linkage,area):
    if(area!="0"):
        data_indikator=keluaran.getAllIndikatorby_Area(area)
        data_area=area_model.getById(area)
        namaArea=data_area['name'][3:]
    else: 
        data_indikator=['indeks']
        namaArea="Indeks"
    
    df = keluaran.getDfAByareaYear(area,year,linkage)
    fig = plt.figure(figsize=(10, 6))
    plt.title("Dend2 "+year+" berdasarkan "+namaArea)
    features = df[data_indikator]
    dend = sch.dendrogram(sch.linkage(features, method=linkage))
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    # Membuat respons HTTP dengan gambar sebagai byte stream
    return Response(output.getvalue(), mimetype='image/png')


@isi_bp.route('/api/'+model.table_name+'/agglo_score/<string:year>/<string:linkage>/<string:area>')
def get_agglo_score_index(year,linkage,area):
    df=keluaran.getDfAByareaYear(area,year,linkage)
    return jsonify(df['silhouette_score'])
@isi_bp.route('/api/'+model.table_name+'/res_agglo/<string:year>/<string:linkage>')
def get_res_agglo_indexByYear(year, linkage):
    df_dict = model.getDfAByYear(year, linkage).to_dict(orient='records')
    return jsonify(df_dict)

@isi_bp.route('/api/'+model.table_name+'/insert/<string:instansi>/<string:year>/<string:indeks>')
def insert_by_index(instansi,year,indeks):
    initial_guess=[]
    bounds=[]
    for i in range(47):
        initial_guess.append(1)
        bounds.append([1,5])
    constraint = {'type': 'eq', 'fun': lambda params: float(indeks)- objective(params)}
    # Melakukan minimasi
    result = minimize(objective, initial_guess, bounds=bounds, constraints=constraint)
    indikator=[]
    # Menampilkan hasil
    for i in range(47):
        indikator.append(round(result.x[i]))


    if model.create_bulk(instansi=instansi,year=year,values=indikator):
        return jsonify({'message': model.table_name.capitalize()+' created'}), 201
    else:
        return jsonify({'message': 'Failed to create '+model.table_name}), 500
   
# Fungsi objektif untuk minimasi
def objective(params):
    i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,i21,i22,i23,i24,i25,i26,i27,i28,i29,i30,i31,i32,i33,i34,i35,i36,i37,i38,i39,i40,i41,i42,i43,i44,i45,i46,i47=params
    domain1=(i1+i2+i3+i4+i5+i6+i7+i8+i9+i10)*(1.3/13)
    
    aspek2=(i11+i12+i13+i14)*(2.5/10)
    aspek3=(i15+i16+i17+i18)*(2.5/10)
    aspek4=(i19+i20)*(2.5/5)
    aspek5=(i21+i22+i23+i24+i25+i26+i27+i28)*(1.5/12)
    aspek6=(i29+i30+i31)*(1.5/4.5)
    aspek7=(i32+i33+i34+i35+i36+i37+i38+i39+i40+i41)*(2.75/27.5)
    aspek8=(i42+i43+i44+i45+i46+i47)*(3/18)
    domain2=(aspek2*(10/25))+(aspek3*(10/25))+(aspek4*(5/25))
    domain3=(aspek5*(12/16.5))+(aspek6*(4.5/16.5))
    domain4=(aspek7*(27.5/45.5))+(aspek8*(18/45.5))
    # print(domain1,domain2,domain3,domain4)
    return (domain1*(13/100))+(domain2*(25/100))+(domain3*(16.5/100))+(domain4*(45.5/100))
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
@isi_bp.route('/api/'+model.table_name+'/pca/<string:year>/<string:cari>')
def pcaByYear(year,cari):
    df = keluaran.getDfK("0",year)
    if(cari=="semua"):
        X = df[['i1','i2','i3','i4','i5','i6','i7','i8','i9','i10',
        'i11','i12','i13','i14','i15','i16','i17','i18','i19','i20',
        'i21','i22','i23','i24','i25','i26','i27','i28','i29','i30',
        'i31','i32','i33','i34','i35','i36','i37','i38','i39','i40',
        'i41','i42','i43','i44','i45','i46','i47','indeks']]
    elif(cari=="domain_1"):
        X = df[['i1','i2','i3','i4','i5','i6','i7','i8','i9','i10','domain1']]
    elif(cari=="domain_2"):
        X = df[[ 'i11','i12','i13','i14','i15','i16','i17','i18','i19','i20','domain2']]
    elif(cari=="domain_3"):
        X = df[[ 'i21','i22','i23','i24','i25','i26','i27','i28','i29','i30','i31','domain3']]
    elif(cari=="domain_4"):
        X = df[['i32','i33','i34','i35','i36','i37','i38','i39','i40',
        'i41','i42','i43','i44','i45','i46','i47', 'domain4']]
    else:
         df = keluaran.getDfK(cari,year)
         data_indikator=keluaran.getAllIndikatorby_Area(cari)
         X=df[data_indikator]
    

    # Apply PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(X)
    

    # Create a DataFrame with the first two principal components and additional information
    pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
    pca_df['Cluster'] = df['Cluster']

    # Scatter plot
    # fig, ax = plt.subplots()

    fig, ax = plt.subplots(figsize=(15, 6))
    sns.scatterplot(x='PC1', y='PC2', data=pca_df, hue='Cluster',s=100, palette='Set1')
    plt.title('PCA KMeans')
    plt.xlabel('Principal Component 1 (PC1)')
    plt.ylabel('Principal Component 2 (PC2)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Adjust legend position
    
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    
    return Response(output.getvalue(), mimetype='image/png')
@isi_bp.route('/api/'+model.table_name+'/res_pca/<string:year>/<string:cari>')
def respcaByYear(year,cari):
    df = model.getDfKByYear(year)
    # print(df)
    if(cari=="semua"):
        X = df[['I1','I2','I3','I4','I5','I6','I7','I8','I9','I10',
        'I11','I12','I13','I14','I15','I16','I17','I18','I19','I20',
        'I21','I22','I23','I24','I25','I26','I27','I28','I29','I30',
        'I31','I32','I33','I34','I35','I36','I37','I38','I39','I40',
        'I41','I42','I43','I44','I45','I46','I47','Indeks']]
    elif(cari=="domain_1"):
        X = df[['I1','I2','I3','I4','I5','I6','I7','I8','I9','I10','Domain 1']]
    elif(cari=="domain_2"):
        X = df[['I11','I12','I13','I14','I15','I16','I17','I18','I19','I20','Domain 2']]
    elif(cari=="domain_3"):
        X = df[['I21','I22','I23','I24','I25','I26','I27','I28','I29','I30','I31','Domain 3']]
    elif(cari=="domain_4"):
        X = df[['I32','I33','I34','I35','I36','I37','I38','I39','I40',
        'I41','I42','I43','I44','I45','I46','I47', 'Domain 4']]
    

    # Apply PCA

    pca = PCA(n_components=2)
    data_pca = pca.fit_transform(X)
    # print(data_pca);
    PC1 = pca.components_[0]
    PC2 = pca.components_[1]
    PC1_values = dict(zip(X.columns, PC1))
    PC2_values = dict(zip(X.columns, PC2))

    # Tentukan threshold untuk kelompok pertama
    # threshold_PC1 = 0.5
    # threshold_PC2 = -0.5
    # Tentukan threshold untuk fitur yang signifikan
    threshold_signifikan = 0.2

    # Ambil sampel yang memenuhi kriteria kelompok pertama
    # kelompok_pertama_indices = np.where((data_pca[:, 0] > threshold_PC1) & (data_pca[:, 1] < threshold_PC2))[0]
    # print(kelompok_pertama_indices)
    # Ambil data asli untuk kelompok pertama
    # kelompok_pertama_data = X.columns[kelompok_pertama_indices, :]
    # print(kelompok_pertama_data)

    # Identifikasi fitur yang signifikan dalam membentuk komponen utama
    fitur_signifikan_PC1 = [f'{X.columns[i]}' for i in range(len(PC1)) if abs(PC1[i]) > threshold_signifikan]
    fitur_signifikan_PC2 = [f'{X.columns[i]}' for i in range(len(PC2)) if abs(PC2[i]) > threshold_signifikan]
    kelompok_1 = [f'{X.columns[i]}' for i in range(len(PC1)) if PC1[i] > 0 and PC2[i] > 0]#pc1>0 dan pc2>0
    kelompok_2 = [f'{X.columns[i]}' for i in range(len(PC1)) if PC1[i] < 0 and PC2[i] > 0]#pc1<0 dan pc2>0
    kelompok_3 = [f'{X.columns[i]}' for i in range(len(PC1)) if PC1[i] < 0 and PC2[i] < 0]#pc1<0 dan pc2<0
    kelompok_4 = [f'{X.columns[i]}' for i in range(len(PC1)) if PC1[i] > 0 and PC2[i] < 0]#pc1>0 dan pc2<0


    res={"PC1_values":PC1_values,"PC2_values":PC2_values,"fitur_signifikan_PC1":fitur_signifikan_PC1,"fitur_signifikan_PC2":fitur_signifikan_PC2,"kelompok_1":kelompok_1,"kelompok_2":kelompok_2,"kelompok_3":kelompok_3,"kelompok_4":kelompok_4};

    return jsonify(res);

@isi_bp.route('/api/'+model.table_name+'/svd/<string:year>/<string:area>')
def svdByYear(year,area):
    # df = model.getDfKByYear(year)

    df=keluaran.getDfK(area,year)
    if(area=="0"):
        X = df[['i1','i2','i3','i4','i5','i6','i7','i8','i9','i10',
            'i11','i12','i13','i14','i15','i16','i17','i18','i19','i20',
            'i21','i22','i23','i24','i25','i26','i27','i28','i29','i30',
            'i31','i32','i33','i34','i35','i36','i37','i38','i39','i40',
            'i41','i42','i43','i44','i45','i46','i47','indeks']]
    else:
        data_indikator=keluaran.getAllIndikatorby_Area(area)
        X=df[data_indikator]
   
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
   
    return Response(output.getvalue(), mimetype='image/png')
@isi_bp.route('/api/'+model.table_name+'/pca_agglo/<string:year>/<string:cari>/<string:linkage>')
def pcaAggloByYear(year,linkage, cari):
    df = keluaran.getDfAByareaYear('0',year,linkage)
   
    if(cari=="semua"):
        X = df[['i1','i2','i3','i4','i5','i6','i7','i8','i9','i10',
        'i11','i12','i13','i14','i15','i16','i17','i18','i19','i20',
        'i21','i22','i23','i24','i25','i26','i27','i28','i29','i30',
        'i31','i32','i33','i34','i35','i36','i37','i38','i39','i40',
        'i41','i42','i43','i44','i45','i46','i47','indeks']]
    elif(cari=="domain_1"):
        X = df[['i1','i2','i3','i4','i5','i6','i7','i8','i9','i10','domain1']]
    elif(cari=="domain_2"):
        X = df[[ 'i11','i12','i13','i14','i15','i16','i17','i18','i19','i20','domain2']]
    elif(cari=="domain_3"):
        X = df[[ 'i21','i22','i23','i24','i25','i26','i27','i28','i29','i30','i31','domain3']]
    elif(cari=="domain_4"):
        X = df[['i32','i33','i34','i35','i36','i37','i38','i39','i40',
        'i41','i42','i43','i44','i45','i46','i47', 'domain4']]
    else:
         df = keluaran.getDfK(cari,year)
         data_indikator=keluaran.getAllIndikatorby_Area(cari)
         X=df[data_indikator]
   
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(X)
   
    # Create a DataFrame with the first two principal components and additional information
    pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
    pca_df['Cluster'] = df['Cluster']

   

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
    
    return Response(output.getvalue(), mimetype='image/png')
@isi_bp.route('/api/'+model.table_name+'/res_pca_agglo/<string:year>/<string:linkage>/<string:cari>')
def respcaAggloByYear(year,linkage, cari):
    df = model.getDfAByYear(year,linkage)
   
    if(cari=="semua"):
        X = df[['I1','I2','I3','I4','I5','I6','I7','I8','I9','I10',
        'I11','I12','I13','I14','I15','I16','I17','I18','I19','I20',
        'I21','I22','I23','I24','I25','I26','I27','I28','I29','I30',
        'I31','I32','I33','I34','I35','I36','I37','I38','I39','I40',
        'I41','I42','I43','I44','I45','I46','I47','Indeks']]
    elif(cari=="domain_1"):
        X = df[['I1','I2','I3','I4','I5','I6','I7','I8','I9','I10','Domain 1']]
    elif(cari=="domain_2"):
        X = df[['I11','I12','I13','I14','I15','I16','I17','I18','I19','I20','Domain 2']]
    elif(cari=="domain_3"):
        X = df[['I21','I22','I23','I24','I25','I26','I27','I28','I29','I30','I31','Domain 3']]
    elif(cari=="domain_4"):
        X = df[['I32','I33','I34','I35','I36','I37','I38','I39','I40',
        'I41','I42','I43','I44','I45','I46','I47', 'Domain 4']]
   
    pca = PCA(n_components=2)
    data_pca = pca.fit_transform(X)
    PC1 = pca.components_[0]
    PC2 = pca.components_[1]
    PC1_values = dict(zip(X.columns, PC1))
    PC2_values = dict(zip(X.columns, PC2))

    # Tentukan threshold untuk kelompok pertama
    # threshold_PC1 = 0.5
    # threshold_PC2 = -0.5
    # Tentukan threshold untuk fitur yang signifikan
    threshold_signifikan = 0.2

    # Ambil sampel yang memenuhi kriteria kelompok pertama
    # kelompok_pertama_indices = np.where((data_pca[:, 0] > threshold_PC1) & (data_pca[:, 1] < threshold_PC2))[0]
    # print(kelompok_pertama_indices)
    # Ambil data asli untuk kelompok pertama
    # kelompok_pertama_data = X.columns[kelompok_pertama_indices, :]
    # print(kelompok_pertama_data)

    # Identifikasi fitur yang signifikan dalam membentuk komponen utama
    fitur_signifikan_PC1 = [f'{X.columns[i]}' for i in range(len(PC1)) if abs(PC1[i]) > threshold_signifikan]
    fitur_signifikan_PC2 = [f'{X.columns[i]}' for i in range(len(PC2)) if abs(PC2[i]) > threshold_signifikan]
    kelompok_1 = [f'{X.columns[i]}' for i in range(len(PC1)) if PC1[i] > 0 and PC2[i] > 0]#pc1>0 dan pc2>0
    kelompok_2 = [f'{X.columns[i]}' for i in range(len(PC1)) if PC1[i] < 0 and PC2[i] > 0]#pc1<0 dan pc2>0
    kelompok_3 = [f'{X.columns[i]}' for i in range(len(PC1)) if PC1[i] < 0 and PC2[i] < 0]#pc1<0 dan pc2<0
    kelompok_4 = [f'{X.columns[i]}' for i in range(len(PC1)) if PC1[i] > 0 and PC2[i] < 0]#pc1>0 dan pc2<0


    res={"PC1_values":PC1_values,"PC2_values":PC2_values,"fitur_signifikan_PC1":fitur_signifikan_PC1,"fitur_signifikan_PC2":fitur_signifikan_PC2,"kelompok_1":kelompok_1,"kelompok_2":kelompok_2,"kelompok_3":kelompok_3,"kelompok_4":kelompok_4};

    return jsonify(res);

@isi_bp.route('/api/'+model.table_name+'/svd_agglo/<string:year>/<string:linkage>')
def svdAggloByYear(year,linkage):
    df = model.getDfAByYear(year,linkage)
    
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

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
# @isi_bp.route('/api/'+model.table_name+'/svd_agglo/<string:year>/<string:linkage>')
# def svdAggloByYear(year,linkage):
#     df = model.getDfAByYear(year,linkage)
    
#     X = df[['I1','I2','I3','I4','I5','I6','I7','I8','I9','I10',
#     'I11','I12','I13','I14','I15','I16','I17','I18','I19','I20',
#     'I21','I22','I23','I24','I25','I26','I27','I28','I29','I30',
#      'I31','I32','I33','I34','I35','I36','I37','I38','I39','I40',
#       'I41','I42','I43','I44','I45','I46','I47','Indeks']]
#     # print(X)
#     # X=df[['Indeks']]
    
#     target=df['Cluster'].values
#     X['target']=target
    # svd = TruncatedSVD(n_components=2)
    # df_svd = svd.fit_transform(X)
    # fig, ax = plt.subplots()
    # print(df_svd[:, 1])
    # scatter = ax.scatter(df_svd[:, 0], df_svd[:, 1], c=df['Cluster'], cmap='viridis', edgecolors='k', alpha=0.7)
    # ax.set_title('SVD Agglomerative')
    # ax.set_xlabel('SVD Component 1')
    # ax.set_ylabel('SVD Component 2')
    # legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
    # ax.add_artist(legend1)

    # output = io.BytesIO()
    # FigureCanvas(fig).print_png(output)
    # return Response(output.getvalue(), mimetype='image/png')

# @isi_bp.route('/api/'+model.table_name+'/df_indikator')
# def allIndikator():
#     df = model.getDfAllIndikator()
#     return jsonify(df)
    


