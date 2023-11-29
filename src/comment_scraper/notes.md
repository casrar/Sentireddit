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
                        "value": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzAxMzI2NjAxLjc0OTY4OSwiaWF0IjoxNzAxMjQwMjAxLjc0OTY4OSwianRpIjoiT1l2MjI5UVFUcms3VU96REZZX3lNWkViR2hLM093IiwiY2lkIjoiOXRMb0Ywc29wNVJKZ0EiLCJsaWQiOiJ0Ml9xbmViaWt0IiwiYWlkIjoidDJfcW5lYmlrdCIsImxjYSI6MTUxNTAwMTgzNTg1Mywic2NwIjoiZUp4a2tkR090REFJaGQtbDF6N0JfeXBfTmh0c2NZYXNMUWFvazNuN0RWb2NrNzN5d1BuYXd2Rl9ncHk1TjB0VHlvS2xrR21hRWhieXpySUNTWnJTazlSWTNtbEtWTEFabWN1VmRxelE0SUZwU3BWTDVyYlE0OUltTkhkajBiTVRWMVV1S3ctcUFxMm5hbXpqRnJZbnhwbU4xWVpVWEpkVG1jQ3lVRDZMRl8yUXE3ZjItVFA5SnJTRFlVVlZlS0IzQktFY240M0ZGMVBZX1QwMTZkbTZZRkY3cndlcGZhN0g3dHBuelVLemNfczVucjgya25FNUxzMVBzSDkzX1JJNjhNanpNcU1PWU1RYWZwUmhSOWJoWDNVQWxRc0tHRXNRbjBZZ1Z5N2Zfa3V3WFpQLU5XNUhmUEhOaUp2ZThGc3pVTThsaUVPZnh0ZHZBQUFBX18tQ3lkUW4iLCJyY2lkIjoieWVxY0VndzdycWJvYU52WjRXdzdkUTZlM1BPN2w5NkJOUVpzQkVoUS1rTSIsImZsbyI6Mn0.PH4Wf6uR3ODuvy0le0ZF4ZTnA8MB-jcacSqIPL5qbLNZrIe1PNDlE5ZtmFOlAyAwVJqsZSgFD475a10L7I_1_D3suizYr9TelPEqmV4VHkzKFmH-4enBOlVJKVUQn_Itp_iDaboKKvUrwzEjB-9IIG6RBey18NymYd1vu8DLvjhQEIbR4qqeN_viBPYzcJ_xRrzuqzEB_iCfO89onwYXTZBzCijXkeYRjpa6lYCGNfcnaasaelqwunpSDlpKJU-JofcWrHnc7ncnZ7Gp_p4Ia-bQmKWg1yZKCy1XQh0vX813swNGYWo-mBd-qt5ksxx2vQvLJfP4zwtWErOuyqbmLw"
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
                        "value": "00000000000qnebikt.2.1515001835853.Z0FBQUFBQmtyeURPNG9xZ2hXTE84dG14T21SWlVRVEFGMzZzRE9GNW1pVmpMRjVLZ0hoT1JTVUN5cjNtNFdnZkl5SERWSVFXdmZFYTlaT29pS254b1VaNVM3SnFuQlBscVhBYUtvYjYwMmxfZW5jU2pscm1FSmc0TEtpTE9pcXFkYkhyY1NQNlA4RUo"
                    },
                    {
                        "name": "x-reddit-session",
                        "value": "igjmhebadjpeppldoh.0.1701241275130.Z0FBQUFBQmxadUc3aDlrYmc1bGFGZmdkVkluejJST21iTk9CZnEwU3NIb1RRZXNqZzVUNjNqQ09RU2wyNjJoSnhHaml3YTJmZ3czSzNDdW80VzVOZjRoNFV1NWxOWlFlazZNQWtFbWxvZUpBaVVzeGtmcjd5LU5ORmVSRGJQbk01dGRyd2ZROWJFWHY"
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
