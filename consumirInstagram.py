
# -*- coding: utf-8 -*-
import requests
from pprint import pprint
from instagram.client import InstagramAPI
from InstagramAPI import InstagramAPI

"""
client_id = "b28aa0994706450283ecea64cb924221"
client_secret = "f131eb605dae458bbb59c6840d7ad431"

token = "EAACEdEose0cBAMOFDTgL7WqODulTOEO2plwBt8uapZC64TjEZCpCwIXhMc8VdIcGJvSiGZCSDYBLHrsq5nNCSmbPrV3G0ZBWXhABdQRZAbt4dZCDJS8fW31GBg6OVahCNGS9o0c9IpMRlXuZCh0TavnYYOJJXEZALbK27OaeIDrpGLu5aA6mDaZCANZArCL4cLhMP013wyRLyvsgZDZD"
resp = "https://www.instagram.com/oauth/authorize/?client_id=b28aa0994706450283ecea64cb924221&redirect_uri=http://google.com&response_type=token"
token_secret = requests.get(resp)
print(token_secret)

access_token= "1284504225.b28aa09.38be2583294243d58f62b4677798e3bd"
search = ("https://api.instagram.com/v1/tags/search?q=coritiba&access_token=%s" % access_token)
response = requests.get(search)
print(response.text)

#https://www.google.com.br/?gws_rd=cr&dcr=0&ei=jYNmWoa4D4SDwgS9vaGwAQ#access_token=1284504225.b28aa09.38be2583294243d58f62b4677798e3bd

username="lennyscosta"
InstagramAPI = InstagramAPI(username, )
InstagramAPI.login()


InstagramAPI.getProfileData()
result = InstagramAPI.LastJson
print(result)
"""

access_token = "1284504225.b28aa09.38be2583294243d58f62b4677798e3bd"
client_secret = "f131eb605dae458bbb59c6840d7ad431"
api = InstagramAPI(client_id='b28aa0994706450283ecea64cb924221', client_secret='f131eb605dae458bbb59c6840d7ad431')
popular_media = api.media_popular(count=20)
for media in popular_media:
    print (media.images['standard_resolution'].url)

