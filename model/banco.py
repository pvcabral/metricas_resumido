import pandas as pd 
from sqlalchemy import create_engine

class Banco:
    def __init__(self,conection):
        self.engine = create_engine(conection)
        self.conexao = self.engine.connect()

    def __del__(self):
        self.conexao.close()

    def select(self,sql):
        return pd.read_sql(sql,self.conexao)

