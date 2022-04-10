### Nesse desafio, vamos fazer uma consulta em SQL com uma condição e fazer o tratamento das informações no Python usando o pandas

# - Calcule o lucro diário da empresa 

#- Tabela com as Vendas -> dbo.FactSales
#- Lucro é -> Sales Amount - TotalCost - DiscountAmount
#- Lembre que podemos ter mais de 1 transação por dia na tabela, então uma opção é usar o método groupby do pandas
#- Sugestão para ajudar na análise é plotar um gráfico do lucro diário

import pyodbc
import pandas as pd

dados_conexao = ("Driver={SQL Server};"
                 "Server=CHARLESEPI0L;"
                 "Database=ContosoRetailDW;")
conexao = pyodbc.connect(dados_conexao)
print('Conexão bem sucedida')
cursor = conexao.cursor()

# Puxando a tabela de vendas da base de dados
vendas_df = pd.read_sql('SELECT * FROM ContosoRetailDW.dbo.FactSales', conexao)

# Criando a coluna do lucro
vendas_df['Lucro'] = vendas_df['SalesAmount'] - vendas_df['TotalCost'] - vendas_df['DiscountAmount']

vendas_diarias_df = vendas_df.groupby(['DateKey']).sum()
vendas_diarias_df['Lucro'].plot(figsize=(15, 5))
