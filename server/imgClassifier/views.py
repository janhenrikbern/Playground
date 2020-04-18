from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    component = render(request, 'imgClassifier/index.html', {
        'content': [

        ]
    })

    return component

def classifier(request):
    return HttpResponse("Hello there, this is a placeholder for a future image classifier")
