import requests 
import urllib.parse
import json

page_url = 'https://gql.reddit.com/'

data = {
    'id': '6c87f86c5706',
    'variables': {
        'authorsAfter': None,
        'commentsAfter': 'MjQ=',
        'communitiesAfter': None,
        'communitySearch': True,
        'customFeedSearch': False,
        'filters': [
            {
                'key': 'nsfw',
                'value': '1',
            },
            {
                'key': 'subreddit_names',
                'value': 'redditdev',
            },
        ],
        'includeAuthors': False,
        'includeComments': True,
        'includeCommunities': False,
        'includePosts': False,
        'postsAfter': None,
        'productSurface': 'web2x',
        'query': 'example search',
        # 'searchInput': {
        #     'queryId': '051122fa-2f89-4257-ae00-264da78563cd',
        #     'structureType': 'search',
        # },
        'sort': None,
        'subredditNames': [
            'redditdev',
        ],
    }
}

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
           'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzAwMjU0NjE0LjU5Njc3MiwiaWF0IjoxNzAwMTY4MjE0LjU5Njc3MiwianRpIjoibE9GLTZTOVBubFp6WlZhS1hGX1h4eHhIVlJzNGlnIiwiY2lkIjoiOXRMb0Ywc29wNVJKZ0EiLCJsaWQiOiJ0Ml9xbmViaWt0IiwiYWlkIjoidDJfcW5lYmlrdCIsImxjYSI6MTUxNTAwMTgzNTg1Mywic2NwIjoiZUp4a2tkR090REFJaGQtbDF6N0JfeXBfTmh0c2NZYXNMUWFvazNuN0RWb2NrNzN5d1BuYXd2Rl9ncHk1TjB0VHlvS2xrR21hRWhieXpySUNTWnJTazlSWTNtbEtWTEFabWN1VmRxelE0SUZwU3BWTDVyYlE0OUltTkhkajBiTVRWMVV1S3ctcUFxMm5hbXpqRnJZbnhwbU4xWVpVWEpkVG1jQ3lVRDZMRl8yUXE3ZjItVFA5SnJTRFlVVlZlS0IzQktFY240M0ZGMVBZX1QwMTZkbTZZRkY3cndlcGZhN0g3dHBuelVLemNfczVucjgya25FNUxzMVBzSDkzX1JJNjhNanpNcU1PWU1RYWZwUmhSOWJoWDNVQWxRc0tHRXNRbjBZZ1Z5N2Zfa3V3WFpQLU5XNUhmUEhOaUp2ZThGc3pVTThsaUVPZnh0ZHZBQUFBX18tQ3lkUW4iLCJyY2lkIjoielRBYUluREZPLWdIZVdtYUhXSjZGVmxDaXFST2lNZVJuS1E0OS0tdERIOCIsImZsbyI6Mn0.EfHkSIVR7I2lCsf3zosRMZE23-uvp63xYNuh4uDByyuYo99KAj6-KROVR36fSXWOmDU8gxg_5zbuZWxq1VJXqoXc3ROOBdVITaccWxM2fink4C-IjbucLbr9o522QYj0gXUnvouCb4aPtxF1WVTgz_sChujRcEB9GErB4ZLurAuVMAY7lwQ9mRK3pzvAf2LkyJ8sTHlJgRRkuVsQkuEsRtDw7wo174bE3ks_nZcp703PMLu40HMZLr0uiUMEOZBPl5g77C0S4GhTKvCg_JiAb8oG2np6jIPMZkCjCxAIt271cC2-RwUljrB69EAVclGauXhzWIpMWKStynE6PpNS5g',
           'Content-Type': 'application/json'}
res = requests.post(url=page_url, json=data, headers=headers)

res = res.json()
print(res['data']['search']['general']['comments']['feedMetadata'])
print(res['data']['search']['general']['comments']['pageInfo'])

# file_path = "temp.txt"
# with open(file_path, 'w') as file:
#     # Write the text to the file
#     file.write(res.json['data']['search']['general']['comments']['feedMetadata'])
