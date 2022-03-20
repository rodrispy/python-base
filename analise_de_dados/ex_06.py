import pandas as pd

# Com um link de download direto
url = 'https://drive.google.com/uc?authuser=0&id=1UzlPy6CZQeAzDXhfc_2sHEyK_Jb50vJs&export=download'
cotacao_df = pd.read_csv(url)
display(cotacao_df)


# Com um link de requisição que precisa ser tratado:
import requests
import io

url = 'http://portalweb.cooxupe.com.br:8080/portal/precohistoricocafe_2.jsp'
conteudo_url = requests.get(url).content
arquivo = io.StringIO(conteudo_url.decode('latin1'))
cafe_df = pd.read_csv(arquivo, sep=r'\t', engine='python')
display(cafe_df)

