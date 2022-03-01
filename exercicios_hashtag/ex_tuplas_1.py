## 1. Análise de Vendas

# Nesse exercício vamos fazer uma "análise simples" de atingimento de Meta.
# Temos uma lista com os vendedores e os valores de vendas e queremos identificar (printar) quais os vendedores que bateram a meta e qual foi o valor que eles venderam.

meta = 10000
vendas = [
    ('João', 15000),
    ('Julia', 27000),
    ('Marcus', 9900),
    ('Maria', 3750),
    ('Ana', 10300),
    ('Alon', 7870),
]

# Unpacking das tuplas direto no for (vendedor corresponde à vendas[0], qtde correspode à vendas[1])
for vendedor, qtde in vendas:
    if qtde >= meta:
        print(f'{vendedor} bateu a meta, vendeu {qtde} unidades.')
        
        
## 2. Comparação com Ano Anterior

# Digamos que você está analisando as vendas de produtos de um ecommerce e quer identificar quais produtos tiveram no ano de 2020 mais vendas do que no ano de 2019, para reportar isso para a diretoria.
# Sua resposta pode ser um print de cada produto, qual foi a venda de 2019, a venda de 2020 e o % de crescimento de 2020 para 2019.
# Lembrando, para calcular o % de crescimento de um produto de um ano para o outro, podemos fazer: (vendas_produto2020/vendas_produto2019 - 1)
# A lógica da tupla é: (produto, vendas2019, vendas2020)

vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604), ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331), ('adega', 892292, 646016), ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704), ('notebook asus', 887061, 324831), ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633), ('caixa de som', 489705, 725316), ('microfone', 328311, 644622), ('câmera canon', 591120, 994303)]

for produto, vendas2019, vendas2020 in vendas_produtos:
    if vendas2019 < vendas2020:
        crescimento = (vendas2020/vendas2019) - 1
        print(f'{produto.capitalize()} vendeu {vendas2019} em 2019 e {vendas2020} em 2020, com um crescimento de {crescimento:.2%}')