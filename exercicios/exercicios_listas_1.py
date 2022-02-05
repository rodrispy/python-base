# Exercícios sobre Listas, do curso Python Impressionador da Hashtag

## 1. Faturamento do Melhor e do Pior Mês do Ano
# Qual foi o valor de vendas do melhor mês do Ano?
# E valor do pior mês do ano?

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

# Somando as listas
vendas = vendas_1sem + vendas_2sem

# Identificando o maior e menor valor
maiorValor = max(vendas)
menorValor = min(vendas)

# Identificando o mês do maior e menor valor
melhorMes = vendas.index(maiorValor)
piorMes = vendas.index(menorValor)


## 2. Continuação
# Agora relacione as duas listas para printar 'O melhor mês do ano foi {} com {} vendas' e o mesmo para o pior mês do ano.
# Calcule também o faturamento total do Ano e quanto que o melhor mês representou do faturamento total.
# Obs: Para o faturamento total, pode usar a função sum(lista) que soma todos os itens de uma lista

print(f'O melhor mês do ano foi {meses[melhorMes]} com {maiorValor} vendas, \nE o pior mês do ano foi {meses[piorMes]} com {menorValor} vendas.')

# Calculando o total com o metodo sum()
total = sum(vendas)
print(f'O faturamento total foi de R$ {total:.2f}.')

# Percentual
percentual = (maiorValor / total)
print(f'O maior mês representa {percentual:.2%} do total de vendas.')

## 3. Crie uma lista com o top 3 valores de vendas do ano (sem fazer "no olho")
# Dica: o método remove retira um item da lista.

top3 = []

# Duplicando a lista, utilizando o metodo copy() para não perder a posição em relação aos meses e removendo o maior valor
lista_temp = vendas.copy()

# O maior valor já é o primeiro do top 3
# Criando um loop para encontrar os 3 maiores valores, removendo o item de maior valor da lista temporaria e adicionando-o no top3
x = 1
while x < 4:
    top3.append(max(lista_temp))
    lista_temp.remove(max(lista_temp))
    x += 1

# Relacionando os top valores com a lista dos meses
# Criando um for simples com range do tamanho da lista
# Cada índice do top3 corresponderá a um valor da lista original de vendas, e com isso podemos relacionar a posição de cada valor com a posição de cada mes na lista meses
print(f'Os meses com maiores vendas foram:')
for i in range(0, len(top3)):
    print(f'{meses[vendas.index(top3[i])]} com {top3[i]}')

teste