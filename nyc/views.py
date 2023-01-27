from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#request handler
#request->response


def say_hello(request):
    #pull data from a database
    #transform data
    #send emails
    return render(request,'hello.html',{'name':'Samiya'})

