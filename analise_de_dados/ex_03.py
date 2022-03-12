# Filtrando um dataframe
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
display(vendas_df)
# PRIMEIROS PASSOS - PADRÃO



# Calculando a % de vendas que foi devolvido
qtde_vendida = vendas_df['Quantidade Vendida'].sum()
qtde_devolvida = vendas_df['Quantidade Devolvida'].sum()
print(f'{(qtde_devolvida / qtde_vendida):.2%}')


# Se quisermos fazer a mesma análise apenas para 1 loja
# Primeiro vamos filtrar pelo ID da loja. O pandas já tem uma funcionalidade parecida com uma condicional para isso
# O que fazemos é passar uma lista para o dataframe a ser criado, de True or False para cada ID de Loja. Se a informação é verdadeira, ele aplica no filtro, se não, não aplica
vendas_lojaeuropeonline = vendas_df[vendas_df['ID Loja'] == 306]
display(vendas_lojaeuropeonline)

# Outra forma de se fazer seria:
loja306 = vendas_df['ID Loja'] == 306
vendas_lojaeuropeonline = vendas_df[loja306]


# Agora repetindo o procedimento para o calculo da % de vendas devolvidas
qtde_vendida = vendas_lojaeuropeonline['Quantidade Vendida'].sum()
qtde_devolvida = vendas_lojaeuropeonline['Quantidade Devolvida'].sum()
print(f'{(qtde_devolvida / qtde_vendida):.2%}')


