import requests 
import urllib.parse
import json
from dotenv import dotenv_values

config = dotenv_values(".env")

# page_url = 'https://gql.reddit.com/'

# data = {
#     "id": "6c87f86c5706",
#     "variables": {
#         "authorsAfter": None,
#         "commentsAfter": 'Mg==',
#         "communitiesAfter": None,
#         "communitySearch": True,
#         "customFeedSearch": False,
#         "filters": [
#             {
#                 "key": "nsfw",
#                 "value": "1"
#             },
#             {
#                 "key": "subreddit_names",
#                 "value": "redditdev"
#             }
#         ],
#         "includeAuthors": False,
#         "includeComments": True,
#         "includeCommunities": False,
#         "includePosts": False,
#         "postsAfter": None,
#         "productSurface": "web2x",
#         "query": "smell",
#         "searchInput": {
#             "queryId": "1b91cfc5-16a4-4477-a698-4be6bec3ba08",
#             "structureType": "search"
#         },
#         "sort": None,
#         "subredditNames": [
#             "redditdev"
#         ]
#     }
# }

# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
#            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzAxMjM2NjY4Ljg0Mzk5NiwiaWF0IjoxNzAxMTUwMjY4Ljg0Mzk5NiwianRpIjoiWDlRUHRDMGE0enBlRThOVXpnVWFkRWVYOUdESF9nIiwiY2lkIjoiOXRMb0Ywc29wNVJKZ0EiLCJsaWQiOiJ0Ml9xbmViaWt0IiwiYWlkIjoidDJfcW5lYmlrdCIsImxjYSI6MTUxNTAwMTgzNTg1Mywic2NwIjoiZUp4a2tkR090REFJaGQtbDF6N0JfeXBfTmh0c2NZYXNMUWFvazNuN0RWb2NrNzN5d1BuYXd2Rl9ncHk1TjB0VHlvS2xrR21hRWhieXpySUNTWnJTazlSWTNtbEtWTEFabWN1VmRxelE0SUZwU3BWTDVyYlE0OUltTkhkajBiTVRWMVV1S3ctcUFxMm5hbXpqRnJZbnhwbU4xWVpVWEpkVG1jQ3lVRDZMRl8yUXE3ZjItVFA5SnJTRFlVVlZlS0IzQktFY240M0ZGMVBZX1QwMTZkbTZZRkY3cndlcGZhN0g3dHBuelVLemNfczVucjgya25FNUxzMVBzSDkzX1JJNjhNanpNcU1PWU1RYWZwUmhSOWJoWDNVQWxRc0tHRXNRbjBZZ1Z5N2Zfa3V3WFpQLU5XNUhmUEhOaUp2ZThGc3pVTThsaUVPZnh0ZHZBQUFBX18tQ3lkUW4iLCJyY2lkIjoielRBYUluREZPLWdIZVdtYUhXSjZGVmxDaXFST2lNZVJuS1E0OS0tdERIOCIsImZsbyI6Mn0.e6iGXSoqSCp0QtYXqaYbdT8izQnN4gK2PtzJEgs9tXGblIP_0rxJ0AeoYS020qX_6gaqNqWlAK9tPGPHD-YYNRbq1zd9bUh4rRhb9LbVlPzQQAY1T4JrRmw7SSF-S4t_bNNBeiFoTFYRkApuZjhgUKbGIPCRgiq8TnC20qkA8Ukvgw1cIufnmvo-LVK-X-boIJoa-FPIY97TkgJMDalmglrH2qXzBCeWa01hZISQR0U8PT-zBqhum8IUygpEyVQVIyxt03M0HccD6jyhizEczZ42QxdMTnEmzgfOIaSuEyn45lQ5uYpw6j78cWDXAPxddnOb-nnfhTO2ScMyQ_4AEQ',
#            'Content-Type': 'application/json'}
# res = requests.post(url=page_url, json=data, headers=headers)

# res = res.json()
# print(res)
# print(res['data']['search']['general']['comments']['feedMetadata'])
# print(res['data']['search']['general']['comments']['pageInfo'])

# file_path = "temp.txt"
# with open(file_path, 'w') as file:
#     # Write the text to the file
#     file.write(res.json['data']['search']['general']['comments']['feedMetadata'])



from GQLNewCommentIterator import GQLNewCommentIterator


gcni = GQLNewCommentIterator(search_term='search', proxy_url='', subreddit='')
print(gcni.__iter__())
temp = str(gcni.__next__())
file_path = "temp.txt"
with open(file_path, 'w') as file:
    file.write(temp)
