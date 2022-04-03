# Desafio: criar uma tabela apenas com as vendas da loja Contoso Europe Online e que não tiveram nenhuma devolução
# Criar essa tabela e saber quantas vendas são.

from sys import displayhook
import pandas as pd

# PRIMEIROS PASSOS - PADRÃO
vendas_df = pd.read_csv(r'Contoso - Vendas - 2017.csv', sep=';')
produtos_df = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';')
lojas_df = pd.read_csv(r'Contoso - Lojas.csv', sep=';')
clientes_df = pd.read_csv(r'Contoso - Clientes.csv', sep=';')

# Para selecionar mais de 1 coluna é necessário que seja passada uma lista dentro do colchete (por isso do duplo colchete [[]])
clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]

# Juntando os dataframes para ter 1 único dataframe com tudo organizado
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')
# PRIMEIROS PASSOS - PADRÃO



# tudo junto:
df_loja306semdev = vendas_df[(vendas_df['ID Loja'] == 306) & (vendas_df['Quantidade Devolvida'] == 0)]
display(df_loja306semdev)

# separado:
loja306 = vendas_df['ID Loja'] == 306
qtde_devolvida_0 = vendas_df['Quantidade Devolvida'] == 0
df2_loja306semdev = vendas_df[loja306 & qtde_devolvida_0]
display(df2_loja306semdev)