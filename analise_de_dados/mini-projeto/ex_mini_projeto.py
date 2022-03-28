# Exercício - Mini Projeto de Análise de Dados

# Temos os dados de 2019 de uma empresa de prestação de serviços. 
# - CadastroFuncionarios
# - CadastroClientes
# - BaseServiçosPrestados

# Obs1: Para ler arquivos csv, temos o read_csv<br>
# Obs2: Para ler arquivos xlsx (arquivos em excel normais, que não são padrão csv), temos o read_excel

# 1. Valor Total da Folha Salarial -> Qual foi o gasto total com salários de funcionários pela empresa? <br>
#    Sugestão: calcule o salário total de cada funcionário, salário + benefícios + impostos, depois some todos os salários
       
# 2. Qual foi o faturamento da empresa?<br>
#    Sugestão: calcule o faturamento total de cada serviço e depois some o faturamento de todos
     
# 3. Qual o % de funcionários que já fechou algum contrato?<br>
#    Sugestão: na base de serviços temos o funcionário que fechou cada serviço. Mas nem todos os funcionários que a empresa tem já fecharam algum serviço.<br>
#    . Na base de funcionários temos uma lista com todos os funcionários<br>
#    . Queremos calcular Qtde_Funcionarios_Fecharam_Serviço / Qtde_Funcionários_Totais<br>
#    . Para calcular a qtde de funcionários que fecharam algum serviço, use a base de serviços e conte quantos funcionários tem ali. Mas lembre-se, cada funcionário só pode ser contado uma única vez.<br><br>
#    Dica: se você aplicar o método .unique() em uma variável que é apenas 1 coluna de um dataframe, ele vai excluir todos os valores duplicados daquela coluna.<br>
#    Ex: unicos_colunaA = dataframe['colunaA'].unique() te dá como resposta uma lista com todos os itens da colunaA aparecendo uma única vez. Todos os valores repetidos da colunaA são excluidos da variável unicos_colunaA 
       
# 4. Calcule o total de contratos que cada área da empresa já fechou

# 5. Calcule o total de funcionários por área

#6. Qual o ticket médio mensal (faturamento médio mensal) dos contratos?<br>
#    Dica: .mean() calcula a média -> exemplo: media_colunaA = dataframe['colunaA'].mean()

# Obs: Lembrando as opções mais usuais de encoding:<br>
# encoding='latin1', encoding='ISO-8859-1', encoding='utf-8' ou então encoding='cp1252'


import pandas as pd

funcionarios_df = pd.read_csv('CadastroFuncionarios.csv', sep=';', decimal=',')
display(funcionarios_df)

#1 Calculando o valor total da folha salarial
