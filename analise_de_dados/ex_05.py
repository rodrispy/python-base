import pandas as pd

vendas_produtos = {'iphone': [558147, 951642], 'galaxy': [712350, 244295], 'ipad': [573823, 26964], 'tv': [405252, 787604], 'máquina de café': [718654, 867660], 'kindle': [531580, 78830], 'geladeira': [973139, 710331], 'adega': [892292, 646016], 'notebook dell': [422760, 694913], 'notebook hp': [154753, 539704], 'notebook asus': [887061, 324831], 'microsoft surface': [438508, 667179], 'webcam': [237467, 295633], 'caixa de som': [489705, 725316], 'microfone': [328311, 644622], 'câmera canon': [591120, 994303]}

# Transformando um dicionário em um dataframe
# Por padrão, as chaves do dicionário viram as colunas e os valores viram as linhas;
vendas_produtos_df = pd.DataFrame.from_dict(vendas_produtos)
display(vendas_produtos_df)


# Para transformar as chaves em índices podemos utilizar o parâmetro orient:
vendas_produtos_df = pd.DataFrame.from_dict(vendas_produtos, orient='index')
display(vendas_produtos_df)

# Renomeando as colunas
vendas_produtos_df = vendas_produtos_df.rename(columns={0: 'Vendas 2019', 1: 'Vendas 2020'})
display(vendas_produtos_df)


# Exportando para .csv
# Adicionando o parâmetro encoding para resolver o problema dos caracteres especiais
vendas_produtos_df.to_csv(r'Tabela.csv', sep=';', encoding='latin1')