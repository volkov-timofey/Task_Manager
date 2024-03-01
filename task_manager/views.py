from django.shortcuts import render
from django.views.decorators.http import require_http_methods

def index(request):
    return render(request, 'index.html', context={
        'who': 'World',
    })


@require_http_methods(['GET', 'POST'])
def login(request):
    return render(request, 'check_in.html')

# context={          'username': request.GET['username']        }