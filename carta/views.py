from django.shortcuts import render

# Create your views here.
def carta_list(request):
    return render(request, 'carta/indexV2.html', {})
    
def carta(request):
    return render(request, 'carta/products.html', {})

def about(request):
    return render(request, 'carta/about.html', {})

def contact(request):
    return render(request, 'carta/store.html', {})