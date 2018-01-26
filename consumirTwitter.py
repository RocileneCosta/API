# -*- coding: utf-8 -*-
import oauth2
import json
import urllib.parse
from pprint import pprint
import sqlalchemy
import sqlalchemy.orm

#Pesquisando Palavras no banco
engine = sqlalchemy.create_engine("mysql://user.rocilene:miti2018@10.0.100.66/dbclp", encoding='utf-8')
sessionmaker = sqlalchemy.orm.sessionmaker(bind=engine)

#pesquisando palavras com um código fixo
select = """SELECT p.dsPalavra
            FROM PALAVRACONTRATADA pc
            INNER JOIN PALAVRA p ON p.cdPalavra = pc.cdPalavra
            WHERE pc.cdPerfil = '29968' 
            LIMIT 100;""" 
#Exemplos: 29968 - Acrimat 2986-Coritiba
session = sessionmaker()

try:
    palavras = session.execute(select)
    session.close()

except Exception as e:
    print(e)

#Chaves de acesso à API
consumer_key = '8Cb5GIPaNeqe0e89ih1Rv3BRX'
consumer_secret = 'hyAHcf5TUhgzbThoCWQCKaSsTdgs0TMkriUzFZ1hdjOBnax7dl'

token_key = '932641261193977856-8OhVGO563z9Wc6XeqV2Cu1pVa4pXbhO'
token_secret = 'psQpIJoeZeocYhv2M6YAvceuaOUDlbjyYa4pvMdzqmgPK'

#cria novos tokens de acesso
consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

for palavra in palavras:
    
    query = str(palavra)
    query_codificada = urllib.parse.quote(query, safe='')
    requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada + '&lang=pt')

    decodificar = requisicao[1].decode()

    objeto = json.loads(decodificar)
    twittes = objeto['statuses']

    for twit in twittes:
        total = (len(twittes))
        print("quantidade: %s" % total)
        print(twit['user']['screen_name'])
        pprint(twit ['text'])
        print()
#Fornece os Twittes dos últimos 7 dias com operadores padrão
