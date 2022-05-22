#Criando um script para enviar SMS através do Twilio a partir de sua API
#É necessário instalar a biblioteca do Twilio => pip install twilio

#Importando o módulo a ser utilizado
from twilio.rest import Client

#Definindo as chaves de acordo com o uso da API
account_sid = ''
token = ''

remetente = ''
destino = ''

client = Client(account_sid, token)

message = client.messages.create(
    to=destino,
    from_=remetente,
    body="Feliz Tragonight Day")

print(message.sid)