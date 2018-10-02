from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://felipebasnun:1a2s3d4f@felipebasnun.mysql.pythonanywhere-services.com/felipebasnun$primeiro'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Relacional
# Orientada a Objeto

# ORM = Object Relational Mapping
# Mapeamento Objeto Relacional


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


@app.route('/')
def index():
    return 'Hello world!'


@app.route('/add/<nnome>/<nemail>')
def add(nnome, nemail):
    novousuario = Usuario(nome=nnome, email=nemail)
    db.session.add(novousuario)
    db.session.commit()
    return "Foi"


@app.route('/listaTudo')
def listaTudo():
    usuarios = Usuario.query.all()
    resposta = ''
    for usuario in usuarios:
        resposta = resposta + 'Nome: '+usuario.nome+' email: '+usuario.email+'<br>'
    return resposta

@app.route('/qualEmail/<nnome>')
def busca(nnome):
    quem = Usuario.query.filter_by(nome=nnome).first()
    return quem.email

@app.route('/delete/<nnome>')
def delete(nnome):
    quem = Usuario.query.filter_by(nome=nnome).first()
    db.session.delete(quem)
    db.session.commit()
    return "Deletei"

@app.route('/atualiza/<nnomeAntigo>/<nnome>')
def atualiza(nnomeAntigo, nnome):
    quem = Usuario.query.filter_by(nome=nnomeAntigo).first()
    quem.nome = nnome
    db.session.add(quem)
    db.session.commit()
    return "Atualizei"


db.create_all()

