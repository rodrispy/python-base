# Desafio Python e E-mail

# Digamos que você trabalha em uma indústria e está responsável pela área de inteligência de negócio.
# Todo dia, você, a equipe ou até mesmo um programa, gera um report diferente para cada área da empresa:
# - Financeiro
# - Logística
# - Manutenção
# - Marketing
# - Operações
# - Produção
# - Vendas

# Cada um desses reports deve ser enviado por e-mail para o Gerente de cada Área.
# Crie um programa que faça isso automaticamente. A relação de Gerentes (com seus respectivos e-mails) e áreas está no arquivo 'Enviar E-mails.xlsx'.
# Dica: Use o pandas read_excel para ler o arquivo dos e-mails que isso vai facilitar.

import pandas as pd
import win32com.client as win32

gerentes_df = pd.read_excel('Enviar E-mails.xlsx')


for i, email in enumerate(gerentes_df['E-mail']):
    gerente = gerentes_df.loc[i, 'Gerente']
    area = gerentes_df.loc[i, 'Relatório']
    
    mail = outlook.CreateItem(0)
    mail.To = email
    mail.Subject = f'Relatório de {area}'
    mail.Body = f'''
    Prezado {gerente}, 
    Segue em anexo o Relatório de {area}, conforme solicitado.
    Qualquer dúvida estou à disposição.
    Att.,
    '''
    attachment  = r'C:\Users\joaop\Google Drive\Python Impressionador\{}.xlsx'.format(area)
    mail.Attachments.Add(attachment)

    mail.Send()