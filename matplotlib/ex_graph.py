import matplotlib.pyplot as plt
import numpy as np

vendas_meses = [1500, 1727, 1350, 999, 1050, 1027, 1022, 1500, 2000, 2362, 2100, 2762]
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

plt.plot(meses, vendas_meses, 'ro', color='blue') # 'ro' é o parametro do tipo de apontamento no grafico (pontos, linhas, etc)
plt.ylabel('Vendas')
plt.xlabel('Meses')
plt.axis([0, 12, 0, max(vendas_meses)+500])
plt.show

plt.plot(meses, vendas_meses, color='green')
plt.ylabel('Vendas')
plt.xlabel('Meses')
plt.axis([0, 12, 0, max(vendas_meses)+500])
plt.show


# grafico de dispersão
plt.scatter(meses, vendas_meses)
plt.show()

# grafico de barras
plt.bar(meses, vendas_meses)
plt.show()

# multiplos graficos
plt.figure(1, figsize=(15, 10))
plt.subplot(1, 3, 1)
plt.plot(meses, vendas_meses, color='green')
plt.ylabel('Vendas')
plt.xlabel('Meses')
plt.axis([0, 12, 0, max(vendas_meses)+500])
plt.show()

plt.subplot(1, 3, 2)
plt.scatter(meses, vendas_meses)
plt.show()

plt.subplot(1, 3, 3)
plt.bar(meses, vendas_meses)
plt.show()