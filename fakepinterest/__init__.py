#Arquivo necessario para inicializar o site para o uso do flax
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt           #Necessario para cryptografia


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db" #Necessario para criar o banco de dados
app.config["SECRET_KEY"] = "2dcd10741ea93c932d3d88548ae6efd8"
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"   #homepage prq vai ser na homepage o login


from fakepinterest import routs
