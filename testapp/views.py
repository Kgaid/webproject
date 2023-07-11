from django.shortcuts import render

# Create your views here.
from datetime import datetime
from django.http import JsonResponse

def get_example(request):
    response = {'request': {'time': datetime.now().isoformat(),
                            'method': request.method,
                            'path': request.path,
                            'params': request.GET,
                            'headers': dict(request.headers)}}
    return JsonResponse(response, safe=False, json_dumps_params={'indent': 2})
