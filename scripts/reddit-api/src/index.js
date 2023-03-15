export default {
  async fetch(request, env) {
    const params = await new URL(request.url).searchParams
    const response = await fetch(`https://www.reddit.com/r/${params.get('subreddit')}.json?after=${params.get('after')}&limit=100`)
    const responseJSON = await response.json()
    return new Response(JSON.stringify(responseJSON))
  }
}