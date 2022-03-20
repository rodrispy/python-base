# Modificando o DataFrame
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


# Convertendo os valores da coluna de datas para valores que serão objetos data
vendas_df['Data da Venda'] = pd.to_datetime(vendas_df['Data da Venda'], format='%d/%m/%Y')

# Extraindo as datas de forma simples: criando colunas para anos meses e dias
vendas_df['Ano da Venda'] = vendas_df['Data da Venda'].dt.year
vendas_df['Mes da Venda'] = vendas_df['Data da Venda'].dt.month
vendas_df['Dia da Venda'] = vendas_df['Data da Venda'].dt.day


# Modificando valores específicos
# O método .head() pega as 5 primeiras linhas da tabela
novo_produtos_df = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';')
display(novo_produtos_df.head())

# Setando o índice do DF como a coluna Nome do Produto
novo_produtos_df = novo_produtos_df.set_index('Nome do Produto')

# Para modificar o preço do produto ID 873 (Contoso Wireless Laser Mouse E50 Grey) para 23 reais
# Utilizando o método .loc[]
novo_produtos_df.loc['Contoso Wireless Laser Mouse E50 Grey', 'Preco Unitario'] = 23
display(novo_produtos_df.head())

# Poderíamos fazer também através da seleção de outra coluna:
novo_produtos_df.loc[novo_produtos_df['ID Produto'] == 873, 'Preco Unitario'] = 23
display(novo_produtos_df.head())