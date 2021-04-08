from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("This is my response!")

def success(request):
    return HttpResponse("This is a sentence")

def bear(request,name,age):
    return HttpResponse(f"The name of the bear is {name} and the age is {age}")

