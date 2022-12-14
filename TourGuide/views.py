from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return HTTPResponse('Here are our products')

def project(request, pk):
    return HttpResponse('Single project' + '' + str(pk))


# Create your views here.
