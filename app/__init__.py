from flask import Flask,render_template,send_file,request
from app.controllers.instansi_controller import instansi_bp
from app.controllers.domain_controller import domain_bp
from app.controllers.aspek_controller import aspek_bp
from app.controllers.indikator_controller import indikator_bp
from app.controllers.isi_controller import isi_bp
from app.controllers.predikat_controller import predikat_bp
from app.controllers.grup_instansi_controller import grup_instansi_bp
min_year=2021
app = Flask(__name__, template_folder='views')
app.register_blueprint(instansi_bp)
app.register_blueprint(domain_bp)
app.register_blueprint(aspek_bp)
app.register_blueprint(indikator_bp)
app.register_blueprint(isi_bp)
app.register_blueprint(predikat_bp)
app.register_blueprint(grup_instansi_bp)
# front end
@app.route("/")
def index():
    return render_template("index.html",page_url=request.path)
@app.route("/grup")
def grup():
    return render_template("grup.html",page_url=request.path)
@app.route("/predikat")
def predikat():
    return render_template("predikat.html",page_url=request.path)
@app.route("/domain")
def domain():
    return render_template("domain.html",page_url=request.path)
@app.route("/aspek")
def aspek():
    return render_template("aspek.html",page_url=request.path)
@app.route("/instansi")
def instansi():
    return render_template("instansi.html",page_url=request.path)
@app.route("/indikator")
def indikator():
    return render_template("indikator.html",page_url=request.path)
@app.route("/assets/js/indikator.js")
def indikatorJs():
    return send_file("static/js/indikator.js")
@app.route("/isi")
def isi():
    return render_template("isi.html",page_url=request.path,min_year=min_year)
@app.route("/assets/js/isi.js")
def isiJs():
    return send_file("static/js/isi.js")
@app.route("/index_indikator_instansi")
def tabel_indikator():
    return render_template("tabel_indikator.html",page_url=request.path,min_year=min_year)
@app.route("/assets/js/tabel_indikator.js")
def tabel_indikatorJs():
    return send_file("static/js/tabel_indikator.js")
@app.route("/index_aspek_instansi")
def tabel_aspek():
    return render_template("tabel_aspek.html",page_url=request.path,min_year=min_year)
@app.route("/assets/js/tabel_aspek.js")
def tabel_aspekJs():
    return send_file("static/js/tabel_aspek.js")
@app.route("/index_domain_instansi")
def tabel_domain():
    return render_template("tabel_domain.html",page_url=request.path,min_year=min_year)
@app.route("/assets/js/tabel_domain.js")
def tabel_domainJs():
    return send_file("static/js/tabel_domain.js")
@app.route("/perbandingan_indikator")
def perbandingan_indikator():
    return render_template("perbandingan_indikator.html",page_url=request.path)
@app.route("/assets/js/perbandingan_indikator.js")
def perbandingan_indikatorJs():
    return send_file("static/js/perbandingan_indikator.js")
@app.route("/assets/css/perbandingan_indikator.css")
def perbandingan_indikatorCss():
    return send_file("static/css/perbandingan_indikator.css")
@app.route("/perbandingan_aspek")
def perbandingan_aspek():
    return render_template("perbandingan_aspek.html",page_url=request.path)
@app.route("/assets/js/perbandingan_aspek.js")
def perbandingan_aspekJs():
    return send_file("static/js/perbandingan_aspek.js")
@app.route("/perbandingan_aspek_indikator")
def perbandingan_aspek_indikator():
    return render_template("perbandingan_aspek_indikator.html",page_url=request.path)
@app.route("/assets/js/perbandingan_aspek_indikator.js")
def perbandingan_aspek_indikatorJs():
    return send_file("static/js/perbandingan_aspek_indikator.js")
@app.route("/perbandingan_domain")
def perbandingan_domain():
    return render_template("perbandingan_domain.html",page_url=request.path)
@app.route("/assets/js/perbandingan_domain.js")
def perbandingan_domainJs():
    return send_file("static/js/perbandingan_domain.js")
@app.route("/perbandingan_domain_aspek")
def perbandingan_domain_aspek():
    return render_template("perbandingan_domain_aspek.html",page_url=request.path)
@app.route("/assets/js/perbandingan_domain_aspek.js")
def perbandingan_domain_aspekJs():
    return send_file("static/js/perbandingan_domain_aspek.js")
@app.route("/perbandingan_domain_indikator")
def perbandingan_domain_indikator():
    return render_template("perbandingan_domain_indikator.html",page_url=request.path)
@app.route("/assets/js/perbandingan_domain_indikator.js")
def perbandingan_domain_indikatorJs():
    return send_file("static/js/perbandingan_domain_indikator.js")
@app.route("/perbandingan_index_indikator")
def perbandingan_index_indikator():
    return render_template("perbandingan_index_indikator.html",page_url=request.path)
@app.route("/assets/js/perbandingan_index_indikator.js")
def perbandingan_index_indikatorJs():
    return send_file("static/js/perbandingan_index_indikator.js")
@app.route("/perbandingan_index_aspek")
def perbandingan_index_aspek():
    return render_template("perbandingan_index_aspek.html",page_url=request.path)
@app.route("/assets/js/perbandingan_index_aspek.js")
def perbandingan_index_aspekJs():
    return send_file("static/js/perbandingan_index_aspek.js")
@app.route("/perbandingan_index_domain")
def perbandingan_index_domain():
    return render_template("perbandingan_index_domain.html",page_url=request.path)
@app.route("/assets/js/perbandingan_index_domain.js")
def perbandingan_index_domainJs():
    return send_file("static/js/perbandingan_index_domain.js")
@app.route("/elbow_indikator")
def elbow_indikator():
    return render_template("elbow_indikator.html",page_url=request.path)
@app.route("/assets/js/elbow_indikator.js")
def elbow_indikatorJs():
    return send_file("static/js/elbow_indikator.js")
@app.route("/elbow_aspek")
def elbow_aspek():
    return render_template("elbow_aspek.html",page_url=request.path)
@app.route("/assets/js/elbow_aspek.js")
def elbow_aspekJs():
    return send_file("static/js/elbow_aspek.js")
@app.route("/elbow_aspek_indikator")
def elbow_aspek_indikator():
    return render_template("elbow_aspek_indikator.html",page_url=request.path)
@app.route("/assets/js/elbow_aspek_indikator.js")
def elbow_aspek_indikatorJs():
    return send_file("static/js/elbow_aspek_indikator.js")
# static page
@app.route("/assets/js/main.js")
def mainJs():
    return send_file("static/js/main.js")
@app.route("/assets/js/grup.js")
def grupJs():
    return send_file("static/js/grup.js")
@app.route("/assets/js/domain.js")
def domainJs():
    return send_file("static/js/domain.js")
@app.route("/assets/js/aspek.js")
def aspekJs():
    return send_file("static/js/aspek.js")
@app.route("/assets/js/predikat.js")
def predikatJs():
    return send_file("static/js/predikat.js")
@app.route("/assets/js/instansi.js")
def instansiJs():
    return send_file("static/js/instansi.js")
@app.route("/assets/css/main.css")
def maincss():
    return send_file("static/css/main.css")