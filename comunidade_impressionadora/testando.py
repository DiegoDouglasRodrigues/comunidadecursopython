from comunidade_impressionadora import app, database
from comunidade_impressionadora.models import Usuario

#
# with app.app_context():
#     database.create_all()


with app.app_context():
    meus_usuario = Usuario.query.all()
    user2 = meus_usuario[2]
    print(user2.username)
    print(user2.email)
    print(user2.senha)


#verificar senha
#bcrypt.check_password_hash(senha_cript, senha)

