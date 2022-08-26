from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from redditapp.redditapi import *


from .models import *
from .forms import *

globalcontext = {
    'mainpages':[{'link':'home','title':'Home'},{'link':'popular','title':'Popular'},{'link':'all','title':'All'}, ],
    'communities':getSubbedSubreddits(),
    'currentmain':''
}

# Create your views here.

def index(request):
    return render(request, 'index.html', context=globalcontext)

def page(request,subreddit):
    if subreddit == "home":
        return page_home(request)
    mapping = {'all':'All','popular':'Popular'}
    if subreddit in ["all","popular"]:
        subreddit = mapping[subreddit]
    globalcontext['currentmain'] = subreddit
    context = {**globalcontext,
        'posts':getPosts(subreddit),
    }
    return render(request,'page.html', context)

def page_home(request):
    globalcontext['currentmain'] = "Home"
    context = {**globalcontext,
        'posts':getPosts("home"),
    }
    if 'homesearch' in globalcontext:
        homesearch = globalcontext['homesearch']
        globalcontext.pop('homesearch', None)
        context = {**globalcontext,
        'posts':makequery("all",homesearch),
    }

    return render(request,'page.html', context)

def vote(request, subreddit, vote, post_id):
    makevote(post_id, vote)
    return redirect(request.META['HTTP_REFERER'])

    # return page(request,subreddit)

def comment(request,post_id):
    if request.method == "POST":
        comment = request.POST.get('comment')
        # print(post_id,comment)
        if len(comment) > 0:
            response = makecomment(comment, post_id)
            # print(response)
    return redirect(request.META['HTTP_REFERER'])

def query(request,subreddit):
    if request.method == "POST":
        querystring = request.POST.get('query')
    context = {**globalcontext,
        'posts':makequery(subreddit,querystring),
    }
    if subreddit == "Home":
        globalcontext["homesearch"] = querystring
        return redirect(request.META['HTTP_REFERER'])
    return render(request,'page.html', context)

