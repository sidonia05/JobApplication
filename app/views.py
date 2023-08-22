from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello (request):
    return HttpResponse ('Never give up. Today is hard, '
                         'tomorrow will be worse, but the day after tomorrow will be sunshine.')

def job_detail(request):
    return HttpResponse ('Job detail page')