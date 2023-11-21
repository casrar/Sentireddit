class TopNewCommentSearch:
    def __init__(self):
        self.__api_call__ = {
            'id': '6c87f86c5706',
            'variables': {
                'authorsAfter': None,
                'commentsAfter': None, # This will change
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

    def get_call(self):
        return self.__api_call__
