from django.shortcuts import render

# Create your views here.
def carta_list(request):
    return render(request, 'carta/carta.html', {})