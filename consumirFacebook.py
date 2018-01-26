# -*- coding: utf-8 -*-
import requests
from pprint import pprint
import facebook
import json

graph = facebook.GraphAPI("EAACyRYKnAbcBAKwZC8CjhFfpv2XzfaGFkiWPUSkKLZB0dzBHyOUPaetAUnEgh2MCpPlb1wXB4ZCOF1fVARZBWN9Splvupoz0tuoLgY84TyZBB003BSMfnjVmNv0OUB9HpLXZC8G5vlv0MxJaKTL45ZAZAMaw6uLGMO8kP4j3w87wFgZDZD")
app_id = '196011614470583'
app_secret = '80e069e408c8010253d193a20ffac2e8'

extended_token = graph.extend_access_token(app_id, app_secret)
#token = extended_token["access_token"] #verify that it expires in 60 days

#search = 'https://graph.facebook.com/v2.9/search?q=coritiba&type=page&access_token='+token

#response_me = requests.get(search)
#pprint(response_me.text)

token = "EAACyRYKnAbcBAM8Mj0IpAaLn0OdF6ZBymIJq0GRMk01ts3PNK4ispYM7dKHQH7Cr6zfRrccpK5LQh2fbAiR1zxosG8klZC1qL3UIxZA74mdoNZCvqqN3zunZAX6Gyn45Y83YLULnRD1FNdJ10BVIMHPjVShVbnTEZD"
grafico = facebook.GraphAPI (access_token = token, version = 2.7)
page_search = graph.request ('/search?q=coritiba&type=page&limit=2&debug=all')

pages = page_search['data']
pages_a = pages[1]["id"]
pprint(pages)



#event1 = graph.get_object (id = eventid, campos = 'description, id, place, name')


#description = event1['description']
#id = event1['id']
#place = event1['place']
#name = event1['name']
