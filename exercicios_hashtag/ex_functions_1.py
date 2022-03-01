# Exercícios

## 1. Function para Cálculo de Carga Tributária

# Imagine que você trabalha no setor contábil de uma grande empresa de Varejo. 

# Crie uma function que calcule qual o % de carga tributária que está sendo aplicado sobre um determinado produto, dado o preço de venda, o "lucro" e os custos (com exceção do imposto) dele.
# Repare que preço - custo não é igual ao lucro, porque ainda foi descontado o imposto. Sua functiona deve calcular qual foi o % de imposto aplicado sobre o preço total.

preco = 1500
custo = 400
lucro = 800

def calculaCarga(preco, custo, lucro):
    imposto = preco - custo - lucro
    return imposto / preco

print(f'A carga tributaria foi de {calculaCarga(preco, custo, lucro):.1%}')
    