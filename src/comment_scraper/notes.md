- gql.reddit.com 
    - GraphQL endpoint for Reddit
    - XHR requests are typically aimed here
    - Bearer token changes, need to figure out a way to update that
    - Uses 'id' in request to define what type of action
        - e39d1d540f0a 
            - Provides search functionality, called every time search bar is interfaced with (e.g. clicked, typed in)
            - Response returns Subreddits and Profiles matching your search 
        - 2c3efcfc2552
            - Unknown functionality, pairs with e39d1d540f0a during search bar interface
        - 6c87f86c5706
            - Provides the comment search
            - Response returns searched query with comment filter
            - unsure what search input does, query id is different for evry query, probably hashed
                "searchInput": {
                        "queryId": "1b91cfc5-16a4-4477-a698-4be6bec3ba08",
                        "structureType": "search"
                    }
            - request headers
        {
            "Request Headers (2.271 kB)": {
                "headers": [
                    {
                        "name": "Accept",
                        "value": "*/*"
                    },
                    {
                        "name": "Accept-Encoding",
                        "value": "gzip, deflate, br"
                    },
                    {
                        "name": "Accept-Language",
                        "value": "en-US,en;q=0.5"
                    },
                    {
                        "name": "Authorization",
                        "value": "Bearer {value}"
                    },
                    {
                        "name": "Cache-Control",
                        "value": "no-cache"
                    },
                    {
                        "name": "Connection",
                        "value": "keep-alive"
                    },
                    {
                        "name": "Content-Length",
                        "value": "545"
                    },
                    {
                        "name": "Content-Type",
                        "value": "application/json"
                    },
                    {
                        "name": "Host",
                        "value": "gql.reddit.com"
                    },
                    {
                        "name": "Origin",
                        "value": "https://www.reddit.com"
                    },
                    {
                        "name": "Pragma",
                        "value": "no-cache"
                    },
                    {
                        "name": "Referer",
                        "value": "https://www.reddit.com/"
                    },
                    {
                        "name": "Sec-Fetch-Dest",
                        "value": "empty"
                    },
                    {
                        "name": "Sec-Fetch-Mode",
                        "value": "cors"
                    },
                    {
                        "name": "Sec-Fetch-Site",
                        "value": "same-site"
                    },
                    {
                        "name": "Sec-GPC",
                        "value": "1"
                    },
                    {
                        "name": "TE",
                        "value": "trailers"
                    },
                    {
                        "name": "User-Agent",
                        "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
                    },
                    {
                        "name": "x-reddit-compression",
                        "value": "1"
                    },
                    {
                        "name": "x-reddit-loid",
                        "value": "{value}"
                    },
                    {
                        "name": "x-reddit-session",
                        "value": "{value}"
                    }
                ]
            }
        }
        - Time is returned in 'ISO 8601 format with an associated timezone offset' ex: 2023-11-28T20:24:54.557000+0000

- GQLNewCommentIterator
    - returns edges, which contain post and comment data
        - edges contains a list of these
        - within each edge i am interested in node -> content -> markdown, and node -> created

- General
    - Need to figure out how to keep the bearer tokens updated
    - Become familar with the proxy tool
    - I forsee the tokens and the proxy tool becoming an issue, may need to figure something out to automatically grab and update bearer 
    - for some reason i dont use the GQL api on incognito browser, need more research
    - GQl endpoint only works if you are logged in
        - There is a way around it with partials and normal scraping; hit the normal endpoint, then grab url in ```<faceplate-partial loading="lazy"```, 
        continue to grab ```<faceplate-partial loading="lazy" on each page```, grab individual comments and post data 
            - ```https://www.reddit.com/r/redditdev/search/?q=creating&type=comment``
                - ```/>  <faceplate-partial loading="lazy" src="/svc/shreddit/r/redditdev/search/?q=creating&amp;type=comment&amp;commentsCursor=MjQ%3D"``>
            - ```https://www.reddit.com/svc/shreddit/r/redditdev/search/?q=creating&type=comment&commentsCursor=MjQ%3D```
            - the post is stored in ````#search-comment-t1_jeyb0s0-post-rtjson-content``` and time in ```faceplate-timeago
```


