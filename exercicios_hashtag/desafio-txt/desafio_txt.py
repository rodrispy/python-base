### Desafio onde vamos aprender:

# - Na Hashtag, sempre analisamos o nosso "Funil de Vendas". Para isso, rastreamos de onde veio os alunos por meio de um código, do tipo:
#    - hashtag_site_org -> Pessoas que vieram pelo site da Hashtag
#    - hashtag_yt_org -> Pessoas que vieram pelo Youtube da Hashtag
#    - hashtag_ig_org -> Pessoas que vieram pelo Instagram da Hashtag
#    - hashtag_igfb_org -> Pessoas que vieram pelo Instagram ou Facebook da Hashtag

# Os códigos diferentes disso, são códigos de anúncio da Hashtag.

# - Queremos analisar quantos alunos vieram de anúncio e quantos vieram "orgânico".
# - Qual a melhor fonte "orgânica" de alunos

# Obs: orgânico é tudo aquilo que não veio de anúncios.

# No nosso sistema, conseguimos exportar um txt com as informações dos alunos, conforme o arquivo Alunos.txt<br>
# (Os dados foram gerados aleatoriamente para simular uma situação real, já que não podemos fornecer os dados reais dos alunos por questões de segurança)

# - No final, para treinar, vamos escrever todas essas respostas em um novo arquivo txt

with open('Alunos.txt', 'r') as arquivo:
    lista_arquivo = arquivo.readlines()

del lista_arquivo[:4]
#print(lista_arquivo)    

org = 0
anuncio = 0
yt = 0
site = 0
ig = 0
igfb = 0
    
for item in lista_arquivo:
    if 'nan' in item:
        anuncio += 1
    if 'site_org' in item:
        site +=1
        org += 1
    if 'yt_org' in item:
        yt +=1
        org += 1
    if 'ig_org' in item:
        ig += 1
        org += 1
    if 'igfb_org' in item:
        igfb += 1
        org += 1
    
        
print(f'Orgânicos: {org}\nAnúncios: {anuncio}')
print(f'Youtube: {yt}\nSite: {site}\nInstagram: {ig}\nFacebook ou Instagram: {igfb}')


with open('Indicadores.txt', 'w') as arquivo_indicadores:
    arquivo_indicadores.write(f'Orgânicos: {org}\nAnúncios: {anuncio}\nYoutube: {yt}\nSite: {site}\nInstagram: {ig}\nFacebook ou Instagram: {igfb}')