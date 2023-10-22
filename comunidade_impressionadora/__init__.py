from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
#from comunidade_impressionadora.models import Usuario, Post

app = Flask(__name__)

# passo a passo para criar uma nova pagina
#route / funcao / html / barra
# importar os formularios para dentro do main.py
#criar uma instancia dentro da pagina de login e passou para o html

app.config['SECRET_KEY'] = 'exit65a7537d04071fe0650c19be550a2c90'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco_dados.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
LoginManager = LoginManager(app)
LoginManager.login_view = 'login_criar_conta'




from comunidade_impressionadora import routes
