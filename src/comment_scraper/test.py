import requests 
import urllib.parse
import json
from dotenv import dotenv_values

config = dotenv_values(".env")

page_url = 'https://gql.reddit.com/'

from gql_request_models.TopNewCommentSearch import TopNewCommentSearch

tncs = TopNewCommentSearch()
print(tncs.get_call())

# data = {
#     'id': '6c87f86c5706',
#     'variables': {
#         'authorsAfter': None,
#         'commentsAfter': None, # This will change
#         'communitiesAfter': None,
#         'communitySearch': True,
#         'customFeedSearch': False,
#         'filters': [
#             {
#                 'key': 'nsfw',
#                 'value': '1',
#             },
#             {
#                 'key': 'subreddit_names',
#                 'value': 'redditdev',
#             },
#         ],
#         'includeAuthors': False,
#         'includeComments': True,
#         'includeCommunities': False,
#         'includePosts': False,
#         'postsAfter': None,
#         'productSurface': 'web2x',
#         'query': 'example search',
#         # 'searchInput': {
#         #     'queryId': '051122fa-2f89-4257-ae00-264da78563cd',
#         #     'structureType': 'search',
#         # },
#         'sort': None,
#         'subredditNames': [
#             'redditdev',
#         ],
#     }
# }

# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
#            'Authorization': config['BEARER_TOKEN'],
#            'Content-Type': 'application/json'}
# res = requests.post(url=page_url, json=data, headers=headers)

# res = res.json()
# print(res['data']['search']['general']['comments']['feedMetadata'])
# print(res['data']['search']['general']['comments']['pageInfo'])

# file_path = "temp.txt"
# with open(file_path, 'w') as file:
#     # Write the text to the file
#     file.write(res.json['data']['search']['general']['comments']['feedMetadata'])
