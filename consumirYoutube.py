from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import pandas as pd
import pprint 
import urllib
import urllib.parse
from httplib2 import Http

"""
endpoint='https://accounts.google.com/o/oauth2/token'
data={'client_id':'109385016292-vqcg14kl2g6kkmt29rgv7jq06rodni7a.apps.googleusercontent.com',
'client_secret':'kqWMkblBxUTEabngx4RqapWj','refresh_token':'AIzaSyAJ_ft_4Y4QaIAy7WL6Q4HNA5yOTL7QyHs',
'grant_type':'refresh_token'}
encodedData=urllib.parse.quote_plus(data)
#h = Http()
#resp, content = h.request(uri=endpoint,
#                          method="POST", 
#                          body=encodedData, 
#                          headers={'Content-type': 'application/x-www-form-urlencoded'})


"""
DEVELOPER_KEY = "AIzaSyAJ_ft_4Y4QaIAy7WL6Q4HNA5yOTL7QyHs"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(q, max_results=50,order="relevance", token=None, location=None, location_radius=None):
  
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
  q=q,
  type="video",
  pageToken=token,
  order = order,
  part="id,snippet", # Part signifies the different types of data you want 
  maxResults=max_results,
  location=location,
  locationRadius=location_radius).execute()

  title = []
  channelId = []
  channelTitle = []
  categoryId = []
  videoId = []
  viewCount = []
  likeCount = []
  dislikeCount = []
  commentCount = []
  favoriteCount = []
  category = []
  tags = []
  videos = []

  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":

      title.append(search_result['snippet']['title']) 

      videoId.append(search_result['id']['videoId'])

      response = youtube.videos().list(
          part='statistics, snippet',
          id=search_result['id']['videoId']).execute()

      channelId.append(response['items'][0]['snippet']['channelId'])
      channelTitle.append(response['items'][0]['snippet']['channelTitle'])
      categoryId.append(response['items'][0]['snippet']['categoryId'])
      favoriteCount.append(response['items'][0]['statistics']['favoriteCount'])
      viewCount.append(response['items'][0]['statistics']['viewCount'])
      likeCount.append(response['items'][0]['statistics']['likeCount'])
      dislikeCount.append(response['items'][0]['statistics']['dislikeCount'])

      if 'commentCount' in response['items'][0]['statistics'].keys():
          commentCount.append(response['items'][0]['statistics']['commentCount'])
      else:
          commentCount.append([])
  
      if 'tags' in response['items'][0]['snippet'].keys():
          tags.append(response['items'][0]['snippet']['tags'])
      else:
          tags.append([])

  youtube_dict = {'tags':tags,'channelId': channelId,'channelTitle': channelTitle,'categoryId':categoryId,'title':title,'videoId':videoId,'viewCount':viewCount,'likeCount':likeCount,'dislikeCount':dislikeCount,'commentCount':commentCount,'favoriteCount':favoriteCount}

  return youtube_dict

teste = youtube_search("Imagine Dragons")
teste.values()
#print(teste)

df = pd.DataFrame(data=teste)
df.head()

df1 = df[['title','viewCount','channelTitle','commentCount','likeCount','dislikeCount','tags','favoriteCount','videoId','channelId','categoryId']]
df1.columns = ['Title','viewCount','channelTitle','commentCount','likeCount','dislikeCount','tags','favoriteCount','videoId','channelId','categoryId']
df1.head()
print(df1)


