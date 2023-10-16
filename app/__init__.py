from flask import Flask
from app.controllers.instansi_controller import instansi_bp
from app.controllers.domain_controller import domain_bp

app = Flask(__name__)
app.register_blueprint(instansi_bp)
app.register_blueprint(domain_bp)