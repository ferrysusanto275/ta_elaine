from flask import Flask,render_template,send_file
from app.controllers.instansi_controller import instansi_bp
from app.controllers.domain_controller import domain_bp
from app.controllers.aspek_controller import aspek_bp
from app.controllers.indikator_controller import indikator_bp
from app.controllers.isi_controller import isi_bp
from app.controllers.predikat_controller import predikat_bp
from app.controllers.grup_instansi_controller import grup_instansi_bp
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
    return render_template("index.html")
@app.route("/grup")
def grup():
    return render_template("grup.html")
@app.route("/predikat")
def predikat():
    return render_template("predikat.html")
@app.route("/domain")
def domain():
    return render_template("domain.html")
@app.route("/aspek")
def aspek():
    return render_template("aspek.html")
@app.route("/instansi")
def instansi():
    return render_template("instansi.html")
@app.route("/indikator")
def indikator():
    return render_template("indikator.html")
@app.route("/assets/js/indikator.js")
def indikatorJs():
    return send_file("static/js/indikator.js")
@app.route("/isi")
def isi():
    return render_template("isi.html")
@app.route("/assets/js/isi.js")
def isiJs():
    return send_file("static/js/isi.js")
@app.route("/index_indikator_instansi")
def tabel_indikator():
    return render_template("tabel_indikator.html")
@app.route("/assets/js/tabel_indikator.js")
def tabel_indikatorJs():
    return send_file("static/js/tabel_indikator.js")
@app.route("/index_aspek_instansi")
def tabel_aspek():
    return render_template("tabel_aspek.html")
@app.route("/assets/js/tabel_aspek.js")
def tabel_aspekJs():
    return send_file("static/js/tabel_aspek.js")
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