from django.shortcuts import render

from django.http import HttpResponse

from django.http import JsonResponse
# Create your views here.

def index(request):
    # print("1111111")
    return render(request, 'index.html')

# def test1(request):
#     print("222222")
#     print(request.POST)
#     return render(request, 'index.html')

