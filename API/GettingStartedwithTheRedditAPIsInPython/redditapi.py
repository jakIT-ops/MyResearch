from jinja2 import Undefined
import praw
import requests
import html

def gettoken():
    reddit = praw.Reddit(
        client_id="{{CLIENT_ID}}",
        client_secret="{{CLIENT_SECRET}}",
        refresh_token="{{REFRESH_TOKEN}}",
        user_agent="testscript by u/{{USERNAME}}"
    )

    return(reddit)

def getUser():
    reddit = gettoken()
    return(reddit.user)

def getPosts(subreddit):
    reddit = gettoken()
    if (subreddit == "home"):
        posts =  reddit.front.hot(limit=10)
        posts_list = list(posts)
        final_posts = []
        for post in posts_list:
            url = getimageurl(post)
            final_posts.append((post,url))
        return final_posts
    posts = reddit.subreddit(subreddit).hot(limit=10)
    posts_list = list(posts)
    final_posts = []
    for post in posts_list:
        url = getimageurl(post)
        final_posts.append((post,url))

    return final_posts

def getSubbedSubreddits():
    reddit = gettoken()
    SubbedSubreddits = list(reddit.user.subreddits(limit=None))
    SubbedSubreddits = [i.display_name for i in SubbedSubreddits]
    with_u = [i for i in SubbedSubreddits if i.startswith("u_")]
    without_u = [i for i in SubbedSubreddits if i not in with_u]
    return(without_u)

def makevote(post_id, vote):
    reddit = gettoken()
    submission = reddit.submission(post_id)
    if vote == "up":
        response = submission.upvote()
    if vote == "down":
        response = submission.downvote()
    return(response)

def makecomment(comment, post_id):
    reddit = gettoken()
    submission = reddit.submission(post_id)
    response = submission.reply(comment)
    return(response)

def makequery(subreddit,query):
    reddit = gettoken()
    submissions = reddit.subreddit(subreddit).search(query,limit=10)
    posts_list = list(submissions)
    final_posts = []
    for post in posts_list:
        url = getimageurl(post)
        final_posts.append((post,url))
    return(final_posts)

def getimageurl(post):
        
    headers = {
        'User-Agent': 'testscript by u/{{USERNAME}}',
        'Authorization': "bearer {{ACCESS_TOKEN}}",
        "Accept":"application/json"
    }
    url = "https://oauth.reddit.com" + post.permalink[:-1] + ".json"

    response = requests.get(url=url, headers=headers)

    img_url = None
    data = response.json()[0]["data"]["children"][0]["data"]
    if "preview" in data.keys():
        for image in data["preview"]["images"]:
            image_url = image["source"]["url"]
            img_url = html.unescape(image_url)
    elif "media_metadata" in data.keys():
        for image in data["media_metadata"].keys():
            if "p" in data["media_metadata"][image].keys():
                img_url = html.unescape(data["media_metadata"][image]["p"][0]["u"])
    return img_url
    