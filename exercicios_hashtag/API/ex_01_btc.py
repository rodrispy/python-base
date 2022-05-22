import requests
import json
import matplotlib.pyplot as plt

cotacoes_btc = requests.get('https://economia.awesomeapi.com.br/json/daily/BTC-BRL/100?start_date=20200101&end_date=20201031')
cotacoes_btc_dic = cotacoes_btc.json()

lista_cotacoes_btc = [float(item['bid']) for item in cotacoes_btc_dic]
lista_cotacoes_btc.reverse()
print(lista_cotacoes_btc)

plt.figure(figsize=(15, 5))
plt.plot(lista_cotacoes_btc)
plt.show()