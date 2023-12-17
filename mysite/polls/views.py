from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    response = """<h1>This is the home page. Thank you for using our website!</h1>"""
    return HttpResponse(response)

def owner(request):
    return HttpResponse("Hello, world. e2e34797 is the polls index.")

def details(request, question_id):
    return HttpResponse(f'You are looking at question {question_id}')

def results(request, question_id):
    return HttpResponse(f'You are looking at the results of question {question_id}')

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")