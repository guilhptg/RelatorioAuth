from sqlalchemy import create_engine, Integer, String, Boolean, Column
from sqlalchemy.orm import sessionmaker, declarative_base

# Criar a pasta onde vai ser salvo o Database
db = create_engine("sqlite:///database/dashboardauth.db")
Session = sessionmaker(bind=db)
session = Session()


Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    nome = Column('nome', String)
    email = Column('email', String, nullable=False)
    senha = Column('senha', String, nullable=False)
    admin = Column('admin', Boolean)

    def __init__(self, nome, email, senha, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.admin = admin



Base.metadata.create_all(bind=db)