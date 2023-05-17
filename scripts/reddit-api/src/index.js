export default {
  async fetch(request, env) {
    const params = await new URL(request.url).searchParams
    if (params.get("q") == null) {
      return new Response()
    }
    if (params.get("subreddit") == null) {
      return new Response()
    }
    if (params.get("after") == null) {
      return new Response()
    }
    const response = await fetch(`https://api.pushshift.io/reddit/search/comment/?q=${params.get("q")}&subreddit=${params.get("subreddit")}&after=${params.get("after")}&size=500`)
    const responseJSON = await response.json()
    if (responseJSON["data"] == null) {
      return new Response()
    }

    const responseData = { "posts": [] }

    responseJSON["data"].forEach(element => {
      responseData["posts"].push(element["body"])
    });

    return new Response(JSON.stringify(responseData))
  }
}