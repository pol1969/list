from django.shortcuts import render

# Create your views here.
def home_page(request):
    ''' домашняя страница'''
    return render(request, 'home.html')