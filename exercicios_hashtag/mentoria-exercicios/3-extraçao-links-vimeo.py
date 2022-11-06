### 3 - Extração dos links de Download de Vídeos do Vimeo
# - Precisamos pegar os links em 1080p, 720p e 540p para importar os vídeos para uma nova plataforma

# para pegar o dicionario do vimeo, use:
from dic import dicionario_vimeo
import pprint

# você precisa chegar em:
# videos = [
#     {'uri': video_uri, 'nome': nome_video, 'duracao': duracao, 'link540p': link540p, 'link720p': link720p, 'link1080p': link1080p},
# ]

# IDENTIFICANDO AS INFORMAÇÕES DO DICIONÁRIO
# CRIANDO UMA LISTA COM AS CHAVES DO DICIONÁRIO 'data'
lista_informacoes = dicionario_vimeo['data']
# pprint.pprint(lista_informacoes)

# IDENTIFICANDO QUAIS AS CHAVES DE CADA SUBDICIONÁRIO
# for chave in lista_informacoes[0]:
#     print(chave)
    
# EXTRAINDO AS INFORMAÇÕES
videos = []
for dicionario_video in lista_informacoes:
    uri = dicionario_video['uri']
    nome = dicionario_video['name']
    duracao = dicionario_video['duration']
    infos_download = dicionario_video['download']
    
    link540p = ''
    link720p = ''
    link1080p = ''
    for dic_download in infos_download:
        if dic_download['rendition'] == '720p':
            link720p = dic_download['link']
        elif dic_download['rendition'] == '540p':
            link540p = dic_download['link']
        elif dic_download['rendition'] == '1080p':
            link1080p = dic_download['link']
            
    videos.append({
        'uri': uri,
        'nome': nome,
        'duracao': duracao,
        'link540p': link540p,
        'link720p': link720p,
        'link1080p': link1080p
    })
    
pprint.pprint(videos)