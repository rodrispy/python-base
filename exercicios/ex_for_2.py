## 1. Calculando % de uma lista

# Faremos algo parecido com "filtrar" uma lista. Mais pra frente no curso aprenderemos outras formas de fazer isso, mas com o nosso conhecimento atual já conseguimos resolver o desafio.
# Digamos que a gente tenha uma lista de vendedores e ao invés de saber todos os vendedores que bateram a meta, eu quero conseguir calcular a % de vendedores que bateram a meta. Ou seja, se temos 10 vendedores e 3 bateram a meta, temos 30% dos vendedores que bateram a meta.

meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

# Vamos resolver de 2 formas:
# Criando uma lista auxiliar apenas com os vendedores que bateram a meta

lista_bateu_meta = []

for item in vendas:
    if item[1] >= meta:
        if item[0] in lista_bateu_meta:
            pass
        else:
            lista_bateu_meta.append(item[0])

print(f'Vendedores que bateram a meta: ')
for item in lista_bateu_meta:
    print(item)

print()
print(f'A porcentagem de vendedores que bateram a meta foi de {len(lista_bateu_meta) / len(vendas):.1%}')
        
            
# Fazendo o cálculo diretamente na lista que já temos
qtde_vendedores_acima = 0

for venda in vendas:
    if venda[1] >= meta:
        qtde_vendedores_acima += 1

print(f'A porcentagem de vendedores que bateram a meta foi de {qtde_vendedores_acima / len(vendas):.1%}')


## Para treinar uma estrutura parecida, crie um código para responder: quem foi o vendedor que mais vendeu?
melhor_vendedor = ''
maior_vendas = 0

for venda in vendas:
    if venda[1] > maior_vendas:
        maior_vendas = venda[1]
        melhor_vendedor = venda[0]

print(f'O melhor vendedor foi {melhor_vendedor} com {maior_vendas}.')