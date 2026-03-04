# Importa o sqlalchemy e passa os parametros necessários para uma tabela
from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
# Importa a função para traduzir o código em comando SQL
from sqlalchemy.orm import declarative_base
# Formatação especial para o tipo de String (utilizado na coluna STATUS DO PEDIDO)
from sqlalchemy_utils.types import ChoiceType 

# Cria a conexão do banco de dados
db = create_engine("sqlite:///banco.db")

# Cria a base do banco de dados
Base = declarative_base()


# Classes/Tabelas do banco

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String, nullable=False)
    email = Column('email', String, nullable=False)
    senha = Column('senha', String, nullable=False)
    ativo = Column('ativo', Boolean, default=True)
    admin = Column('admin', Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

class Pedido(Base):
    __tablename__ = 'pedidos'

    #STATUS_PEDIDO = (
     #   ('PENDENTE', 'PENDENTE'),
     #   ('FINALIZADO', 'FINALIZADO'),
     #   ('CANCELADO', 'CANCELADO')
    #)

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    status = Column('status', String) 
    usuario = Column('usuario', String, ForeignKey("usuarios.id")) 
    preco = Column('preco', Float)
    #itens = 

    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario
        self.status = status
        self.preco = preco

class ItensPedido(Base):
    __tablename__ = 'pedido_itens'

   # TAMANHO_PIZZA = (
   #     ('PEQUENA', 'PEQUENA'),
   #     ('MEDIA', 'MEDIA'),
   #     ('GRANDE', 'GRANDE')
    #)

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    quantidade = Column('quantidade', Integer)
    sabor = Column('sabor', String)
    tamanho = Column('tamanho', String) 
    preco_unitario = Column('preco_unitario', Float)
    pedido = Column('pedido', ForeignKey('pedidos.id'))

    def __init__(self, sabor, tamanho, pedido, preco_unitario, quantidade):
        self.sabor = sabor
        self.tamanho = tamanho
        self.pedido = pedido
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade

    