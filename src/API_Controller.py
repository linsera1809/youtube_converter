import os
import requests
import urllib.parse
import string
import json
import pathlib
import re
import time
from datetime import date
from collections import defaultdict 

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

class API_Controller:
  def __init__(self, config):
    self.config = config
    print('Welcome to Controllers')

  def search(self, query):
      #TODO: error-handler: sanitize query
      query = urllib.parse.quote(query)
      
      #TODO: error-handler: check to make sure api_key exists
      try:
          url = "https://www.googleapis.com/youtube/v3/search?part=snippet&q={}&key={}".format(query, self.config)
          payload = {}
          headers = {
              'Accept': 'application/json'
          }

          response = requests.request("GET", url, headers=headers, data = payload)
          if(response.ok):
              print('Success')
              return(response.json())
          else:
              print('Something went wrong with the request.')
              print('Status Code: ', response.status_code)

      except NameError as err:
          print('API_KEY does not exist.')
          print(err)

      except requests.exceptions.Timeout as err:
          print('Request timeout error.')
          print('Query failed on: ', url)
          print(err)

      except requests.exceptions.TooManyRedirects as err:
          print('URL is malformed. Try again.')
          print(err)

      except requests.exceptions.RequestException as err:
          # catastrophic error. bail.
          print('Catastrophic error with API Call.')
          print(err)
          raise SystemExit(err)

  def parse_response(self, res):
      json_obj = {
          'totalResults': res['pageInfo']['totalResults'], 
          'items': [
              {
              'videoId-0': res['items'][0]['id']['videoId'],
              'title-0': res['items'][0]['snippet']['title'],
              'description-0': res['items'][0]['snippet']['description'],
              'thumbnail-0': res['items'][0]['snippet']['thumbnails']['default']['url'],
              'channelTitle-0': res['items'][0]['snippet']['channelTitle']
              },
              {
              'videoId-1': res['items'][1]['id']['videoId'],
              'title-1': res['items'][1]['snippet']['title'],
              'description-1': res['items'][1]['snippet']['description'],
              'thumbnail-1': res['items'][1]['snippet']['thumbnails']['default']['url'],
              'channelTitle-1': res['items'][1]['snippet']['channelTitle']
              },
              {
              'videoId-2': res['items'][2]['id']['videoId'],
              'title-2': res['items'][2]['snippet']['title'],
              'description-2': res['items'][2]['snippet']['description'],
              'thumbnail-2': res['items'][2]['snippet']['thumbnails']['default']['url'],
              'channelTitle-2': res['items'][2]['snippet']['channelTitle']
              },
              {
              'videoId-3': res['items'][3]['id']['videoId'],
              'title-3': res['items'][3]['snippet']['title'],
              'description-3': res['items'][3]['snippet']['description'],
              'thumbnail-3': res['items'][3]['snippet']['thumbnails']['default']['url'],
              'channelTitle-3': res['items'][3]['snippet']['channelTitle']
              },
              {
              'videoId-4': res['items'][4]['id']['videoId'],
              'title-4': res['items'][4]['snippet']['title'],
              'description-4': res['items'][4]['snippet']['description'],
              'thumbnail-4': res['items'][4]['snippet']['thumbnails']['default']['url'],
              'channelTitle-4': res['items'][4]['snippet']['channelTitle']
              },
          ]
      }
      print(json_obj)
      return(json_obj)

  #---------------------------------------------------------------------------#
# if __name__ == "__main__":
#   #GLOBALS
#   env='./sec/env.json'
#   # output_location = 'C:/Users/blins/dev/projects/youtube_converter/out/'

