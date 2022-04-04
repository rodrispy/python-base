### Desafio

# Você trabalha em uma empresa que tem 18 lojas espalhadas por todo o Brasil e divididas em 5 estados diferentes:
#- RJ
#- SP
#- MG
#- GO
#- AM

# Todo trimestre, são calculados os indicadores de cada funcionário de cada loja e esses indicadores são armazenados em um arquivo em Excel.
# Cada estado tem 1 Gerente Geral responsável por todas as lojas daqueles estados.
# Pediram para você enviar para cada Gerente Geral todas as bases de indicadores correspondentes às lojas que ele é responsável, porque a equipe deles precisa desses indicadores.
# Obs: Não vamos enviar por e-mail porque ainda não aprendemos a fazer isso, mas vamos deixar todos os arquivos em uma pasta única para cada gerente, ou seja, para cada estado.

# Então o seu desafio é separar todos os arquivos de forma que cada arquivo esteja na pasta do estado correspondente aquele arquivo.
# Obs: Para pegar o nome de um arquivo como um texto no pathlib, você pode usar Path.name ou arquivo.name:<br>

# caminho = Path('Pasta/Arquivo.csv')
# print(caminho.name) -> resposta: 'Arquivo.csv'


from pathlib import Path
import shutil

# Criando todas as pastas
Path('Estados').mkdir()

estados = ['RJ', 'SP', 'MG', 'GO', 'AM']
for estado in estados:
    Path(f'Estados/{estado}').mkdir()

# Definindo os caminhos em variáveis para facilitar a escrita
caminho_original = Path('Arquivos_Lojas/')
caminho_nova_pasta = Path('Estados/')

# Verificando se o arquivo selecionado é um .csv
arquivos = caminho_original.iterdir()
for arquivo in arquivos:
    nome_arquivo = arquivo.name
    if nome_arquivo[-3:] == 'csv':
        estado = nome_arquivo[-6:-4]
        shutil.copy2(arquivo, (caminho_nova_pasta/Path(f'{estado}/{nome_arquivo}')))
                         
