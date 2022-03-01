# Exercícios sobre Listas, do curso Python Impressionador da Hashtag

## 1. Mudança de Carga Tributária
# Reformas e mudanças de cargas tributárias são bem comuns no Brasil.
# Digamos que você trabalhe em uma empresa de ecommerce
# No Brasil, o imposto sobre livros é zerado. De um ano para o outro, o governo criou um novo imposto que incide em 10% sobre o valor dos livros e agora você precisa alterar o registro dos preços dos livros da empresa para garantir que esse imposto vai ser repassado para o preço final do produto.

# Crie um código que recalcule o valor do livro da sua lista de produtos e ajuste na tabela.
# Além disso, calcule qual vai ser o impacto financeiro da criação desse imposto para a empresa (ou seja, quanto que o imposto vai aumentar de custo para a empresa)

from re import I


produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 'ar condicionado', 'alexa', 'máquina de café', 'kindle']

# Cada item da lista dos produtos corresponde a quantidade de vendas no mês e preço, nessa ordem
produtos_ecommerce = [
    [10000, 2500],
    [50000, 40],
    [7000, 1200],
    [20000, 1500],
    [5800, 1300],
    [7200, 2500],
    [200, 800],
    [3300, 700],
    [1900, 400]
]

## Resolução
# Verificando se o produto existe na lista
# Calculando o valor do imposto e substituindo o valor na lista
if 'livro' in produtos:
    i_livro = produtos.index('livro')
    produtos_ecommerce[i_livro][1] = produtos_ecommerce[i_livro][1] * 1.1
    print(f'O novo valor de cada livro será de R$ {produtos_ecommerce[i_livro][1]:.2f}')
else:
    print('Não temos livros no estoque')