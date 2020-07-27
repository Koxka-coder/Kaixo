from django.shortcuts import render

# Create your views here.
def carta(request):
    return render(request, 'carta/carta_list.html', {})