#   #TESTING
#   res = {
#     "kind": "youtube#searchListResponse",
#     "etag": "XHZd1d8PZX_tELlj7xuu3J5p-TE",
#     "nextPageToken": "CBkQAA",
#     "regionCode": "US",
#     "pageInfo": {
#       "totalResults": 1000000,
#       "resultsPerPage": 25
#     },
#     "items": [
#       {
#         "kind": "youtube#searchResult",
#         "etag": "Czs85HfG0zrE1LmCOGGqp194fjk",
#         "id": {
#           "kind": "youtube#video",
#           "videoId": "dQw4w9WgXcQ"
#         },
#         "snippet": {
#           "publishedAt": "2009-10-25T06:57:33Z",
#           "channelId": "UC38IQsAvIsxxjztdMZQtwHA",
#           "title": "Rick Astley - Never Gonna Give You Up (Video)",
#           "description": "Rick Astley's official music video for “Never Gonna Give You Up” Listen to Rick Astley: https://RickAstley.lnk.to/_listenYD Subscribe to the official Rick Astley ...",
#           "thumbnails": {
#             "default": {
#               "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/default.jpg",
#               "width": 120,
#               "height": 90
#             },
#             "medium": {
#               "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/mqdefault.jpg",
#               "width": 320,
#               "height": 180
#             },
#             "high": {
#               "url": "https://i.ytimg.com/vi/dQw4w9WgXcQ/hqdefault.jpg",
#               "width": 480,
#               "height": 360
#             }
#           },
#           "channelTitle": "RickAstleyVEVO",
#           "liveBroadcastContent": "none",
#           "publishTime": "2009-10-25T06:57:33Z"
#         }
#       },
#       {
#         "kind": "youtube#searchResult",
#         "etag": "7WbSSNVxfxn1wX10j6Z3L5SKHGQ",
#         "id": {
#           "kind": "youtube#video",
#           "videoId": "ykLGXWb-AtA"
#         },
#         "snippet": {
#           "publishedAt": "2020-05-24T05:05:39Z",
#           "channelId": "UCxjmyGocg2EH-2q-C_s6nsg",
#           "title": "I *RICK ROLL* MY ENTIRE ZOOM CLASS! (Updated)",
#           "description": "this is a reupload. imagine if i didn't fail. this would have been legendary. Subscribe to my epic boi bruce: ...",
#           "thumbnails": {
#             "default": {
#               "url": "https://i.ytimg.com/vi/ykLGXWb-AtA/default.jpg",
#               "width": 120,
#               "height": 90
#             },
#             "medium": {
#               "url": "https://i.ytimg.com/vi/ykLGXWb-AtA/mqdefault.jpg",
#               "width": 320,
#               "height": 180
#             },
#             "high": {
#               "url": "https://i.ytimg.com/vi/ykLGXWb-AtA/hqdefault.jpg",
#               "width": 480,
#               "height": 360
#             }
#           },
#           "channelTitle": "thespacestalker",
#           "liveBroadcastContent": "none",
#           "publishTime": "2020-05-24T05:05:39Z"
#         }
#       },
#       {
#         "kind": "youtube#searchResult",
#         "etag": "jyAm-kR3PK68H2Rjd0xvH0YUFtE",
#         "id": {
#           "kind": "youtube#video",
#           "videoId": "L9MEdkgWLEY"
#         },
#         "snippet": {
#           "publishedAt": "2020-03-02T16:02:23Z",
#           "channelId": "UCRKlKgzX4pL3rB7iBND4Omw",
#           "title": "||TOP 10 Rick Roll’s||",
#           "description": "Number 15 #RickAstley #RickRoll #meme #funny #crindge I just..im sorry for these hashtags its simpley youtube.",
#           "thumbnails": {
#             "default": {
#               "url": "https://i.ytimg.com/vi/L9MEdkgWLEY/default.jpg",
#               "width": 120,
#               "height": 90
#             },
#             "medium": {
#               "url": "https://i.ytimg.com/vi/L9MEdkgWLEY/mqdefault.jpg",
#               "width": 320,
#               "height": 180
#             },
#             "high": {
#               "url": "https://i.ytimg.com/vi/L9MEdkgWLEY/hqdefault.jpg",
#               "width": 480,
#               "height": 360
#             }
#           },
#           "channelTitle": "The RaNd0m channle",
#           "liveBroadcastContent": "none",
#           "publishTime": "2020-03-02T16:02:23Z"
#         }
#       },
#       {
#         "kind": "youtube#searchResult",
#         "etag": "psOzKauaIQZbO0F2AgiLZRixgss",
#         "id": {
#           "kind": "youtube#video",
#           "videoId": "H52TTCoS7To"
#         },
#         "snippet": {
#           "publishedAt": "2013-02-28T19:28:46Z",
#           "channelId": "UC0v-tlzsn0QZwJnkiaUSJVQ",
#           "title": "YOUTUBERS REACT TO RICKROLL",
#           "description": "Rickroll EXTRA REACTIONS: https://goo.gl/ewhqiY SUBSCRIBE THEN HIT THE ! New Videos 2pm PST on FBE! http://goo.gl/aFu8C Watch all main React ...",
#           "thumbnails": {
#             "default": {
#               "url": "https://i.ytimg.com/vi/H52TTCoS7To/default.jpg",
#               "width": 120,
#               "height": 90
#             },
#             "medium": {
#               "url": "https://i.ytimg.com/vi/H52TTCoS7To/mqdefault.jpg",
#               "width": 320,
#               "height": 180
#             },
#             "high": {
#               "url": "https://i.ytimg.com/vi/H52TTCoS7To/hqdefault.jpg",
#               "width": 480,
#               "height": 360
#             }
#           },
#           "channelTitle": "REACT",
#           "liveBroadcastContent": "none",
#           "publishTime": "2013-02-28T19:28:46Z"
#         }
#       },
#       {
#         "kind": "youtube#searchResult",
#         "etag": "j8RInOd9Ji2U334_4wCF0Gn3bO4",
#         "id": {
#           "kind": "youtube#video",
#           "videoId": "ZYooh1LxB80"
#         },
#         "snippet": {
#           "publishedAt": "2011-03-08T22:05:00Z",
#           "channelId": "UCso-UInzbHIV4R1pV6pOXrQ",
#           "title": "I Rick Roll My Entire Chemistry Class!",
#           "description": "So we had to make this presentation on group 4a and carbon and somehow Rick Astley ended up getting involved.",
#           "thumbnails": {
#             "default": {
#               "url": "https://i.ytimg.com/vi/ZYooh1LxB80/default.jpg",
#               "width": 120,
#               "height": 90
#             },
#             "medium": {
#               "url": "https://i.ytimg.com/vi/ZYooh1LxB80/mqdefault.jpg",
#               "width": 320,
#               "height": 180
#             },
#             "high": {
#               "url": "https://i.ytimg.com/vi/ZYooh1LxB80/hqdefault.jpg",
#               "width": 480,
#               "height": 360
#             }
#           },
#           "channelTitle": "007pranksterman",
#           "liveBroadcastContent": "none",
#           "publishTime": "2011-03-08T22:05:00Z"
#         }
#       },
#       {
#         "kind": "youtube#searchResult",
#         "etag": "5z-WA3b-BfuxiqL1L67EtGGYZAY",
#         "id": {
#           "kind": "youtube#video",
#           "videoId": "U9Gxcmvb2c4"
#         },
#         "snippet": {
#           "publishedAt": "2017-11-07T22:00:01Z",
#           "channelId": "UC0v-tlzsn0QZwJnkiaUSJVQ",
#           "title": "YOUTUBERS REACT TO RICKROLL - 10th ANNIVERSARY",
#           "description": "Give lots of love and support to the people in this video by subscribing to them all! Click “Show More” for links to their channels. Join the SuperFam and support ...",
#           "thumbnails": {
#             "default": {
#               "url": "https://i.ytimg.com/vi/U9Gxcmvb2c4/default.jpg",
#               "width": 120,
#               "height": 90
#             },
#             "medium": {
#               "url": "https://i.ytimg.com/vi/U9Gxcmvb2c4/mqdefault.jpg",
#               "width": 320,
#               "height": 180
#             },
#             "high": {
#               "url": "https://i.ytimg.com/vi/U9Gxcmvb2c4/hqdefault.jpg",
#               "width": 480,
#               "height": 360
#             }
#           },
#           "channelTitle": "REACT",
#           "liveBroadcastContent": "none",
#           "publishTime": "2017-11-07T22:00:01Z"
#         }
#       },
#       {
#         "kind": "youtube#searchResult",
#         "etag": "y7q4ebgepab5inI7K_hMt46tRps",
#         "id": {
#           "kind": "youtube#video",
#           "videoId": "oHg5SJYRHA0"
#         },
#         "snippet": {
#           "publishedAt": "2007-05-15T07:24:30Z",
#           "channelId": "UCxnNQpMtVrZRZh3aOkmnK4w",
#           "title": "RickRoll&#39;D",
#           "description": "https://www.facebook.com/rickroll548 Reddit AMA: https://www.reddit.com/r/IAmA/comments/mx53y/i_am_youtube_user_cotter548_aka_the_inventor_of/ As ...",
#           "thumbnails": {
#             "default": {
#               "url": "https://i.ytimg.com/vi/oHg5SJYRHA0/default.jpg",
#               "width": 120,
#               "height": 90
#             },
#             "medium": {
#               "url": "https://i.ytimg.com/vi/oHg5SJYRHA0/mqdefault.jpg",
#               "width": 320,
#               "height": 180
#             },
#             "high": {
#               "url": "https://i.ytimg.com/vi/oHg5SJYRHA0/hqdefault.jpg",
#               "width": 480,
#               "height": 360
#             }
#           },
#           "channelTitle": "cotter548",
#           "liveBroadcastContent": "none",
#           "publishTime": "2007-05-15T07:24:30Z"
#         }
#       },
#       {
#         "kind": "youtube#searchResult",
#         "etag": "njISCjrriwWy-4nTKEzfStnxOOg",
#         "id": {
#           "kind": "youtube#video",
#           "videoId": "o6kKHm0UA50"
#         },
#         "snippet": {
#           "publishedAt": "2020-07-26T15:53:33Z",
#           "channelId": "UClqG38nWMnjTqB_28HGk5Hw",
#           "title": "PewDiePie getting Rickrolled Compilation",
#           "description": "PewDiePie #compilation #RickRolled This is a compilation of PewDiePie getting rickrolled. He also rages.",
#           "thumbnails": {
#             "default": {
#               "url": "https://i.ytimg.com/vi/o6kKHm0UA50/default.jpg",
#               "width": 120,
#               "height": 90
#             },
#             "medium": {
#               "url": "https://i.ytimg.com/vi/o6kKHm0UA50/mqdefault.jpg",
#               "width": 320,
#               "height": 180
#             },
#             "high": {
#               "url": "https://i.ytimg.com/vi/o6kKHm0UA50/hqdefault.jpg",
#               "width": 480,
#               "height": 360
#             }
#           },
#           "channelTitle": "Reposter of Memes",
#           "liveBroadcastContent": "none",
#           "publishTime": "2020-07-26T15:53:33Z"
#         }
#       },
#       {
#         "kind": "youtube#searchResult",
#         "etag": "QduMit1UilpPffN842KkOQBTpN0",
#         "id": {
#           "kind": "youtube#video",
#           "videoId": "VEPSO-mU08c"
#         },
#         "snippet": {
#           "publishedAt": "2020-09-03T07:40:48Z",
#           "channelId": "UCL5kwpLz3I0BMhnrB8dyJEA",
#           "title": "Every time PewDiePie got rick rolled",
#           "description": "Rick roll lol first clip: https://youtu.be/qj9Auh0hRAc third clip: https://youtu.be/g6-sx7sIL6I fourth clip: https://youtu.be/eS4rlDJ1aVQ fifth ...",
#           "thumbnails": {
#             "default": {
#               "url": "https://i.ytimg.com/vi/VEPSO-mU08c/default.jpg",
#               "width": 120,
#               "height": 90
#             },
#             "medium": {
#               "url": "https://i.ytimg.com/vi/VEPSO-mU08c/mqdefault.jpg",
#               "width": 320,
#               "height": 180
#             },
#             "high": {
#               "url": "https://i.ytimg.com/vi/VEPSO-mU08c/hqdefault.jpg",
#               "width": 480,
#               "height": 360
#             }
#           },
#           "channelTitle": "Not_MyUsernamesThis",
#           "liveBroadcastContent": "none",
#           "publishTime": "2020-09-03T07:40:48Z"
#         }
#       },
#       {
#         "kind": "youtube#searchResult",
#         "etag": "VI8Yshfq6Z15NCwLMFVA6C0FvMk",
#         "id": {
#           "kind": "youtube#video",
#           "videoId": "dULug6PlmBo"
#         },
#         "snippet": {
#           "publishedAt": "2017-09-21T23:25:39Z",
#           "channelId": "UCaFjhAeXmimOIMXeZ0hAXzA",
#           "title": "Wheel of Fortune Rick Rolls us (9/21/2017)",
#           "description": "Never gonna give you up.... PS sorry about the mouth breathing sounds. I swear I was breathing through my nose.",
#           "thumbnails": {
#             "default": {
#               "url": "https://i.ytimg.com/vi/dULug6PlmBo/default.jpg",
#               "width": 120,
#               "height": 90
#             },
#             "medium": {
#               "url": "https://i.ytimg.com/vi/dULug6PlmBo/mqdefault.jpg",
#               "width": 320,
#               "height": 180
#             },
#             "high": {
#               "url": "https://i.ytimg.com/vi/dULug6PlmBo/hqdefault.jpg",
#               "width": 480,
#               "height": 360
#             }
#           },
#           "channelTitle": "alternageek",
#           "liveBroadcastContent": "none",
#           "publishTime": "2017-09-21T23:25:39Z"
#         }
#       },
#       {
#         "kind": "youtube#searchResult",
#         "etag": "VUIEZtUFFsG1ooIe3JWzqIAo_IA",
#         "id": {
#           "kind": "youtube#video",
#           "videoId": "L4K8fY2QkPw"
#         },
#         "snippet": {
#           "publishedAt": "2020-02-17T03:55:21Z",
#           "channelId": "UCRRyyvlodqN-BHx7ILwheGw",
#           "title": "RICK ROLLING TWITCH STREAMERS #1 *HILARIOUS*",
#           "description": "RICK ROLLING TWITCH STREAMERS #1 *HILARIOUS* Open for MORE!! Use code 'FRONT' at checkout for 10% off your purchase https://gfuel.com Support ...",
#           "thumbnails": {
#             "default": {
#               "url": "https://i.ytimg.com/vi/L4K8fY2QkPw/default.jpg",
#               "width": 120,
#               "height": 90
#             },
#             "medium": {
#               "url": "https://i.ytimg.com/vi/L4K8fY2QkPw/mqdefault.jpg",
#               "width": 320,
#               "height": 180
#             },
#             "high": {
#               "url": "https://i.ytimg.com/vi/L4K8fY2QkPw/hqdefault.jpg",
#               "width": 480,
#               "height": 360
#             }
#           },
#           "channelTitle": "Atoms",
#           "liveBroadcastContent": "none",
#           "publishTime": "2020-02-17T03:55:21Z"
#         }
#       },
#       {
#         "kind": "youtube#searchResult",
#         "etag": "wATiUqs-mMnW7YQ8V1gIKxKrgzw",
#         "id": {
#           "kind": "youtube#playlist",
#           "playlistId": "PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx"
#         },
#         "snippet": {
#           "publishedAt": "2019-05-21T23:59:38Z",
#           "channelId": "UCTF71BeugpgUjsTBupT-iDA",
#           "title": "Disguised Rick-Rolls",
#           "description": "If you have a disguised Rick Roll you'd like me to add, go to my channel discussion and post the link and I'll add it!",
#           "thumbnails": {
#             "default": {
#               "url": "https://i.ytimg.com/vi/HPk-VhRjNI8/default.jpg",
#               "width": 120,
#               "height": 90
#             },
#             "medium": {
#               "url": "https://i.ytimg.com/vi/HPk-VhRjNI8/mqdefault.jpg",
#               "width": 320,
#               "height": 180
#             },
#             "high": {
#               "url": "https://i.ytimg.com/vi/HPk-VhRjNI8/hqdefault.jpg",
#               "width": 480,
#               "height": 360
#             }
#           },
#           "channelTitle": "Bajà Blast",
#           "liveBroadcastContent": "none",
#           "publishTime": "2019-05-21T23:59:38Z"
#         }
#       },
#       {
#         "kind": "youtube#searchResult",
#         "etag": "5ZWVOzH9gnoCK_pXGftk2jwgtNc",
#         "id": {
#           "kind": "youtube#video",
#           "videoId": "e-yfYhSR7YE"
#         },
#         "snippet": {
#           "publishedAt": "2018-04-24T14:28:43Z",
#           "channelId": "UCLQtPA5-ZFyDg4itdzigphg",
#           "title": "Chatting with Rick Astley About the &#39;Rickroll&#39; Phenomenon",
#           "description": "Rick Astley's hit single 'Never Gonna Give You Up' is one of the biggest songs of the 1980s. He went on to have a hit of string hits and now is back in Chicago for ...",
#           "thumbnails": {
#             "default": {
#               "url": "https://i.ytimg.com/vi/e-yfYhSR7YE/default.jpg",
#               "width": 120,
#               "height": 90
#             },
#             "medium": {
#               "url": "https://i.ytimg.com/vi/e-yfYhSR7YE/mqdefault.jpg",
#               "width": 320,
#               "height": 180
#             },
#             "high": {
#               "url": "https://i.ytimg.com/vi/e-yfYhSR7YE/hqdefault.jpg",
#               "width": 480,
#               "height": 360
#             }
#           },
#           "channelTitle": "The Jam TV Show",
#           "liveBroadcastContent": "none",
#           "publishTime": "2018-04-24T14:28:43Z"
#         }
#       },
#       {
#         "kind": "youtube#searchResult",
#         "etag": "GGq1diXWZ5bW7skRxu21Wig62Jc",
#         "id": {
#           "kind": "youtube#video",
#           "videoId": "sXwaRjU7Tj0"
#         },
#         "snippet": {
#           "publishedAt": "2020-08-01T11:08:30Z",
#           "channelId": "UCHY_zuXXPafTD0mNTWjIU7A",
#           "title": "The Smartest RickRoll",
#           "description": "This is a video showing how I really got rickrolled in the smartest way.",
#           "thumbnails": {
#             "default": {
#               "url": "https://i.ytimg.com/vi/sXwaRjU7Tj0/default.jpg",
#               "width": 120,
#               "height": 90
#             },
#             "medium": {
#               "url": "https://i.ytimg.com/vi/sXwaRjU7Tj0/mqdefault.jpg",
#               "width": 320,
#               "height": 180
#             },
#             "high": {
#               "url": "https://i.ytimg.com/vi/sXwaRjU7Tj0/hqdefault.jpg",
#               "width": 480,
#               "height": 360
#             }
#           },
#           "channelTitle": "SpaceBerries",
#           "liveBroadcastContent": "none",
#           "publishTime": "2020-08-01T11:08:30Z"
#         }
#       },
#       {
#         "kind": "youtube#searchResult",
#         "etag": "kbRGi-Mdhq2gdRuW4M4Odo6NeXM",
#         "id": {
#           "kind": "youtube#playlist",
#           "playlistId": "PLVbxVQf7e2KRz1J34jFf7jDJFDT9lvnQ9"
#         },
#         "snippet": {
#           "publishedAt": "2018-12-22T03:46:03Z",
#           "channelId": "UC__Qh1cAXJa1Iht0FyBScbw",
#           "title": "Rick Rolls To Trick People With",
#           "description": "Yep, I Do This Shit For A Hobby. I Found Some Great Rick Rolls That Don't Have Never Gonna Give You Up In The Title Of The Videos Because A Lot Of ...",
#           "thumbnails": {
#             "default": {
#               "url": "https://i.ytimg.com/vi/rEtZzcxQ_pA/default.jpg",
#               "width": 120,
#               "height": 90
#             },
#             "medium": {
#               "url": "https://i.ytimg.com/vi/rEtZzcxQ_pA/mqdefault.jpg",
#               "width": 320,
#               "height": 180
#             },
#             "high": {
#               "url": "https://i.ytimg.com/vi/rEtZzcxQ_pA/hqdefault.jpg",
#               "width": 480,
#               "height": 360
#             }
#           },
#           "channelTitle": "Strawberry Pimp",
#           "liveBroadcastContent": "none",
#           "publishTime": "2018-12-22T03:46:03Z"
#         }
#       },
#       {
#         "kind": "youtube#searchResult",
#         "etag": "DIdoGSfBIku5mWxTlTdSB-BsDcE",
#         "id": {
#           "kind": "youtube#video",
#           "videoId": "6_b7RDuLwcI"
#         },
#         "snippet": {
#           "publishedAt": "2008-07-02T18:28:59Z",
#           "channelId": "UCuoFoUKfg2XsApaZAvdSvPA",
#           "title": "Rick Astley Never gonna give you up lyrics!!!",
#           "description": "the rick rolled thing was an inside joke thing. not many people know what it means. but yet alot do!",
#           "thumbnails": {
#             "default": {
#               "url": "https://i.ytimg.com/vi/6_b7RDuLwcI/default.jpg",
#               "width": 120,
#               "height": 90
#             },
#             "medium": {
#               "url": "https://i.ytimg.com/vi/6_b7RDuLwcI/mqdefault.jpg",
#               "width": 320,
#               "height": 180
#             },
#             "high": {
#               "url": "https://i.ytimg.com/vi/6_b7RDuLwcI/hqdefault.jpg",
#               "width": 480,
#               "height": 360
#             }
#           },
#           "channelTitle": "Jaysean",
#           "liveBroadcastContent": "none",
#           "publishTime": "2008-07-02T18:28:59Z"
#         }
#       },
#       {
#         "kind": "youtube#searchResult",
#         "etag": "45tN87lD0eaDS7l-eINZCG8LSLQ",
#         "id": {
#           "kind": "youtube#video",
#           "videoId": "cvh0nX08nRw"
#         },
#         "snippet": {
#           "publishedAt": "2018-01-08T11:46:01Z",
#           "channelId": "UC1iK6gmYyIVKwib_uONz5Qg",
#           "title": "rickroll, but it never starts",
#           "description": "",
#           "thumbnails": {
#             "default": {
#               "url": "https://i.ytimg.com/vi/cvh0nX08nRw/default.jpg",
#               "width": 120,
#               "height": 90
#             },
#             "medium": {
#               "url": "https://i.ytimg.com/vi/cvh0nX08nRw/mqdefault.jpg",
#               "width": 320,
#               "height": 180
#             },
#             "high": {
#               "url": "https://i.ytimg.com/vi/cvh0nX08nRw/hqdefault.jpg",
#               "width": 480,
#               "height": 360
#             }
#           },
#           "channelTitle": "Alexey Kutepov",
#           "liveBroadcastContent": "none",
#           "publishTime": "2018-01-08T11:46:01Z"
#         }
#       },
#       {
#         "kind": "youtube#searchResult",
#         "etag": "KH9OKe6YkbWH8_0SIYAX0MdK9uw",
#         "id": {
#           "kind": "youtube#video",
#           "videoId": "MO7bRMa9bmA"
#         },
#         "snippet": {
#           "publishedAt": "2017-09-07T20:26:22Z",
#           "channelId": "UCV66PFgX2rfbU-H3Ya-3ixA",
#           "title": "Big Ben&#39;s Final Rick Roll",
#           "description": "Hello you wonderful people of the internet! It appears you have found my channel! Well then,while your here could you take 1.7 secs to like this video! I would ...",
#           "thumbnails": {
#             "default": {
#               "url": "https://i.ytimg.com/vi/MO7bRMa9bmA/default.jpg",
#               "width": 120,
#               "height": 90
#             },
#             "medium": {
#               "url": "https://i.ytimg.com/vi/MO7bRMa9bmA/mqdefault.jpg",
#               "width": 320,
#               "height": 180
#             },
#             "high": {
#               "url": "https://i.ytimg.com/vi/MO7bRMa9bmA/hqdefault.jpg",
#               "width": 480,
#               "height": 360
#             }
#           },
#           "channelTitle": "Foxy",
#           "liveBroadcastContent": "none",
#           "publishTime": "2017-09-07T20:26:22Z"
#         }
#       },
#       {
#         "kind": "youtube#searchResult",
#         "etag": "MErE6PvgRkiMAufu7cbCDNrAy4c",
#         "id": {
#           "kind": "youtube#video",
#           "videoId": "JfsOZLBpDoE"
#         },
#         "snippet": {
#           "publishedAt": "2020-02-15T00:36:00Z",
#           "channelId": "UCuu0tYMuv4sUAatTGEBHysQ",
#           "title": "Streamers React to the *NEW* RICK ROLL Emote!! *INSANE* | Fortnite Highlights &amp; Funny Moments",
#           "description": "Streamers React to the *NEW* RICK ROLL Emote!! *INSANE* | Fortnite Highlights & Funny Moments Daily Fortnite highlights, funny moments, fails and plays ...",
#           "thumbnails": {
#             "default": {
#               "url": "https://i.ytimg.com/vi/JfsOZLBpDoE/default.jpg",
#               "width": 120,
#               "height": 90
#             },
#             "medium": {
#               "url": "https://i.ytimg.com/vi/JfsOZLBpDoE/mqdefault.jpg",
#               "width": 320,
#               "height": 180
#             },
#             "high": {
#               "url": "https://i.ytimg.com/vi/JfsOZLBpDoE/hqdefault.jpg",
#               "width": 480,
#               "height": 360
#             }
#           },
#           "channelTitle": "GamingStyle",
#           "liveBroadcastContent": "none",
#           "publishTime": "2020-02-15T00:36:00Z"
#         }
#       },
#       {
#         "kind": "youtube#searchResult",
#         "etag": "vAHIWoKTqsNUXukIrTi3SK6xiLE",
#         "id": {
#           "kind": "youtube#video",
#           "videoId": "qDs7KkGcQ6M"
#         },
#         "snippet": {
#           "publishedAt": "2019-08-27T00:57:12Z",
#           "channelId": "UCXDFQQ2-I18FRYeIMCXVKPQ",
#           "title": "Red Sox get Rick Roll&#39;d by Padres [Full Clip] [HD]",
#           "description": "The Boston Red Sox get trolled by the San Diego Padres, badly. Yes, this really happened, it's not fake. Be sure to subscribe, follow me on Twitter ...",
#           "thumbnails": {
#             "default": {
#               "url": "https://i.ytimg.com/vi/qDs7KkGcQ6M/default.jpg",
#               "width": 120,
#               "height": 90
#             },
#             "medium": {
#               "url": "https://i.ytimg.com/vi/qDs7KkGcQ6M/mqdefault.jpg",
#               "width": 320,
#               "height": 180
#             },
#             "high": {
#               "url": "https://i.ytimg.com/vi/qDs7KkGcQ6M/hqdefault.jpg",
#               "width": 480,
#               "height": 360
#             }
#           },
#           "channelTitle": "Chris6d",
#           "liveBroadcastContent": "none",
#           "publishTime": "2019-08-27T00:57:12Z"
#         }
#       },
#       {
#         "kind": "youtube#searchResult",
#         "etag": "jnnoCn48paar6Dos4JMvWql4Q2E",
#         "id": {
#           "kind": "youtube#video",
#           "videoId": "VG_8zrsLPJA"
#         },
#         "snippet": {
#           "publishedAt": "2009-06-04T02:01:14Z",
#           "channelId": "UCMR9_DA4ndG169e2OFw8HSA",
#           "title": "i rick roll my entire school at talent show",
#           "description": "j stern noel jf n gomes.",
#           "thumbnails": {
#             "default": {
#               "url": "https://i.ytimg.com/vi/VG_8zrsLPJA/default.jpg",
#               "width": 120,
#               "height": 90
#             },
#             "medium": {
#               "url": "https://i.ytimg.com/vi/VG_8zrsLPJA/mqdefault.jpg",
#               "width": 320,
#               "height": 180
#             },
#             "high": {
#               "url": "https://i.ytimg.com/vi/VG_8zrsLPJA/hqdefault.jpg",
#               "width": 480,
#               "height": 360
#             }
#           },
#           "channelTitle": "Unrealtrain",
#           "liveBroadcastContent": "none",
#           "publishTime": "2009-06-04T02:01:14Z"
#         }
#       },
#       {
#         "kind": "youtube#searchResult",
#         "etag": "6M9INNemjT0hAbO16zaP3mDD3e0",
#         "id": {
#           "kind": "youtube#video",
#           "videoId": "3g5_bC0WXmw"
#         },
#         "snippet": {
#           "publishedAt": "2020-02-16T00:48:13Z",
#           "channelId": "UC_jQ64mgxDbvATLv94lMwaw",
#           "title": "I Trolled Him With NEW &quot;Rick Roll&quot; Emote.. (Fortnite)",
#           "description": "I Trolled Him With NEW \"Rick Roll\" Emote.. (Fortnite Battle Royale) Lox: https://www.youtube.com/channel/UCmp41vA53WoRtC_oDjosDBQ Today in fortnite ...",
#           "thumbnails": {
#             "default": {
#               "url": "https://i.ytimg.com/vi/3g5_bC0WXmw/default.jpg",
#               "width": 120,
#               "height": 90
#             },
#             "medium": {
#               "url": "https://i.ytimg.com/vi/3g5_bC0WXmw/mqdefault.jpg",
#               "width": 320,
#               "height": 180
#             },
#             "high": {
#               "url": "https://i.ytimg.com/vi/3g5_bC0WXmw/hqdefault.jpg",
#               "width": 480,
#               "height": 360
#             }
#           },
#           "channelTitle": "MrTop5",
#           "liveBroadcastContent": "none",
#           "publishTime": "2020-02-16T00:48:13Z"
#         }
#       },
#       {
#         "kind": "youtube#searchResult",
#         "etag": "NqRqrzMLfJHbWLYNNmgNFVyFeUA",
#         "id": {
#           "kind": "youtube#video",
#           "videoId": "iik25wqIuFo"
#         },
#         "snippet": {
#           "publishedAt": "2020-04-20T05:12:01Z",
#           "channelId": "UCmTV2m4ULohfAs22-fKLv-Q",
#           "title": "Rick roll, but with different link",
#           "description": "Never gonna give you up.",
#           "thumbnails": {
#             "default": {
#               "url": "https://i.ytimg.com/vi/iik25wqIuFo/default.jpg",
#               "width": 120,
#               "height": 90
#             },
#             "medium": {
#               "url": "https://i.ytimg.com/vi/iik25wqIuFo/mqdefault.jpg",
#               "width": 320,
#               "height": 180
#             },
#             "high": {
#               "url": "https://i.ytimg.com/vi/iik25wqIuFo/hqdefault.jpg",
#               "width": 480,
#               "height": 360
#             }
#           },
#           "channelTitle": "Rick roll, but with a different link",
#           "liveBroadcastContent": "none",
#           "publishTime": "2020-04-20T05:12:01Z"
#         }
#       },
#       {
#         "kind": "youtube#searchResult",
#         "etag": "ytnLBiaPRMG-0wrU-l_V3byx8Gc",
#         "id": {
#           "kind": "youtube#playlist",
#           "playlistId": "PL8LxeO4qJhBPheX-UV2INbVcfHjZwW239"
#         },
#         "snippet": {
#           "publishedAt": "2020-03-29T08:04:45Z",
#           "channelId": "UCbo5MnFuWUUcKIlFxGb6kIQ",
#           "title": "Rick Rolls in disguised trolls( ͡° ͜ʖ ͡°)",
#           "description": "I love Rick Rolling.",
#           "thumbnails": {
#             "default": {
#               "url": "https://i.ytimg.com/vi/j5a0jTc9S10/default.jpg",
#               "width": 120,
#               "height": 90
#             },
#             "medium": {
#               "url": "https://i.ytimg.com/vi/j5a0jTc9S10/mqdefault.jpg",
#               "width": 320,
#               "height": 180
#             },
#             "high": {
#               "url": "https://i.ytimg.com/vi/j5a0jTc9S10/hqdefault.jpg",
#               "width": 480,
#               "height": 360
#             }
#           },
#           "channelTitle": "Chow Blip",
#           "liveBroadcastContent": "none",
#           "publishTime": "2020-03-29T08:04:45Z"
#         }
#       },
#       {
#         "kind": "youtube#searchResult",
#         "etag": "PgLiJSxa4CPSLj8WiQpRzhmNyBI",
#         "id": {
#           "kind": "youtube#video",
#           "videoId": "nsCRrJAzJJE"
#         },
#         "snippet": {
#           "publishedAt": "2008-11-12T03:43:45Z",
#           "channelId": "UCXcwD7UDGbD_vy03b9KkQTw",
#           "title": "ABC News Rick Rolls 4 Million Americans",
#           "description": "Watch In High Quality. ABC News Nighline aired a report Thursday, November 6, 2008 concerning the popularity of the Rick Astley song. WDIO-DT.",
#           "thumbnails": {
#             "default": {
#               "url": "https://i.ytimg.com/vi/nsCRrJAzJJE/default.jpg",
#               "width": 120,
#               "height": 90
#             },
#             "medium": {
#               "url": "https://i.ytimg.com/vi/nsCRrJAzJJE/mqdefault.jpg",
#               "width": 320,
#               "height": 180
#             },
#             "high": {
#               "url": "https://i.ytimg.com/vi/nsCRrJAzJJE/hqdefault.jpg",
#               "width": 480,
#               "height": 360
#             }
#           },
#           "channelTitle": "ABCNEWSER",
#           "liveBroadcastContent": "none",
#           "publishTime": "2008-11-12T03:43:45Z"
#         }
#       }
#     ]
#   }

  # res = call_data_api('rick roll', config['api_key'])
  # parse_response(res)