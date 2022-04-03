# Aprendendo a tratar dados, manipular colunas e renomeá-las, com o pandas

from sys import displayhook
import pandas as pd

vendas_df = pd.read_csv(r'Contoso - Vendas - 2017.csv', sep=';')
produtos_df = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';')
lojas_df = pd.read_csv(r'Contoso - Lojas.csv', sep=';')
clientes_df = pd.read_csv(r'Contoso - Clientes.csv', sep=';')

display(vendas_df)


# o parametro axis deve ser 1 para indicar colunas
clientes_df = clientes_df.drop(['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10'], axis=1)

# Para pegar apenas algumas colunas da tabela
# Para selecionar mais de 1 coluna é necessário que seja passada uma lista dentro do colchete (por isso do duplo colchete [[]])
clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]


# Juntando os dataframes para ter 1 único dataframe com tudo organizado
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')
display(vendas_df)


# Renomeando o nome de uma coluna
vendas_df = vendas_df.rename(columns={'E-mail': 'E-mail do Cliente'})
display(vendas_df)


# Contando quantas vezes cada cliente comprou na loja
frequencia_clientes = vendas_df['E-mail do Cliente'].value_counts()
display(frequencia_clientes)

# Plotando um gráfico com a frequencia adquirida, dos 5 primeiros itens
frequencia_clientes[:5].plot(figsize=(15,5))


# Qual loja mais vendeu?
# Criando um dataframe que agrupa todos os nomes de loja repetidos e somando os valores
vendas_lojas = vendas_df.groupby('Nome da Loja').sum()


# Selecionando apenas uma coluna dentro do novo dataframe
# Aqui passamos dentro do duplo colchete apenas para que o python organize melhor visualmente a tabela, mas como é apenas 1 coluna não seria obrigatório.
vendas_lojas = vendas_lojas[['Quantidade Vendida']]
display(vendas_lojas)


# Descobrindo a loja que mais vendeu
# Ordenando o dataframe
vendas_lojas = vendas_lojas.sort_values('Quantidade Vendida')
display(vendas_lojas)

# Utilizando os métodos .max() e .idxmax(), para achar o maior valor e o índice do maior valor
maior_valor = vendas_lojas['Quantidade Vendida'].max()
melhor_loja = vendas_lojas['Quantidade Vendida'].idxmax()
print(melhor_loja, maior_valor)

# Utilizando os métodos .min() e .idxmin(), para achar o menor valor e o índice do menor valor
menor_valor = vendas_lojas['Quantidade Vendida'].min()
pior_loja = vendas_lojas['Quantidade Vendida'].idxmin()
print(pior_loja, menor_valor)

# Ou ainda podemos simplesmente pegar o primeiro ou último valor da lista já ordenada em ordem crescente
display(vendas_lojas[:1])
display(vendas_lojas[-1:])