from django.shortcuts import render

def post_list(request):
    return render(request, 'dashboard/main.html', {})
# Create your views here.
