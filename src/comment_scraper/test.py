import requests 
import urllib.parse
import json
from dotenv import dotenv_values

config = dotenv_values(".env")

# page_url = 'https://gql.reddit.com/'

# API testing
# data = {
# 	"id": "6c87f86c5706",
# 	"variables": {
# 		"authorsAfter": None,
# 		"commentsAfter": None,
# 		"communitiesAfter": None,
# 		"communitySearch": True,
# 		"customFeedSearch": False,
# 		"filters": [
# 			{
# 				"key": "nsfw",
# 				"value": "1"
# 			},
# 			{
# 				"key": "subreddit_names",
# 				"value": "redditdev"
# 			}
# 		],
# 		"includeAuthors": False,
# 		"includeComments": True,
# 		"includeCommunities": False,
# 		"includePosts": False,
# 		"postsAfter": None,
# 		"productSurface": "web2x",
# 		"query": "search",
# 		"searchInput": {
# 			"originPageType": "home",
# 			"queryId": "5aed4a8a-65b1-452a-b4a7-6b30f04fd9e9",
# 			"structureType": "history"
# 		},
# 		"sort": None,
# 		"subredditNames": [
# 			"redditdev"
# 		]
# 	}
# }
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
#         #    bearer token changes
#            'Authorization': config['BEARER_TOKEN'],
#            'Content-Type': 'application/json'}
# res = requests.post(url=page_url, json=data, headers=headers)
# print(res)
# res = res.json()
# print(res['data']['search']['general']['comments']['feedMetadata'])
# print(res['data']['search']['general']['comments']['pageInfo'])

# file_path = "temp.txt"
# with open(file_path, 'w') as file:
#     # Write the text to the file
#     file.write(res.json['data']['search']['general']['comments']['feedMetadata'])



# Class testing
# as of right now, this is in a good state, leaving this for notes
from RedditNewCommentIterator import RedditNewCommentIterator

gcni = RedditNewCommentIterator(query='smell', proxy_url='', subreddit='redditdev')
print(gcni.__iter__())
posts = gcni.__next__()
print(gcni._RedditNewCommentIterator__reddit_partial_url)

file_path = "comment_scraper/temp.txt"
with open(file_path, 'w') as file:
    file.write(str(posts))
