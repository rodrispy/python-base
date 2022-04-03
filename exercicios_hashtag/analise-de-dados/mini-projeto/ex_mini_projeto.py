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


### Programa principal
# Importação de módulos e arquivos
import pandas as pd

funcionarios_df = pd.read_csv('CadastroFuncionarios.csv', sep=';', decimal=',')
clientes_df = pd.read_csv('CadastroClientes.csv', sep=';', decimal=',')
servicos_df = pd.read_excel('BaseServiçosPrestados.xlsx')

# Retirar colunas Estado Civil e Cargo da tabela de funcionários
# Lista de colunas, axis=1 para indicar coluna
funcionarios_df = funcionarios_df.drop(['Estado Civil', 'Cargo'], axis=1)

display(funcionarios_df)
display(clientes_df)
display(servicos_df)

##1 Folha Salarial
funcionarios_df['Salario Total'] = funcionarios_df['Salario Base'] + funcionarios_df['Impostos'] + funcionarios_df['Beneficios'] + funcionarios_df['VT'] + funcionarios_df['VR']

print(f'Total da Folha Salarial Mensal é de R$ {funcionarios_df["Salario Total"].sum():,}')

##2 Faturamento da Empresa
# Criando um DF auxiliar com as colunas das outras tabelas que serão necessárias para o cálculo e dando um merge de acordo com o ID do cliente
faturamentos_df = servicos_df[['ID Cliente', 'Tempo Total de Contrato (Meses)']].merge(clientes_df[['ID Cliente', 'Valor Contrato Mensal']], on='ID Cliente')

# Criando a coluna de faturamento para cada cliente e somando tudo ao final
faturamentos_df['Faturamento Total'] = faturamentos_df['Tempo Total de Contrato (Meses)'] * faturamentos_df['Valor Contrato Mensal']

print(f'Faturamento Total: R${sum(faturamentos_df["Faturamento Total"]):,}')

##3 % Funcionários Fecharam Contrato
# Utilizando o método .unique() para pegar apenas valores únicos da coluna
qtde_funcionarios_contrato = len(servicos_df['ID Funcionário'].unique())
qtde_funcionarios_total = len(funcionarios_df['ID Funcionário'])
print(f'Percentual de funcionários que fecharam contrato: {qtde_funcionarios_contrato/qtde_funcionarios_total:.2%}')

##4 Quantidade de Contratos por Área
contratos_area_df = servicos_df[['ID Funcionário']].merge(funcionarios_df[['ID Funcionário', 'Area']], on='ID Funcionário')
display(contratos_area_df)

contratos_area_qtde = contratos_area_df['Area'].value_counts()
print(contratos_area_qtde)

##5 Funcionários por Área
funcionarios_area = funcionarios_df['Area'].value_counts()
funcionarios_area.plot(kind='bar')

##6 Ticket Médio Mensal
ticket_medio = clientes_df['Valor Contrato Mensal'].mean()
print(f'Ticket Médio Mensal: R${ticket_medio:,.2f}')