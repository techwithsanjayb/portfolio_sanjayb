from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def blog_list(request):
    return render(request, 'core/blog_list.html')

def resource_details(request):
    return render(request, 'core/resource_details.html')
    