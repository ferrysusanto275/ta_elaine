from flask import Flask
from app.controllers.instansi_controller import instansi_bp
from app.controllers.domain_controller import domain_bp
from app.controllers.aspek_controller import aspek_bp
from app.controllers.indikator_controller import indikator_bp

app = Flask(__name__)
app.register_blueprint(instansi_bp)
app.register_blueprint(domain_bp)
app.register_blueprint(aspek_bp)
app.register_blueprint(indikator_bp)