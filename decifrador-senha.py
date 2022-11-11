# Durante uma expedição tecnológica, sua equipe encontrou o que parece ser a senha que lhes dá acesso a um grande tesouro digital. Por sorte, sua equipe é formada pelas pessoas mais feras em programação e vocês rapidamente descobriram como decifrá-la.

# Com a possibilidade de que vocês encontrem mais códigos contendo outras senhas, você foi designado à tarefa de desenvolver um algoritmo que decifra os códigos para não precisarem fazer isso de forma manual.

# A senha é representada por um número binário de 10 dígitos formado pelo dígito predominante de cada coluna. Caso a coluna tenha a mesma quantidade de dígitos 0 e 1, deve se considerar o número 1.

# Exemplo: A primeira coluna da lista tem como dígito predominante o número 1, sendo assim, o primeiro dígito - dos 10 - da senha é 1.
# 0110100000
# 1001011111
# 1110001010
# 0111010101
# 0011100110
# 1010011001
# 1101100100
# 1011010100
# 1001100111
# 1000011000

# Desenvolva um algoritmo que receba um array de valores binários (como o exemplo acima) e retorne a representação decimal da senha.

senha = ["0110100000","1001011111","1110001010","0111010101","0011100110","1010011001","1101100100","1011010100","1001100111","1000011000"]

# Definindo a função que separa os números das linhas por colunas
def separa_colunas(senha):
    colunas = []
    numero = ''
    i = 0
    while i < len(senha):
        for linha in senha:
            numero = numero + linha[i]
        i += 1
        colunas.append(numero)
        numero = ''
    return colunas

# Definindo a função que conta a quantidade de zeros e um e traduz para o valor correto
def decifrador(lista):
    binario = ''
    for coluna in lista:
        zero = coluna.count('0')
        um = coluna.count('1')
        if um >= zero:
            binario = binario + '1'
        else:
            binario = binario + '0'
    return binario

# Definindo o conversor de binário para decimal
def binario_para_decimal(binario):
    length = len(binario)
    decimal = 0
    for i in binario:
        if i == '1':
            decimal = decimal + (2**(length-1))
            length = length - 1
        elif i == '0':
            decimal = decimal + 0
            length = length - 1
    return decimal
    

# Rodando o programa completo
lista_colunas = separa_colunas(senha)
binario = decifrador(lista_colunas)
print(binario_para_decimal(binario))
    