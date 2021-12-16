from django.shortcuts import render, request



def index(request):
    return render(request, "heroku/index.html")

def index_test2(request, methods=['POST']):
    print(request)
    return request