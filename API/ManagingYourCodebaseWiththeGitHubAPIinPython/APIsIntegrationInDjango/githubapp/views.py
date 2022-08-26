from django.shortcuts import render, redirect
import requests
import json
from django.contrib import messages


USERNAME='{{USERNAME}}'

headers = {
    'Authorization': 'token {{ACCESS_TOKEN}}',
    'Accept': 'application/vnd.github.v3+json',
}

def index(request):
    return render(request, 'githubapp/index.html')

def search(request):
    if request.method == "POST":
        query = request.POST.get('query')
        query = query.replace(' ', '+')
        print(query)
        url = "https://api.github.com/search/repositories?q="+query+"&sort=stars&order=desc"
        response = requests.get(url, headers=headers)
        context = {
            'repos': response.json()['items']
        }
        return render(request, 'githubapp/search.html', context)
    else:
        return render(request, 'githubapp/search.html')

def createRepo(request):
    if request.method == 'POST':
        url="https://api.github.com/user/repos"
        data=json.dumps({'name': request.POST.get('repoName')})
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 201:
            messages.success(request, 'The repository "'+request.POST.get('repoName')+'" has been created successfully.')
            return redirect('githubapp:index')
        else:
            messages.error(request, 'Some error occurred. Try again.')

    return render(request, 'githubapp/create_repo.html')

def updateRepo(request):
    if request.method == 'POST':
        url= "https://api.github.com/repos/" + USERNAME + "/" + request.POST.get('currentName')
        data=json.dumps({'name': request.POST.get('newName')})
        response = requests.patch(url, headers=headers, data=data)
        if response.status_code == 200:
            messages.success(request, 'The repository "'+request.POST.get('currentName')+'" has been successfully renamed to "'+request.POST.get('newName')+'".')
            return redirect('githubapp:index')
        else:
            messages.error(request, 'Some error occurred. Try again.')
    
    return render(request, 'githubapp/update_repo.html')

def deleteRepo(request):
    if request.method == 'POST':
        url="https://api.github.com/repos/" + USERNAME + "/" + request.POST.get('repoName')
        response = requests.delete(url, headers=headers)
        if response.status_code == 204:
            messages.success(request, 'The repository "'+request.POST.get('repoName')+'" was deleted successfully.')
            return redirect('githubapp:index')
        else:
            messages.error(request, 'Some error occurred. Try again.')
    
    return render(request, 'githubapp/delete_repo.html')

def repos(request):
    if request.method == 'POST':
        url= "https://api.github.com/users/" + request.POST.get('username') + "/repos"
        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            context={
                'repos': response.json
            }
            return render(request, 'githubapp/repos.html', context)
        else:
            messages.error(request, 'Some error occurred. Try again.')
    
    return render(request, 'githubapp/repos.html')


def branches(request):
    if request.method == 'POST':
        url = 'https://api.github.com/repos/' + request.POST.get('username') + '/' + request.POST.get('repoName') + '/branches'
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            context={
                'branches': response.json
            }
            return render(request, 'githubapp/branches.html', context)
        else:
            messages.error(request, 'Some error occurred. Try again.')
    
    return render(request, 'githubapp/branches.html')

def commits(request):
    if request.method == 'POST':
        url='https://api.github.com/repos/' + request.POST.get('username') + '/' + request.POST.get('repoName') + '/commits'
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            context={
                'commits': response.json
            }
            return render(request, 'githubapp/commits.html', context)
        else:
            messages.error(request, 'Some error occurred. Try again.')
    
    return render(request, 'githubapp/commits.html')  

def collaborators(request):
    if request.method == 'POST':
        url='https://api.github.com/repos/' + USERNAME + '/' + request.POST.get('repoName') + '/collaborators'
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            context={
                'collaborators': response.json
            }
            return render(request, 'githubapp/collaborators.html', context)
        else:
            messages.error(request, 'Some error occurred. Try again.')
    
    return render(request, 'githubapp/collaborators.html')

def createRepoProject(request):
    if request.method == 'POST':
        data = '{"name" : "' + request.POST.get('projectName') + '"}'
        url='https://api.github.com/repos/' + USERNAME + '/' + request.POST.get('repoName') + '/projects'
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 201:
            messages.success(request, 'The repository project "' + request.POST.get('projectName') + '" has been created successfully.')
            return redirect('githubapp:index')
        else:
            messages.error(request, 'Some error occurred. Try again.')    
    
    return render(request, 'githubapp/create_repo_project.html')

def repoProjects(request):
    if request.method == 'POST':
        url = 'https://api.github.com/repos/' + request.POST.get('username') + '/' + request.POST.get('repoName') + '/projects'
        response = requests.get(url, headers=headers)
        print(response.status_code)

        if response.status_code == 200:
            context={
                'projects': response.json
            }
            return render(request, 'githubapp/repo_projects.html', context)
        else:
            messages.error(request, 'Some error occurred. Try again.')
    
    return render(request, 'githubapp/repo_projects.html')

def createProject(request):
    if request.method == 'POST':
        data = '{"name" : "' + request.POST.get('projectName') + '"}'
        url='https://api.github.com/user/projects'
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 201:
            messages.success(request, 'The project "' + request.POST.get('projectName') + '" has been created successfully.')
            return redirect('githubapp:index')
        else:
            messages.error(request, 'Some error occurred. Try again.')    
    
    return render(request, 'githubapp/create_project.html')

def projects(request):
    if request.method == 'POST':
        url = 'https://api.github.com/users/' + request.POST.get('username') + '/projects'
        response = requests.get(url, headers=headers)
        print(response.status_code)

        if response.status_code == 200:
            context={
                'projects': response.json
            }
            return render(request, 'githubapp/projects.html', context)
        else:
            messages.error(request, 'Some error occurred. Try again.')
    
    return render(request, 'githubapp/projects.html')