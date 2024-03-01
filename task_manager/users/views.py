from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'users/index.html', context={
        'all_users': '',
    })


def create(request):
    return render(request, 'users/registration.html', context={
        'all_users': '',
    })