from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidade_impressionadora.models import Usuario
from flask_login import current_user
#
# class FormCriarConta(FlaskForm):
#     username = StringField('Nome do Usuario', validators=[DataRequired()])
#     email = StringField('E-mail', validators=[DataRequired(), Email()])
#     senha = PasswordField('Senha',validators=[DataRequired(), Length(6 , 20)])
#     confirmacao = PasswordField('Confirmar Senha',validators=[DataRequired(), EqualTo("senha")])
#     botao_submit_criar_conta = SubmitField('Criar Conta')
#
#
#
#
#
# class FormLogin(FlaskForm):
#     email = SubmitField('E-mail',validators=[DataRequired(), Email])
#     Senha = PasswordField('Senha',validators=[DataRequired(), Length(6 , 20)])
#     botao_submit_login = SubmitField('Fazer Login')



class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    #verifica ja tem o e-mail no banco de dados, fazendo com que exista apenas 1 e-mail
    # a facao deve comecar com validate
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail ja cadastrado. Cadastre-se com outro e-mail, ou faça login para continuar')




class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar dados de acesso')
    botao_submit_login = SubmitField('Fazer Login')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar foto do perfil', validators=[FileAllowed(['jpg', 'png', 'jpeg'])] )

    curso_excel = BooleanField('Excel Impressionador')
    curso_vba = BooleanField('VBA Impressionador')
    curso_powerbi = BooleanField('Power BI Impressionador')
    curso_python = BooleanField('Python Impressionador')
    curso_ppt = BooleanField('Power Point Impressionador')
    curso_sql = BooleanField('SQL Impressionador')

    botao_submit_editarperfil = SubmitField('Confirmar ediçao')

    def validate_email(self, email):
        #verificar se mudou de e-mail
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Ja existe um usuario com este e-mail! Cadastre outro e-mail')



class FormCriarPost(FlaskForm):
    titulo = StringField('Titilo do Post', validators=[DataRequired(), Length(2, 140) ])
    corpo = TextAreaField('Escreva seu post aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post')