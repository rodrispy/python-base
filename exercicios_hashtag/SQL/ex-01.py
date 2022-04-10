import pyodbc
import pandas as pd

dados_conexao = ("Driver={SQL Server};"
                 "Server=CHARLESEPI0L;"
                 "Database=ContosoRetailDW;")
conexao = pyodbc.connect(dados_conexao)
print('Conexão bem sucedida')
cursor = conexao.cursor()

produtos_df = pd.read_sql('SELECT * FROM ContosoRetailDW.dbo.DimProduct', conexao)
display(produtos_df)