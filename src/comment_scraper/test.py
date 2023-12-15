import requests 
import urllib.parse
import json
from dotenv import dotenv_values

config = dotenv_values(".env")

# Class testing
# as of right now, this is in a good state, leaving this for notes
from RedditNewCommentIterator import RedditNewCommentIterator

gcni = RedditNewCommentIterator(query='test', proxy_url='', subreddit='redditdev')
print(gcni.__iter__())
posts = []
posts.append(gcni.__next__())
posts.append(gcni.__next__())
print(gcni._RedditNewCommentIterator__reddit_partial_url)

file_path = "temp.txt"
with open(file_path, 'w') as file:
    for page in posts:
        file.write(str(page))
