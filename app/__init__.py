from flask import Flask,render_template,send_file
from app.controllers.instansi_controller import instansi_bp
from app.controllers.domain_controller import domain_bp
from app.controllers.aspek_controller import aspek_bp
from app.controllers.indikator_controller import indikator_bp
from app.controllers.isi_controller import isi_bp

app = Flask(__name__, template_folder='views')
app.register_blueprint(instansi_bp)
app.register_blueprint(domain_bp)
app.register_blueprint(aspek_bp)
app.register_blueprint(indikator_bp)
app.register_blueprint(isi_bp)
# front end
@app.route("/")
def index():
    return render_template("index.html")
# static page
@app.route("/assets/js/main.js")
def mainJs():
    return send_file("static/js/main.js")
@app.route("/assets/css/main.css")
def maincss():
    return send_file("static/css/main.css")