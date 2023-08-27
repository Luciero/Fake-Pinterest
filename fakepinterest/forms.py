#Criar formularios do nosso site
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest.models import Usuario


class FormLogin(FlaskForm):
    email = EmailField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Confirmar")


class FormCriarConta(FlaskForm):
    email = EmailField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Nome de usuario", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confimar_senha = PasswordField("Confirmar Senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            return ValidationError("E-mail ja cadastrado, cadastre-se novamente!")

class FormFoto(FlaskForm):
    imagem = FileField("Foto", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Enviar")