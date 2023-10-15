from flask import Flask
from app.controllers.instansi_controller import instansi_bp

app = Flask(__name__)
app.register_blueprint(instansi_bp)