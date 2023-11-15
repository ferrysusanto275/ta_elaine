from flask import Blueprint,jsonify,request,render_template
from app.models.grup_instansi import grup_instansiModel
from app.models.instansi import instansiModel
from app.models.indikator import indikatorModel
from app.models.aspek import aspekModel
from app.models.isi import isiModel
import os

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
@isi_bp.route('/api/'+model.table_name+'/<string:indikator1>/<string:indikator2>/grup/<string:gi>')
def getPerbandingan(indikator1,indikator2,gi):
    data_gi=gi_model.getById(gi)
    
    dfIndikator1=model.getAllValue(indikator1,gi)
    dfIndikator2=model.getAllValue(indikator2,gi)
    dataIndikator1=indikator_model.getById(indikator1)
    dataIndikator2=indikator_model.getById(indikator2)
    # print(dataIndikator1['name'])
    plt.scatter(dfIndikator1,dfIndikator2,alpha=0.5)
    plt.title(dataIndikator1['name']+" VS "+dataIndikator2['name']+" "+data_gi['name'])
    plt.xlabel(dataIndikator1['name'])
    plt.ylabel(dataIndikator2['name'])
    plt.show()
    return jsonify("")
@isi_bp.route('/api/'+model.table_name+'/aspek/<string:aspek1>/<string:aspek2>/grup/<string:gi>')
def getPerbandinganAspek(aspek1,aspek2,gi):
    data_gi=gi_model.getById(gi)
    dfAspek1=model.getAllAspek(aspek1,gi)
    dfAspek2=model.getAllAspek(aspek2,gi)
    # print(aspek2)
    # print(len(dfAspek2))
    dataAspek1=aspek_model.getById(aspek1)
    dataAspek2=aspek_model.getById(aspek2)
    # print(dataIndikator1['name'])
    plt.scatter(dfAspek1,dfAspek2,alpha=0.5)
    plt.title(dataAspek1['name']+" VS "+dataAspek2['name']+" "+data_gi['name'])
    plt.xlabel(dataAspek1['name'])
    plt.ylabel(dataAspek2['name'])
    plt.show()
    return jsonify("")
    # Buat scatter plot
    # fig = create_scatter_plot(dfIndikator1, dfIndikator2,dataIndikator1['name'],dataIndikator2['name'])
    # current_dir = os.getcwd()
    #     # Create the 'static' directory if it doesn't exist
    # if not os.path.exists('static'):
    #     os.makedirs('static')
    # # Simpan plot sebagai gambar
    # img_path = os.path.join(current_dir,"static", f'plot.png')
    # fig.savefig(img_path)
    # plt.close(fig)
    # return render_template('tampil_plt.html', img_path=img_path)
def create_scatter_plot(array1, array2,nm_array1,nm_array2):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.scatter(array1, array2)
    axis.set_xlabel(nm_array1)
    axis.set_ylabel(nm_array2)
    return fig