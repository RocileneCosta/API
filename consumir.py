# -*- coding: utf-8 -*-
import oauth2
import json
import urllib.parse
from pprint import pprint

#dados do Facebook API  ****Token de usuário expira do app não
userToken = 'EAACyRYKnAbcBAIkQgV9VXFmWWwZB6l2a184KE2kLKjXljUoWZCt8vT4MKyAtuxuWCZBp5tj6ERw5gZBHFnGILvUycFm9GWW30Xt1Snx1Xx6ps4Vf90huCyGcZAeF3ZCmMS2NpvdslEvbeCdpW8M4v1GYpjc8u0S0Y26eOlNJZBGd34jDUMAefAraqQeYsUAahIZD'
appToken = '196011614470583|K3JP_CGRCg7prLyt0K3ik6z8C_Q'

idApp = '196011614470583'
chaveApp = '80e069e408c8010253d193a20ffac2e8'

consumer_key = '8Cb5GIPaNeqe0e89ih1Rv3BRX'
consumer_secret = 'hyAHcf5TUhgzbThoCWQCKaSsTdgs0TMkriUzFZ1hdjOBnax7dl'

token_key = '932641261193977856-8OhVGO563z9Wc6XeqV2Cu1pVa4pXbhO'
token_secret = 'psQpIJoeZeocYhv2M6YAvceuaOUDlbjyYa4pvMdzqmgPK'

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

query = input("Pesquisa: ")
query_codificada = urllib.parse.quote(query, safe='')
requisicao = cliente.request(' ' + query_codificada + '&lang=pt')

decodificar = requisicao[1].decode()

objeto = json.loads(decodificar)
twittes = objeto['statuses']

#Fornece os Twittes dos últimos 7 dias com operadores padrão
for twit in twittes:
    print(twit['user']['screen_name'])
    pprint(twit['text'])
    print()


#url = requests.get('https://ads-api.twitter.com')
#dados = url.json()
