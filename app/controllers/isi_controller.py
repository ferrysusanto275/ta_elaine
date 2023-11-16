from flask import Blueprint,jsonify,request,render_template,Response
from app.models.grup_instansi import grup_instansiModel
from app.models.instansi import instansiModel
from app.models.indikator import indikatorModel
from app.models.aspek import aspekModel
from app.models.isi import isiModel
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
    if('id' not in data_gi):
        return jsonify({'message': model.table_name.capitalize()+' grup found'}), 404
        
    dataIndikator1=indikator_model.getById(indikator1)
    if(dataIndikator1 is None):
        return jsonify({'message': model.table_name.capitalize()+' Indikator 1 not found'}), 404
    dataIndikator2=indikator_model.getById(indikator2)
    if(dataIndikator2 is None):
        return jsonify({'message': model.table_name.capitalize()+' Indikator 2 not found'}), 404
    dfIndikator1=model.getAllValue(indikator1,gi)
    dfIndikator2=model.getAllValue(indikator2,gi)
    fig, ax = plt.subplots()
    ax.scatter(dfIndikator1,dfIndikator2,alpha=0.5)
    ax.set_xlabel(dataIndikator1['name'])
    ax.set_ylabel(dataIndikator2['name'])
    ax.set_title(dataIndikator1['name']+" VS "+dataIndikator2['name']+" "+data_gi['name'])
   # Menggunakan BytesIO untuk menangkap output plot sebagai byte stream
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    # Membuat respons HTTP dengan gambar sebagai byte stream
    return Response(output.getvalue(), mimetype='image/png')
@isi_bp.route('/api/'+model.table_name+'/aspek/<string:aspek1>/<string:aspek2>/grup/<string:gi>')
def getPerbandinganAspek(aspek1,aspek2,gi):
    data_gi=gi_model.getById(gi)
    if(data_gi is None):
        return jsonify({'message': model.table_name.capitalize()+' group not found'}), 404
    dataAspek1=aspek_model.getById(aspek1)
    if(dataAspek1 is None):
        return jsonify({'message': model.table_name.capitalize()+' Aspek 1 not found'}), 404
    dataAspek2=aspek_model.getById(aspek2)
    if(dataAspek2 is None):
        return jsonify({'message': model.table_name.capitalize()+' Aspek 2 not found'}), 404
    dfAspek1=model.getAllAspek(aspek1,gi)
    dfAspek2=model.getAllAspek(aspek2,gi)
    fig, ax = plt.subplots()
    ax.scatter(dfAspek1,dfAspek2,alpha=0.5)
    ax.set_xlabel(dataAspek1['name'])
    ax.set_ylabel(dataAspek2['name'])
    ax.set_title(dataAspek1['name']+" VS "+dataAspek2['name']+" "+data_gi['name'])
   # Menggunakan BytesIO untuk menangkap output plot sebagai byte stream
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    # Membuat respons HTTP dengan gambar sebagai byte stream
    return Response(output.getvalue(), mimetype='image/png')
@isi_bp.route('/api/'+model.table_name+'/aspek_indikator/<string:aspek>/<string:indikator>/grup/<string:gi>')
def getPerbandinganAspekIndikator(aspek,indikator,gi):
    data_gi=gi_model.getById(gi)
    if(data_gi is None):
        return jsonify({'message': model.table_name.capitalize()+' group not found'}), 404
    dataAspek=aspek_model.getById(aspek)
    if(dataAspek is None):
        return jsonify({'message': model.table_name.capitalize()+' Aspek not found'}), 404
    dataIndikator=indikator_model.getById(indikator)
    if(dataIndikator is None):
        return jsonify({'message': model.table_name.capitalize()+' Indikator 1 not found'}), 404
    dfAspek=model.getAllAspek(aspek,gi)
    dfIndikator=model.getAllValue(indikator,gi)
    fig, ax = plt.subplots()
    ax.scatter(dfAspek,dfIndikator,alpha=0.5)
    ax.set_xlabel(dataAspek['name'])
    ax.set_ylabel(dataIndikator['name'])
    ax.set_title(dataAspek['name']+" VS "+dataIndikator['name']+" "+data_gi['name'])
   # Menggunakan BytesIO untuk menangkap output plot sebagai byte stream
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)

    # Membuat respons HTTP dengan gambar sebagai byte stream
    return Response(output.getvalue(), mimetype='image/png')
